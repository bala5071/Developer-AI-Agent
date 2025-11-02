"""
Module: calculator.py
Purpose: Provides functions for basic arithmetic operations.

Public Functions:
- add(a: float, b: float) -> float
- subtract(a: float, b: float) -> float
- multiply(a: float, b: float) -> float
- divide(a: float, b: float) -> float

"""

from typing import Union


def add(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.

    Args:
        a (float): The first addend.
        b (float): The second addend.

    Returns:
        float: The sum of a and b.

    Examples:
        >>> add(3, 2)
        5
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Returns the difference between two numbers.

    Args:
        a (float): The minuend.
        b (float): The subtrahend.

    Returns:
        float: The difference a - b.

    Examples:
        >>> subtract(5, 3)
        2
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Returns the product of two numbers.

    Args:
        a (float): The first factor.
        b (float): The second factor.

    Returns:
        float: The product of a and b.

    Examples:
        >>> multiply(4, 3)
        12
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Returns the quotient of two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient a / b.

    Raises:
        ValueError: If the divisor b is zero.

    Examples:
        >>> divide(10, 2)
        5.0

    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

