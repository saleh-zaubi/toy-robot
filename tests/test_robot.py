import pytest

from libs.direction.direction_factory import DirectionFactory
from libs.surface.table import Table
from toy.robot import Robot

class TestRobot:
    test_cases = [
                    ([[0, 0, "NORTH"], "MOVE", "REPORT"], (0,1,"NORTH")),
                    ([[0, 0, "NORTH"], "LEFT", "RIGHT", "RIGHT", "MOVE", "REPORT"], (1,0,"EAST")),
                    ([[4, 2, "WEST"], "MOVE", "MOVE", "LEFT", "RIGHT", "REPORT"], (2,2,"WEST")),
                    ([[1, 2, "EAST"], "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"], (3,3,"NORTH")),
                    ([[1, 2, "EAST"], "MOVE", "MOVE", "RIGHT", "MOVE", "RIGHT", "REPORT"], (3,1,"WEST")),
                    ([[3, 2, "SOUTH"], "LEFT", "REPORT"], (3,2,"EAST"))
                ]

    test_cases_exception = [
                    ([[1, -5, "SOUTH"], "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"], pytest.raises(ValueError)),
                    ([[1, 3, "PLA"], "MOVE", "MOVE", "MOVE", "REPORT"], pytest.raises(ValueError))
                ]

    @pytest.mark.parametrize("case, result", test_cases)
    def test_run(self, case: list, result: tuple):
        place, *actions = case
        surface = Table(5, 5)
        direction = DirectionFactory.getInstance(place[2])
        robot = Robot(place[0], place[1], direction, surface)
        for action in actions:
            action = action.lower()
            if action == "move":
                robot.move()
            elif action in ["left", "right"]:
                robot.turn(action)
            elif action == "report":
                break

        assert robot.getLocation() == result

    @pytest.mark.parametrize("case, result", test_cases_exception)
    def test_run_exception(self, case: list, result: tuple):
        with result:
            place = case[0]
            surface = Table(5, 5)
            direction = DirectionFactory.getInstance(place[2])
            Robot(place[0], place[1], direction, surface)