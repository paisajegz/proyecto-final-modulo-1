from infraestructure.console.show_message import Print
from infraestructure.repository.dto.product import Product
from infraestructure.repository.history_repository import HistoryRepository
from infraestructure.repository.product_repository import ProductRepository


class StoreItemInventory:
    _repo_product: ProductRepository
    _repo_history: HistoryRepository

    def __init__(
        self,
        repo_product: ProductRepository = ProductRepository(),
        repo_history: HistoryRepository = HistoryRepository(),
    ) -> None:
        self._repo_product = repo_product
        self._repo_history = repo_history

    def Execute(self):
        try:
            product = Product()
            Print.print_success("iniciando proceso para almnacenar productos")
            Print.print_default("digite nombre:")
            product.name = Print.scan()
            Print.print_default("digite cantidad:")
            product.quantity = int(Print.scan())
            Print.print_default("digite precio del producto:")
            product.price = float(Print.scan())
            register = self._repo_product.add_product(product)
            if not register:
                Print.print_warning("error insertando producto")
                return
            Print.print_success("producto insertado sastifactoriamente")
        except ValueError:
            Print.print_warning("error al ingresar formato de datos")
            self.Execute()
