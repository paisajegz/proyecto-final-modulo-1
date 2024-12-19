from infraestructure.repository.checkout_repository import CheckoutRepository
from infraestructure.console.show_message import Print
from infraestructure.repository.dto.checkout import Checkout
from infraestructure.repository.product_repository import ProductRepository
from infraestructure.repository.user_repository import UserRepository
from infraestructure.session.index import SessionProvider


class AddItemCheckout:
    _repo_checkout: CheckoutRepository
    _repo_product: ProductRepository
    _repo_user: UserRepository

    def __init__(
        self,
        repo_checkout: CheckoutRepository = CheckoutRepository(),
        repo_product: ProductRepository = ProductRepository(),
        repo_user: UserRepository = UserRepository(),
    ) -> None:
        self._repo_checkout = repo_checkout
        self._repo_product = repo_product
        self._repo_user = repo_user

    def Execute(self):
        try:
            Print.print_success("iniciando proceso de hacer compras")
            Print.print_success("Mostrando items")
            products = self._repo_product.show_products()
            Print.print_default(
                "#######################################################"
            )
            if len(products) == 0:
                Print.print_warning("no hay productos en el inventario")
                return
            for product in products:
                Print.print_default(product.to_string())
                Print.print_default(
                    "#######################################################"
                )
            Print.print_success("advertencia solo puedes comprar un producto")
            Print.print_default("busca por id el item que quiere comprar:")
            id_product = int(Print.scan())
            product = self._repo_product.show_product_by_id(id_product)
            if product.name == "":
                Print.print_warning("id del producto invalido")
                return
            Print.print_default("digite cantidad del producto a comprar")
            quantity = int(Print.scan())
            if product.quantity < quantity:
                Print.print_warning("stock insuficiente del producto")
                return
            checkout = Checkout()
            checkout.id_product = product.id
            checkout.id_user = SessionProvider.get_session().id_user
            checkout.quantity = quantity
            checkout.price = product.price
            register_checkout = self._repo_checkout.add_checkout(checkout)
            if not register_checkout:
                Print.print_warning("error registrando venta")
                return
            self._repo_checkout
            product.quantity -= quantity
            update_stock = self._repo_product.update_stock(product.id, product.quantity)
            if not update_stock:
                Print.print_warning("no se pudo actualizar el stock del producto")
                return
            session = SessionProvider.get_session()
            session._count_buyer += 1
            update_user = self._repo_user.update_count_stock(
                session.id_user, session._count_buyer
            )
            if not update_user:
                Print.print_warning("no se pudo actualizar el stock del usuario")
                return
            Print.print_success("compra registrada sastifactoriamente")
        except ValueError:
            Print.print_warning("error al digitar un dato dentro de la compra")
