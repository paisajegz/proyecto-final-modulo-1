from infraestructure.repository.dto.user import User
from infraestructure.repository.database import DatabaseSingleton
import sqlite3


class UserRepository:
    _database: DatabaseSingleton

    def __init__(self, database: DatabaseSingleton = DatabaseSingleton()) -> None:
        self._database = database

    def add_user(self, usr: User) -> bool:
        try:
            query = """
            INSERT INTO users (first_name , last_name , email, password , count_checkout ) VALUES ( ? , ? , ? , ? , ?)
            """
            data_insert = (
                usr.first_name,
                usr.last_name,
                usr.email,
                usr.password,
                usr.count_checkout,
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

    def delete_user(self, id: int) -> bool:
        try:
            query = """
            DELETE FROM  users  where id = ?
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

    def login_user(self, email: str) -> User:
        try:
            query = "SELECT * FROM users WHERE email = ?"
            data = (email,)
            self._database.get_cursor().execute(query, data)
            result = self._database.get_cursor().fetchone()
            user = User(*result)
            return user
        except sqlite3.IntegrityError as e:
            # Error relacionado con integridad, como violación de claves únicas o nulas
            print(f"Error de integridad de la base de datos: {e}")
            self._database.rollback()
            return User()
        except sqlite3.OperationalError as e:
            # Error relacionado con operaciones de base de datos, como sintaxis incorrecta
            print(f"Error operativo en la base de datos: {e}")
            self._database.rollback()
            return User()
        except sqlite3.DatabaseError as e:
            # Otros errores generales de la base de datos
            print(f"Error general de la base de datos: {e}")
            self._database.rollback()
            return User()
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            self._database.rollback()
            return User()

    def update_count_stock(self, id: int, stock: int) -> bool:
        try:
            query = """
            UPDATE users SET count_checkout = ? where id = ?
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

    def show_users(self) -> list[User]:
        return list()

    def user_most_checkout(self) -> list[User]:
        try:
            query = "SELECT * FROM users ORDER BY count_checkout DESC LIMIT 10"
            self._database.get_cursor().execute(query)
            results = self._database.get_cursor().fetchall()
            users = [User(*row) for row in results]
            return users
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

    def user_least_checkout(self) -> list[User]:
        try:
            query = "SELECT * FROM users Where count_checkout=0"
            self._database.get_cursor().execute(query)
            results = self._database.get_cursor().fetchall()
            users = [User(*row) for row in results]
            return users
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
