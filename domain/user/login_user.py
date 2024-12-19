from domain.menu.user.menu import MenuUser
from infraestructure.repository.user_repository import UserRepository
from infraestructure.console.show_message import Print
from infraestructure.crypt.index import Crypt
from infraestructure.session.index import Session, SessionProvider


class LoginUser:
    _repo_user: UserRepository
    _menu_user: MenuUser

    def __init__(
        self,
        repo_user: UserRepository = UserRepository(),
        menu_user: MenuUser = MenuUser(),
    ) -> None:
        self._repo_user = repo_user
        self._menu_user = menu_user

    def Execute(self):
        session = SessionProvider.get_session()
        if session.type_user == "user":
            self._menu_user.show()
            return
        Print.print_success("iniciando proceso de login para el usuario")
        Print.print_default("digite el correo:")
        email = Print.scan()
        Print.print_default("digite la clave:")
        password = Print.scan()
        Print.print_default("procesando ...")
        user = self._repo_user.login_user(email)
        if user.email == "":
            Print.print_warning("Usuario no Logeado por favor vuelva a intentar.")
            return
        passwordValid = Crypt.verify_password(password, user.password)
        if not passwordValid:
            Print.print_warning(
                "Usuario con clave erronea, por favor vuelva a intentar."
            )
            return
        session = Session()
        session.type_user = "user"
        session.id_user = user.id
        session.first_name = user.first_name
        session.last_name = user.last_name
        session.email = user.email
        session._count_buyer = user.count_checkout
        SessionProvider.set_session(session)
        Print.print_success("Bienvenido usuario")
        self._menu_user.show()
