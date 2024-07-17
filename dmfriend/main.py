import pygame

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
MAIN_MENU_OFFSET = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

main_menu = pygame.Rect(MAIN_MENU_OFFSET, MAIN_MENU_OFFSET, (SCREEN_WIDTH - (MAIN_MENU_OFFSET*2)), (SCREEN_HEIGHT - (MAIN_MENU_OFFSET*2)))
run = True
while run:

    screen.fill('black')

    pygame.draw.rect(screen, (125, 0, 175), main_menu)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
