import pygame
import HomeScreen
import OpponentSelectionScreen
import StageSelectionScreen
import BattleScreen
import tkMessageBox

# Initialize pygame.
pygame.init()
pygame.font.init()

# Define the width and height of the game.
WIDTH = 600
HEIGHT = 600

# Initialize the display.
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holy Wars")

# Initialize the clock.
clock = pygame.time.Clock()
clock.tick(360)

# Initialize the home screen.
home = HomeScreen.Home(WIDTH, HEIGHT)

# Continue drawing the frame until the game has been closed.
quit = False
next = False
while (not(quit or next)):
    # Process any events.
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit = True
        elif (event.type == pygame.MOUSEBUTTONUP and home.in_button(mouse_position)):
            next = True

    # Change the button color if the mouse is inside the button.
    if (home.in_button(mouse_position)):
        home.button_hover()
    else:
        home.button_leave()

    # Draw the home screen.
    home.draw(display)
    pygame.display.flip()

# Quit the game.
if (quit):
    pygame.quit()

# Initialize the opponent selection screen.
opponent_selection = OpponentSelectionScreen.OpponentSelection(WIDTH, HEIGHT)

# Continue to the opponent selection screen.
quit = False
next = False
opponent = None
while (not(quit or next)):
    # Process any events.
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit = True
        elif (event.type == pygame.MOUSEBUTTONUP and opponent_selection.in_button(mouse_position)):
            opponent = opponent_selection.get_selection()
            if (opponent is None):
                tkMessageBox.showinfo("Select Opponent", "Please select an opponent before beginning the battle.")
            else:
                next = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            opponent_selection.made_selection(mouse_position)

    # Determine if the mouse is within the button.
    if (opponent_selection.in_button(mouse_position)):
        opponent_selection.button_hover()
    else:
        opponent_selection.button_leave()

    # Determine if the mouse is hovering within once of the selections.
    opponent_selection.in_a_choice(mouse_position)

    # Draw the player selection screen.
    opponent_selection.draw(display)
    pygame.display.flip()

# Quit the game.
if (quit):
    pygame.quit()

# Initialize the opponent selection screen.
battleground_selection = StageSelectionScreen.StageSelection(WIDTH, HEIGHT)

# Continue to the battleground selection screen.
quit = False
next = False
battleground = None
while (not(quit or next)):
    # Process any events.
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit = True
        elif (event.type == pygame.MOUSEBUTTONUP and battleground_selection.in_button(mouse_position)):
            battleground = battleground_selection.get_selection()
            if (battleground is None):
                tkMessageBox.showinfo("Select Stage", "Please select a battleground before beginning the battle.")
            else:
                next = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            battleground_selection.made_selection(mouse_position)

    # Determine if the mouse is within the button.
    if (battleground_selection.in_button(mouse_position)):
        battleground_selection.button_hover()
    else:
        battleground_selection.button_leave()

    # Determine if the mouse is hovering within once of the selections.
    battleground_selection.in_a_choice(mouse_position)

    # Draw the player selection screen.
    battleground_selection.draw(display)
    pygame.display.flip()

if (quit):
    pygame.quit()

# Initialize the opponent selection screen.
battle = BattleScreen.Battle(WIDTH, HEIGHT, opponent, battleground)

# Continue to the battle screen.
quit = False
next = False
while (not(quit or next)):
    # Process any events.
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit = True

    # Draw the player selection screen.
    battle.draw(display)
    pygame.display.flip()

if (quit):
    pygame.quit()