"""
Author: Raviteja Burugu
Date: 2025-04-29
Description: Rover class for movements on the 5x5 tabletop.
"""
class Rover:
    """Rover class for different movements on a tabletop based on the commands 
    """
    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
    def __init__(self,table):
        self.table = table
        self.x = None 
        self.y = None 
        self.facing = None   
        
    def place(self , x, y, facing):
        if self.table.is_valid_position(x,y):
            self.x, self.y, self.facing = x,y,facing
            print(f"Robot placed at ({self.x}, {self.y})facing {self.facing}") 
            
    def report(self):
        if self.x is not None: 
            return f"{self.x},{self.y},{self.facing}" 
        return "Rover not yet placed "
    
    def move(self):
        if self.facing is None:
            return 
        move_map={
            "NORTH": (0,1),
            "SOUTH": (0,-1),
            "EAST": (1,0),
            "WEST": (-1,0),
        }
        dx, dy = move_map[self.facing]
        updated_x , updated_y = self.x+dx, self.y+dy
        if self.table.is_valid_position(updated_x , updated_y):
            self.x , self.y = updated_x , updated_y
            print(f"Rover has moved now to ({self.x}, {self.y}) and facing the direction {self.facing}")
            
    def turn(self,direction):
        if self.facing and direction in ("left", "right"):
            idx = self.DIRECTIONS.index(self.facing)
        if direction == "left":
            self.facing = self.DIRECTIONS[(idx - 1) % 4]
            print(f"Rover turned left and now its facing {self.facing}.")
        elif  direction == "right":
            self.facing = self.DIRECTIONS[(idx + 1) % 4]
            print(f"Rover turned right and now its facing {self.facing}.")
            
    def report(self):
        if self.x is not None and self.y is not None and self.facing:
            return f"current robot position and direction {self.x},{self.y},{self.facing}"
        return None