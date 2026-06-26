# ## Small Coding Challenge
# Your program should:<br>

# Ask the user for:<br>
#   •Name<br>
#   •Age<br>
#   •University<br>
#   •Course of study<br>

# Display a profile like this:<br>

# ------ STUDENT PROFILE ------<br>
# Name: Yaw<br>
# Age: 20<br>
# University: UPSA<br>
# Course: Information Technology<br>
# -----------------------------<br>
# Bonus Challenge ⭐<br>
# Make the program calculate how old the student will be after 5 years.


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