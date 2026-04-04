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
OFFICE_NAME = "Main Office"
TAX_RATE = 0.05


def process_expenses(item_name, price, quantity):
    """Calculates total cost and returns total + summary."""
    
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    summary = f"{item_name} x{quantity} | Subtotal: ${subtotal:.2f} | Total: ${total:.2f}"

    return total, summary


def main():
    print(f"--- {OFFICE_NAME} EXPENSE SYSTEM ---")

    item = input("Enter item name: ")

    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Defaulting to 1.00")
        price = 1.00

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Defaulting to 1")
        qty = 1

    # KEYWORD ARGUMENTS + UNPACKING
    final_total, summary_text = process_expenses(
        item_name=item,
        price=price,
        quantity=qty
    )

    print("\n--- RECEIPT ---")
    print(summary_text)
    print(f"Final Total (with tax): ${final_total:.2f}")


main()

