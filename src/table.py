"""
Author: Raviteja Burugu
Date: 2025-04-29
Description: Table class for checking the rover position during motion planning to ensure it stays within the given 5x5 grid.
"""

class Table:
    """
    Table class to check whether the position of the rover is within the boundary conditions of the 5x5 grid.
    """

    def is_valid_position(self, x, y):
        """
        Checks if the given position (x, y) is within the boundaries of the 5x5 grid.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.

        Returns:
            bool: True if the position is valid (within the grid), False otherwise.

        Raises:
            TypeError: If x or y is not an integer.
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Input for both x and y must be integers.")
        return 0 <= x < 5 and 0 <= y < 5