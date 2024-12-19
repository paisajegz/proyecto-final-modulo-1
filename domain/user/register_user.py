from domain.menu.user.menu import MenuUser
from infraestructure.crypt.index import Crypt
from infraestructure.repository.dto.user import User
from infraestructure.repository.user_repository import UserRepository
from infraestructure.console.show_message import Print


class RegisterUser:
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
        user = User()
        Print.print_success("Iniciando proceso de registro para el usuario")
        Print.print_default("digite nombres:")
        user.first_name = Print.scan()
        Print.print_default("digite apellidos:")
        user.last_name = Print.scan()
        Print.print_default("digite email:")
        user.email = Print.scan()
        Print.print_default("digite clave:")
        password = Print.scan()
        user.password = Crypt.encrypt_password(password)
        Print.print_default("Procesando ...")
        register = self._repo_user.add_user(user)
        if not register:
            Print.print_warning("el usuario no se pudo registrar")
            return
        Print.print_success("usuario registrado sastifactoriamente")
        Print.print_default("deseas iniciar session (si,no) ?")
        init_session = Print.scan()
        if init_session.upper() == "NO":
            return
        if init_session.upper() == "SI":
            Print.print_success("Bienvendo usuario")
            self._menu_user.show()
            return
