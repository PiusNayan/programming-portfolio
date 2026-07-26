# 📘 Day 5 — Functions II

## 📋 Lesson Overview

Day 5 built directly on the Day 4 function introduction by going deeper into **how** and **when** functions are used. The session covered the three sources of functions available in Python, advanced argument passing techniques (`*args`, `**kwargs`, default parameters), the purpose of `return`, and how to classify functions by their role in a program. The day concluded with a **Banking System** mini-project that applied all these ideas.

---

## 📚 Resources Used

- Personal lecture notes — Functions II (see notes summary below)
- [`warmup_day5.py`][warmup] — Four warmup exercises practising user-defined functions
- [`banking_system.py`][banking] — End-of-day mini-project: a function-based banking system

---

## 🧠 Key Concepts

### Why Functions Matter

Without functions, code becomes:

| Problem | Impact |
|---------|--------|
| Inconsistent behaviour | Same logic written differently in different places |
| Hard to change | One fix requires edits in many locations |
| Time consuming | Repetitive re-writing of the same logic |
| Hard to read | Long, unbroken scripts with no clear structure |
| Risky to modify | A change in one spot can silently break another |

Functions solve all of these by storing logic **once** and **calling** it wherever needed.

---

### Three Sources of Functions

#### 1. Built-In Functions

Pre-installed with Python — no import required.

```python
print("Hello")   # output to console
len("Python")    # length of a sequence
sum([1, 2, 3])   # sum of an iterable
max(10, 20)      # largest value
```

#### 2. Standard Library

Developed and maintained by the Python team. Must be **imported** before use.

```python
import math
import datetime
import random
```

External packages (e.g. `pandas`, `matplotlib`, `numpy`) are also available but must be **installed first** (`pip install <package>`), then imported.

#### 3. User-Defined Functions

Functions you create yourself for your specific program needs.

```python
def greet(name):
    return f"Hello {name}\nWelcome to Python!"
```

#### The Golden Rule — Which Source to Use?

```
1. Check built-in functions first
         ↓
2. Check standard / external libraries
         ↓
3. Write a user-defined function
```

---

### Function Definition vs Function Call

A function has two distinct parts:

```python
# --- Definition: describes WHAT the function does ---
def function_name():
    # line of code
    # line of code

# --- Call: makes the function execute ---
function_name()
```

The function **does nothing** until it is called.

---

### Positional vs Keyword Arguments

```python
def clean_name(first_name, last_name):
    first = first_name.strip().capitalize()
    second = last_name.strip().capitalize()
    print(first + " " + second)

# Positional — order matters
clean_name("MAYaM", "Pius")

# Keyword — order does not matter
clean_name(first_name="MAYaM", last_name="Pius")
```

> **Rule:** When mixing both, positional arguments must always come first.

---

### Default Parameters

A parameter can be given a default value that is used when no argument is passed:

```python
def clean_name(first_name, last_name, country="Ghana"):
    ...
```

> **Rule:** Parameters **without** default values must appear **before** parameters with default values.

---

### `*args` and `**kwargs`

Used when the number of arguments is not known in advance.

```python
# *args — accepts any number of positional arguments (stored as a tuple)
def total(*args):
    return sum(args)

total(1, 2, 3)   # args = (1, 2, 3)
```

```python
# **kwargs — accepts any number of keyword arguments (stored as a dict)
def create_user(**kwargs):
    # kwargs = {"name": "Pius", "phone": "+233..."}
    print(kwargs)

create_user(name="Pius", phone="+233...")
```

| | `*args` | `**kwargs` |
|-|---------|------------|
| Type | Tuple | Dictionary |
| Argument style | Positional | Keyword |
| Best used when | Data is of similar type | Data has different types/labels |

---

### Return Values

`return` sends the function's output back to the caller so it can be stored and reused:

```python
def add(a, b):
    return a + b

result = add(3, 4)   # result = 7 — value is preserved
```

Without `return`, the output is lost after the function finishes.

---

### Functions by Purpose

| Type | Role | Examples |
|------|------|---------|
| **Action** | Performs a side effect — does not return a value | `print()`, `send_email()`, `show_menu()` |
| **Transformational** | Takes raw data, processes it, returns the result | `celsius_to_fahrenheit()`, `deposit()` |
| **Validation** | Checks a condition and returns `True` or `False` | `is_valid_age()`, `has_funds()` |
| **Orchestrator** | Calls other functions in the correct order to control program flow | `main()`, `run_app()` |

---

## ✅ Exercises Completed

All four warmup exercises are in [`warmup_day5.py`][warmup]:

### Exercise 1 — Greeting Function [`warmup_day5.py`][warmup]

A simple **transformational function** that builds and returns a greeting string:

```python
def greet(name):
    """Returns a personalised greeting message."""
    return f"Hello {name}\nWelcome to Python!"

print(greet("Yaw"))
```

---

### Exercise 2 — Rectangle Area [`warmup_day5.py`][warmup]

Demonstrates **positional parameters** and a numeric `return` value:

```python
def rectangle_area(length, width):
    """Calculates and returns the area of a rectangle."""
    area = length * width
    return area

print(rectangle_area(10, 5))   # Output: 50
```

---

### Exercise 3 — Temperature Converter [`warmup_day5.py`][warmup]

Two **transformational functions** applying temperature conversion formulas:

```python
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius. Formula: C = (F - 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9
```

---

### Exercise 4 — Simple Calculator [`warmup_day5.py`][warmup]

Four single-purpose functions — each performing one arithmetic operation. The `divide` function includes a **validation guard**:

```python
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    """Guards against division by zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(100, 5))   # Output: 20.0
```

---

## 🏦 Banking System [`banking_system.py`][banking]

A function-based console banking system that demonstrates all four function types in a single program.

### Functions Overview

| Function | Type | Description |
|----------|------|-------------|
| `show_menu()` | Action | Prints the bank menu — no return value |
| `check_balance()` | Action / Transformational | Returns current balance as a formatted string |
| `deposit(amount)` | Transformational | Validates and adds amount to balance |
| `withdraw(amount)` | Transformational | Validates and deducts amount from balance |

### Key Implementation Details

**Shared global state** — a single `balance` variable is shared across all functions using the `global` keyword:

```python
balance = 1000

def deposit(amount):
    global balance   # required to modify the outer variable
    if amount <= 0:
        return "Invalid amount."
    balance += amount
    return balance
```

**Validation guards in `withdraw`** — two conditions are checked before any deduction:

```python
def withdraw(amount):
    global balance

    if amount <= 0:
        return "Invalid amount."

    if amount > balance:
        return "Insufficient funds."

    balance -= amount
    return balance
```

---

## ⚠️ Challenges Faced & Fixes Applied

 created an unused local variable that shadowed the function name. Removed.
- **Critical bug in `deposit()`** — `balance = deposit` on the original line 13 overwrote the numeric balance with the function object itself, breaking all subsequent operations. Fixed by removing the erroneous line (the `balance += amount` above it already performs the update correctly).
- **Inconsistent validation in `deposit()`** — The original `deposit` rejected `amount < 0` but allowed `amount == 0`. Aligned with `withdraw`'s guard to reject `amount <= 0`.

---

## 💭 Reflection

Day 5 made the concept of functions feel much more structured. Knowing there are three *sources* of functions (built-in, library, user-defined) and a clear order to check them before writing new code is a practical rule I'll carry forward. Classifying functions by *purpose* (action, transformational, validation, orchestrator) was particularly useful — it gave me a vocabulary for thinking about what a function is supposed to do before writing it. The Banking System was a satisfying project because it naturally combined all four function types in one program.

---

## 📊 Self-Evaluation

| Area | Rating | Notes |
|------|--------|-------|
| Sources of functions | ⭐⭐⭐⭐⭐ | Clear understanding of built-in → library → user-defined |
| Function definition & call | ⭐⭐⭐⭐⭐ | Consistent and correct across all exercises |
| Parameters & arguments | ⭐⭐⭐⭐☆ | Positional and keyword understood; *args/*kwargs still needs practice |
| Return values | ⭐⭐⭐⭐☆ | Applied correctly; recognised the missing return bug in deposit |
| Function types by purpose | ⭐⭐⭐⭐☆ | Can identify; orchestrator pattern not yet applied in projects |
| Code quality & naming | ⭐⭐⭐☆☆ | Several typos found; improving with docstrings |

**Overall**: Strong conceptual day. The function taxonomy (by source and by purpose) gives a clear mental model for structuring programs going forward.

---

## 📝 Git Commit Message

```
feat(day5): add functions II exercises and banking system mini-project

- Add warmup_day5.py with four function exercises:
  greeting, rectangle area, temperature converter, simple calculator
- Add banking_system.py: function-based banking system demonstrating
  action, transformational, and validation function types
- Fix typos in parameter names and docstrings across warmup_day5.py
- Fix critical bug in banking_system.py: deposit() balance overwrite
```

---

## 🔗 Reference Links

- [warmup_day5.py](./warmup_day5.py) — Warmup exercises (greeting, area, temperature, calculator)
- [banking_system.py](./banking_system.py) — Banking System mini-project

<!-- Reference definitions used by inline badges in exercise headings above -->
[warmup]: ./warmup_day5.py
[banking]: ./banking_system.py
