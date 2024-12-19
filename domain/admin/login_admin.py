from domain.menu.admin.menu import MenuAdmin
from infraestructure.repository.admin_repository import AdminRepository

from infraestructure.console.show_message import Print
from infraestructure.crypt.index import Crypt
from infraestructure.session.index import Session, SessionProvider


class LoginAdmin:
    _repo_admin: AdminRepository
    _menu_admin: MenuAdmin

    def __init__(
        self,
        repo_admin: AdminRepository = AdminRepository(),
        menu_admin: MenuAdmin = MenuAdmin(),
    ) -> None:
        self._repo_admin = repo_admin
        self._menu_admin = menu_admin

    def Execute(self):
        session = SessionProvider.get_session()
        if session.type_user == "admin":
            self._menu_admin.show()
            return
        Print.print_success("iniciando proceso de login para el usuario")
        Print.print_default("digite el correo:")
        email = Print.scan()
        Print.print_default("digite la clave:")
        password = Print.scan()
        Print.print_default("procesando ...")
        user = self._repo_admin.login_admin(email)
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
        session.id_user = user.id
        session.type_user = "admin"
        session.first_name = user.first_name
        session.last_name = user.last_name
        session.email = user.email
        SessionProvider.set_session(session)
        Print.print_success("Bienvenido usuario")
        self._menu_admin.show()
