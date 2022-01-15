from libs.surface.surface import Surface


class Table(Surface):

    def __init__(self, x_axis_length: int, y_axis_length: int) -> None:
        self.x_axis_length = x_axis_length
        self.y_axis_length = y_axis_length

    @property
    def x_axis_length(self) -> int:
        return self.__x_axis_length

    @x_axis_length.setter
    def x_axis_length(self, value) -> None:
        self.__validateAxisLength(value)
        self.__x_axis_length = value

    @property
    def y_axis_length(self) -> int:
        return self.__y_axis_length

    @y_axis_length.setter
    def y_axis_length(self, value) -> None:
        self.__validateAxisLength(value)
        self.__y_axis_length = value

    def __validateAxisLength(self, value) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid Surface Axis Length")

    def isValidPosition(self, x, y):
        if self.__isValidPoint(x, self.x_axis_length) and self.__isValidPoint(y, self.y_axis_length):
            return True

        return False

    def __isValidPoint(self, val: int, compare_to: int) -> bool:
        if isinstance(val, int) and val >= 0 and val <= compare_to:
            return True

        return False
