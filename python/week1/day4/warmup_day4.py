# =============================================================================
# Day 4 Warmup Exercises — Introduction to Functions
# =============================================================================
# Three exercises that practice defining and calling functions with parameters
# and return values.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1 — Largest of Three Numbers
# -----------------------------------------------------------------------------

def largest_num(num_1, num_2, num_3):
    """
    Returns the largest of three numbers.

    Args:
        num_1 (int | float): First number.
        num_2 (int | float): Second number.
        num_3 (int | float): Third number.

    Returns:
        int | float: The largest value among the three inputs.
    """
    numbers = [num_1, num_2, num_3]

    # Start by assuming the first number is the largest
    largest = numbers[0]

    # Compare each number against the current largest
    for number in numbers:
        if number > largest:
            largest = number

    return largest


# -----------------------------------------------------------------------------
# Exercise 2 — Leap Year Checker
# -----------------------------------------------------------------------------

def leap_year(year):
    """
    Prints whether a given year is a leap year or not.

    Leap year rules (checked in order of precedence):
        1. Divisible by 400 → leap year
        2. Divisible by 100 → NOT a leap year
        3. Divisible by 4   → leap year
        4. Otherwise        → NOT a leap year

    Args:
        year (int): The year to check.
    """
    if year % 400 == 0:
        print("Leap year!")
    elif year % 100 == 0:
        # Divisible by 100 but not 400 — century years that are not leap years
        print("Not a leap year")
    elif year % 4 == 0:
        print("Leap year!")
    else:
        print("Not a leap year")


# -----------------------------------------------------------------------------
# Exercise 3 — Sum of Numbers
# -----------------------------------------------------------------------------

def sum_numbers(num):
    """
    Calculates and returns the sum of all integers from 1 up to num (inclusive).

    Example:
        sum_numbers(5) → 1 + 2 + 3 + 4 + 5 = 15

    Args:
        num (int): The upper bound of the range to sum.

    Returns:
        int: The total sum from 1 to num.
    """
    total = 0

    # Accumulate each integer in the range [1, num]
    for i in range(1, num + 1):
        total += i

    return total


# -----------------------------------------------------------------------------
# Quick test calls
# -----------------------------------------------------------------------------

print(largest_num(3, 7, 5))   # Expected output: 7
leap_year(2000)                # Expected output: Leap year!
leap_year(1900)                # Expected output: Not a leap year
leap_year(2024)                # Expected output: Leap year!
print(sum_numbers(5))          # Expected output: 15