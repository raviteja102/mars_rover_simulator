from src.rover import Rover
from src.table import Table

def test_rover_place():
    rover = Rover(Table())
    rover.place(3,4,"SOUTH")
    assert rover.report() == "current robot position and direction 3,4,SOUTH"