from domain.gateway.entity import Entity


class Product(Entity):
    _id: int
    _quantity: int
    _name: str
    _price: float

    def __init__(
        self, id: int = 0, name: str = "", quantity: int = 0, price: float = 0
    ) -> None:
        self._name = name
        self._quantity = quantity
        self._price = price
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    def to_string(self) -> str:
        return f"""
        id del producto : {self._id}
        nombre del producto: {self._name} 
        cantidad del producto: {self._quantity}
        precio del producto: $ {self._price}
        """

    def migrate(self) -> str:
        return """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    );
        """
