# 🤖 RobIT — The Robot That Does What It's Told (Mostly)

Welcome to **RobIT** — your loyal, grid-loving robot who follows simple directions with unwavering determination. Built in Python with love (and a few coffee stains), RobIT is here to walk, turn, and report — all inside a nice rectangular world you define.

No batteries included. Just raw directional obedience.

---

## What is this?

This is a command-line robot simulator, created as part of a technical coding challenge. RobIT lives in a grid-based room, starts at a given position, and follows a sequence of commands:

- `L`: Turn left
- `R`: Turn right
- `F`: Move forward
- `B`: (Bonus) Move backward like a ninja in reverse

If RobIT tries to walk off the edge of the world... well, it lets you know and refuses to die silently.

---

## How to run it

Make sure you have Python 3.10+ and a sense of adventure.

python main.py

---

## How to test RobIT
To make sure it behaves well:

python -m unittest discover tests

---

## Design notes
RobIT is built with clean separation of concerns:

Grid handles the map and boundaries

Robot manages state and movement

Direction keeps RobIT oriented (geographically, not existentially)

main.py is where it all comes together

All written with modularity and testability in mind, like a good robot citizen.

## Why the name “RobIT”?
Because:

It’s a robot

It’s an IT challenge

And naming things is hard...

---

## Final thoughts
"In a grid full of uncertainty, be like RobIT: take small steps, turn with intention, and never fall silently."

Made with ❤️, clean code, and just the right amount of caffeine.  
Committed proudly as: `git commit -m "feat: bring robot to life"`  
— Alianne Elm