from domain.gateway.entity import Entity


class User(Entity):
    _id: int
    _first_name: str
    _last_name: str
    _email: str
    _password: str
    _count_checkout: int

    def __init__(
        self, id=0, first_name="", last_name="", email="", password="", count_checkout=0
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
        self._email = email
        self._password = password
        self.count_checkout = count_checkout

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, _first_name):
        self._first_name = _first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, _last_name):
        self._last_name = _last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, _email):
        self._email = _email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, _passowrd):
        self._password = _passowrd

    @property
    def count_checkout(self):
        return self._count_checkout

    @count_checkout.setter
    def count_checkout(self, count_checkout: int):
        self._count_checkout = count_checkout

    def to_string(self):
        return f"""
        nombres usuario: {self.first_name}
        apellidos usuario: {self.last_name}
        correo usuario: {self.email}
        cantidad de compras : {self.count_checkout}
        """

    def migrate(self) -> str:
        return """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        count_checkout INTEGER NOT NULL
    );
        """
