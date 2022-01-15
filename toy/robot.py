from libs.direction.direction import Direction
from libs.location.location import Location
from libs.surface.surface import Surface

class Robot:

    def __init__(self, x_coordinate: int, y_coordinate: int, direction: Direction, surface: Surface) -> None:
        self.__surface = surface
        self.__direction = direction
        self.__setCoordinates(x_coordinate, y_coordinate)

    def __setCoordinates(self, x_coordinate: int, y_coordinate: int) -> None:
        self.__validateCoordinate(x_coordinate, y_coordinate)
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def __validateCoordinate(self, x_coordinate: int, y_coordinate: int) -> None:
        if not self.__surface.isValidPosition(x_coordinate, y_coordinate):
            raise ValueError("Invalid Robot Coordinates")

    def turn(self, to: str) -> None:
        if to == "left":
            self.__direction = self.__direction.left()
        elif to == "right":
            self.__direction = self.__direction.right()

    def move(self) -> None:
        new_x_coordinate = self.__x_coordinate + self.__direction.adjusment.get("x")
        new_y_coordinate = self.__y_coordinate + self.__direction.adjusment.get("y")

        if self.__surface.isValidPosition(new_x_coordinate, new_y_coordinate):
            self.__x_coordinate = new_x_coordinate
            self.__y_coordinate = new_y_coordinate

    def getLocation(self) -> tuple:
        location = Location(self.__x_coordinate, self.__y_coordinate, self.__direction.direction)
        return location.getInfo()
