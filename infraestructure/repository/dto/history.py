from domain.gateway.entity import Entity
from infraestructure.repository.dto.product import Product


class History(Entity):
    _id: int
    _id_product: int
    _id_user: int
    _type_history: str
    _quantity: int
    _product: Product

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
    def type_history(self):
        return self._type_history

    @type_history.setter
    def type_history(self, type_history: str):
        self._type_history = type_history

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product: Product):
        self._product = product

    def migrate(self) -> str:
        return """
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER NOT NULL,
        id_product INTEGER NOT NULL,
        type_history TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (id_user) REFERENCES users(id),
        FOREIGN KEY (id_product) REFERENCES products(id)
    );
        """
