# 📘 Day 5 — Functions II

## 📋 Lesson Overview

Day 5 built directly on Day 4 by going deeper into **how** and **when** functions are used. The session covered the three sources of functions available in Python, advanced argument passing (`*args`, `**kwargs`, default parameters), the purpose of `return`, and how to classify functions by their role in a program. The day ended with a **Banking System** mini-project that put all of these ideas into practice.

---

## 📚 Resources Used

- Personal lecture notes — Functions II (sources, golden rule, function types by purpose)
- [`warmup_day5.py`][warmup] — Four warmup exercises practising user-defined functions
- [`banking_system.py`][banking] — End-of-day mini-project: a full menu-driven banking system

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
External packages (e.g. `pandas`, `matplotlib`, `numpy`) must be **installed first** (`pip install <package>`), then imported.

#### 3. User-Defined Functions
Functions you write yourself for your specific program needs.

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

```python
# Definition — describes WHAT the function does
def function_name():
    # body
    pass

# Call — makes the function execute
function_name()
```

The function **does nothing** until it is called.

---

### Positional vs Keyword Arguments

```python
def clean_name(first_name, last_name):
    print(first_name.strip().capitalize() + " " + last_name.strip().capitalize())

# Positional — order matters
clean_name("MAYaM", "Pius")

# Keyword — order does not matter
clean_name(first_name="MAYaM", last_name="Pius")
```

> **Rule:** When mixing both, positional arguments must always come first.

---

### Default Parameters

```python
def clean_name(first_name, last_name, country="Ghana"):
    ...
```
> **Rule:** Parameters **without** default values must appear **before** those with default values.

---

### `*args` and `**kwargs`

Used when the number of arguments is not known in advance.

```python
# *args — stored as a tuple
def total(*args):
    return sum(args)

total(1, 2, 3)   # args = (1, 2, 3)
```

```python
# **kwargs — stored as a dictionary
def create_user(**kwargs):
    print(kwargs)

create_user(name="Pius", phone="+233...")
```

| | `*args` | `**kwargs` |
|-|---------|------------|
| Type | Tuple | Dictionary |
| Argument style | Positional | Keyword |

---

### Return Values

`return` sends the function's output back to the caller so it can be stored and reused:

```python
def add(a, b):
    return a + b

result = add(3, 4)   # result = 7
```

---

### Functions by Purpose

| Type | Role | Example in this project |
|------|------|------------------------|
| **Action** | Performs a side effect — no return value | `show_manu()` |
| **Transformational** | Takes input, processes it, returns the result | `deposit()`, `withdraw()`, `check_balnce()` |
| **Validation** | Checks a condition and returns `True` or `False` | *(handled inline in `main()`)* |
| **Orchestrator** | Calls other functions in the correct order | `main()` |

---

## ✅ Exercises Completed

All four warmup exercises are in [`warmup_day5.py`][warmup]:

### Exercise 1 — Greeting Function [`warmup_day5.py`][warmup]

```python
def greet(name):
    """Returns a personalised greeting message."""
    return f"Hello {name}\nWelcome to Python!"

print(greet("Yaw"))
```

### Exercise 2 — Rectangle Area [`warmup_day5.py`][warmup]

```python
def rectangle_area(length, width):
    """Calculates and returns the area of a rectangle."""
    area = length * width
    return area

print(rectangle_area(10, 5))   # Output: 50
```

### Exercise 3 — Temperature Converter [`warmup_day5.py`][warmup]

```python
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32"""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius. Formula: C = (F - 32) × 5/9"""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
```

### Exercise 4 — Simple Calculator [`warmup_day5.py`][warmup]

```python
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    """Guards against division by zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

---

## 🏦 Banking System [`banking_system.py`][banking]

This is a full menu-driven banking system written in your own style. It goes significantly beyond the basic version — adding a complete `main()` orchestrator, `try/except` input validation, nested retry loops for amounts, and formatted output with separators and emojis.

### Functions Overview

| Function | Type | Role |
|----------|------|------|
| `show_menu()` | Action | Prints the bank menu — no return value |
| `check_balance()` | Transformational | Returns the current balance as a formatted string |
| `deposit(amount)` | Transformational | Adds amount to balance, returns success message |
| `withdraw(amount)` | Transformational | Deducts amount from balance, returns success message |
| `main()` | Orchestrator | Runs the full program loop, routes to all other functions |

### Program Flow

```
main() starts
    │
    ├─ show_menu()          ← displays options every loop
    │
    ├─ try/except           ← catches invalid (non-numeric) menu input
    │
    ├─ choice == 1 ─────── check_balance()     ← shows balance
    ├─ choice == 2 ─────── nested loop ──── deposit(amount)
    ├─ choice == 3 ─────── nested loop ──── withdraw(amount)
    ├─ choice == 4 ─────── break            ← exits program cleanly
    └─ else ───────────── invalid message, loop restarts
```

### Key Code Snippets

**The `main()` orchestrator loop with `try/except` input guard:**

```python
def main():
    while True:
        show_menu()
        try:
            choice = float(input("Enter an option: "))
        except ValueError:
            print("\n⚠️  Invalid input! Please enter a number between 1 and 4.")
            continue
```

**Deposit with nested retry loop and amount validation:**

```python
elif choice == 2:
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("⚠️  Invalid input! Please enter numbers only.\n")
            continue
        if amount == 0:
            print("\nOperation cancelled.")
            break
        elif amount < 0:
            print("⚠️  Invalid input! Enter a positive amount to deposit.\n")
            continue
        print(f'\n{deposit(amount)}')
        break
```

**Withdrawal with insufficient funds guard:**

```python
elif choice == 3:
    while True:
        ...
        elif amount > balance:
            print("Insufficient funds.")
            continue
        print(withdraw(amount))
        break
```

**Clean exit:**

```python
elif choice == 4:
    print(f"{'\U0001f44b THANK YOU \U0001f44b':^50}")
    print("Thank you for banking with us! Have a great day. \U0001f600")
    break
```



## 💭 Reflection

Day 5 made function design feel much more intentional. Rewriting the Banking System in my own style — with a proper `main()` function, formatted output, and nested validation loops — showed how an orchestrator function brings structure to a whole program. Using `try/except` to handle bad input felt like a meaningful step up from just assuming the user enters the right thing. The classification of functions by purpose (action, transformational, validation, orchestrator) gave me a useful way to think about *what* each function should do before writing it.

---

## 📊 Self-Evaluation

| Area | Rating | Notes |
|------|--------|-------|
| Function sources (built-in / library / user-defined) | ⭐⭐⭐⭐⭐ | Clear and applied correctly |
| Function definition & calling | ⭐⭐⭐⭐⭐ | Consistent across all exercises and project |
| Parameters & return values | ⭐⭐⭐⭐⭐ | Used correctly in all four exercise functions |
| `try/except` input validation | ⭐⭐⭐⭐⭐ | Applied confidently in both menu and amount inputs |
| Orchestrator pattern (`main()`) | ⭐⭐⭐⭐⭐ | Well structured — cleanly separates concerns |

**Overall**: Strong day — the Banking System shows real growth in thinking about program structure, not just individual functions.

---

## 📝 Git Commit Message

```
feat(day5): rewrite banking system with orchestrator and input validation

- Add warmup_day5.py with four function exercises:
  greeting, rectangle area, temperature converter, simple calculator
- Rewrite banking_system.py in student's own style:
  add main() orchestrator, try/except input guards, nested retry loops
  for deposit/withdraw amounts, formatted output with emoji headers
- Add docstrings and section comments to all functions
```

---

## 🔗 Reference Links

- [warmup_day5.py](./warmup_day5.py) — Warmup exercises (greeting, area, temperature, calculator)
- [banking_system.py](./banking_system.py) — Banking System mini-project

<!-- Reference definitions used by inline badges in exercise headings above -->
[warmup]: ./warmup_day5.py
[banking]: ./banking_system.py
