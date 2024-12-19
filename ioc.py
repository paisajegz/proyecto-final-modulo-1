import inject
from domain.sales.total_sales_renueve import TotalSalesRenueve
from domain.user.user_with_least_checkout import UserWithLeastCheckout
from domain.user.user_with_most_checkout import UserWithMostCheckout
from infraestructure.repository.database import DatabaseSingleton
from infraestructure.repository.user_repository import UserRepository
from infraestructure.repository.admin_repository import AdminRepository
from infraestructure.repository.checkout_repository import CheckoutRepository
from infraestructure.repository.history_repository import HistoryRepository
from infraestructure.repository.product_repository import ProductRepository

from domain.inventory.see_inventory import SeeInventory
from domain.inventory.delete_product_inventory import DeleteProductInventory
from domain.inventory.update_stock_product import UpdateStockInventory
from domain.inventory.store_product_inventory import StoreItemInventory

from domain.user.login_user import LoginUser
from domain.user.register_user import RegisterUser

from domain.admin.login_admin import LoginAdmin
from domain.admin.reigster_admin import RegisterAdmin

from domain.sales.see_item_checkout import SeeItemCheckout
from domain.sales.add_item_checkout import AddItemCheckout

from domain.menu.admin.menu import MenuAdmin
from domain.menu.user.menu import MenuUser
from domain.menu.index import Menu

from infraestructure.migrate.generate_migrate import GenerateMigrate


def configure(binder: inject.Binder) -> None:
    binder.bind(DatabaseSingleton, DatabaseSingleton())

    # repository
    binder.bind(UserRepository, UserRepository())
    binder.bind(AdminRepository, AdminRepository())
    binder.bind(CheckoutRepository, CheckoutRepository())
    binder.bind(HistoryRepository, HistoryRepository())
    binder.bind(ProductRepository, ProductRepository())

    ##inventory
    binder.bind(SeeInventory, SeeInventory())
    binder.bind(DeleteProductInventory, DeleteProductInventory())
    binder.bind(UpdateStockInventory, UpdateStockInventory())
    binder.bind(StoreItemInventory, StoreItemInventory())

    # user
    binder.bind(LoginUser, LoginUser())
    binder.bind(RegisterUser, RegisterUser())
    binder.bind(UserWithMostCheckout, UserWithMostCheckout())
    binder.bind(UserWithLeastCheckout, UserWithLeastCheckout())

    # admin
    binder.bind(LoginAdmin, LoginAdmin())
    binder.bind(RegisterAdmin, RegisterAdmin())

    # sales
    binder.bind(SeeItemCheckout, SeeItemCheckout())
    binder.bind(AddItemCheckout, AddItemCheckout())
    binder.bind(TotalSalesRenueve, TotalSalesRenueve())

    # menus
    binder.bind(MenuUser, MenuUser())
    binder.bind(MenuAdmin, MenuAdmin())
    binder.bind(Menu, Menu())
    binder.bind(GenerateMigrate, GenerateMigrate())
