from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def migrate(self) -> str:
        pass
