from libs.direction.direction import Direction
import libs.direction.north as north
import libs.direction.south as south


class East(Direction):

    def __init__(self) -> None:
        self._direction = "east"
        self._adjusment = {"x" : 1, "y": 0}

    def left(self) -> None:
        return north.North()

    def right(self) -> None:
        return south.South()