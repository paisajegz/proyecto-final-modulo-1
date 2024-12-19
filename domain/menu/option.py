from typing import Callable


class Option:
    _text: str
    _callback: Callable[[], None]

    def __init__(self, text: str, callback: Callable[[], None]) -> None:
        self._text = text
        self._callback = callback

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    def run(self):
        self._callback()
