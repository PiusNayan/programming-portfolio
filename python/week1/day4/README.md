# 📘 Day 4 — Introduction to Functions in Python

## 📋 Lesson Overview

Day 4 focused on **Python functions** — one of the most fundamental building blocks of programming. The session introduced how to define, call, and structure functions using the `def` keyword, as well as how to use parameters, arguments, and return values to write clean, reusable code. The day concluded with a practical mini-project: a **Student Management System** built using loops and conditionals.

---

## 📚 Resources Used

- [`function-introduction-notes.md`](./function-introduction-notes.md) — personal notes covering function syntax, parameters, arguments, return values, and the benefits of modular programming
- [`warmup_day4.py`](./warmup_day4.py) — warmup exercises implementing functions from scratch
- [`student_management.py`](./student_management.py) — end-of-day project: a menu-driven student record system

---

## 🧠 Key Concepts

### What is a Function?
A function is a reusable block of code that performs a specific task. Instead of repeating the same instructions, you define them once and call the function wherever needed.

```python
def greet():
    print("Hello, welcome!")

greet()
```

### Function Syntax

```python
def function_name(parameters):
    # body of the function
    statement(s)
    return value   # optional
```

| Part | Role |
|------|------|
| `def` | Keyword used to define a function |
| `function_name` | The name given to the function |
| `parameters` | Placeholder variables the function receives |
| `return` | Sends a value back to the caller |

### Parameters vs Arguments
- **Parameters** are the variables listed in the function definition (placeholders).
- **Arguments** are the actual values passed when calling the function.

```python
def greet(name):          # 'name' is a parameter
    print("Hello, " + name)

greet("Alice")            # "Alice" is the argument
```

### Return Values
Functions can send results back to the caller using `return`:

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
```

### Built-in vs User-Defined Functions

| Type | Description | Examples |
|------|-------------|---------|
| Built-in | Come pre-installed with Python | `print()`, `len()`, `max()` |
| User-defined | Created by the programmer | Any `def` block you write |

### Benefits of Modular Programming
Breaking programs into smaller functions means:
- Each function has one clear purpose
- Code is easier to read, test, and debug
- Changes in one place don't break everything else

---

## ✅ Exercises Completed

All three warmup exercises in [`warmup_day4.py`](./warmup_day4.py) were implemented as standalone functions:

### Exercise 1 — Largest of Three Numbers [`warmup_day4.py`][warmup]
Finds the largest value among three inputs by iterating through a list:

```python
def largest_num(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest
```

### Exercise 2 — Leap Year Checker [`warmup_day4.py`][warmup]
Determines whether a given year is a leap year using the standard divisibility rules (400 → 100 → 4):

```python
def leap_year(year):
    if year % 400 == 0:
        print("Leap year!")
    elif year % 100 == 0:
        print("Not a leap year")
    elif year % 4 == 0:
        print("Leap year!")
    else:
        print("Not a leap year")
```

### Exercise 3 — Sum of Numbers [`warmup_day4.py`][warmup]
Calculates the sum of all integers from 1 up to a given number using a `for` loop:

```python
def sum_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total += i

    return total
```

---

## 🗂️ Student Management System [`student_management.py`][sms]

[`student_management.py`](./student_management.py) is a menu-driven console application that manages a single student's information using a `while True` loop and `if/elif` branching.

### Features

| Option | Action |
|--------|--------|
| `1` | Register a student (name, age, course) |
| `2` | View the registered student's details |
| `3` | Update the student's information |
| `4` | Exit the program |

### How It Works

The program stores student data in three plain variables and loops until the user exits:

```python
name = ""
age = 0
course = ""

while True:
    print(f'===== STUDENT MANAGEMENT SYSTEM ===== \n')
    print(f'1. Register Student\n'
          '2. View Student\n'
          '3. Update Student\n'
          '4. Exit')

    option = int(input("Select an option (1-4): "))
```

**Registering a student** captures name, age, and course, and includes a validation guard for negative ages:

```python
    if option == 1:
        name = input("Please enter your name: ")
        age = int(input('Please enter your age: '))
        course = input('Please enter your course of study: ')

        if age < 0:
            print(f'Age must be greater than 0.')
            continue

        print(f'Student registered successfully.\n')
```

**Viewing a student** checks whether any record has been registered before displaying it:

```python
    elif option == 2:
        if name == "":
            print(f'No student registered yet.\n')
        else:
            print(f'Name: {name}\n'
                  f'Age: {age}\n'
                  f'Course: {course}\n')
```

---

## ⚠️ Challenges Faced

- **Understanding `return` vs `print`** — It was initially unclear when a function should `return` a value versus just `print` it directly inside the function body. Working through the exercises made this distinction clearer.
- **Leap year logic ordering** — The divisibility conditions for leap years needed to be in the correct order (400 before 100 before 4) to produce accurate results; reversing them would cause incorrect outputs.
- **Single-student limitation** — The Student Management System only holds one student record at a time. Adding a second student via option 1 silently overwrites the first, which is a limitation of using plain variables rather than a list or dictionary.
---

## 💭 Reflection

Day 4 was a significant step forward. Functions transformed the way I think about code — instead of writing a long script from top to bottom, I started thinking in terms of **small, single-purpose blocks** that can be composed together. The Student Management System felt like a real program because it responds to user input and loops until explicitly told to stop, which made it satisfying to build. I can see how a future version could use a list of dictionaries to store multiple students and functions to handle each menu option cleanly.

---

## 📊 Self-Evaluation

| Area | Rating | Notes |
|------|--------|-------|
| Understanding function syntax | ⭐⭐⭐⭐⭐ | Confident with `def`, parameters, and `return` |
| Applying functions to exercises | ⭐⭐⭐⭐☆ | All three warmup exercises completed correctly |
| Leap year logic | ⭐⭐⭐⭐☆ | Correct, though ordering required care |
| Student Management System | ⭐⭐⭐⭐☆ | Works well; limited to one student record |
| Code readability & naming | ⭐⭐⭐☆☆ | Minor typo in `sum_numbres`; could add more comments |
| Modular thinking | ⭐⭐⭐⭐☆ | Growing confidence; SMS could be refactored into functions |

**Overall**: Solid day. Functions clicked conceptually, and the mini-project tied together loops, conditionals, and user input from earlier in the week.

---

## 📝 Git Commit Message

```
feat(day4): add function exercises and student management system

- Add warmup_day4.py with three function exercises:
  largest of three numbers, leap year checker, and sum of numbers
- Add student_management.py: menu-driven console app to register,
  view, and update a single student record with input validation
- Add function-introduction-notes.md covering def syntax,
  parameters, arguments, return values, and modular programming
```

---

## 🔗 Reference Links

[warmup]: ./warmup_day4.py
[sms]: ./student_management.py
[notes]: ./function-introduction-notes.md

