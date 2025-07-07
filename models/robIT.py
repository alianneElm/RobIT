from models.direction import Direction
import sys
from utils.interface import RED, GREEN, RESET
from math import factorial


class RobIT:
    """
    RobIT, your rule-abiding grid traveler.
    Keeps track of his position (x, y) and where he's facing (N, E, S, W).
    Never complains, but he *will* warn you if you try to throw him off the map.
    """

    def __init__(self, x: int, y: int, direction: Direction, grid_width: int, grid_height: int):
        """
        Initializes RobIT at a given position and direction within the grid.
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_width = grid_width
        self.grid_height = grid_height

    def turn_left(self):
        """
        RobIT turns left (counter-clockwise).
        """
        self.direction = self.direction.left()

    def turn_right(self):
        """
        RobIT turns right (clockwise).
        """
        self.direction = self.direction.right()

    def move_forward(self):
        """
        RobIT takes a step forward in his current direction.
        """
        dx, dy = self._get_delta(self.direction)
        self._move(dx, dy)

    def move_backward(self):
        """
        RobIT steps backward by calculating the opposite direction.
        """
        opposite = self.direction.left().left()
        dx, dy = self._get_delta(opposite)
        self._move(dx, dy)

    def _move(self, dx: int, dy: int):
        """
        RobIT attempts to move by (dx, dy). It checks grid boundaries.
        """
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < self.grid_width and 0 <= new_y < self.grid_height:
            self.x = new_x
            self.y = new_y
        else:
            print(f"{RED}Error: RobIT attempted to move outside the grid. Exiting program.{RESET}")
            sys.exit(1)

    def move_turbo(self, n: int = 3):
        """
        Activates turbo mode if grid is at least 10x10.
        Moves forward factorial(n) steps.
        """
        if self.grid_width < 10 or self.grid_height < 10:
            print(f"{RED}Turbo unavailable: Grid must be at least 10x10.{RESET}")
            return

        steps = factorial(n)
        print(f"{GREEN}Turbo mode activated! Moving forward {steps} steps.{RESET}")
        for _ in range(steps):
            self.move_forward()

    def _get_delta(self, direction: Direction):
        """
        Converts RobIT's direction into movement deltas.
        """
        if direction == Direction.N:
            return (0, 1)
        elif direction == Direction.E:
            return (1, 0)
        elif direction == Direction.S:
            return (0, -1)
        elif direction == Direction.W:
            return (-1, 0)
        else:
            raise ValueError(f"{RED}Invalid direction: {direction}{RESET}")

    def report(self) -> str:
        """
        Reports RobIT's current position and orientation.
        """
        return f"{self.x} {self.y} {self.direction}"

    def execute(self, commands: str):
        """
        Processes a string of commands (L, R, F, B).
        """
        for command in commands.upper():
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'F':
                self.move_forward()
            elif command == 'B':
                self.move_backward()
            elif command == 'T':
                self.move_turbo()    
            else:
                print(f"{RED}Invalid command: '{command}' — Ignored.{RESET}")
