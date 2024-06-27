import pygame

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

main_menu = pygame.Rect(25, 25, (SCREEN_WIDTH-25), (SCREEN_HEIGHT-25))
run = True
while run:

    screen.fill(0,0,0)

    pygame.draw.rect(screen, (125, 0, 175), main_menu)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
