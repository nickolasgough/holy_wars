# Represents a character's ability.
class Ability:
    # Store the name of the ability.
    __name = ""

    # Store the damage caused by the ability.
    __damage = 0

    # Initialize the ability.
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    # Retrieve the name.
    def get_name(self):
        return self.__name

    # Retrieve the damage dealt.
    def get_damage(self):
        return self.__damage