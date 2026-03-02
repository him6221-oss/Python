"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
Name: Robert
-----------------------------------------------------------------------
"""

import random

# Magic 8 Ball responses
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "It is certain",
    "Very doubtful",
    "Outlook good",
    "Cannot predict now"
)

print("Welcome to the Magic 8 Ball!")

while True:
    question = input("Ask a question (or type 'quit' to exit): ")

    # Sanitize input
    clean_question = question.strip().lower()

    # Exit condition
    if "quit" in clean_question:
        print("Goodbye!")
        break

    # Random response
    answer = random.choice(RESPONSES)
    print("The 8ball says:", answer)