from infraestructure.repository.dto.admin import Admin
from infraestructure.repository.database import DatabaseSingleton
import sqlite3


class AdminRepository:
    def __init__(self, database: DatabaseSingleton = DatabaseSingleton()) -> None:
        self._database = database

    def add_admin(self, admin: Admin) -> bool:
        try:
            query = """
            INSERT INTO admins (first_name , last_name , email, password  ) VALUES ( ? , ? , ? , ?)
            """
            data_insert = (
                admin.first_name,
                admin.last_name,
                admin.email,
                admin.password,
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

    def login_admin(self, email: str) -> Admin:
        try:
            query = "SELECT * FROM admins WHERE email = ?"
            data = (email,)
            self._database.get_cursor().execute(query, data)
            result = self._database.get_cursor().fetchone()
            user = Admin(*result)
            return user
        except sqlite3.IntegrityError as e:
            # Error relacionado con integridad, como violación de claves únicas o nulas
            print(f"Error de integridad de la base de datos: {e}")
            self._database.rollback()
            return Admin()
        except sqlite3.OperationalError as e:
            # Error relacionado con operaciones de base de datos, como sintaxis incorrecta
            print(f"Error operativo en la base de datos: {e}")
            self._database.rollback()
            return Admin()
        except sqlite3.DatabaseError as e:
            # Otros errores generales de la base de datos
            print(f"Error general de la base de datos: {e}")
            self._database.rollback()
            return Admin()
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            self._database.rollback()
            return Admin()
