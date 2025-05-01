"""
Author: Raviteja Burugu
Date: 2025-04-29
Description: Rover class for movements on the 5x5 tabletop.
"""

class Rover:
    """
    Rover class for different movements on a tabletop based on the commands.
    """
    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, table):
        """
        Initializes the Rover object with a reference to the table and sets its initial position and direction.

        Args:
            table (Table): The table object to validate the rover's position.
        """
        self.table = table
        self.x = None 
        self.y = None 
        self.facing = None
        self.is_placed = False   
        
    def place(self, x, y, facing):
        """
        Places the rover at the specified position and direction if the position is valid.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
            facing (str): The direction the rover is facing (e.g., "NORTH", "EAST").
        """
        if facing not in self.DIRECTIONS:
            return  # Ignore invalid facing direction
        if self.table.is_valid_position(x, y):
            self.x, self.y, self.facing = x, y, facing
            self.is_placed = True
        #    print(f"Robot placed at ({self.x}, {self.y}) facing {self.facing}") 
            
    def report(self):
        """
        Reports the current position and direction of the rover.

        Returns:
            str: A string representing the rover's position and direction (e.g., "1,2,NORTH").
            None: If the rover is not placed, returns None.
        """
        if self.is_placed:
            return f"{self.x},{self.y},{self.facing}"
        return "Rover not yet placed"
    
    def move(self):
        """
        Moves the rover one step forward in the direction it is currently facing, 
        if the new position is within the boundaries of the table.
        """
        if not self.is_placed:
            return 
        move_map = {
            "NORTH": (0, 1),
            "SOUTH": (0, -1),
            "EAST": (1, 0),
            "WEST": (-1, 0),
        }
        dx, dy = move_map[self.facing]
        updated_x, updated_y = self.x + dx, self.y + dy
        if self.table.is_valid_position(updated_x, updated_y):
            self.x, self.y = updated_x, updated_y
        #    print(f"Rover has moved now to ({self.x}, {self.y}) and facing the direction {self.facing}")
            
    def turn(self, direction):
        """
        Turns the rover left or right based on the given direction.

        Args:
            direction (str): The direction to turn ("left" or "right").
        """
        if self.facing and direction in ("left", "right"):
            idx = self.DIRECTIONS.index(self.facing)
            if direction == "left":
                self.facing = self.DIRECTIONS[(idx - 1) % 4]
            #    print(f"Rover turned left and now its facing {self.facing}.")
            elif direction == "right":
                self.facing = self.DIRECTIONS[(idx + 1) % 4]
            #    print(f"Rover turned right and now its facing {self.facing}.")