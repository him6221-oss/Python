"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""


# Task 1: The Nagging Kid
keep_asking = True

#While loop keep asking YES
while keep_asking:
    answer = input("Are we there yet? ")
    if answer == "yes":
        print("Hooray! We made it!")
        keep_asking = False
    else:
        print("Not yet!")

        #For loop 99 bottles
        for bottles in range(99, 0, -1):
            print(bottles, "bottles of beer on the wall")