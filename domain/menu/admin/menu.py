import sys
from domain.admin.reigster_admin import RegisterAdmin
from domain.inventory.delete_product_inventory import DeleteProductInventory
from domain.inventory.see_inventory import SeeInventory
from domain.inventory.store_product_inventory import StoreItemInventory
from domain.inventory.update_stock_product import UpdateStockInventory
from domain.menu.option import Option
from domain.menu.steps import Step
from domain.sales.total_sales_renueve import TotalSalesRenueve
from domain.user.user_with_least_checkout import UserWithLeastCheckout
from domain.user.user_with_most_checkout import UserWithMostCheckout
from infraestructure.console.show_message import Print


class MenuAdmin:
    _step_admin: Step
    _store_product_inventory: StoreItemInventory
    _see_inventory: SeeInventory
    _update_stock_inventory: UpdateStockInventory
    _delete_product_inventory: DeleteProductInventory
    _register_admin: RegisterAdmin
    _user_with_least_checkout: UserWithLeastCheckout
    _user_with_most_checkout: UserWithMostCheckout
    _total_sales_renueve: TotalSalesRenueve

    def __init__(
        self,
        store_product_inventory: StoreItemInventory = StoreItemInventory(),
        see_inventory: SeeInventory = SeeInventory(),
        update_stock_product: UpdateStockInventory = UpdateStockInventory(),
        delete_product_inventory: DeleteProductInventory = DeleteProductInventory(),
        register_admin: RegisterAdmin = RegisterAdmin(),
        user_with_most_checkout: UserWithMostCheckout = UserWithMostCheckout(),
        user_with_least_checkout: UserWithLeastCheckout = UserWithLeastCheckout(),
        total_sales_renueve: TotalSalesRenueve = TotalSalesRenueve(),
    ) -> None:
        self._store_product_inventory = store_product_inventory
        self._see_inventory = see_inventory
        self._update_stock_inventory = update_stock_product
        self._delete_product_inventory = delete_product_inventory
        self._register_admin = register_admin
        self._user_with_least_checkout = user_with_least_checkout
        self._user_with_most_checkout = user_with_most_checkout
        self._total_sales_renueve = total_sales_renueve
        self._step_admin = Step()
        optionAddItem = Option(
            text="1) agregar nuevo producto al inventario.",
            callback=self._store_product_inventory.Execute,
        )
        optionSeeInventory = Option(
            text="2) ver inventario.", callback=self._see_inventory.Execute
        )
        optionUpdateStock = Option(
            text="3) actualizar stock de un producto del inventario.",
            callback=self._update_stock_inventory.Execute,
        )
        optionDeleteProduct = Option(
            text="4) eliminar producto del inventario.",
            callback=self._delete_product_inventory.Execute,
        )
        optionCreateAdmin = Option(
            text="5) crear nuevo usuario administrador del sistema.",
            callback=self._register_admin.Execute,
        )
        optionUserWithMostCheckout = Option(
            text="6) ver el top 10 de los mejores compradores",
            callback=self._user_with_most_checkout.Execute,
        )

        optionUserWithLeastCheckout = Option(
            text="7) ver los usuarios que no tienen compras",
            callback=self._user_with_least_checkout.Execute,
        )

        optionTotalSalesRenueve = Option(
            text="8) ver ventas hechas", callback=self._total_sales_renueve.Execute
        )

        optionCloseSection = Option(
            text="9) cerrar session", callback=self.close_section
        )

        self._step_admin.addOption(optionAddItem)
        self._step_admin.addOption(optionSeeInventory)
        self._step_admin.addOption(optionUpdateStock)
        self._step_admin.addOption(optionDeleteProduct)
        self._step_admin.addOption(optionCreateAdmin)
        self._step_admin.addOption(optionUserWithMostCheckout)
        self._step_admin.addOption(optionUserWithLeastCheckout)
        self._step_admin.addOption(optionTotalSalesRenueve)
        self._step_admin.addOption(optionCloseSection)

    def show(self):
        Print.print_success("Elige la opcion deseada")
        self.init()

    def init(self):
        self._step_admin.excetute()
        self._step_admin.scan()

    def close_section(self):
        Print.print_success("cerrando session ...")
        Print.print_success("Cerrando programa ...")
        sys.exit()
