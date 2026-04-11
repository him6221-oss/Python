"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: THE HERO BLUEPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class named 'Hero'.
[ ] 3. Use __init__ to give the hero a name and a power.
[ ] 4. Add a method 'intro' that prints "I am [name] and I use [power]!".
[ ] 5. Instantiate two hero objects and call their 'intro' method.
-----------------------------------------------------------------------
"""

# HERO CLASS (Blueprint)
class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def intro(self):
        print(f"I am {self.name} and I use {self.power}!")


# CREATE TWO HERO OBJECTS
hero1 = Hero("Batman", "My Brain")
hero2 = Hero("Flash", "The Speed Force")


# CALL METHODS
hero1.intro()
hero2.intro()