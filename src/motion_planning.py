"""
Author: Raviteja Burugu
Date: 2025-04-29
Description: Rover class for movements on the 5x5 tabletop.
"""
import argparse
from rover import Rover 
from table import Table 

def read_commands(file_path):
    """
    Reads commands from the specified file.

    Args:
        file_path (str): Path to the input file containing commands.

    Returns:
        list: A list of commands as strings, with whitespace stripped.
    """
    with open(file_path, 'r') as f: 
        return [line.strip() for line in f if line.strip()]

def parse_place_command(command):
    """
    Parses a PLACE command to extract the x, y coordinates and facing direction.

    Args:
        command (str): The PLACE command string (e.g., "PLACE 1,2,NORTH").

    Returns:
        tuple: A tuple (x, y, facing) if the command is valid, otherwise None.
    """
    try:
        _, args = command.split(" ")
        x_str, y_str, facing = args.split(",")
        return int(x_str), int(y_str), facing.upper()
    except ValueError:
        print(f"Not a valid PLACE format: {command}")
        return None 
    
def process_command(rover, command):
    """
    Processes a single command and performs the corresponding action on the rover.

    Args:
        rover (Rover): The rover object to execute the command on.
        command (str): The command to process (e.g., "MOVE", "LEFT", "PLACE 1,2,NORTH").
    """
    if command.startswith("PLACE"):
        result = parse_place_command(command)
        if result:
            x, y, facing = result
            rover.place(x, y, facing)
    elif command == "REPORT":
        report = rover.report()
        if report:
            print(report)   
    elif command == "MOVE":
        rover.move()
    elif command == "RIGHT":
        rover.turn("right")
    elif command == "LEFT":
        rover.turn("left")

def main():
    """
    Main function to start the motion planning of the rover.

    Parses command-line arguments, reads commands from the input file, and processes them.
    """
    # print("Motion planning of rover started.")
    parser = argparse.ArgumentParser(description="Mars Rover Simulator") 
    parser.add_argument("--file", type=str, required=True, help="Path to input file")
    args = parser.parse_args()
    # print(f"Read commands from a file: {args.file}")
    commands = read_commands(args.file)
    rover = Rover(Table())
    for command in commands:
        process_command(rover, command)        

if __name__ == "__main__":
    main()