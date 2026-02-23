"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# List of seats
seats = list(range(1, 21))

while True:
    # If no seats left, stop
    if len(seats) == 0:
        print("All seats are sold out.")
        break

    # Show available seats
    print("\nAvailable seats:")
    for seat in seats:
        print(seat, end=" ")
    print()

    # Ask for seat number
    choice = int(input("Enter seat number (0 to quit): "))

    # Exit
    if choice == 0:
        print("Thank you. Goodbye.")
        break

    # Check if seat is available
    if choice in seats:
        seats.remove(choice)
        print("Seat", choice, "sold.")
    else:
        print("That seat is not available.")
