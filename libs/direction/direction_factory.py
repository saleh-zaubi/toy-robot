from libs.direction.direction import Direction
from libs.direction.east import East
from libs.direction.north import North
from libs.direction.south import South
from libs.direction.west import West

class DirectionFactory:

    @staticmethod
    def getInstance(dir: str) -> Direction:
        dir = dir.lower()
        if dir in Direction.directions():
            if dir == "north":
                return North()
            if dir == "south":
                return South()
            if dir == "west":
                return West()
            if dir == "east":
                return East()
        
        raise ValueError("Unsupported direction")