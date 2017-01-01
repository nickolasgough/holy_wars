import pygame
import HomeScreen

# Initialize pygame.
pygame.init()
pygame.font.init()

# Define the width and height of the game.
WIDTH = 800
HEIGHT = 600

# Initialize the display.
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")

# Initialize the clock.
clock = pygame.time.Clock()
clock.tick(100)

# Initialize the home screen.
home = HomeScreen.HomeScreen(WIDTH, HEIGHT)

# Continue drawing the frame until the game has been closed.
quit = False
while (not quit):
    # Process any events.
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            if (home.in_button(mouse_position)):
                quit = True

    # Change the button color if the mouse is inside the button.
    if (home.in_button(mouse_position)):
        home.button_hover()
    else:
        home.button_leave()

    # Draw the home screen.
    home.draw(display)

    # Update the screen.
    pygame.display.update()

# Quit the game.
pygame.quit()