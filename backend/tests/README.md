# Backend Tests

This directory contains tests for the Coffee Shop Backend API.

## Test Structure

```
tests/
├── __init__.py
├── test_api.py          # API endpoint tests
├── test_auth.py         # Authentication tests
├── conftest.py          # Pytest fixtures
└── README.md            # This file
```

## Running Tests

### Install Test Dependencies

```bash
pip install pytest pytest-cov
```

### Run All Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=src --cov-report=html
```

### Run Specific Test File

```bash
pytest tests/test_api.py
```

### Run Specific Test

```bash
pytest tests/test_api.py::DrinkAPITestCase::test_get_drinks_public_endpoint
```

## Test Coverage

Current test coverage includes:
- ✅ Public endpoint (GET /drinks)
- ✅ Drink model methods (short, long, CRUD)
- ✅ Error handlers (404, 422, 400)
- ✅ Authentication decorators
- ✅ Permission checking

## Fixtures

The `conftest.py` file provides:
- `client`: Flask test client
- `sample_drink_data`: Sample drink data

## Writing New Tests

1. Create test file: `test_module_name.py`
2. Import required modules
3. Use fixtures from `conftest.py`
4. Follow naming convention: `test_function_name()`

Example:
```python
def test_get_drinks(client):
    response = client.get('/drinks')
    assert response.status_code == 200
```

