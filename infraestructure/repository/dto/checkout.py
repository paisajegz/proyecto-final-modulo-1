from domain.gateway.entity import Entity


class Checkout(Entity):
    _id: int
    _id_product: int
    _id_user: int
    _quantity: int
    _first_name: str
    _last_name: str
    _product_name: str
    _price: float

    def __init__(
        self,
        id: int = 0,
        id_product: int = 0,
        id_user: int = 0,
        quantity: int = 0,
        first_name: str = "",
        last_name: str = "",
        product_name: str = "",
        price: float = 0,
    ) -> None:
        self._id = id
        self._id_user = id_user
        self._id_product = id_product
        self._quantity = quantity
        self._first_name = first_name
        self._last_name = last_name
        self._product_name = product_name
        self._price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def id_product(self):
        return self._id_product

    @id_product.setter
    def id_product(self, id_product: int):
        self._id_product = id_product

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user: int):
        self._id_user = id_user

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    def to_string(self):
        return f"""
            nombre del producto: {self._product_name}
            precio del producto en su momento : {self._price}
            cantidad comprada: {self.quantity}
            usuario que compro: {self._first_name} { self._last_name}
        """

    def migrate(self) -> str:
        return """
    CREATE TABLE IF NOT EXISTS checkout (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER NOT NULL,
        id_product INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (id_user) REFERENCES users(id),
        FOREIGN KEY (id_product) REFERENCES products(id)
    );
        """
