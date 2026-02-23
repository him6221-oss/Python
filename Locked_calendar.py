"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

# MONTHS is a constant tuple (should not be changed)
MONTHS = ("January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December")

# Display each month
for month in MONTHS:
    print(month)

print("\nTrying to change the calendar")

# Try to change the tuple
try:
    MONTHS[0] = "march-ember"
except TypeError:
    print("Error: You cannot change months!!")
