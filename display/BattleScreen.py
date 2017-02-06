import pygame
import AbilitySelectionPanel
import Ability

# Define necessary colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Represents the battle screen.
class Battle:
    # Define and store the player and opponent names.
    __player_name = None
    __PLAYER_COORDINATES = ()
    __opponent_name = None
    __OPPONENT_COORDINATES = ()
    __NAME_SIZE = 50
    __NAME_DIMENSIONS = (200, 50)
    __NAME_COLOR = (55, 125, 239)

    # Store the colors for displaying the health and ability points.
    __HEALTH_COLOR = (3, 175, 17)
    __ABILITY_COLOR = (255, 191, 0)
    __THICKNESS = 13

    # Store the background image.
    __battleground = None

    # Store the opponent.
    __opponent = None

    # Store the width and the height of the screen.
    __WIDTH = 0
    __HEIGHT = 0

    # Store the ability selection panel.
    __ability_selection = None

    # Initialize the battle screen.
    def __init__(self, width, height, opponent_name, battleground):
        # Initialize the width and height.
        self.__WIDTH = width
        self.__HEIGHT = height

        # Initialize the collection of abilities.
        abilities = []
        abilities.append(Ability.Ability("Something", 50, 50))
        abilities.append(Ability.Ability("Something", 50, 50))
        abilities.append(Ability.Ability("Something", 50, 50))
        abilities.append(Ability.Ability("Something", 50, 50))

        # Initialize the ability selection panel.
        panel_width = width
        panel_height = 100
        panel_y = height-panel_height
        self.__ability_selection = AbilitySelectionPanel.AbilitySelection(panel_width, panel_height, panel_y, abilities)

        # Initialize the names.
        font = pygame.font.Font(None, self.__NAME_SIZE)
        self.__player_name = font.render("Gingko", True, BLACK)
        rect = self.__player_name.get_rect()
        self.__PLAYER_COORDINATES = ((self.__NAME_DIMENSIONS[0]/2)-(rect[2]/2), (self.__NAME_DIMENSIONS[1]/2)-(rect[3]/2))

        font = pygame.font.Font(None, self.__NAME_SIZE)
        opponent_name = opponent_name[0].upper()+opponent_name[1:]
        self.__opponent_name = font.render(opponent_name, True, BLACK)
        rect = self.__opponent_name.get_rect()
        self.__OPPONENT_COORDINATES = (width-(self.__NAME_DIMENSIONS[0]/2)-(rect[2]/2), (self.__NAME_DIMENSIONS[1]/2)-(rect[3]/2))

        # Initialize the background image.
        battleground = pygame.image.load("../images/"+battleground+".png")
        self.__battleground = pygame.transform.scale(battleground, (self.__WIDTH, self.__HEIGHT))

    # Draw the battle screen.
    def draw(self, display):
        # draw the battleground.
        display.blit(self.__battleground, (0, 0))

        # Draw the player's name, health, and ability points.
        dimensions = (0, 0, self.__NAME_DIMENSIONS[0], self.__NAME_DIMENSIONS[1])
        pygame.draw.rect(display, self.__NAME_COLOR, dimensions)
        display.blit(self.__player_name, self.__PLAYER_COORDINATES)

        health_coords = (0, self.__NAME_DIMENSIONS[1])
        ability_coords = (0, health_coords[1]+self.__THICKNESS)
        self.draw_health_ability(display, 100, health_coords, 100, ability_coords)

        # Draw the opponent's name, health, and ability points.
        dimensions = (self.__WIDTH-self.__NAME_DIMENSIONS[0], 0, self.__NAME_DIMENSIONS[0], self.__NAME_DIMENSIONS[1])
        pygame.draw.rect(display, self.__NAME_COLOR, dimensions)
        display.blit(self.__opponent_name, self.__OPPONENT_COORDINATES)

        health_coords = (self.__WIDTH-100, self.__NAME_DIMENSIONS[1])
        ability_coords = (self.__WIDTH-100, health_coords[1]+self.__THICKNESS)
        self.draw_health_ability(display, 100, health_coords, 100, ability_coords)

        # Draw the ability selection panel.
        self.__ability_selection.draw(display)

    # Draw the health and ability points.
    def draw_health_ability(self, display, health, health_coords, ability, ability_coords):
        # Draw the health bar.
        dimensions = (health_coords[0], health_coords[1], health, self.__THICKNESS)
        pygame.draw.rect(display, self.__HEALTH_COLOR, dimensions)

        # Draw the ability bar.
        dimensions = (ability_coords[0], ability_coords[1], ability, self.__THICKNESS)
        pygame.draw.rect(display, self.__ABILITY_COLOR, dimensions)