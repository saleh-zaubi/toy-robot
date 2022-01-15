from abc import ABC, abstractmethod


class Surface(ABC):

    @abstractmethod
    def isValidPosition(self, x, y) -> bool:
        pass
