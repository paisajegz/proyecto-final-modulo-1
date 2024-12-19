from infraestructure.repository.checkout_repository import CheckoutRepository
from infraestructure.session.index import SessionProvider
from infraestructure.console.show_message import Print


class SeeItemCheckout:
    _repo_checkout: CheckoutRepository

    def __init__(
        self, repo_checkout: CheckoutRepository = CheckoutRepository()
    ) -> None:
        self._repo_checkout = repo_checkout

    def Execute(self):
        session = SessionProvider.get_session()
        checkouts = self._repo_checkout.show_checkout_by_user(session.id_user)
        Print.print_default("#######################################################")
        if len(checkouts) == 0:
            Print.print_warning("no hay ventas registrados")
        for checkout in checkouts:
            Print.print_default(checkout.to_string())
            Print.print_default(
                "#######################################################"
            )
