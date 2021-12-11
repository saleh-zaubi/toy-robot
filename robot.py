from surface import Surface


class Robot:
    
    __directions = ['north', 'east', 'south', 'west']
    __directions_to_value = {"north": 1, "east": 1, "south": -1, "west": -1}
    __to = {"left": -1, "right": 1}

    def __init__(self, x_coordinate: int, y_coordinate: int, direction: str, surface: Surface) -> None:
        self.__surface = surface
        self.__setCoordinates(x_coordinate, y_coordinate)
        self.__setDirection(direction)

    def __setCoordinates(self, x_coordinate: int, y_coordinate: int) -> None:
        self.__validateCoordinate(x_coordinate, "x", "set")
        self.__validateCoordinate(y_coordinate, "y", "set")
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def __validateCoordinate(self, coordinate: int, type: str, action="move") -> bool:
        if isinstance(coordinate, int) and coordinate >= 0:
            if (type == "x" and coordinate <= self.__surface.x_axis_length) or (type == "y" and coordinate <= self.__surface.y_axis_length):
                return True

        if action == "set":
            raise ValueError("Invalid Robot Coordinates")

        return False

    def __setDirection(self, direction: str) -> None:
        self.__validateDirection(direction)
        self.__direction = direction.lower()

    def __validateDirection(self, direction: str) -> None:
        if not isinstance(direction, str) or direction.lower() not in self.__directions:
            raise ValueError("Invalid Robot Facing")

    def __validateTurn(self, to: str) -> bool:
        if isinstance(to, str) and to.lower() in self.__to:
            return True

        return False

    def __getIndex(self, val: int) -> int:
        new_index = self.__directions.index(self.__direction) + val
        turns_list_last_index = len(self.__directions) - 1

        if new_index > turns_list_last_index:
            return 0
        elif new_index < 0:
            return turns_list_last_index

        return new_index

    def turn(self, to: str) -> None:
        if self.__validateTurn(to):
            self.__direction = self.__directions[self.__getIndex(self.__to.get(to.lower()))]

    def move(self) -> None:
        value_to_add = self.__directions_to_value.get(self.__direction)
        if self.__directions.index(self.__direction) % 2 == 0:
            if self.__validateCoordinate(self.__y_coordinate + value_to_add, "y"):
                self.__y_coordinate += value_to_add
        else:
            if self.__validateCoordinate(self.__x_coordinate + value_to_add, "x"):
                self.__x_coordinate += value_to_add

    def getLocation(self) -> str:
        return f"{self.__x_coordinate},{self.__y_coordinate},{self.__direction.upper()}"
