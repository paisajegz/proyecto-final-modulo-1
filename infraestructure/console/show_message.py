class Print:
    # Definimos los códigos de color ANSI para los colores deseados
    COLORS = {
        "green": "\033[32m",  # Verde para éxito
        "red": "\033[31m",  # Rojo para advertencias
        "white": "\033[37m",  # Blanco por defecto
        "reset": "\033[39m",  # Restablecer color por defecto
    }

    @staticmethod
    def print_success(text: str) -> None:
        """Imprime un mensaje en color verde (éxito)."""
        print(f"{Print.COLORS['green']}{text}{Print.COLORS['reset']}")

    @staticmethod
    def print_warning(text: str) -> None:
        """Imprime un mensaje en color rojo (advertencia)."""
        print(f"{Print.COLORS['red']}{text}{Print.COLORS['reset']}")

    @staticmethod
    def print_default(text: str) -> None:
        """Imprime un mensaje en color blanco (por defecto)."""
        print(f"{Print.COLORS['white']}{text}{Print.COLORS['reset']}")

    @staticmethod
    def scan() -> str:
        return input("")
