from infraestructure.console.show_message import Print
from infraestructure.repository.history_repository import HistoryRepository
from infraestructure.repository.product_repository import ProductRepository


class DeleteProductInventory:
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
            Print.print_success("iniciando proceso de eliminacion de productos")
            Print.print_default("digite el id del producto que desea eliminar:")
            id_product = int(Print.scan())
            product = self._repo_product.show_product_by_id(id_product)
            if product.name == "":
                Print.print_warning("el producto que desea eliminar no existe")
                return
            delete = self._repo_product.delete_product(id_product)
            if not delete:
                Print.print_warning("error al eliminar el producto")
                return
            Print.print_success("producto eliminado sastifactoriamente")
        except ValueError:
            Print.print_warning("formato invalido del id del producto")
