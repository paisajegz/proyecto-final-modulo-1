from infraestructure.repository.checkout_repository import CheckoutRepository
from infraestructure.console.show_message import Print


class TotalSalesRenueve:
    _repo_checkout: CheckoutRepository

    def __init__(
        self, repo_checkout: CheckoutRepository = CheckoutRepository()
    ) -> None:
        self._repo_checkout = repo_checkout

    def Execute(self):
        sale_renueve = self._repo_checkout.show_sale_revenue()
        Print.print_default("#######################################################")
        Print.print_default(sale_renueve.to_string())
        Print.print_default("#######################################################")
