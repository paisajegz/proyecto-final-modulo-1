from infraestructure.repository.dto import checkout
from infraestructure.repository.dto.checkout import Checkout
from infraestructure.repository.database import DatabaseSingleton
import sqlite3


class SaleRevenue:
    _count_sales: int
    _total_sales: float

    def __init__(self, count_sales: int = 0, total_sales: float = 0) -> None:
        self._count_sales = count_sales
        self._total_sales = total_sales

    @property
    def count_sales(self):
        return self._count_sales

    @count_sales.setter
    def count_sales(self, count_sales: int):
        self._count_sales = count_sales

    @property
    def total_sales(self):
        return self._total_sales

    @total_sales.setter
    def total_sales(self, total_sales: float):
        self._total_sales = total_sales

    def to_string(self):
        return f"""
            cantidad de ventas realizadas {self.count_sales}
            cantidad de dinero realizado {self.total_sales}
        """


class CheckoutRepository:
    def __init__(self, database: DatabaseSingleton = DatabaseSingleton()) -> None:
        self._database = database

    def add_checkout(self, checkout: Checkout) -> bool:
        try:
            query = """
            INSERT INTO checkout  (id_user , id_product , quantity, price ) VALUES ( ? , ? , ?, ?)
            """
            data_insert = (
                checkout.id_user,
                checkout.id_product,
                checkout.quantity,
                checkout.price,
            )
            self._database.get_cursor().execute(query, data_insert)
            self._database.commit()
        except sqlite3.IntegrityError as e:
            # Error relacionado con integridad, como violación de claves únicas o nulas
            print(f"Error de integridad de la base de datos: {e}")
            self._database.rollback()
            return False
        except sqlite3.OperationalError as e:
            # Error relacionado con operaciones de base de datos, como sintaxis incorrecta
            print(f"Error operativo en la base de datos: {e}")
            self._database.rollback()
            return False
        except sqlite3.DatabaseError as e:
            # Otros errores generales de la base de datos
            print(f"Error general de la base de datos: {e}")
            self._database.rollback()
            return False
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            self._database.rollback()
            return False
        return True

    def show_checkout_by_user(self, id_user: int) -> list[Checkout]:
        try:
            query = """
                select checkout.id as id  ,checkout.id_product as id_product , checkout.id_user as id_user , checkout.quantity as quantity , users.first_name as first_name , users.last_name as last_name , products.name as product_name, checkout.price as price 
                from checkout INNER JOIN users 
                ON checkout.id_user = users.id 
                INNER JOIN products on checkout.id_product = products.id where checkout.id_user = ?
            """
            data = (id_user,)

            self._database.get_cursor().execute(query, data)
            results = self._database.get_cursor().fetchall()
            checkout = [Checkout(*row) for row in results]
            return checkout
        except sqlite3.IntegrityError as e:
            # Error relacionado con integridad, como violación de claves únicas o nulas
            print(f"Error de integridad de la base de datos: {e}")
            self._database.rollback()
            return list()
        except sqlite3.OperationalError as e:
            # Error relacionado con operaciones de base de datos, como sintaxis incorrecta
            print(f"Error operativo en la base de datos: {e}")
            self._database.rollback()
            return list()
        except sqlite3.DatabaseError as e:
            # Otros errores generales de la base de datos
            print(f"Error general de la base de datos: {e}")
            self._database.rollback()
            return list()
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            self._database.rollback()
            return list()

    def show_sale_revenue(self) -> SaleRevenue:
        try:
            query = "SELECT  count(*) as count_sales , sum(price) as total_sales from checkout"
            self._database.get_cursor().execute(query)
            result = self._database.get_cursor().fetchone()
            user = SaleRevenue(*result)
            return user
        except sqlite3.IntegrityError as e:
            # Error relacionado con integridad, como violación de claves únicas o nulas
            print(f"Error de integridad de la base de datos: {e}")
            self._database.rollback()
            return SaleRevenue()
        except sqlite3.OperationalError as e:
            # Error relacionado con operaciones de base de datos, como sintaxis incorrecta
            print(f"Error operativo en la base de datos: {e}")
            self._database.rollback()
            return SaleRevenue()
        except sqlite3.DatabaseError as e:
            # Otros errores generales de la base de datos
            print(f"Error general de la base de datos: {e}")
            self._database.rollback()
            return SaleRevenue()
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            self._database.rollback()
            return SaleRevenue()
