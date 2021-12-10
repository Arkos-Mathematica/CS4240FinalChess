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

in_game = False

pieces_dict={
    "p" : "Pieces/BP.png",
    "P" : "Pieces/WP.png",
    "r" : "Pieces/BR.png",
    "R" : "Pieces/WR.png",
    "n" : "Pieces/BN.png",
    "N" : "Pieces/WN.png",
    "b" : "Pieces/BB.png",
    "B" : "Pieces/WB.png",
    "q" : "Pieces/BQ.png",
    "Q" : "Pieces/WQ.png",
    "k" : "Pieces/BK.png",
    "K" : "Pieces/WK.png",
    "0" : "Pieces/0.png"
}


pygame.init()

# Set the width and height of the screen [width, height]
size = (8*width+9*margin + 70, 8*height+9*margin)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('segoeuisymbol', height, False)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False



#start creating button classes from http://programarcadegames.com/python_examples/show_file.php?file=sprite_collect_blocks.py
class Button(pygame.sprite.Sprite):
    """
    This class represents the button
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block, the function it calls,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([50, 30])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.y = y
        self.rect.x = x

# start/back as instances of Button class
board_sprites = pygame.sprite.Group()
home_sprites = pygame.sprite.Group()

start = Button(GREEN, (size[0]//2)-25, (size[1]//2)-15)
home_sprites.add(start)

back = Button(GREEN, size[0]-60, 10)
board_sprites.add(back)

def change_status():
    print("changing status")
    global in_game
    in_game = not in_game


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
                    piece = pygame.image.load(pieces_dict[str(board[row][col])])
                    piece = pygame.transform.scale(piece, (width, height))
                    screen.blit(piece, [margin+col*(margin+width), (7*height+8*margin) - (row*(margin+height))])
    else:
        for row in range (8):
            for col in range(8):
                pygame.draw.rect(screen, WHITE, [margin+col*(margin+width),margin+row*(margin+height),width, height])
                if ((row + col)% 2) == 0:
                    pygame.draw.rect(screen, GREEN, [(margin+col*(margin+width)) , (margin+row*(margin+height)), width, height], ((height - width)))

        for row in range(8):
            for col in range(8):
                if board[row][col] != 0:
                    piece = pygame.image.load(pieces_dict[str(board[row][col])])
                    piece = pygame.transform.scale(piece, (width, height))
                    screen.blit(piece, [(7*width+8*margin)-(col*(margin+width)), margin+(row*(margin+height))])
    board_sprites.draw(screen)
def print_home():
    #code for a home Screen
    screen.fill(WHITE)
    font = pygame.font.SysFont('montserrat', height, True)
    text = font.render("Welcome to Sanspassant", True, BLACK)
    screen.blit(text, [size[0]/12, size[1]//3])
    home_sprites.draw(screen)



def turn(row, column):

    global position1
    global position2
    global color
    global start_row
    global start_col
    global end_row
    global end_col

    if position1 == 0:

        if color:
            start_row, start_col=row-1, column-1
            position1 = 1

        else:

            start_row, start_col = 8 - row, 8 - column
            position1 = 1

        print(start_col+1, start_row+1)

    elif position2 == 0:

        if color:
            end_row, end_col = row-1, column-1
            position2 = 1

        else:

            end_row, end_col = 8 - row, 8 - column
            position2 = 1

        print(end_col+1, end_row+1)

        position1, position2 = 0, 0

        if end_row > 7:

            end_row = 7

        if end_row < 0:

            end_row = 0

        if end_col > 7:

            end_col = 7

        if end_col < 0:

            end_col = 0

        if start_row > 7:

            start_row = 7

        if start_row < 0:

            start_row = 0

        if start_col > 7:

            start_col = 7

        if start_col < 0:

            start_col = 0

        if move(start_row, start_col, end_row, end_col, board, color) == "Illegal Move":

            pass

        else:

            color = (color + 1) % 2

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
            pos = event.pos
            if start.rect.collidepoint(pos) or back.rect.collidepoint(pos):
                print("you clicked a button!")
                change_status()
                color = 1
                clear_board()
                print(in_game)
            elif in_game:
                column = 1+(pos[0] // (width + margin))
                row = 8-(pos[1] // (height + margin))
                turn(row, column)


    # --- Game logic should go here
    # --- Screen-clearing code goes here


    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # --- Drawing code should go here


    if in_game:
        print_board(color)
    else:
        print_home()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
