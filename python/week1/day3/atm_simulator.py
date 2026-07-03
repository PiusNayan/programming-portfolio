"""
ATM Simulator
=============

A simple command-line ATM that allows the user to:
- Check balance
- Deposit money
- Withdraw money
- Exit

All operations are handled through a continuous input loop until
the user chooses to exit.
"""

# Starting account balance
BALANCE = 1000.0


# Display menu options
print(f'===== ATM MENU =====') 
print("1. Check Balance \n" 
      "2. Deposit \n" 
      "3. Withdraw \n" 
      "4. Exit") 

while True: 
    menu = int(input("Enter an option (1-4): ")) 
    if menu == 1: 
        print(f'Current balance: {BALANCE}') 
    elif menu == 2: 
        deposit = int(input("Deposit amount: ₡")) 
        BALANCE += deposit
        print(f'New balance: ₡{BALANCE}') 
    elif menu == 3: 
        withdraw = int(input("Withdrawal amount: ₡")) 
        if BALANCE > withdraw: 
            print(f'Withdrawal Successful') 
            BALANCE -= withdraw
            print(f'New balance: ₡{BALANCE}') 
        elif BALANCE < withdraw: 
            print(f'Insufficient funds.') 
    elif menu == 4: 
        break 
    else: 
        print(f'Invalid input. \nChoose between 1 and 4') 
        continue