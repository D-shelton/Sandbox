import pygame
import random

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
#sets window size
MAIN_MENU_OFFSET = 50
#sets width between edge of menu and edge of program window
NUM_STATS = 6
#sets number of stats to be rolled, 6 for D&D

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#define program window size as screen

main_menu = pygame.Rect(MAIN_MENU_OFFSET, MAIN_MENU_OFFSET, (SCREEN_WIDTH - (MAIN_MENU_OFFSET*2)), (SCREEN_HEIGHT - (MAIN_MENU_OFFSET*2)))
run = True
#sets main menu window placement


while run:
#game loop
    screen.fill('black')
    #set background image
    pygame.draw.rect(screen, (125, 0, 175), main_menu)
    #draw main menu box
    key = pygame.key.get_pressed()
    #get current key
    for event in pygame.event.get():
        #quit game logic searching for quit event
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    #update screen at end of loop
pygame.quit()
