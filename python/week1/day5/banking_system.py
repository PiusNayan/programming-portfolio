# =============================================================================
# Banking System — Day 5 Mini Project
# =============================================================================
# A menu-driven banking application demonstrating all four function types:
#
#   Action Function        → show_menu()      Prints the menu (side effect only)
#   Action Function        → main()           Orchestrates the full program loop
#   Transformational       → check_balance()  Returns the current balance string
#   Transformational       → deposit()        Adds an amount and returns confirmation
#   Transformational       → withdraw()       Deducts an amount and returns confirmation
#   Orchestrator           → main()           Controls program flow with a while loop
#
# Key techniques used:
#   - global keyword       : allows deposit() and withdraw() to modify `balance`
#   - try / except         : catches non-numeric input gracefully
#   - Nested while loops   : lets the user retry bad deposit/withdrawal input
#   - Formatted output     : headers with "=" separators and emoji labels
# =============================================================================


# --- Shared account balance (starting amount) --------------------------------
balance = 1000


# -----------------------------------------------------------------------------
# Action Function — Display Menu
# -----------------------------------------------------------------------------
def show_menu():
    """
    Prints the main bank menu to the console.

    This is an action function — it produces a side effect (output)
    and does not return a value.
    """
    print("\n===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


# -----------------------------------------------------------------------------
# Transformational Function — Check Balance
# -----------------------------------------------------------------------------
def check_balance():
    """
    Returns the current account balance as a formatted string.

    Reads the global `balance` variable (read-only — no `global` keyword
    needed because the value is not being modified).

    Returns:
        str: Balance displayed in the format "Balance: $<amount>"
    """
    return f'Balance: ${balance}'


# -----------------------------------------------------------------------------
# Transformational Function — Deposit
# -----------------------------------------------------------------------------
def deposit(amount):
    """
    Adds the given amount to the account balance and returns a confirmation.

    Uses the `global` keyword to modify the shared `balance` variable.
    Input validation (amount > 0, numeric check) is handled in main().

    Args:
        amount (float): The amount to deposit. Assumed to be positive.

    Returns:
        str: A success message showing the new balance.
    """
    global balance
    balance += amount
    return f'\nDeposit Successful\nNew balance ${balance} \n'


# -----------------------------------------------------------------------------
# Transformational Function — Withdraw
# -----------------------------------------------------------------------------
def withdraw(amount):
    """
    Deducts the given amount from the account balance and returns a confirmation.

    Uses the `global` keyword to modify the shared `balance` variable.
    Input validation (amount > 0, sufficient funds) is handled in main().

    Args:
        amount (float): The amount to withdraw. Assumed to be valid.

    Returns:
        str: A success message showing the new balance.
    """
    global balance
    balance -= amount
    return f'\nWithdrawal Successful\nNew balance: ${balance}\n'


# -----------------------------------------------------------------------------
# Orchestrator Function — Main Program Loop
# -----------------------------------------------------------------------------
def main():
    """
    Controls the full program flow of the banking system.

    This is an orchestrator function — it calls the other functions
    (show_menu, check_balance, deposit, withdraw) in the correct order
    based on the user's menu choice.

    Program flow:
        1. Show menu
        2. Read and validate menu input (try/except for non-numeric values)
        3. Route to the correct operation based on choice (1–4)
        4. For deposit/withdraw: use a nested loop to validate the amount
        5. Exit cleanly when choice 4 is selected (break)
    """
    while True:
        show_menu()

        # --- Read menu choice, guard against non-numeric input ---------------
        try:
            choice = float(input("Enter an option: "))
        except ValueError:
            print("\n⚠️  Invalid input! Please enter a number between 1 and 4.")
            continue

        # --- Option 1: Check Balance -----------------------------------------
        if choice == 1:
            print("\n" + "=" * 50)
            print(f"{'💳 BALANCE INQUIRY 💳':^50}")
            print("=" * 50)

            print(check_balance())   # Display current balance

            print("-" * 50)
            print("Returning to Main Menu...")
            print("=" * 50)

        # --- Option 2: Deposit -----------------------------------------------
        elif choice == 2:
            print("\n" + "=" * 50)
            print(f"{'🏦 DEPOSIT FIELD 🏦':^50}")
            print("=" * 50)

            # Nested loop — keeps asking until a valid amount is entered
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

                print(f'\n{deposit(amount)}')   # Perform deposit and show result
                break

            print("-" * 50)
            print("Returning to Main Menu...")
            print("=" * 50 + "\n")

        # --- Option 3: Withdraw ----------------------------------------------
        elif choice == 3:
            print("\n" + "=" * 50)
            print(f"{'📤 WITHDRAWAL FIELD 📤':^50}")
            print("=" * 50)

            # Nested loop — keeps asking until a valid amount is entered
            while True:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                except ValueError:
                    print("⚠️  Invalid input! Please enter numbers only.\n")
                    continue

                if amount == 0:
                    print("\nOperation cancelled.")
                    break
                elif amount > balance:
                    print("Insufficient funds.")
                    continue
                elif amount < 0:
                    print("⚠️  Invalid input! Enter a positive amount to withdraw.\n")
                    continue

                print(withdraw(amount))   # Perform withdrawal and show result
                break

            print("-" * 50)
            print("Returning to Main Menu...")
            print("=" * 50)

        # --- Option 4: Exit --------------------------------------------------
        elif choice == 4:
            print("\n" + "=" * 50)
            print(f"{'👋 THANK YOU 👋':^50}")
            print("=" * 50)
            print("Thank you for banking with us! Have a great day. 😀")
            print("=" * 50 + "\n")
            break   # Exit the while loop and end the program

        # --- Invalid choice --------------------------------------------------
        else:
            print("\n⚠️  Invalid choice. Please select an option from 1 to 4")
            continue


# --- Entry point — run the program -------------------------------------------
main()