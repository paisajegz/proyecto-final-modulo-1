from domain.gateway.entity import Entity
from infraestructure.repository.database import DatabaseSingleton
from infraestructure.repository.dto.admin import Admin
from infraestructure.repository.dto.checkout import Checkout
from infraestructure.repository.dto.history import History
from infraestructure.repository.dto.product import Product
from infraestructure.repository.dto.user import User


class GenerateMigrate:
    _list_migrate: list[Entity]
    _database: DatabaseSingleton

    def __init__(self, database: DatabaseSingleton = DatabaseSingleton()):
        self._database = database
        self._list_migrate = list()
        self._list_migrate.append(User())
        self._list_migrate.append(Admin())
        self._list_migrate.append(Product())
        self._list_migrate.append(Checkout())
        self._list_migrate.append(History())

    def generate_migration(self):
        for entity in self._list_migrate:
            query_migrate = entity.migrate()
            self._database.get_cursor().execute(query_migrate)
        self._database.commit()
