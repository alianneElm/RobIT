# 🤖 RobIT — The Robot That Does What It's Told

Welcome to **RobIT** — your loyal, grid-loving robot who follows simple directions with unwavering determination. Built in Python, RobIT is here to walk, turn, and report — all inside a nice rectangular world you define.

No batteries included. Just raw directional obedience.

## What is this?

This is a command-line robot simulator, created as part of a technical coding challenge. RobIT lives in a grid-based room, starts at a given position, and follows a sequence of commands:

- `L`: Turn left
- `R`: Turn right
- `F`: Move forward
- `B`: (Bonus) Move backward like a ninja in reverse
- `T`: (Bonus) Turbo forward with factorial logic (3!)

If RobIT tries to walk off the edge of the world... well, it lets you know and refuses to die silently.

---

## How to run it

Make sure you have Python 3.10+ and a sense of adventure.

```python3 main.py```

---

## How to test RobIT
To make sure it behaves well:

With coverage report:

```pytest tests --cov=models --cov=main --cov-branch --cov-report=term-missing```

To run using unittest:

```python -m unittest discover tests```

## To lint and autofix your code:

```ruff check . --fix```

---

## ✅ Features implemented:
✅ Custom grid size

✅ Safe initial placement and direction

✅ Turn left/right

✅ Move forward and backward

✅ Ignores invalid commands (with warning)

✅ Detects and exits gracefully if going out of bounds

✅ Directional emoji rendering

✅ CLI reporting (position + direction)

✅ Color-coded messages for UX

✅ Full test suite with pytest and unittest

✅ 100% test coverage on core logic

✅ Continuous Integration (CI) with GitHub Actions

✅ Test coverage report uploaded to Codecov

✅ Linting with ruff

✅ Styled console output with ANSI colors

✅ Modular design: main, robIT, direction, interface

✅ Robust error handling

✅ Clear test separation by module

✅ Automated GitHub Releases for versioned deployment

---

## 🛠️ Developer Experience
CI/CD via GitHub Actions

Coverage via Codecov (coverage.xml generated on push/PR)

Static analysis & linting via Ruff

Colored output for easier debugging

Custom exceptions and edge case tests

Ready for GitHub Pages + MkDocs

---

## Security

Please refer to SECURITY.md for information on responsible vulnerability disclosure.

---

## Documentation

Documentation available at: [https://alianneelm/.github.io/RobIT](https://alianneelm.github.io/RobIT/)
Generated with MkDocs and hosted via GitHub Pages.

---

## Design notes
RobIT is built with clean separation of concerns:

Grid handles the map and boundaries

Robot manages state and movement

Direction keeps RobIT oriented (geographically, not existentially)

main.py is where it all comes together

All written with modularity and testability in mind, like a good robot citizen.

---

## Final thoughts
"In a grid full of uncertainty, be like RobIT: take small steps, turn with intention, and never fall silently."

Made with ❤️, clean code, and just the right amount of caffeine.   
— Alianne Elm
