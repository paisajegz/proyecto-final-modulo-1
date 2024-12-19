from infraestructure.repository.user_repository import UserRepository
from infraestructure.console.show_message import Print


class UserWithLeastCheckout:
    _repo_user: UserRepository

    def __init__(self, repo_user: UserRepository = UserRepository()) -> None:
        self._repo_user = repo_user

    def Execute(self):
        Print.print_success("clientes que nunca ha realizado compras")
        topListUser = self._repo_user.user_least_checkout()
        if len(topListUser) == 0:
            Print.print_warning("no hay usuarios registrados en el sistema")
        Print.print_default("#######################################################")
        for user in topListUser:
            Print.print_default(user.to_string())
            Print.print_default(
                "#######################################################"
            )
