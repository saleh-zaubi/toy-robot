
# ToyRobot
Python version: 3.8.10

Packages: pytest, pytest-cov



# Usage
Run the main.py file

Execute the commands


Ex:

 - Inputs:

	   PLACE 0,0,NORTH
	   
	   MOVE
	   
	   REPORT


 - Output:

	   0,1,NORTH



At anytime you can type "exit" to exit the app



# Test
Run the command:

    python -m pytest --cov . tests/

or for html report:

    python -m pytest --cov . --cov-report html:tests/coverage tests/

(Optional) Add more cases to the test_cases variable in the tests/test_robot.py file


# Run the app using docker
- Build the image:
 
        docker build -t toy-robot-app:1.0

- Create container using the image:

        docker run -it toy-robot-app:1.0
        
- execute your commands
