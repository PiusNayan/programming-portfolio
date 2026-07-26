# =============================================================================
# Banking System — Day 5 Mini Project
# =============================================================================
# A simple function-based banking system demonstrating:
#   - Action functions   : show_menu(), check_balance()
#   - Transformational   : deposit(), withdraw()
#   - Global state       : a shared `balance` variable across functions
#
# NOTE: This version stores a single account balance. A production system
# would use a class or a database to manage multiple accounts.
# =============================================================================


# --- Shared account balance --------------------------------------------------
balance = 1000


# --- Action Functions --------------------------------------------------------

def check_balance():
    """
    Returns the current account balance as a formatted string.

    Returns:
        str: Current balance in the format "Balance: $<amount>".
    """
    return f"Balance: ${balance}"


def show_menu():
    """Prints the main banking menu to the console."""
    print("===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


# --- Transformational Functions ----------------------------------------------

def deposit(amount):
    """
    Deposits a given amount into the account balance.

    Validates that the amount is positive before updating the balance.

    Args:
        amount (int | float): The amount to deposit. Must be greater than 0.

    Returns:
        int | float | str: Updated balance on success, or 'Invalid amount.'
                           if the amount is not positive.
    """
    global balance

    if amount <= 0:
        return "Invalid amount."

    balance += amount
    return balance


def withdraw(amount):
    """
    Withdraws a given amount from the account balance.

    Validates that:
      - The amount is positive (> 0).
      - Sufficient funds are available before deducting.

    Args:
        amount (int | float): The amount to withdraw. Must be greater than 0.

    Returns:
        int | float | str: Updated balance on success, or an error string
                           if the amount is invalid or funds are insufficient.
    """
    global balance

    if amount <= 0:
        return "Invalid amount."

    if amount > balance:
        return "Insufficient funds."

    balance -= amount
    return balance
