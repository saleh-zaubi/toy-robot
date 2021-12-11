from surface import Surface
from robot import Robot
from typing import Union

class ToyRobotApp:

    def __init__(self) -> None:
        self.__command: Union[None, str] = None
        self.__action: Union[None, str] = None
        self.__robot: Union[None, Robot] = None
        self.__data: list = []
        self.__messages: list = []

    def run(self) -> None:
        while True:
            self.__command = input().lower().strip()
            if self.__command == "exit":
                break
            self.__setAction()
            self.__execute()
            while self.__messages:
                print(self.__messages.pop(0))

    def __execute(self) -> None:
        if self.__action == "place":
            self.__inializeRobot()
        elif self.__action == "move":
            self.__robot.move()
        elif self.__action in ["left", "right"]:
            self.__robot.turn(self.__action)
        elif self.__action == "report":
            self.__messages.append(self.__robot.getLocation())
        else:
            self.__messages.append("Invalid command!")

    def __setAction(self) -> None:
        if self.__command.startswith("place"):
            self.__action = "place"
        elif self.__robot is not None:
            self.__action = self.__command
        else:
            self.__action = None

    def __inializeRobot(self) -> None:
        self.__rest()
        self.__setData()
        self.__buildRobot()

    def __rest(self) -> None:
        if self.__robot is not None:
            self.__robot = None
            self.__messages.append("Reset...")

    def __setData(self) -> None:
        data = self.__command[5:].split(",")
        self.__data = [int(x) if x.strip().isnumeric() else x.strip() for x in data]

    def __buildRobot(self) -> None:
        try:
            surface = Surface(5, 5)
            self.__robot = Robot(self.__data[0], self.__data[1], self.__data[2], surface)
        except ValueError:
            self.__messages.append("Invalid robot values (x,y,direction)!")
        except IndexError:
            self.__messages.append("Invalid place command!")

def main():
    toy_robot = ToyRobotApp()
    toy_robot.run()

if __name__ == "__main__":
    main()
