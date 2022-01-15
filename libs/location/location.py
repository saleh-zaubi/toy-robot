from libs.direction.direction import Direction


class Location:

    def __init__(self, x: int, y: int, dir: str) -> None:
        self.x_aixs = x
        self.y_aixs = y
        self.direction = dir

    @property
    def x_aixs(self) -> int:
        return self.__x_axis

    @x_aixs.setter
    def x_aixs(self, x: int) -> None:
        self.__validateValue(x)
        self.__x_axis = x

    @property
    def y_aixs(self) -> int:
        return self.__y_axis

    @y_aixs.setter
    def y_aixs(self, y: int) -> None:
        self.__validateValue(y)
        self.__y_axis = y

    def __validateValue(self, val: int) -> None:
        if not isinstance(val, int) and val < 0:
            raise ValueError("Invalid coordinates!")

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, dir: str) -> None:
        self.__validateDirection(dir)
        self.__direction = dir.upper()

    def __validateDirection(self, dir: str) -> None:
        if not isinstance(dir, str) or dir.lower() not in Direction.directions():
            raise ValueError("Invalid direction!")

    def getInfo(self) -> tuple:
        return (self.x_aixs, self.y_aixs, self.direction)