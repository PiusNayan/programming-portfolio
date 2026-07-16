# =============================================================================
# Student Management System
# =============================================================================
# A simple menu-driven console application that allows the user to register,
# view, and update a single student's information. The program loops until
# the user explicitly chooses to exit (option 4).
# =============================================================================


# --- Student record variables (holds one student at a time) ------------------
name = ""
age = 0
course = ""

# --- Main application loop ---------------------------------------------------
while True:
    # Display the main menu on every iteration
    print(f'===== STUDENT MANAGEMENT SYSTEM ===== \n')
    print(f'1. Register Student\n'
          '2. View Student\n'
          '3. Update Student\n'
          '4. Exit')

    option = int(input("Select an option (1-4): "))

    # --- Option 1: Register a new student ------------------------------------
    if option == 1:
        name = input("Please enter your name: ")
        age = int(input('Please enter your age: '))
        course = input('Please enter your course of study: ')

        # Validate age — must be a positive number
        if age < 0:
            print(f'Age must be greater than 0.')
            continue  # Skip the success message and restart the loop

        print(f'Student registered successfully.\n')

    # --- Option 2: View the registered student -------------------------------
    elif option == 2:
        # Guard against viewing before any student has been registered
        if name == "":
            print(f'No student registered yet.\n')
        else:
            print(f'Name: {name}\n'
                  f'Age: {age}\n'
                  f'Course: {course}\n')

    # --- Option 3: Update the registered student's information ---------------
    elif option == 3:
        name = input("Please enter your name: ")
        age = int(input('Please enter your age: '))
        course = input('Please enter your course of study: ')
        print(f'Student information updated.\n')

    # --- Option 4: Exit the program ------------------------------------------
    elif option == 4:
        print(f'Have a nice day!')
        break  # Exit the while loop and end the program

    # --- Invalid input --------------------------------------------------------
    else:
        print(f'Invalid option. Please choose between 1 and 4.\n')