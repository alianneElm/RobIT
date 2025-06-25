# Architecture

RobIT is modular and cleanly separated:

- `main.py`: Entry point and CLI logic
- `models/robIT.py`: Movement, execution, reporting
- `models/direction.py`: Cardinal logic
- `utils/interface.py`: CLI prompts and styling

Test files are grouped by module.

CI is configured via GitHub Actions.