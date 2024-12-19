import sqlite3
import threading


class DatabaseSingleton:
    _instance = None
    _lock = (
        threading.Lock()
    )  # Asegura que solo haya una instancia incluso en un entorno multi-hilo

    _conn: sqlite3.Connection
    _cursor: sqlite3.Cursor

    def __new__(cls):
        # Si no existe una instancia, la crea
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._conn = sqlite3.connect("store.db")
                cls._instance._cursor = cls._instance._conn.cursor()
        return cls._instance

    def get_cursor(self):
        return self._cursor

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        self._conn.close()
        DatabaseSingleton._instance = (
            None  # Opcional, para permitir la recolección de basura
        )
