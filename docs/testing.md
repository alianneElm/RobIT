## How to test RobIT

To make sure it behaves well:

With coverage report:

```pytest tests --cov=models --cov=main --cov-branch --cov-report=term-missing```

To run using unittest:

```python -m unittest discover tests```

## To lint and autofix your code:

```ruff check . ```

```ruff check . --fix```

CI runs tests and uploads coverage to Codecov.

---