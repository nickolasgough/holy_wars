import pygame
import AbilityChoice

# Represents the ability selection panel.
class AbilitySelection:
    # Store the width and height of the panel.
    __WIDTH = 0
    __HEIGHT = 0

    # Store the abilities that will be displayed.
    __abilities = []
    __ability_coords = []
    __ABILITY_DIMENSIONS = (100, 50)

    # Store the y_position.
    __Y_POSITION = 0

    # Store the color of the panel.
    __BACKGROUND_COLOR = (55, 125, 239)

    # Initialize the ability selection panel.
    def __init__(self, width, height, y_position, abilities):
        # Initialize the width and height of the ability selection panel.
        self.__WIDTH = width
        self.__HEIGHT = height

        # Initialize the abilities.
        self.__abilities = abilities

        # Initialize the y position of the ability selection panel.
        self.__Y_POSITION = y_position

        # Initialize the ability selections.
        x1 = 0
        x2 = 150
        width = self.__ABILITY_DIMENSIONS[0]
        height = self.__ABILITY_DIMENSIONS[1]
        for a in abilities:
            # Initialize the ability.
            coordinates = (x1+(x2 / 2)-(self.__ABILITY_DIMENSIONS[0]/2), self.__Y_POSITION+(self.__HEIGHT/2)-(self.__ABILITY_DIMENSIONS[1]/2))
            self.__abilities.append(AbilityChoice.Choice(width, height, coordinates, "something"))

            # Increment the x location.
            x1 += x2

    # Draw the ability panel.
    def draw(self, display):
        # Draw the ability selection panel.
        dimensions = (0, self.__Y_POSITION, self.__WIDTH, self.__HEIGHT)
        pygame.draw.rect(display, self.__BACKGROUND_COLOR, dimensions)

        # Draw the ability selections.
        for ability in self.__abilities:
            # Draw the ability.
            ability.draw(display)