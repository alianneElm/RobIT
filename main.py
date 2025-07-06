from models.robIT import RobIT
from utils.interface import (
    get_valid_position,
    get_valid_direction,
    display_grid,
    print_intro,
    get_valid_grid
)
from utils.interface import GREEN, BLUE, RED, RESET

def main():
    print_intro()  

    # Grid setup with validation
    try:
        width = get_valid_grid("Enter grid width: ")
        height = get_valid_grid("Enter grid height: ")
        print(f"{GREEN}Grid size set to {width}x{height}{RESET}")
    except ValueError as e:
        print(f"{RED}{e}{RESET}")


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
        commands = input("\nEnter commands (L, R, F, B) or type 'exit' to quit: ").strip().lower()
        if commands in ["exit", "quit", "q"]:
            print(f"\n{BLUE}Report:{RESET}")
            print(robit.report())
            display_grid(width, height, robit_x=robit.x, robit_y=robit.y, robit_dir=robit.direction)
            break

        robit.execute(commands.upper())
        print(f"\n{GREEN}RobIT's current state:{RESET}")
        print(robit.report())
        display_grid(width, height, robit_x=robit.x, robit_y=robit.y, robit_dir=robit.direction)

if __name__ == "__main__": # pragma: no cover
    main()