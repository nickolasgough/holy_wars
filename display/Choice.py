import pygame

# Define necessary colors.
BLACK = (0, 0, 0)

# Represents a choice within the opponent selection screen.
class Choice:
    # Store if this choice has been selected.
    __selected = False

    # Store the dimensions of the rectangle.
    __DIMENSIONS = ()

    # Define and store the original rectangle color.
    __ORIGINAL_COLOR = (55, 125, 239)
    __HOVER_COLOR = (131, 175, 247)

    # Define and store the stroke width to use.
    __STROKE_WIDTH = 3

    # Store the image to be displayed within the rectange.
    __images = []
    __IMAGE_DIMENSIONS = ()
    __IMAGE_COORDINATES = ()
    __current_image = 0

    # Store the name of the character represented by this choice.
    __name = ""
    __FONT_SIZE = 30
    __text = None
    __TEXT_COORDINATES = ()

    # Store a boolean to determine if the mouse is hovering over the choice.
    __hovering = False

    # Define and store the counter and max counter value for switching images.
    __counter = 0
    __MAX_COUNTER = 250

    # Initialize the choice.
    def __init__(self, dimensions, images, image_dimensions, name):
        # Initialize the dimensions of the choice.
        self.__DIMENSIONS = dimensions

        # Initialize the image.
        self.__images = images
        self.__IMAGE_DIMENSIONS = image_dimensions
        self.__IMAGE_COORDINATES = (self.__DIMENSIONS[0]+(image_dimensions[0]/2), self.__DIMENSIONS[1]+(image_dimensions[1]/2))

        # Initialize the name.
        self.__name = name
        name = name[0].upper()+name[1:]
        font = pygame.font.Font(None, self.__FONT_SIZE)
        self.__text = font.render(name, True, BLACK)
        rect = self.__text.get_rect()
        x = self.__DIMENSIONS[0]+(self.__DIMENSIONS[2]/2)-(rect[2]/2)
        y = self.__DIMENSIONS[1]+(self.__DIMENSIONS[3])-(rect[3]*3/2)
        self.__TEXT_COORDINATES = (x, y)

    # Draw the choice.
    def draw(self, display):
        # Draw the rectangle.
        color = self.__ORIGINAL_COLOR
        if (self.__hovering or self.__selected):
            color = self.__HOVER_COLOR
        pygame.draw.rect(display, color, self.__DIMENSIONS)

        # Draw the name.
        display.blit(self.__text, self.__TEXT_COORDINATES)

        # Draw the image.
        display.blit(self.__images[self.__current_image], self.__IMAGE_COORDINATES)

        # Increment the counter and determine if the image must be changed, if necessary.
        if (self.__hovering):
            self.__counter += 1
            if (self.__counter >= self.__MAX_COUNTER):
                self.__counter = 0
                self.__current_image = (self.__current_image+1)%len(self.__images)
        else:
            self.__counter = 0
            self.__current_image = 0

    # Indicate the mouse is hovering over this choice.
    def is_hovering(self):
        self.__hovering = True

    # Indicate the mouse is not hovering of the choice.
    def not_hovering(self):
        self.__hovering = False

    # Determine if the mouse is within the choice.
    def in_choice(self, mouse_position):
        if (self.__DIMENSIONS[0] <= mouse_position[0] <= self.__DIMENSIONS[0]+self.__DIMENSIONS[2] and self.__DIMENSIONS[1] <= mouse_position[1] <= self.__DIMENSIONS[1]+self.__DIMENSIONS[3]):
            return True

        return False

    # Make the choice selected.
    def selected(self):
        self.__selected = True

    # Make the choice unselected.
    def unselected(self):
        self.__selected = False

    # Retrieve the selection.
    def get_selection(self):
        return self.__selected

    # Retrieve the name of the choice.
    def get_name(self):
        return self.__name