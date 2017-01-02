import pygame

# Define necessary colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Represents the beginning screen of the game.
class Home:
    # Define and store the title text.
    __title_text = None
    __TITLE_SIZE = 100
    __TITLE_COORDINATES = ()

    # Define and store the button dimensions.
    __BUTTON_DIMENSIONS = ()
    __BUTTON_COLOR = (55, 125, 239)
    __ORIGINAL_COLOR = (55, 125, 239)
    __HOVER_COLOR = (131, 175, 247)

    # Define and store the button text.
    __button_text = None
    __TEXT_SIZE = 40
    __TEXT_DIMENSIONS = ()

    # Define and store the background color.
    __BACKGROUND_IMAGE = pygame.image.load("../images/sky.png")
    __BACKGROUND_COLOR = (255, 255, 255)
    __SPEED = 2

    # Load and store the background image.
    __character_image = pygame.image.load("../images/gingko_right_0.png")
    __GINGKO_IMAGES = [pygame.image.load("../images/gingko_right_0.png"), pygame.image.load("../images/gingko_right_1.png"), pygame.image.load("../images/gingko_right_2.png"), pygame.image.load("../images/gingko_right_3.png")]

    # Define and store the image dimensions.
    __IMAGE_DIMENSIONS = ()
    __image_x = 0
    __image_y = 0

    # Store the width and height of the window.
    __WIDTH = 0
    __HEIGHT = 0

    # Define and store the counter for changing images.
    __counter = 0
    __current_image = 0
    __COUNTER_MAX = 40
    __INCREASE = 1

    # Store a boolean to determine if the background image has been drawn.
    __bg_drawn = False

    # Initialize the home screen.
    def __init__(self, width, height):
        # Transform the background image.
        self.__BACKGROUND_IMAGE = pygame.transform.scale(self.__BACKGROUND_IMAGE, (width, height))

        # Initialize the button.
        self.__BUTTON_DIMENSIONS = ((width/2)-(185/2), height-200, 185, 50)
        self.__TEXT_DIMENSIONS = (self.__BUTTON_DIMENSIONS[0]+(self.__TEXT_SIZE/2), self.__BUTTON_DIMENSIONS[1]+(self.__TEXT_SIZE/3))
        font = pygame.font.Font(None, self.__TEXT_SIZE)
        self.__button_text = font.render("Play Game", True, BLACK)

        # Initialize the image dimensions.
        self.__IMAGE_DIMENSIONS = (100, 100)

        # Rescale the images.
        self.__GINGKO_IMAGES[0] = pygame.transform.scale(self.__GINGKO_IMAGES[0], self.__IMAGE_DIMENSIONS)
        self.__GINGKO_IMAGES[1] = pygame.transform.scale(self.__GINGKO_IMAGES[1], self.__IMAGE_DIMENSIONS)
        self.__GINGKO_IMAGES[2] = pygame.transform.scale(self.__GINGKO_IMAGES[2], self.__IMAGE_DIMENSIONS)
        self.__GINGKO_IMAGES[3] = pygame.transform.scale(self.__GINGKO_IMAGES[3], self.__IMAGE_DIMENSIONS)
        self.__character_image = self.__GINGKO_IMAGES[0]

        # Initialize the image x and y positions.
        self.__image_x = 0
        self.__image_y = (height/2)-50

        # Initialize the width and height of the window.
        self.__WIDTH = width
        self.__HEIGHT = height

        # Initialize the title.
        font = pygame.font.Font(None, self.__TITLE_SIZE)
        font.set_underline(True)
        self.__title_text = font.render("Holy Wars", True, BLACK)
        rect = self.__title_text.get_rect()
        x = (self.__WIDTH/2)-(rect[2]/2)
        y = 100
        self.__TITLE_COORDINATES = (x, y)

    # Draw the home screen.
    def draw(self, display):
        # Draw the background image.
        display.blit(self.__BACKGROUND_IMAGE, (0, 0))

        # Draw the title.
        display.blit(self.__title_text, self.__TITLE_COORDINATES)

        # Draw the button.
        pygame.draw.rect(display, self.__BUTTON_COLOR, self.__BUTTON_DIMENSIONS)
        display.blit(self.__button_text, self.__TEXT_DIMENSIONS)

        # Draw the character image.
        self.__image_x += self.__SPEED
        display.blit(self.__character_image, (self.__image_x, self.__image_y))
        if (self.__image_x > self.__WIDTH+self.__IMAGE_DIMENSIONS[0]):
            self.__image_x = 0-self.__IMAGE_DIMENSIONS[0]

        # Increase the counter and change the image if necessary.
        self.__counter += self.__INCREASE
        if (self.__counter >= self.__COUNTER_MAX):
            self.__counter = 0
            self.__current_image = (self.__current_image+1)%len(self.__GINGKO_IMAGES)
            self.__character_image = self.__GINGKO_IMAGES[self.__current_image]


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