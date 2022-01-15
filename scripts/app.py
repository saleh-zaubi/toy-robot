from typing import Union
from scripts.custom_parser import CustomArgsParser
from libs.surface.table import Table
from libs.direction.direction_factory import DirectionFactory
from toy.robot import Robot

class ToyRobotApp:

    def __init__(self) -> None:
        self.__command: Union[None, str] = None
        self.__command_data: list = []
        self.__place_command_parser: Union[None, CustomArgsParser] = None
        self.__robot: Union[None, Robot] = None
        self.__messages: list = []

    def run(self) -> None:
        while True:
            self.__command = input().lower().strip()
            if self.__command == "exit":
                break
            self.__execute()
            while self.__messages:
                print(self.__messages.pop(0))

    def __execute(self) -> None:
        if self.__command.startswith("place") or self.__robot is None:
            self.__inializeRobot()
        elif self.__command == "move":
            self.__robot.move()
        elif self.__command in ["left", "right"]:
            self.__robot.turn(self.__command)
        elif self.__command == "report":
            self.__messages.append(self.__robot.getLocation())
        else:
            self.__messages.append("Invalid command!")

    def __inializeRobot(self) -> None:
        self.__prepareCommandArgs()
        self.__setCommandArgs()
        self.__buildRobot()

    def __prepareCommandArgs(self) -> None:
        data = self.__command.split(" ", 1)
        if len(data) > 1:
            data += data.pop(1).split(",")
            data = [x.strip() for x in data]

        self.__command_data = data

    def __setCommandArgs(self) -> None:
        self.__place_command_parser = CustomArgsParser(description='Handle robot place commands')
        self.__place_command_parser.add_argument('place', metavar='place', choices=["place"], type=str, nargs=1, help="Place command")
        self.__place_command_parser.add_argument('x_coordinate', metavar='x', type=int, nargs=1,
                            help='An integer for the x coordinate of the robot')
        self.__place_command_parser.add_argument('y_coordinate', metavar='y', type=int, nargs=1,
                            help='An integer for the y coordinate of the robot')
        self.__place_command_parser.add_argument('facing', metavar='facing', choices=["north", "south", "east", "west"], type=str, nargs=1,
                            help='A string for the current direction of the robot')

    def __buildRobot(self) -> None:
        try:
            place_command_args = self.__place_command_parser.parse_args(self.__command_data)
            surface = Table(5, 5)
            direction = DirectionFactory.getInstance(place_command_args.facing[0])
            self.__robot = Robot(place_command_args.x_coordinate[0], place_command_args.y_coordinate[0], direction, surface)
        except SystemExit:
            self.__messages.append("Try again!")
        except ValueError as e:
            self.__messages.append(str(e))
