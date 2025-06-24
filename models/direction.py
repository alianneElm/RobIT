from enum import Enum

class Direction(Enum):
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'


    def left(self):
        """
        Returns the direction to the left of the current direction.
        Counter-clockwise order: N → W → S → E → N
        """
        order = [Direction.N, Direction.W, Direction.S, Direction.E]
        idx = order.index(self)
        return order[(idx + 1) % 4]

    def right(self):
        """
        Returns the direction to the right of the current direction.
        Clockwise order: N → E → S → W → N
        """
        order = [Direction.N, Direction.E, Direction.S, Direction.W]
        idx = order.index(self)
        return order[(idx + 1) % 4]

    def __str__(self):
        """
        String representation, returns 'N', 'E', 'S', or 'W'
        """
        return self.value

    @staticmethod
    def from_letter(letter: str):
        """
        Converts a string like 'N', 'E', 'S', or 'W' into a Direction enum.
        Raises ValueError if the input is invalid.
        """
        try:
            return Direction[letter.upper()]
        except KeyError:
            raise ValueError(f"Invalid direction letter: {letter}")

    def to_letter(self):
        """
        Returns the letter corresponding to this direction.
        (Useful for consistency or future flexibility)
        """
        return self.value

