# Setup user credentials as a tuple: (username, PIN)
user_credentials = ("user1", "1234")
balance = 1000.0  # Initial account balance

print("=== Welcome to the Mini-ATM ===")

# --- Step 1: Login Loop (Up to 3 attempts) ---
attempts = 3
logged_in = False

while attempts > 0:
    input_username = input("Enter username: ")
    input_pin = input("Enter 4-digit PIN: ")

    # Check credentials against the tuple
    if input_username == user_credentials[0] and input_pin == user_credentials[1]:
        print("\nLogin successful! Welcome.")
        logged_in = True
        break  # Exit the login loop
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid credentials! You have {attempts} attempt(s) remaining.\n")
        else:
            print("\nAccount locked due to too many failed attempts.")

# --- Step 2: ATM Main Menu Loop ---
while logged_in:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print(f"\nYour current balance is: ${balance:.2f}")

    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit: $"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Successfully deposited ${deposit_amount:.2f}.")
            print(f"New Balance: ${balance:.2f}")
        else:
            print("Invalid amount! Deposit must be greater than $0.")

    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw: $"))
        if withdraw_amount <= 0:
            print("Invalid amount! Withdrawal must be greater than $0.")
        elif withdraw_amount > balance:
            print(f"Insufficient funds! Your balance is only ${balance:.2f}.")
        else:
            balance -= withdraw_amount
            print(f"Successfully withdrew ${withdraw_amount:.2f}.")
            print(f"Remaining Balance: ${balance:.2f}")

    elif choice == "4":
        print("\nThank you for using Mini-ATM. Goodbye!")
        logged_in = False  # Break out of menu loop

    else:
        print("Invalid choice! Please select a valid option from 1 to 4.")