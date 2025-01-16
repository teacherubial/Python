# animal_classes.py
# Tim Ubial

class Pokemon:
    def __init__(self):
        self.name = ""
        self.weight  = 0
        self.num_legs = 0
        self.type = "Normal"

        print("A Pokémon is born! ✨✨")

    def speak(self):
        """Pokemon says its name and its cry."""
        print(f"{self.name} says, 'roooooooooar.'")

    def move(self):
        """Print the Pokemon's default move."""
        print(f"{self.name} used Tackle.")

class Pikachu(Pokemon):
    def __init__(self):
        self.name = "Pikachu"
        self.weight = 0
        self.num_legs = 4
        self.type = "Electric"

        print("⚡️ A Pikachu is born. ⚡️")

    def thundershock(self, defender: Pokemon) -> None:
        """Pikachu uses its secondary attack.
        It also checks for "effectiveness" based
        on the defending Pokemon's type."""

        # Pikachu used thundershock on <defending>
        # ""     ->      "A Pokemon"
        print(f"Pikachu used thundershock on {defender.name if defender.name else 'a pokemon'}.")

        if defender.type.lower() in ["water", "flying"]:
            print("It was super effective.")


# Create two pokemon objects
#    Pikachu
#    Squirtle
pokemon_one = Pikachu() 
pokemon_two = Pokemon()

# Change the properties of pokemon_one
print(pokemon_one.name)
pokemon_one.weight = 5
print(f"{pokemon_one.name} is {pokemon_one.weight} kgs and has {pokemon_one.num_legs} legs!")

# Your turn:
#    * change pokemon_two's properties
#    * print out the properties to validate what you did
pokemon_two.name, pokemon_two.weight, pokemon_two.num_legs = "Squirtle", 20, 2
print(f"{pokemon_two.name} is {pokemon_two.weight} kgs and has {pokemon_two.num_legs} legs!")

# Get pokemon_one and pokemon_two to speak
pokemon_one.speak()
pokemon_two.speak()

pokemon_one.move()
pokemon_two.move()

# Use thundershock from pokemon_one to attack pokemon_two
pokemon_one.thundershock(pokemon_two)
pokemon_two.type = "Water"   # squirtle -> water
pokemon_one.thundershock(pokemon_two)

# pokemon_two.thundershock(pokemon_one)