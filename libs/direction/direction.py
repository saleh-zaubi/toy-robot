from abc import ABC, abstractmethod

class Direction(ABC):

    @staticmethod
    def directions() -> list:
        return ["north", "south", "east", "west"]

    @property
    def direction(self) -> str:
        return self._direction

    @direction.setter
    def direction(self, dir: str) -> None:
        self._direction = dir

    @property
    def adjusment(self) -> dict:
        return self._adjusment

    @adjusment.setter
    def adjusment(self, adjustment: dict) -> None:
        self._adjusment = adjustment

    @abstractmethod
    def left(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass

