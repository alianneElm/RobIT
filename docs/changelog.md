# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-06-24

### Added
- CLI robot simulation with grid-bound movement
- Custom grid size configuration
- Directional movement: left, right, forward, and backward
- Emoji-based directional rendering on grid
- Input validation for direction and grid placement
- Warning system for invalid commands
- Program exits safely if robot moves out of bounds
- Full test suite using `unittest` and `pytest`
- 100% test coverage on core logic
- Continuous Integration with GitHub Actions
- Coverage reporting to Codecov
- Linting with Ruff
- Styled console output with ANSI colors
- Modular architecture (`main`, `robIT`, `direction`, `interface`, `utils`)
- Security policy via `SECURITY.md`
- Automated documentation with MkDocs and GitHub Pages

---

## [Unreleased]

### Planned
- Web interface with real-time simulation (future feature)
- Save/load simulation sessions

