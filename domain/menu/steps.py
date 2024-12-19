from domain.menu.option import Option
from infraestructure.console.show_message import Print


class Step:
    _options: list

    def __init__(self) -> None:
        self._options = []

    def addOption(self, option: Option):
        self._options.append(option)

    def excetute(self):
        for option in self._options:
            opt: Option = option
            Print.print_default(opt.text)

    def scan(self):
        try:
            data = int(input(""))
            if data > len(self._options) or data <= 0:
                Print.print_warning(f"el dato debe ser entre 0 y {len(self._options)}")
                self.excetute()
                self.scan()
                return
            opt: Option = self._options[data - 1]
            opt.run()
        except ValueError:
            Print.print_warning("error al elegir opcion se repetira el menu")
            self.scan()
