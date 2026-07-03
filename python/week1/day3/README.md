# Week 1 - Day 3
## Python Practice & Mini Projects

## 📅 Date

**Completed:** July 1, 2026.

---

## 📖 Overview

Day 3 focused on writing clean, readable Python code using control flow, loops, user input, and string formatting. I completed four practice exercises and built a menu-driven ATM simulator.

---

## 📚 Learning Resources

### Main Book

**Book:** Automate the Boring Stuff with Python by Al Sweigart

#### Chapters Studied

- Chapter 3: Functions
- Chapter 2: Flow Control

#### Topics Covered

- `if` / `elif` / `else` statements
- `for` loops and `while` loops
- `input()` and string formatting
- Conditionals and comparison operators
- Break and continue
- Module docstrings and comments

---

## 🎥 Videos Watched

### Indently

- Python Functions
- Parameters and Arguments
- Return Statements

### CS50P

- Functions
- Variables and Scope

---

## 🎯 Learning Objectives

Today's objectives were to:

- Use `if` statements to branch logic.
- Use `for` and `while` loops to repeat actions.
- Handle user input with `input()`.
- Format output with f-strings.
- Separate script sections with clear comments.
- Build an interactive command-line tool.

---

## 📖 Key Concepts Learned

## Conditionals

`if` / `elif` / `else` statements let Python choose which code to run based on a condition.

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Loops

- **`for` loop** — repeats a block a fixed number of times.
- **`while` loop** — repeats as long as a condition is true.

```python
for i in range(1, 6):
    print(i)

count = 3
while count > 0:
    print(count)
    count -= 1
```

---

## Break and Continue

- `break` exits the loop immediately.
- `continue` skips the rest of the current iteration and moves to the next one.

```python
for _ in range(3):
    guess = input("Enter password: ")
    if guess == password:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        continue
```

---

## String Formatting

F-strings make it easy to insert variables directly into strings.

```python
name = "Pius"
print(f"Hello, {name}!")
```

---

## Docstrings and Comments

- **Docstrings** describe what a script or function does.
- **Comments** explain why something is written a certain way.

```python
"""
Practice exercises for Day 3
=============================

Four small exercises:
1. Even or Odd
2. Multiplication Table
3. Password Checker
4. Number Pattern
"""
```

---

## 💻 Practical Exercises Completed

- ✅ Wrote `if` / `elif` / `else` conditionals.
- ✅ Built `for` loops to generate tables and patterns.
- ✅ Built `while` loops for repeated user input.
- ✅ Used `f` strings to format output.
- ✅ Structured a script with clear section comments.

---

## 🚀 Mini Projects

### Practice Day 3

Four sequential exercises in [`practice_day3.py`](practice_day3.py):

1. **Even or Odd** — checks whether an entered number is even or odd.
2. **Multiplication Table** — prints the 1–10 table for an entered number.
3. **Password Checker** — gives the user 3 attempts to enter the correct password.
4. **Number Pattern** — prints ascending and descending asterisk triangles.

#### Skills Used

- Conditional logic (`if` / `else`)
- `for` loops
- `while` loops with `break` / `continue`
- `input()` and `int()` casting
- String repetition and f-strings

---

### ATM Simulator

A menu-driven command-line ATM in [`atm_simulator.py`](atm_simulator.py). It loops until the user selects Exit, letting them check a balance, deposit, or withdraw.

#### Skills Used

- `while True` menu loop
- `if` / `elif` / `else` menu selection
- Mutable global `BALANCE` state
- Formatted output with colons and currency symbols
- `if __name__ == "__main__"` guard

---

## 📂 Source Files

- [`practice_day3.py`](practice_day3.py) — four sequential practice exercises: Even or Odd, Multiplication Table, Password Checker, and Number Pattern
- [`atm_simulator.py`](atm_simulator.py) — menu-driven ATM with Check Balance, Deposit, Withdraw, and Exit options

---

## 🧠 Challenges Faced

- Aligning the menu option display with the correct `if` branches in the ATM.
- Making sure the ATM loop continues after a deposit or check rather than exiting.
- Choosing a pattern logic that prints a clean ascending and descending triangle.

---

## ✅ Lessons Learned

- Clear section comments make sequential exercises much easier to follow.
- A `while True` loop is the simplest way to build a menu that repeats until the user exits.
- `input()` returns strings, so numeric input always needs casting with `int()` or `float()`.
- F-strings keep output readable and consistent.

---

## 🚀 Next Lesson

**Week 3 – Day 2**

Topics:

- Lists and list methods
- Tuples
- Dictionaries
- Sets
- List comprehensions

---

## 📝 Reflection

This session was mostly about getting comfortable with Python's core control flow tools. The practice exercises reinforced how `if` statements, loops, and string formatting work together in real programs. Writing clear section comments between exercises made the file easy to scan.

The ATM simulator was a useful step up from single-run scripts. Learning to use `while True` for a menu loop and keeping balance state in a single variable showed how small stateful tools are built. The main takeaway is that simple programs become much easier to understand when the loop and branches are cleanly organized.

---

## ⭐ Self Evaluation

| Category | Rating |
|----------|--------|
| Understanding | ⭐⭐⭐⭐⭐ |
| Coding Confidence | ⭐⭐⭐⭐☆ |
| Difficulty | ⭐⭐⭐☆☆ |
| Enjoyment | ⭐⭐⭐⭐⭐ |

---

**Portfolio Goal:** Build a strong foundation in Python while maintaining a well-documented GitHub portfolio that demonstrates continuous learning and practical programming skills.
