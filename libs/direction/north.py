from libs.direction.direction import Direction
import libs.direction.east as east
import libs.direction.west as west


class North(Direction):

    def __init__(self) -> None:
        self.direction = "north"
        self.adjusment = {"x" : 0, "y": 1}

    def left(self) -> Direction:
        return west.West()

    def right(self) -> Direction:
        return east.East()