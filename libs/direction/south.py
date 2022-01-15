from libs.direction.direction import Direction
import libs.direction.east as east
import libs.direction.west as west


class South(Direction):

    def __init__(self) -> None:
        self._direction = "south"
        self._adjusment = {"x" : 0, "y": -1}

    def left(self) -> Direction:
        return east.East()

    def right(self) -> Direction:
        return west.West()