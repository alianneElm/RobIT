from unittest.mock import patch
from main import main
import importlib.util
import os

def test_main_flow(capsys):
    user_inputs = [
        "5",    # grid width
        "5",    # grid height
        "2",    # RobIT x
        "3",    # RobIT y
        "N",    # RobIT direction
        "FFRFF",  # movement commands
        "exit"  # exit command
    ]
    with patch("builtins.input", side_effect=user_inputs):
        main()

    captured = capsys.readouterr()

    print("=== OUTPUT START ===")
    print(captured.out)
    print("=== OUTPUT END ===")

    assert "📍 Final report:" in captured.out

    final_state = "4 4 E"
    lines = captured.out.strip().splitlines()
    assert any(final_state in line for line in lines), (
        f"Expected final state '{final_state}' not found in output:\n{captured.out}"
    )

def test_main_guard_does_not_run_main_on_import(capsys):
    """
    Ensure that main.py does not execute main() on import (if __name__ != '__main__').
    """
    file_path = os.path.join(os.path.dirname(__file__), "../main.py")
    spec = importlib.util.spec_from_file_location("main", file_path)
    main_module = importlib.util.module_from_spec(spec)
    loader = spec.loader
    assert loader is not None
    loader.exec_module(main_module)

    # Captured output should *not* contain intro text
    output = capsys.readouterr().out
    assert "Welcome to the world of 🤖 RobIT!" not in output