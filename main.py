from models.robIT import RobIT
from utils.interface import (
    get_valid_position,
    get_valid_direction,
    display_grid,
    print_intro
)

if __name__ == "__main__":
    print_intro()  

    # Grid setup
    width = int(input("Enter grid width: "))
    height = int(input("Enter grid height: "))
    print(f"Grid size set to {width}x{height}")

    # Show empty grid
    display_grid(width, height)

    # Initial placement
    x = get_valid_position("x", width)
    y = get_valid_position("y", height)
    direction = get_valid_direction()

    robit = RobIT(x, y, direction, width, height)

    # Show grid with RobIT
    display_grid(width, height, robit_x=x, robit_y=y, robit_dir=direction)

    while True:
        commands = input("Enter commands (L, R, F, B) or type 'exit' to quit: ").strip().lower()
        if commands in ["exit", "quit", "q"]:
            print("\n📍 Final report:")
            print(robit.report())
            display_grid(width, height, robit_x=robit.x, robit_y=robit.y, robit_dir=robit.direction)
            break

        robit.execute(commands.upper())
        print("\n📍 RobIT's current state:")
        print(robit.report())
        display_grid(width, height, robit_x=robit.x, robit_y=robit.y, robit_dir=robit.direction)

