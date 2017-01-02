import pygame
import Choice

# Define necessary colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Represents the player selection screen.
class OpponentSelectionScreen:
    # Store the width and height of the screen.
    __WIDTH = 0
    __HEIGHT = 0

    # Store the collection of choices.
    __choices = []

    # Initialize the player selection screen.
    def __init__(self, width, height):
        # Store the height and width of the screen.
        self.__WIDTH = width
        self.__HEIGHT = height

        # Initialize the dimensions and names.
        x, y = 0, 0
        rect_width, rect_height = 200, 200
        names = {
            0: "bahamut",
            1: "ifrit",
            2: "titan",
            3: "death",
            4: "ryuk",
            5: "devil"
        }

        # Initialize the choices.
        for n in range(0, 6):
            # Determine the coordinates.
            if (n == 0 or n == 3):
                x = 0
            if (n == 3):
                y = rect_height

            # Determine the name.
            dimensions = (x, y, rect_width, rect_height)
            image_dimensions = (100, 100)
            choice = self.create_choice(dimensions, image_dimensions, names[n])
            self.__choices.append(choice)

            # Increment the x coordinate.
            x += rect_width

    # Draw the player selection screen.
    def draw(self, display):
        # Fill the background with white.
        display.fill(WHITE)

        # Draw each of the choices.
        for choice in self.__choices:
            choice.draw(display)

    # Create and return a choice element.
    def create_choice(self, dimensions, image_dimensions, name):
        # Load and scale the images.
        images = []
        images.append(pygame.image.load("../images/"+name+"_front_0.png"))
        images.append(pygame.image.load("../images/"+name+"_left_0.png"))
        images.append(pygame.image.load("../images/"+name+"_back_0.png"))
        images.append(pygame.image.load("../images/"+name+"_right_0.png"))
        images[0] = pygame.transform.scale(images[0], image_dimensions)
        images[1] = pygame.transform.scale(images[1], image_dimensions)
        images[2] = pygame.transform.scale(images[2], image_dimensions)
        images[3] = pygame.transform.scale(images[3], image_dimensions)

        # Create and return the choice element.
        choice = Choice.Choice(dimensions, images, image_dimensions, name)
        return choice

    # Determine which choice the mouse is hovering in.
    def in_a_choice(self, mouse_position):
        # Cycle through the choices to determine if the mouse is within one.
        c = None
        for choice in self.__choices:
            if (choice.in_choice(mouse_position)):
                choice.is_hovering()
                c = choice
            else:
                choice.not_hovering()

        return c

    # Determine if a selection was made.
    def made_selection(self, mouse_position):
        # Unselect all the choices.
        for choice in self.__choices:
            choice.unselected()

        # Determine if there is a selection and select it.
        c = self.in_a_choice(mouse_position)
        if (c is not None):
            c.selected()