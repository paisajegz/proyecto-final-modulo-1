from infraestructure.console.show_message import Print
from infraestructure.repository.product_repository import ProductRepository


class SeeInventory:
    _repo_product: ProductRepository

    def __init__(self, repo_product: ProductRepository = ProductRepository()) -> None:
        self._repo_product = repo_product

    def Execute(self):
        Print.print_success("ejecutar proceso mirar productos")
        products = self._repo_product.show_products()
        Print.print_default("#######################################################")
        if len(products) == 0:
            Print.print_default("no hay productos registrados")
        for product in products:
            Print.print_default(product.to_string())
            Print.print_default(
                "#######################################################"
            )
