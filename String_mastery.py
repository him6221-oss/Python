"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Robert Romanowski
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR ---
instrument = "Acoustic Guitar"

print(len(instrument))
print(instrument[0])
print(instrument[len(instrument) - 1])

print(min(instrument))
print(max(instrument))


# --- TASK 2: THE CLEANUP CREW ---
messy_input = "   vOLUME_knob_11   "

cleaned = messy_input.strip()
cleaned = cleaned.upper()
cleaned = cleaned.replace("_", " ")

print(cleaned)


# --- TASK 3: THE VALIDATOR ---
serial_number = "90210"

if serial_number.isdigit():
    print("Valid Serial")
else:
    print("Invalid Serial")


# --- TASK 4: THE DUCK BRIDGE ---
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)

    print("There was a teacher who had a duck and Ducky was his Name-o")
    print((current_name + "\n") * 3)
    print("and Ducky was his Name-o!\n")

    duck_letters[count] = "x"
    count = count + 1


# Finale
final_name = " ".join(duck_letters)
print((final_name + "\n") * 3)
print("and Ducky was his Name-o!")