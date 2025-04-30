class Rover:
    def __init__(self,table):
        self.table = table
        self.x = None 
        self.y = None 
        self.facing = None
        
    def place (self , x, y, facing):
        if self.table.is_valid_position(x,y):
            self.x, self.y, self.facing = x,y,facing 
    
    def report(self):
        if self.x is not None: 
            return f"{self.x},{self.y},{self.facing}" 
        return "Rover not yet placed "