
from models.direction import Direction

def print_intro():
    print("""
        Welcome to the world of 🤖 RobIT!
        Guide your grid explorer through a custom-sized world.
        RobIT follows your commands faithfully — but stays within bounds!
        """)

    print("""
        Legend:
        🤖🔼 = RobIT facing North
        🤖▶️ = RobIT facing East
        🤖🔽 = RobIT facing South
        🤖◀️ = RobIT facing West

        Use commands:
        L - Turn Left
        R - Turn Right
        F - Move Forward
        B - Move Backward
        """)       

def get_valid_position(axis: str, limit: int) -> int:
    """
    Asks the user for a valid position (x or y) within the grid limit.
    """
    while True:
        try:
            value = int(input(f"Enter RobIT's starting {axis} position (0 to {limit - 1}): "))
            if 0 <= value < limit:
                return value
            else:
                print(f"{axis.upper()} must be between 0 and {limit - 1}.")
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_direction() -> Direction:
    """
    Asks the user for a valid initial direction (N, E, S, W).
    """
    while True:
        letter = input("Enter RobIT's starting direction (N, E, S, W): ").upper()
        if letter in {'N', 'E', 'S', 'W'}:
            return Direction.from_letter(letter)
        else:
            print("Invalid direction. Please enter one of: N, E, S, W.")


def get_direction_arrow(direction):
    """
    Returns an arrow emoji representing RobIT's current direction.
    """
    return {
        'N': '🔼',
        'E': '▶️',
        'S': '🔽',
        'W': '◀️'
    }.get(direction, '?')

def display_grid(width, height, robit_x=None, robit_y=None, robit_dir=None):
    """
    Prints a grid of the given dimensions.
    RobIT is shown at (robit_x, robit_y) with an arrow indicating his direction.
    """
    print("\n  Grid view:\n")
    for y in reversed(range(height)):
        row = ""
        for x in range(width):
            if x == robit_x and y == robit_y:
                arrow = get_direction_arrow(str(robit_dir))
                row += f"[🤖{arrow}]"
            else:
                row += "[   ]"
        print(row)