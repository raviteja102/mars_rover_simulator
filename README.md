# Mars Rover Simulator

## Overview
The Mars Rover Simulator is a Python-based application developed as part of the assessment that simulates the movement of a rover on a 5x5 tabletop grid. The rover can be placed, moved, and turned  based on a set of commands provided via an input file. The simulator ensures that the rover does not fall off the table by validating its position before executing any movement.

## Features
- Rover can be placed at a specific position and direction on the grid.
- Move the rover one step forward in the direction it is facing when receives the MOVE command
- Rotate the rover left or right when it receives command either the  RIGHT or LEFT respectively.
- Report the current position along  with direction of the rover for the REPORT Command.
- Ensures it executes any other commands only after rover has been placed else they are ignored
- Ensures that rover is moved with the grid 5 * 5 units with origin as SOUTH-WEST
- Input commands from a file  are being processed as batch .

##  Grid layout (origin at SOUTH-WEST corner):

```text

        ^ NORTH
        |
  4 ┌───┬───┬───┬───┬───┐
    │   │   │   │   │   │
  3 ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
  2 ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
  1 ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
  0 └───┴───┴───┴───┴───┘
     0   1   2   3   4 → EAST

Directions:
    - NORTH: y increases
    - EAST:  x increases
    - SOUTH: y decreases
    - WEST:  x decreases

(0,0) is the bottom-left (SOUTH-WEST) corner of the grid.
Example Usage 
Sequence of Commands 
PLACE 
MOVE 
RIGHT
RIGHT 
RIGHT 
RIGHT 
RIGHT
LEFT 
REPORT

Explanation:
 - PLACE 0,0,NORTH puts the rover in the lower-left corner facing up.
 - MOVE will move the rover now to (0, 1) and facing the direction NORTH
 - RIGHT will turn the rover right and now its facing EAST.
 - RIGHT will turn the rover right and now its facing SOUTH.
 - RIGHT will turn the rover right and now its facing WEST.
 - RIGHT will turn the rover right and now its facing NORTH.
 - RIGHT will turn the rover right and now its facing EAST.
 - LEFT will turn the rover left and now its facing NORTH.
 - REPORT will report the position of rover 0,1,NORTH

## Project Structure
```text
mars_rover_simulator/
├── src/
│   ├── motion_planning.py      # Motion planning will read and process commands 
│   ├── rover.py                # Rover class for movements, contains functions for commands 
│   ├── table.py                # Table class for validation of boundary
├── tests/
│   ├── test_motion_planning.py # Unit tests for motion planning
│   ├── test_rover.py           # Unit tests for Rover class (movements, turns, placement)
│   ├── test_table.py           # Unit tests for Table class (boundary validation)
│   ├── test_input.txt          # Sample input file for testing
│   ├── test_input_two.txt      # Another sample input file
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd mars_rover_simulator

2. Install Dependencies: 
 - Ensure you have Python 3 installed. 
 - No additional dependencies are required for this project.

3. Run the Simulator: 
Use the following command to run the simulator with an input file:
        python3 src/motion_planning.py --file tests/test_input.txt
4. Run Tests: To run the unit tests, use:
        pytest tests/ 
        example pytest tests/test_table.py 
Input File Format
The input file should contain one command per line. 
Supported commands:

- PLACE X,Y,FACING - Places the rover at position (X, Y) facing FACING (e.g., NORTH, EAST, SOUTH, WEST).
- MOVE - Moves the rover one step forward in the direction it is facing.
- LEFT - Rotates the rover 90 degrees to the left.
- RIGHT - Rotates the rover 90 degrees to the right.
- REPORT - Outputs the current position and direction of the rover.

Example Input

PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT

Example Output

3,3,NORTH


Code Overview
- motion_planning.py : Reads commands from an input file and processes each command and interacts with the Rover and Table classes.
- rover.py : Implements the Rover class, which handles placing, moving, turning, and reporting about rover.
- table.py : Implements the Table class, which validates whether a position is within the 5x5 grid.
Testing
Unit tests are provided in the tests/ directory to ensure the correctness of the simulator. Use pytest to run the tests.

Author
Raviteja Burugu