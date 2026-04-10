"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Function 'load_config' reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: receipt.txt file created in workspace.
[ ] 5. Function uses .readlines(), strips spaces, splits commas, and casts to int/float.
[ ] 6. Calculates and prints mathematical Grand Total correctly.
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

def load_config(filename):
    menu = {}

    try:
        file = open(filename, "r")

        for line in file:
            line = line.strip()
            parts = line.split(",")

            key = parts[0]
            values = parts[1:]

            menu[key] = values

        file.close()
        return menu

    except FileNotFoundError:
        print("File not found")
        return {}


def audit_receipt(filename):
    total = 0

    try:
        file = open(filename, "r")
        lines = file.readlines()

        print("\nRECEIPT:")

        for line in lines:
            line = line.strip()
            parts = line.split(",")

            qty = int(parts[0])
            item = parts[1]
            price = float(parts[2])

            line_total = qty * price
            total = total + line_total

            print(qty, "x", item, "@", price, "=", line_total)

        file.close()

        print("----------------")
        print("TOTAL =", total)

    except FileNotFoundError:
        print("Receipt file not found")

    return total


def main():
    print("Loading menu...")

    menu = load_config("menu_config.txt")

    if menu:
        print("Menu Loaded:")
        for key in menu:
            print(key, ":", menu[key])

    audit_receipt("receipt.txt")


main()