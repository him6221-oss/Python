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
OFFICE_NAME = "Hero HQ"
TAX_RATE = 0.05

def process_expenses(item_name, price, quantity):
    """Processes office expenses and returns:"""
    
    subtotal = price * quantity
    total = subtotal + (subtotal * TAX_RATE)
    summary = (
        f"{OFFICE_NAME} - Hero Dashboard Report\n"
        f"Item: {item_name}\n"
        f"Quantity: {quantity}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"Total with Tax: ${total:.2f}\n"
        f"Status: {'Mission Critical' if total > 100 else 'Routine'}"
    )
    return total, summary

def main():
    try:
        # Collect input from user
        item = input("Enter the item name: ")
        price = float(input("Enter the price per item: "))
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        # Fallback defaults
        print("Invalid input detected. Defaulting price to 1.00 and quantity to 1.")
        price = 1.00
        quantity = 1
        item = "Unknown Item"

    # Call the function using keyword arguments and unpack the return values
    final_total, dashboard_report = process_expenses(
        item_name=item, price=price, quantity=quantity
    )

    # Print the results
    print("\n" + dashboard_report)
    print(f"\nFinal Total to Approve: ${final_total:.2f}")

if __name__ == "__main__":
    main()