"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
Name: Robert Romanowski
-----------------------------------------------------------------------
"""

TOPPINGS = ("Pepperoni", "Sausage", "Mushroom", "Onion")


def make_pizza(customer, size, topping, is_delivery=False):
    """Creates a pizza order and displays it."""
    print("\n--- PIZZA ORDER ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")

    if is_delivery:
        print("Delivery: Yes")
    else:
        print("Delivery: No")

    print("Your pizza is being made!")


def main():
    name = input("Enter your name: ")
    size = input("Enter size (Small/Medium/Large): ")

    print("Available toppings:", TOPPINGS)
    topping = input("Choose a topping: ")

    delivery_input = input("Delivery? (yes/no): ").lower()

    if delivery_input == "yes":
        delivery = True
    else:
        delivery = False

    make_pizza(customer=name, size=size, topping=topping, is_delivery=delivery)


main()