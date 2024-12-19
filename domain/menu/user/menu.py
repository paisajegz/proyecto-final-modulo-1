from domain.menu.option import Option
from infraestructure.console.show_message import Print
from domain.menu.steps import Step
from domain.inventory.see_inventory import SeeInventory
from domain.sales.add_item_checkout import AddItemCheckout
from domain.sales.see_item_checkout import SeeItemCheckout
from infraestructure.session.index import SessionProvider
import sys


class MenuUser:
    _step_user: Step
    _see_inventory_handler: SeeInventory
    _add_item_checkout: AddItemCheckout
    _see_item_checkout: SeeItemCheckout

    def __init__(
        self,
        see_inventory: SeeInventory = SeeInventory(),
        add_item_checkout: AddItemCheckout = AddItemCheckout(),
        see_item_checkout: SeeItemCheckout = SeeItemCheckout(),
    ) -> None:
        self._see_inventory_handler = see_inventory
        self._add_item_checkout = add_item_checkout
        self._see_item_checkout = see_item_checkout
        self._step_user = Step()
        optionCheckout = Option(
            text="1) ver historial de compras", callback=self._see_item_checkout.Execute
        )
        optionBuy = Option(
            text="2) hacer una compra", callback=self._add_item_checkout.Execute
        )
        optionSee = Option(
            text="3) solo quiero mirar productos",
            callback=self._see_inventory_handler.Execute,
        )
        optionExit = Option(
            text="4) salir y cerrar session", callback=self.close_section
        )
        self._step_user.addOption(optionCheckout)
        self._step_user.addOption(optionBuy)
        self._step_user.addOption(optionSee)
        self._step_user.addOption(optionExit)

    def show(self):
        Print.print_success("Elige la opcion deseada")
        self.init()

    def init(self):
        self._step_user.excetute()
        self._step_user.scan()

    def close_section(self):
        Print.print_success("cerrando session ...")
        Print.print_success("Cerrando programa ...")
        sys.exit()
