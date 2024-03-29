import pytest
def add(a: int , b: int) -> int:
    return a + b
def subtract(a: int, b: int) -> int:
    return b - a
def multiply(a: int, b: int) -> int:
    return a * b
def divide(a: int, b: int) -> int:
    return b // a

# Path: tests/test_arthmetic_operations.py
def test_add() -> None:
    assert add(1, 1) == 2
def test_subtract() -> None:
    assert subtract(2, 5) == 3
def test_multiply() -> None:
    assert multiply(10, 10) == 100
def test_divide() -> None:
    assert divide(25, 100) == 4

@pytest.fixture
def add_fixture() -> int:
    return add(1, 1)

# test fixtures
def test_add_fixture(add_fixture: int) -> None:
    assert add_fixture == 2