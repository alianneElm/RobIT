import pytest
from models.robIT import RobIT
from models.direction import Direction

"""
Unit tests for the RobIT class, which manages movement and state of the robot.

These tests cover:
- Forward and backward movement
- Grid boundary enforcement (exits on out-of-bounds)
- Rotation handling (left and right)
- Command execution and reporting

This suite ensures that RobIT behaves correctly in all expected directions and
handles grid constraints as specified by the assignment.
"""

@pytest.fixture
def default_robit():
    return RobIT(x=2, y=2, direction=Direction.N, grid_width=5, grid_height=5)

def test_turn_left(default_robit):
    default_robit.turn_left()
    assert default_robit.direction == Direction.W

def test_turn_right(default_robit):
    default_robit.turn_right()
    assert default_robit.direction == Direction.E

def test_move_forward_north(default_robit):
    default_robit.move_forward()
    assert (default_robit.x, default_robit.y) == (2, 3)

def test_move_backward_north(default_robit):
    default_robit.move_backward()
    assert (default_robit.x, default_robit.y) == (2, 1)

def test_move_forward_out_of_bounds_exits():
    robit = RobIT(x=4, y=4, direction=Direction.N, grid_width=5, grid_height=5)
    with pytest.raises(SystemExit) as e:
        robit.move_forward()
    assert e.type == SystemExit
    assert e.value.code == 1

def test_move_backward_out_of_bounds():
    robit = RobIT(x=0, y=0, direction=Direction.N, grid_width=5, grid_height=5)
    with pytest.raises(SystemExit) as e:
        robit.move_backward()
    assert e.type == SystemExit
    assert e.value.code == 1

def test_execute_sequence():
    robit = RobIT(x=1, y=1, direction=Direction.N, grid_width=5, grid_height=5)
    robit.execute("RFFLFF")
    # Expected path: (1,1) N → R (E), FF → (3,1), L (N), FF → (3,3)
    assert (robit.x, robit.y, robit.direction) == (3, 3, Direction.N)

def test_invalid_command():
    robit = RobIT(x=0, y=0, direction=Direction.N, grid_width=5, grid_height=5)
    robit.execute("X")  # Should be ignored
    assert (robit.x, robit.y, robit.direction) == (0, 0, Direction.N)

def test_report(default_robit):
    assert default_robit.report() == "2 2 N"

def test_invalid_direction_delta():
    robit = RobIT(x=0, y=0, direction=Direction.N, grid_width=5, grid_height=5)
    with pytest.raises(ValueError):
        robit._get_delta("Z")

def test_robit_moves_west():
    robit = RobIT(x=2, y=2, direction=Direction.W, grid_width=5, grid_height=5)
    robit.move_forward()
    assert robit.x == 1 and robit.y == 2  # W means -1 on x-axis

def test_robit_moves_backward():
    robit = RobIT(x=2, y=2, direction=Direction.N, grid_width=5, grid_height=5)
    robit.execute("B")
    assert robit.x == 2 and robit.y == 1  # moving backward from N should go south

def test_turbo_unavailable_for_small_grid(capsys):
    robit = RobIT(x=0, y=0, direction=Direction.N, grid_width=9, grid_height=9)
    robit.move_turbo()
    captured = capsys.readouterr()
    assert "Turbo unavailable" in captured.out
    assert (robit.x, robit.y) == (0, 0)

def test_turbo_moves_correct_steps_on_large_grid():
    robit = RobIT(x=0, y=0, direction=Direction.E, grid_width=20, grid_height=20)
    robit.move_turbo(n=3)  # factorial(3) = 6 steps east
    assert (robit.x, robit.y) == (6, 0)

def test_turbo_respects_boundaries():
    robit = RobIT(x=18, y=0, direction=Direction.E, grid_width=20, grid_height=20)
    with pytest.raises(SystemExit) as e:
        robit.move_turbo(n=3)  # factorial(3) = 6 → out of bounds
    assert e.type == SystemExit
    assert e.value.code == 1
