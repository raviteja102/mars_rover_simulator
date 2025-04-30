"""
Author: Raviteja Burugu
Date: 2025-04-29
Description: Table class for checking the rover position during motion_planning if they are with the given 5 units * 5 units .
"""
class Table:
    """Table class to check whether the position of the rover is with in the boundary condition given 
    """
    def is_valid_position(self , x, y):
        return 0<= x< 5 and 0 <= y < 5