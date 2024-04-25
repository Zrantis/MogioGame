import pygame

pygame.init()

# DEBUT GAME WINDOW

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FIN GAME WINDOW

# DEBUT FEATURES

pygame.display.set_caption("Mogio Game")
player = pygame.Rect((640, 360, 32, 64)) #x, y, width, height

# FIN FEATURES

# DEBUT GAME LOOP

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_q] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)

    # DEBUT EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

# FIN EVENT HANDLER

# FIN GAME LOOP

pygame.quit()