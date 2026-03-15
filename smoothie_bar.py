"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# TODO: Define get_price(size)

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic

def get_price(size):
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00


def blend(size, base, fruit, scoops):
    print("\n--- Blending Smoothie ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")
    print("Your smoothie is ready!")


def main():
    print("Welcome to the Smoothie Bar")

    size = input("Size (Small/Medium/Large): ").title().strip()
    base = input("Choose a base (Water/Apple Juice/Orange Juice/Milk): ")
    fruit = input("Choose a fruit (Strawberry/Banana/Mango/Blueberry): ")

    try:
        scoops = int(input("How many fruit scoops?: "))
    except ValueError:
        print("Invalid number. Defaulting to 1 scoop.")
        scoops = 1

    price = get_price(size)

    blend(size, base, fruit, scoops)

    print(f"Total Price: ${price:.2f}")


main()