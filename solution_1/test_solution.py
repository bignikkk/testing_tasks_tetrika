import pytest

from solution import strict


@strict
def add(a: int, b: int) -> int:
    return a + b


def test_correct_add():
    assert add(1, 2) == 3


def test_type_error_raised():
    with pytest.raises(TypeError):
        add(1, "2")
