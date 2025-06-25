# 📦 Changelog

All notable changes to this project will be documented in this file.

---

## [v1.3.0] - 2025-06-25

### 🚀 Features
- Implemented full command-line interface for RobIT with interactive prompts
- Added custom grid size support
- Enabled RobIT to move forward and backward
- Added support for turning left and right
- Rendered grid in console with directional emojis
- Styled CLI output with color-coded ANSI formatting
- Added full modular architecture (`main.py`, `robIT.py`, `direction.py`, `interface.py`)

### 🧪 Testing
- Full test suite with `pytest` and `unittest`
- Reached **100% test coverage** on core logic (`Direction`, `RobIT`, command execution)
- Added validation tests for invalid directions and commands

### ✅ CI/CD and Linting
- GitHub Actions for:
  - Continuous Integration
  - Coverage reports (via `codecov`)
  - Artifact generation on tag push
- Added Ruff for fast and clean linting

### 📚 Documentation
- Integrated **MkDocs** with Material theme
- Published full developer documentation via **GitHub Pages**
- Added `SECURITY.md` and `CHANGELOG.md` to docs section

### 📦 Release
- Final automated release using GitHub Actions and version tagging (`v1.3.0`)
- `.zip` artifact published with source code

---

## [v1.2.0] - 2025-06-24
- Fixes to release pipeline and coverage reports
- Added better error messages and styled reports

## [v1.1.0] - 2025-06-24
- Initial setup for GitHub Actions release workflow (failed run)

## [v1.0.0] - 2025-06-24
- First test release setup for CD (failed run)
