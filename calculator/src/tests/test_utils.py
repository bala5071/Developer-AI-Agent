"""
Test cases for the input validation utilities.
"""

import pytest
from utils.validation import validate_number, InputValidationError


def test_validate_number_valid_inputs():
    assert validate_number("3.5") == 3.5
    assert validate_number(7) == 7.0
    assert validate_number(-2.1) == -2.1


def test_validate_number_invalid_inputs():
    with pytest.raises(InputValidationError):
        validate_number("abc")
    with pytest.raises(InputValidationError):
        validate_number(None)
    with pytest.raises(InputValidationError):
        validate_number([1, 2, 3])

