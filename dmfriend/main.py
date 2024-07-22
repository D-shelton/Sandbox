import pygame
from dicetest import *

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
#sets window size
MAIN_MENU_OFFSET = 50
#sets width between edge of menu and edge of program window
NUM_STATS = 6
#sets number of stats to be rolled, 6 for D&D



def main():
    pygame.display.set_caption("Uncle DenDen's D&D Buddy")
    #sets window name

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #define program window size as screen

    font = pygame.font.Font('Bastarda-wGxw.ttf', 82)
    text = font.render("Uncle DenDens D&D Buddy", True, 'PURPLE', 'BLACK')
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.280 )


    main_menu = pygame.Rect(MAIN_MENU_OFFSET, MAIN_MENU_OFFSET, (SCREEN_WIDTH - (MAIN_MENU_OFFSET*2)), (SCREEN_HEIGHT - (MAIN_MENU_OFFSET*2)))
    #sets main menu window placement

    run = True
    while run:
    #game loop
        screen.fill('black')
        #set background image
        pygame.draw.rect(screen, (125, 0, 175), main_menu)
        screen.blit(text, textRect)
        #draw main menu box
        key = pygame.key.get_pressed()
        #get keypress
        for event in pygame.event.get():
            #quit game logic searching for quit event
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        #update screen at end of loop
    pygame.quit()





if __name__ == '__main__':
    main()