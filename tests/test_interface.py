from models.direction import Direction
from utils.interface import (
    get_valid_position,
    get_valid_direction,
    get_direction_arrow,
    print_intro,
    display_grid,
)

"""
Tests for utility functions in interface.py that handle user input and grid display.

Includes:
- Validation of position input within grid bounds
- Validation of initial direction input
- Correct emoji arrow mapping for each direction
- Display rendering of the grid with or without RobIT's position

These tests ensure input logic is user-friendly and output is visually consistent.
"""

def test_get_direction_arrow():
    assert get_direction_arrow("N") == "🔼"
    assert get_direction_arrow("E") == "▶️"
    assert get_direction_arrow("S") == "🔽"
    assert get_direction_arrow("W") == "◀️"
    assert get_direction_arrow("X") == "?"

def test_print_intro(capsys):
    print_intro()
    captured = capsys.readouterr()
    assert "Welcome to the world of 🤖 RobIT!" in captured.out
    assert "Legend:" in captured.out
    assert "L - Turn Left" in captured.out

def test_get_valid_position_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_valid_position("x", 5) == 3

def test_get_valid_position_out_of_bounds(monkeypatch):
    inputs = iter(["10", "-1", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_valid_position("x", 5) == 2

def test_get_valid_position_invalid_input(monkeypatch):
    inputs = iter(["abc", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_valid_position("y", 5) == 2

def test_get_valid_direction_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert get_valid_direction() == Direction.N

def test_get_valid_direction_invalid_then_valid(monkeypatch):
    inputs = iter(["X", "S"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_valid_direction() == Direction.S

def test_display_grid(capsys):
    display_grid(3, 3, robit_x=1, robit_y=2, robit_dir="E")
    captured = capsys.readouterr()
    assert "🤖▶️" in captured.out
    assert "[   ][🤖▶️][   ]" in captured.out
    
def test_get_valid_grid_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "12")
    from utils.interface import get_valid_grid
    assert get_valid_grid("Enter grid width: ") == 12

def test_get_valid_grid_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["abc", "-5", "0", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    from utils.interface import get_valid_grid
    result = get_valid_grid("Enter grid height: ")
    captured = capsys.readouterr()
    assert result == 7
    assert "Invalid input" in captured.out
    assert "must be greater than zero" in captured.out
