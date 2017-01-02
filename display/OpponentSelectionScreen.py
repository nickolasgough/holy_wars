import pygame
import Choice

# Define necessary colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Represents the player selection screen.
class OpponentSelection:
    # Store the width and height of the screen.
    __WIDTH = 0
    __HEIGHT = 0

    # Define and store the background color.
    __BACKGROUND_COLOR = (1, 63, 163)

    # Store the collection of choices.
    __choices = []

    # Store the title.
    __title_text = None
    __TITLE_COORDINATES = ()
    __TITLE_SIZE = 60

    # Store the button.
    __button_text = None
    __TEXT_COORDINATES = ()
    __BUTTON_DIMENSIONS = ()
    __BUTTON_SIZE = 40
    __BUTTON_COLOR = (55, 125, 239)
    __ORIGINAL_COLOR = (55, 125, 239)
    __HOVER_COLOR = (131, 175, 247)

    # Initialize the player selection screen.
    def __init__(self, width, height):
        # Initialize the title text
        font = pygame.font.Font(None, self.__TITLE_SIZE)
        font.set_underline(True)
        self.__title_text = font.render("Select Your Opponent", True, BLACK)
        rect = self.__title_text.get_rect()
        self.__TITLE_COORDINATES = ((width/2)-rect[2]/2, 25)

        # Store the height and width of the screen.
        self.__WIDTH = width
        self.__HEIGHT = height

        # Initialize the dimensions and names of each choice.
        x, y = 0, 75
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
                y = y+rect_height

            # Determine the name.
            dimensions = (x, y, rect_width, rect_height)
            image_dimensions = (100, 100)
            choice = self.create_choice(dimensions, image_dimensions, names[n])
            self.__choices.append(choice)

            # Increment the x coordinate.
            x += rect_width

        # Initialize the button.
        self.__BUTTON_DIMENSIONS = ((width/2)-(185/2), height-75, 200, 50)
        font = pygame.font.Font(None, self.__BUTTON_SIZE)
        self.__button_text = font.render("Begin Battle", True, BLACK)
        rect = self.__button_text.get_rect()
        self.__TEXT_COORDINATES = (self.__BUTTON_DIMENSIONS[0]+(self.__BUTTON_DIMENSIONS[2]/2)-(rect[2]/2), self.__BUTTON_DIMENSIONS[1]+(self.__BUTTON_DIMENSIONS[3]/2)-(rect[3]/2))

    # Draw the player selection screen.
    def draw(self, display):
        # Fill the background with white.
        display.fill(self.__BACKGROUND_COLOR)

        # Draw the title text.
        display.blit(self.__title_text, self.__TITLE_COORDINATES)

        # Draw the button.
        pygame.draw.rect(display, self.__BUTTON_COLOR, self.__BUTTON_DIMENSIONS)
        display.blit(self.__button_text, self.__TEXT_COORDINATES)

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

    # Determine if the mouse is within the button.
    def in_button(self, mouse_position):
        if (self.__BUTTON_DIMENSIONS[0] <= mouse_position[0] <= self.__BUTTON_DIMENSIONS[0]+self.__BUTTON_DIMENSIONS[2] and self.__BUTTON_DIMENSIONS[1] <= mouse_position[1] <= self.__BUTTON_DIMENSIONS[1]+self.__BUTTON_DIMENSIONS[3]):
            return True

        return False

    # Change the button to hover color.
    def button_hover(self):
        self.__BUTTON_COLOR = self.__HOVER_COLOR

    # Change the button color to the original button color.
    def button_leave(self):
        self.__BUTTON_COLOR = self.__ORIGINAL_COLOR

    # Get the name of the selected choice.
    def get_selection(self):
        # Determine which choice was selected
        c = None
        for choice in self.__choices:
            if (choice.get_selection()):
                c = choice

        if (c is not None):
            return c.get_name()
        else:
            return None