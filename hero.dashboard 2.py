"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS
OFFICE_NAME = "Office Store"
TAX_RATE = 0.05


def process_expenses(item_name, price, quantity):
    # basic math
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # simple message (nothing fancy)
    summary = item_name + " x" + str(quantity)

    return total, summary


def main():
    print("Welcome to", OFFICE_NAME)

    item = input("Enter item name: ")

    try:
        price = float(input("Enter price: "))
    except:
        print("Bad input, using 1.0")
        price = 1.0

    try:
        quantity = int(input("Enter quantity: "))
    except:
        print("Bad input, using 1")
        quantity = 1

    # keyword arguments (required)
    total, summary = process_expenses(
        item_name=item,
        price=price,
        quantity=quantity
    )

    print("Summary:", summary)
    print("Total:", total)


main()