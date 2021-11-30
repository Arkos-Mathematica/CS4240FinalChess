"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

width = 40
height = 40
margin = 10
from chess import board

pygame.init()

# Set the width and height of the screen [width, height]
size = (8*width+9*margin, 8*height+9*margin)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True




    # --- Game logic should go here
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # --- Drawing code should go here

    screen.fill(BLACK)
    for row in range (8):
        for col in range(8):
            pygame.draw.rect(screen, WHITE, [margin+col*(margin+width),margin+row*(margin+height),width, height])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    for row in range(8):
        for col in range(8):
            text = font.render(str(board[row][col]), True, BLACK)
            screen.blit(text, [margin+col*(margin+width),margin+row*(margin+height)])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
