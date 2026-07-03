"""
Student Profile Program

Asks the user for their name, age, university, and course of study,
then prints a formatted profile including their age after 5 years.
"""

name = input("Enter your name: ")
age = int(input("What is your age?: " ))
university = input("What University are you affliated to?: ")
course = input("What is your course of study?: ")

print(f'______STUDENT PROFILE______')
print(f'Name: {name}')
print(f'Age: {age}')
print(f'University: {university}')
print(f'Course: {course}')
print("_____________________________")
print(f'In five years you would be {5+ age} years old.')