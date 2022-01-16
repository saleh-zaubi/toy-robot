from abc import ABC, abstractmethod

class Direction(ABC):

    @staticmethod
    def directions() -> list:
        return ["north", "south", "east", "west"]

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def _direction(self, dir: str) -> None:
        self.__direction = dir

    @property
    def adjusment(self) -> dict:
        return self.__adjusment

    @adjusment.setter
    def _adjusment(self, adjustment: dict) -> None:
        self.__adjusment = adjustment

    @abstractmethod
    def left(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass

