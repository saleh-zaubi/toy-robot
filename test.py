import pytest
from surface import Surface
from robot import Robot

class TestToyRobot:
    test_cases = [
                    ([[0, 0, "NORTH"], "MOVE", "REPORT"], "0,1,NORTH"),
                    ([[0, 0, "NORTH"], "LEFT", "REPORT"], "0,0,WEST"),
                    ([[1, 2, "EAST"], "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"], "3,3,NORTH")
                ]

    @pytest.mark.parametrize(('case', 'result'), test_cases)
    def test_run(self, case: list, result: str):
        place, *actions = case
        surface = Surface(5, 5)
        robot = Robot(place[0], place[1], place[2], surface)
        for action in actions:
            action = action.lower()
            if action == "move":
                robot.move()
            elif action in ["left", "right"]:
                robot.turn(action)
            elif action == "report":
                break
                
        
        assert robot.getLocation() == result