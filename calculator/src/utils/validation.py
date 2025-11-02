"""
Module: validation.py
Purpose: Provides input validation functions and custom exceptions for the calculator.

"""

from typing import Union


class InputValidationError(ValueError):
    """
    Custom exception raised for input validation errors.
    """
    pass


def validate_number(value: Union[str, float, int]) -> float:
    """
    Validates and converts input to a float number.

    Args:
        value (Union[str, float, int]): The value to validate.

    Returns:
        float: Validated floating point number.

    Raises:
        InputValidationError: If value is not a valid number.

    Examples:
        >>> validate_number("3.5")
        3.5
        >>> validate_number(7)
        7.0
    """
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise InputValidationError(f"Invalid number input: {value}")

    return number

