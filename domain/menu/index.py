from domain.admin.login_admin import LoginAdmin
from domain.menu.steps import Step
from domain.user.login_user import LoginUser
from domain.user.register_user import RegisterUser
from infraestructure.console.show_message import Print
from domain.menu.option import Option
import sys

from infraestructure.session.index import SessionProvider


class Menu:
    _step_main: Step
    _register_user: RegisterUser
    _login_user: LoginUser
    _login_admin: LoginAdmin

    def __init__(
        self,
        register_user: RegisterUser = RegisterUser(),
        login_user: LoginUser = LoginUser(),
        login_admin: LoginAdmin = LoginAdmin(),
    ):
        self._login_user = login_user
        self._login_admin = login_admin
        self._register_user = register_user
        self._step_main = Step()
        optionAdmin = Option(
            text="1) soy administrador", callback=self._login_admin.Execute
        )
        optionUser = Option(text="2) Soy Un Usuario", callback=self._login_user.Execute)
        optionRegisterUser = Option(
            text="3) Registrar usuario", callback=self._register_user.Execute
        )
        optionCloseProgram = Option(
            text="4) Cerrar programa", callback=self.handler_close_programa
        )
        self._step_main.addOption(optionAdmin)
        self._step_main.addOption(optionUser)
        self._step_main.addOption(optionRegisterUser)
        self._step_main.addOption(optionCloseProgram)

    def show(self):
        Print.print_success("Bienvenidos a la tienda Online Mercado.com")
        self.init()

    def init(self):
        while True:
            session = SessionProvider.get_session()
            if session.type_user == "user":
                self._login_user.Execute()

            elif session.type_user == "admin":
                self._login_admin.Execute()
                return
            else:
                self._step_main.excetute()
                self._step_main.scan()

    def handler_close_programa(self):
        Print.print_success("gracias por usarnos")
        Print.print_success("cerrando programa")
        sys.exit()
