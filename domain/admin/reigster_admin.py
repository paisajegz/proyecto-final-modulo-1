from infraestructure.repository.admin_repository import AdminRepository
from infraestructure.console.show_message import Print
from infraestructure.crypt.index import Crypt
from infraestructure.repository.dto.admin import Admin


class RegisterAdmin:
    _repo_admin: AdminRepository

    def __init__(
        self,
        repo_admin: AdminRepository = AdminRepository(),
    ) -> None:
        self._repo_admin = repo_admin

    def Execute(self):
        admin = Admin()
        Print.print_success("Iniciando proceso de registro para el administrador")
        Print.print_default("digite nombres:")
        admin.first_name = Print.scan()
        Print.print_default("digite apellidos:")
        admin.last_name = Print.scan()
        Print.print_default("digite email:")
        admin.email = Print.scan()
        Print.print_default("digite clave:")
        password = Print.scan()
        admin.password = Crypt.encrypt_password(password)
        Print.print_default("Procesando ...")
        register = self._repo_admin.add_admin(admin)
        if not register:
            Print.print_warning("el administrador no se pudo registrar")
            return
        Print.print_success("administrador registrado sastifactoriamente")
