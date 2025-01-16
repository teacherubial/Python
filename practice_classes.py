# practice_classes.py
#

class Pokemon:
    def __init__(self):
        """A class representing a Pokemon."""
        self.name = ""
        self.weight = 0      # kgs
        self.num_legs = 0    
        self.type = "Normal"
        self.age = 0         # years

    def speak(self) -> None:
        """Pokemon makes a noise."""
        print(f"{self.name if self.name else "A Pokemon"} says, 'Roaaaaaar!'")

    def move(self) -> None:
        """Pokemon does it's primary move."""
        print(f"{self.name if self.name else "A Pokemon"} used Tackle.")


# Your Activity
"""Above is a class that represents a Pokemon.

Your task is split up into two parts: creating a child class, and creating objects of both classes. See the tasks below."""


# --- Task 1 - Creating a Child Class ---
"""A. Using the example that we did in class as a template, create a child class of Pokemon.

You can choose one of your own if you are familiar with Pokemon.

If you aren't, create a child class that represents Snivy. You can find information here.
https://pokemondb.net/pokedex/snivy

In the constructor of the child class, set the values of name, and type to the respective name and type of the Pokemon.
e.g. if Squirtle is our Pokemon.

...

def __init__(self):
    # If you know how to use super().__init__(), you can here if you wish.
    
    self.name = "Squirtle"
    self.weight = 0
    self.num_legs = 2
    self.type = "Water
    self.age = 0

...


B. Create a new method (function) for your child class that represents a special move of the Pokemon.

Call your method move_two().

It prints out:
    <pokemon-name> used <move>.

One of the moves, for example, for Squirtle found in https://pokemondb.net/move/leaf-storm is Water Pump.

In this example, move_two() would print out:
    Squirtle used Water Pump.
"""




# --- Task 2 - Creating and Testing Pokemon Objects ---
"""Now that you've created your own child class of Pokemon. Let's test them out.

Create one Pokemon object and one of your Child Class object. Store them in variables named pokemon_one and pokemon_two.

Change the name, weight, and age values of each of the pokemon objects.

For each pokemon object, use the speak() and move() methods.

For your child class object, use the move_two() method.
"""

