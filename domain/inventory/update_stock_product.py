from infraestructure.console.show_message import Print
from infraestructure.repository.dto.history import History
from infraestructure.repository.history_repository import HistoryRepository
from infraestructure.repository.product_repository import ProductRepository
from infraestructure.session.index import SessionProvider


class UpdateStockInventory:
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
            Print.print_success("iniciando proceso de actualizacion de stock")
            Print.print_default("digite id del producto:")
            id = int(Print.scan())
            product = self._repo_product.show_product_by_id(id)
            if product.name == "":
                Print.print_warning("producto no encontrado")
                return
            Print.print_default("digite cantidad deseada a agregar:")
            quantity = int(Print.scan())
            history = History()
            history.id_user = SessionProvider.get_session().id_user
            history.id_product = product.id
            history.quantity = quantity
            history.type_history = "update_stock"
            insert_history = self._repo_history.add_history(history)
            if not insert_history:
                Print.print_warning("no se puede guardar historial del producto")
                return
            product.quantity += quantity
            update_stock = self._repo_product.update_stock(product.id, product.quantity)
            if not update_stock:
                Print.print_warning("no se puede actualzar el stock")
                return
            Print.print_success(f"stock del producto actualizado a {product.quantity}")

        except ValueError:
            Print.print_warning("error digitando stock")
