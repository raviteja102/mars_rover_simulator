import pytest
from src.rover import Rover
from src.table import Table

def test_rover_place():
    rover = Rover(Table())
    rover.place(0, 0, "SOUTH") 
    assert rover.report() == "0,0,SOUTH"

def test_rover_place_invalid_position():
    rover = Rover(Table())
    rover.place(1, -1, "NORTH")  # Boundary condition check 
    assert rover.report() == "Rover not yet placed"

def test_rover_move():
    rover = Rover(Table())
    rover.place(1, 1, "NORTH")
    rover.move()
    assert rover.report() == "1,2,NORTH"

def test_rover_move_out_of_bounds():
    rover = Rover(Table())
    rover.place(0, 4, "NORTH")  # At the top edge
    rover.move()
    assert rover.report() == "0,4,NORTH"  #  should ignore the move
    rover.place(4, 0, "SOUTH")  # At the bottom edge
    rover.move()
    assert rover.report() == "4,0,SOUTH"  # should ignore the move

def test_rover_turn_left():
    rover = Rover(Table())
    rover.place(1, 1, "NORTH")
    rover.turn("left")
    assert rover.report() == "1,1,WEST"

def test_rover_turn_right():
    rover = Rover(Table())
    rover.place(1, 1, "NORTH")
    rover.turn("right")
    assert rover.report() == "1,1,EAST"

def test_rover_report_without_place():
    rover = Rover(Table())
    assert rover.report() == "Rover not yet placed"

def test_rover_invalid_facing_direction():
    rover = Rover(Table())
    rover.place(2, 2, "INVALID")  # Input not valid for facing direction
    assert rover.report() == "Rover not yet placed"
