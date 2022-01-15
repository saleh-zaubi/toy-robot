from libs.direction.direction import Direction
import libs.direction.north as north
import libs.direction.south as south


class West(Direction):

    def __init__(self) -> None:
        self._direction = "west"
        self._adjusment = {"x" : -1, "y": 0}

    def left(self) -> Direction:
        return south.South()

    def right(self) -> Direction:
        return north.North()