import pygame
import sys
import os 
import time
from pygame.locals import *
from board import Board
from piece import Piece

pygame.init() # initialize pygame
screen = pygame.display.set_mode((899,650))

# os.path.join properly forms a cross-platform relative path
# by joining directory names

bg = pygame.image.load(os.path.join("sprites", "board.jpg"))

bd = Board()


# size of each box in 65 x 65
# rect = Rect(65*column, 64*row, 65, 65)
        
pygame.display.set_caption('Chess {made by @xlamide}')

row = 1
column = 1
running = True

# Render Chess Board to Screen 
screen.blit(bg, (0,0))
pygame.display.update()

while running:
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            loc = pygame.mouse.get_pos()
            location = Piece.getLocation(loc)
            # print(location)
            pygame.display.update()
            # pygame.draw.rect(screen, (123,123,123), rect)

            screen.blit(bg, (0,0))

                
        if event.type == MOUSEBUTTONUP:
            pass
        if event.type == pygame.QUIT:
            running = False

        

 
    # Render all chess piece according to their position
    for piece in Board.pieces:
        

        if Board.pieces[piece] == "":
            Board.pieces[piece] = "empty"

        shot = pygame.image.load(os.path.join("sprites", str(Board.pieces[piece])+".png"))
        
        # Place each piece in their respective locaton 
        screen.blit(shot,(66*column,66*row))


       

        column +=1

        # print(f"Row: {row}")
        # print(f"Column: {column}")


        # Changing the Column and Row values
        # To arrange the pieces at the right
        # spot
        if column > 8:
            column = 1
            row += 1
        
        if row > 8:
            column = 1
            row = 1
        
        pygame.display.update()

       

pygame.quit()




    
    # pygame.draw.rect(bg, RED, rect)
