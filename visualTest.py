"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

from chess import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (102, 204, 0)
RED = (255, 0, 0)

width = 40
height = 40
margin = 10

color=1

position1 = 0
position2 = 0


pygame.init()

# Set the width and height of the screen [width, height]
size = (8*width+9*margin, 8*height+9*margin)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Calibri', height, True, False)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

#print board function
def print_board(color):
    screen.fill(BLACK)
    if color:
        for row in range (8):
            for col in range(8):
                pygame.draw.rect(screen, WHITE, [margin+col*(margin+width),margin+row*(margin+height),width, height])
                if ((row + col)% 2) != 0:
                    pygame.draw.rect(screen, GREEN, [(margin+col*(margin+width)) , (margin+row*(margin+height)), width, height], ((height - width)))

        for row in range(8):
            for col in range(8):
                if board[row][col] != 0:
                    text = font.render(str(board[row][col]), True, BLACK)
                    screen.blit(text, [margin+col*(margin+width), (7*height+8*margin) - (row*(margin+height))])
    else:
        for row in range (8):
            for col in range(8):
                pygame.draw.rect(screen, WHITE, [margin+col*(margin+width),margin+row*(margin+height),width, height])
                if ((row + col)% 2) == 0:
                    pygame.draw.rect(screen, GREEN, [(margin+col*(margin+width)) , (margin+row*(margin+height)), width, height], ((height - width)))

        for row in range(8):
            for col in range(8):
                if board[row][col] != 0:
                    text = font.render(str(board[row][col]), True, BLACK)
                    screen.blit(text, [(7*width+8*margin)-(col*(margin+width)), margin+(row*(margin+height))])

def turn(row, column):

    global position1
    global position2

    if position1 == 0:

        if color:

            position1=str(row) + str(column)

        else:

            position1=str(9 - column) + str(9 - row)

        print(position1)

    elif position2 == 0:

        if color:

            position2=str(row) + str(column)

        else:

            position2=str(9 - column) + str(9 - row)

        print(position2)

        requested_move = position1 + position2

        move(requested_move, board, color)

        position1, position2 = 0, 0

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    from chess import board

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = 1+(pos[0] // (width + margin))
            row = 8-(pos[1] // (height + margin))
            turn(row, column)


    # --- Game logic should go here

    ##Below, not done

    '''mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed
    MOUSEBUTTONDOWN
    MOUSEBUTTONUP
    MOUSEBUTTONMOTION
'''
    # --- Screen-clearing code goes here


    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # --- Drawing code should go here


    print_board(color)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
