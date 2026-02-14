"""
-----------------------------------------------------------------------
ASSIGNMENT 5B: THE ATM
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. 'while' loop keeps the program running.
[ ] 3. I have handled ValueErrors (Type Safety).
[ ] 4. I have blocked Negative numbers and Overdrafts.
[ ] 5. I have pinned the 'balance' in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

balance = 1000
running = True

while running:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter 1-4: "))
        if choice == 1:
            print("Balance: $", balance)
        elif choice == 2:
            amount = float(input("Deposit amount: "))
            if amount > 0:
                balance = balance + amount
                print("You deposited $", amount)
                print("New balance: $", balance)
            else:
                print("Cannot deposit zero or negative money")
        elif choice == 3:
            amount = float(input("Withdraw amount: "))
            if amount <= 0:
                print("Cannot withdraw zero or negative money")
            elif amount > balance:
                print("Not enough money!")
            else:
                balance = balance - amount
                print("You withdrew $", amount)
                print("New balance: $", balance)
        elif choice == 4:
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice")
    except:
        print("Please type a number")
