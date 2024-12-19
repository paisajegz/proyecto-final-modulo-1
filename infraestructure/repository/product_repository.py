from typing import List
from infraestructure.repository.dto import product
from infraestructure.repository.dto.product import Product

from infraestructure.repository.database import DatabaseSingleton
import sqlite3


class ProductRepository:
    def __init__(self, database: DatabaseSingleton = DatabaseSingleton()) -> None:
        self._database = database

    def add_product(self, product: Product) -> bool:
        try:
            query = """
            INSERT INTO products (name , quantity ,price ) VALUES ( ? , ? , ?)
            """
            data_insert = (
                product.name,
                product.quantity,
                product.price,
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

    def delete_product(self, id: int) -> bool:
        try:
            query = """
            DELETE FROM  products  where id = ?
            """
            data_delete = (id,)
            self._database.get_cursor().execute(query, data_delete)
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

    def show_products(self) -> list[Product]:
        try:
            query = "SELECT * FROM products"

            self._database.get_cursor().execute(query)
            results = self._database.get_cursor().fetchall()
            products = [Product(*row) for row in results]
            return products
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

    def update_stock(self, id: int, stock: int) -> bool:
        try:
            query = """
            UPDATE products SET quantity = ? where id = ?
            """
            data_update = (stock, id)
            self._database.get_cursor().execute(query, data_update)
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

    def show_product_by_id(self, id: int) -> Product:
        try:
            query = "SELECT * FROM products WHERE id = ?"
            data = (id,)
            self._database.get_cursor().execute(query, data)
            result = self._database.get_cursor().fetchone()
            product = Product(*result)
            return product
        except sqlite3.IntegrityError as e:
            # Error relacionado con integridad, como violación de claves únicas o nulas
            print(f"Error de integridad de la base de datos: {e}")
            self._database.rollback()
            return Product()
        except sqlite3.OperationalError as e:
            # Error relacionado con operaciones de base de datos, como sintaxis incorrecta
            print(f"Error operativo en la base de datos: {e}")
            self._database.rollback()
            return Product()
        except sqlite3.DatabaseError as e:
            # Otros errores generales de la base de datos
            print(f"Error general de la base de datos: {e}")
            self._database.rollback()
            return Product()
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            self._database.rollback()
            return Product()
