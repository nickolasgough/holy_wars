# Represents a character.
class Character:
    # Store the character's name.
    __name = ""

    # Store the character's collection of abilities.
    __abilities = []

    # Store the character's image.
    __image = None

    # Initialize the character,
    def __init__(self, name, abilities, image):
        self.__name = name
        self.__abilities = abilities
        self.__image = image

    # Retrieve the character's name.
    def get_name(self):
        return self.__name

    # Retrieve the name of the ability.
    def get_ability_name(self, ability_num):
        # Check that the ability number is within range.
        if (ability_num >= len(self.__abilities)):
            raise Exception("Ability index out of bounds for " + self.__name + ".")
        return self.__abilities[ability_num].get_name()

    # Retrieve the damage of the ability.
    def get_ability_damage(self, ability_num):
        # Check that the ability number is within range.
        if (ability_num >= len(self.__abilities)):
            raise Exception("Ability index out of bounds for " + self.__name + ".")
        return self.__abilities[ability_num].get_damage()