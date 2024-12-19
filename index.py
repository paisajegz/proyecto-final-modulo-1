import inject
from domain.menu.index import Menu
from infraestructure.migrate.generate_migrate import GenerateMigrate
from ioc import configure


inject.configure(configure)

if __name__ == "__main__":
    generate_migrate = inject.instance(GenerateMigrate)
    generate_migrate.generate_migration()
    menu = inject.instance(Menu)
    menu.show()
