# RobIT Internals

## Movement

RobIT can turn and move in a grid. It uses delta vectors to update positions.

- `turn_left` / `turn_right` change its direction.
- `move_forward` / `move_backward` use a delta map.

## Command Execution

Each letter is interpreted and routed. Invalid commands are ignored with a warning.

## Safety

If a move would take RobIT outside the grid, it logs an error and exits with status `1`.
