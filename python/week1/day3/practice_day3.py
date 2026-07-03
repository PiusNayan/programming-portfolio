"""
Practice exercises for Day 3
=============================

This script contains four small exercises:
1. Even or Odd — checks whether a number is even or odd
2. Multiplication Table — prints the multiplication table for a given number
3. Password Checker — allows 3 attempts to enter the correct password
4. Number Pattern — prints an ascending and descending asterisk triangle
"""

# ---------------------------------------------------------------------------
# Exercise 1 — EVEN OR ODD
# Ask the user for a number and determine whether it is even or odd.
# ---------------------------------------------------------------------------
number = int(input("Entre a number: "))
if number % 2 == 0:
    print(f'{number} is an even nuber')
else:
    print(f'{number} is an odd number')

# ---------------------------------------------------------------------------
# Exercise 2 — MULTIPLICATION TABLE
# Ask the user for a number and display its multiplication table from 1–10.
# ---------------------------------------------------------------------------
number = int(input("Enter a number here: "))
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# ---------------------------------------------------------------------------
# Exercise 3 — PASSWORD CHECKER
# Allow the user 3 attempts to enter the correct password.
# ---------------------------------------------------------------------------
password = "Pyhton123"
for _ in range(3):
    check_password = input("Enter your password here: ")
    if check_password == password:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        continue

# ---------------------------------------------------------------------------
# Exercise 4 — NUMBER PATTERN
# Ask the user for a number and print two asterisk triangles:
# one ascending from 1 to n, and one descending from n back to 1.
# ---------------------------------------------------------------------------
number = int(input("Enter a number here: "))
for i in range(1, number + 1, 1):
    print(i * "*")
for i in range(number, 0, -1):
    print(i * "*")