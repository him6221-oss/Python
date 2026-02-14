"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
Assignment: Logic Gate...... DND
Name: Robert Romanowski
Date: January 24, 2026
File Name: logic re-work.py
-----------------------------------------------------------------------
"""



print("Welcome Adventurer, to the Logic Dungeon, Gate!")
print("Your Strength and Constitution will determine if you may enter...")
print("-" * 40)

# Get Adventurers stats
strength = int(input("Enter your Strength stat: "))
constitution = int(input("Enter your Constitution stat : "))

print("\nThe Gatekeeper evaluates your character...\n")

# 1. Both greater than 0
if strength > 0 and constitution > 0:
    print("Both stats are positive.")
else:
    print("One of your stats is zero or less. The Gatekeeper denies entry.")

# 2. Both greater than 100
if strength > 100 and constitution > 100:
    print("You must be a legendary hero! The dungeon trembles before you.")
else:
    print("You are still learning. The gatekeeper remains Skeptical.")

# 3. Either even or odd stats
if strength % 2 == 0 or constitution % 2 == 0:
    print("Your stats are balanced; the Gatekeeper nods approvingly.")
else:
    print("Both stats are odd; You know your missing out on +1 modifier right?")

# 4. Either less than 100
if strength < 100 or constitution < 100:
    print("One stat is low, the dungeon might be tricky.")
else:
    print("Both stats strong, path looks fruitful.")

# 5. Not equal
if strength != constitution:
    print("Your build is strategic. You must have unique skills.")
else:
    print("Your build is balanced, but not exceptional.")

# 6. Not zero
if not (strength == 0 or constitution == 0):
    print("All stats presented. The Gatekeeper allows you to attempt entry!")
else:
    print("Missing a stat! The Gatekeeper blocks the entrance.")

# 7. Entry or denial final check
print("\nFinal Gate Check:")
if strength >= 20 and constitution >= 20:
    print("You are a legendary hero! You enter the dungeon with ease.")
elif strength >= 15 and constitution >= 15:
    print("You are strong! The dungeon gate allows you in, but challenges await.")
elif strength >= 10 and constitution >= 10:
    print("You are average. You may enter, but proceed cautiously.")
else:
    print("You are not ready to enter the dungeon. Train more before attempting again.")

# 8. Strength categorization
print("\nStrength Categorization:")
if strength > 0:
    print("Strength is Positive.")
elif strength < 0:
    print("Strength is Negative.")
else:
    print("Strength is Zero.")
