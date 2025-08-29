# Tests Package

This package contains all test files for the FastAPI Hello World v2 application.

## Structure

- `test_main.py` - Main application endpoint tests
- `test_models.py` - Pydantic model tests (future)
- `conftest.py` - Pytest configuration and fixtures (future)

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_main.py
```
