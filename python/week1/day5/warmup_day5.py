# =============================================================================
# Day 5 Warmup Exercises — Functions II
# =============================================================================
# Four exercises that deepen understanding of user-defined functions,
# parameter passing, return values, and modular code design.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1 — Greeting Function
# -----------------------------------------------------------------------------

def greet(name):
    """
    Returns a personalised greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A two-line greeting string.
    """
    return f"Hello {name}\nWelcome to Python!"

print(greet("Yaw"))


# -----------------------------------------------------------------------------
# Exercise 2 — Rectangle Area
# -----------------------------------------------------------------------------

def rectangle_area(length, width):
    """
    Calculates and returns the area of a rectangle.

    Args:
        length (int | float): The length of the rectangle.
        width  (int | float): The width of the rectangle.

    Returns:
        int | float: The computed area (length × width).
    """
    area = length * width
    return area

print(rectangle_area(10, 5))   # Expected output: 50


# -----------------------------------------------------------------------------
# Exercise 3 — Temperature Converter
# -----------------------------------------------------------------------------

def celsius_to_fahrenheit(celsius):
    """
    Converts a Celsius temperature value to Fahrenheit.

    Formula: F = (C × 9/5) + 32

    Args:
        celsius (int | float): Temperature in Celsius.

    Returns:
        float: Equivalent temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(10))   # Expected output: 50.0


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a Fahrenheit temperature value to Celsius.

    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (int | float): Temperature in Fahrenheit.

    Returns:
        float: Equivalent temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

print(fahrenheit_to_celsius(50.0))   # Expected output: 10.0


# -----------------------------------------------------------------------------
# Exercise 4 — Simple Calculator
# -----------------------------------------------------------------------------

def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the result of subtracting b from a."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """
    Returns the result of dividing a by b.

    Guards against division by zero — returns an error message instead
    of raising a ZeroDivisionError.

    Args:
        a (int | float): The dividend.
        b (int | float): The divisor.

    Returns:
        float | str: The quotient, or an error string if b is zero.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(100, 5))   # Expected output: 20.0