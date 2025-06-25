import pytest
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
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.type == SystemExit
        assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "❌ Error: RobIT attempted to move outside the grid" in captured.out

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

def test_main_command_and_exit(capsys):
    user_inputs = [
        "5",     # grid width
        "5",     # grid height
        "2",     # RobIT x
        "3",     # RobIT y
        "N",     # RobIT direction
        "F",     # move forward (executes robit.execute)
        "exit"   # triggers final report
    ]

    with patch("builtins.input", side_effect=user_inputs):
        try:
            main()
        except SystemExit:
            pass  # If you still raise sys.exit on bounds, ignore it

    captured = capsys.readouterr()

    assert "📍 RobIT's current state:" in captured.out
    assert "📍 Final report:" in captured.out    