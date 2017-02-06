import pygame

# Represents an ability selection.
class Choice:
    # Store the height and width of the choice.
    __WIDTH = 0
    __HEIGHT = 0

    # Store the name of the ability.
    __name = ""

    # Store the coordinates of the choice.
    __COORDINATES = ()

    # Store a boolean indicating if the choice is selected.
    __selected = False

    # Store the color of the choice.
    __ABILITY_COLOR = (0, 63, 255)
    __ORIGINAL_COLOR = (0, 63, 255)
    __HOVER_COLOR = (0, 255, 250)

    # Initialize the choice.
    def __init__(self, width, height, coordinates, name):
        # Initialize the width and height of the choice.
        self.__WIDTH = width
        self.__HEIGHT = height

        # Initialize the coordinates of the choice.
        self.__COORDINATES = coordinates

        # Initialize the name of the ability.
        self.__name = name

    # Draw the choice.
    def draw(self, display):
        # Draw the choice.
        dimensions = (self.__COORDINATES[0], self.__COORDINATES[1], self.__WIDTH, self.__HEIGHT)
        pygame.draw.rect(display, self.__ABILITY_COLOR, dimensions)
