from models.direction import Direction

# ANSI color codes for terminal output
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_intro():
    print(f"""
        {BLUE}Welcome to the world of 🤖 RobIT!{RESET}
        Guide your grid explorer through a custom-sized world.
        RobIT follows your commands faithfully — but stays within bounds!
        """)

    print(f"""
        {GREEN}Legend:{RESET}
        🤖🔼 = RobIT facing North
        🤖▶️ = RobIT facing East
        🤖🔽 = RobIT facing South
        🤖◀️ = RobIT facing West

        {GREEN}Use commands:{RESET}
        L - Turn Left
        R - Turn Right
        F - Move Forward
        B - Move Backward
        T - Turbo Forward (3!)
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
                print(f"{RED}{axis.upper()} must be between 0 and {limit - 1}.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid integer.{RESET}")

def get_valid_direction() -> Direction:
    """
    Asks the user for a valid initial direction (N, E, S, W).
    """
    while True:
        letter = input("Enter RobIT's starting direction (N, E, S, W): ").upper()
        if letter in {'N', 'E', 'S', 'W'}:
            return Direction.from_letter(letter)
        else:
            print(f"{RED}Invalid direction. Please enter one of: N, E, S, W.{RESET}")


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

def get_valid_grid(prompt: str) -> int:
    while True:
        user_input = input(prompt)

        if not user_input.isdigit():
            print(f"{RED}Invalid input: must be a positive integer.{RESET}")
            continue

        value = int(user_input)

        if value <= 0:
            print(f"{RED}Value must be greater than zero.{RESET}")
        else:
            return value

def display_grid(width, height, robit_x=None, robit_y=None, robit_dir=None):
    """
    Prints a grid of the given dimensions.
    RobIT is shown at (robit_x, robit_y) with an arrow indicating his direction.
    """
    print(f"\n{BLUE}____________{RESET}")
    print(f"\n{BLUE}Grid view:{RESET}\n")
    for y in reversed(range(height)):
        row = ""
        for x in range(width):
            if x == robit_x and y == robit_y:
                arrow = get_direction_arrow(str(robit_dir))
                row += f"[🤖{arrow}]"
            else:
                row += "[   ]"
        print(row)