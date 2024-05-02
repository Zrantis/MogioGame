import pygame
import sys

pygame.init()

# DEBUT GAME WINDOW

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# clock = pygame.time.Clock()  # Ajout pour limiter la vitesse de la boucle de jeu


# FIN GAME WINDOW

# DEBUT FEATURES

pygame.display.set_caption("Mogio Game")
player = pygame.image.load("minichad.png")
player_width, player_height = player.get_size()
player_x = 640
player_y = 360
player_speed = 1
player_direction = 1

# Gravité
gravity = 0.02
# Vitesse verticale du joueur
player_y_velocity = 0
# Hauteur du sol
ground_level = 600  # ajuste cette valeur selon tes besoins
# Vitesse de saut
jump_velocity = -3  # ajuste cette valeur pour contrôler la hauteur des sauts

# Couleur du sol
# ground_color = (34, 139, 34)  # Vert

# Chargement de l'image de fond
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Chargement de l'image du sol
ground_image = pygame.image.load("ground.png")
ground_image = pygame.transform.scale(ground_image, (ground_image.get_width(), SCREEN_HEIGHT - ground_level))

# POLICES
font_title = pygame.font.SysFont(None, 100)
font_button = pygame.font.SysFont(None, 50)

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)


# FIN FEATURES

# DEBUT GAME LOOP

run = True
menu = False

while run:

    # DEBUT EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = not menu  # Activer ou désactiver le menu en appuyant sur la touche Échap
        elif event.type == pygame.MOUSEBUTTONDOWN and menu:
            mouse_pos = pygame.mouse.get_pos()
            if return_button_rect.collidepoint(mouse_pos):
                menu = False
            elif quit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()


    if menu:
        screen.fill(black)
        title_text = font_title.render("MOGIO GAME", True, white)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

        return_button = font_button.render("RETOUR", True, white)
        quit_button = font_button.render("QUITTER", True, white)

        return_button_rect = return_button.get_rect(midleft=(SCREEN_WIDTH // 2 - 200, 250))
        quit_button_rect = quit_button.get_rect(midleft=(SCREEN_WIDTH // 2 + 200, 250))

        pygame.draw.rect(screen, green, return_button_rect, border_radius=5)
        pygame.draw.rect(screen, green, quit_button_rect, border_radius=5)

        screen.blit(return_button, return_button_rect)
        screen.blit(quit_button, quit_button_rect)
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_y == ground_level - player_height:  # Vérifie si le joueur est au sol avant de sauter
            player_y_velocity = jump_velocity
        if keys[pygame.K_q]:
            player_x -= player_speed
            player_direction = 1  # Définir la direction vers la gauche
        if keys[pygame.K_d]:
            player_x += player_speed
            player_direction = -1  # Définir la direction vers la droite
        if keys[pygame.K_s]:
            player_y += player_speed

        # Gravité
        player_y_velocity += gravity
        player_y += player_y_velocity

        # Vérifie si le joueur touche le sol
        if player_y >= ground_level - player_height:
            player_y = ground_level - player_height
            player_y_velocity = 0

        screen.blit(background_image, (0, 0))  # Affiche l'image de fond

        # Affiche l'image du sol répétée horizontalement
        for x in range(0, SCREEN_WIDTH, ground_image.get_width()):
            screen.blit(ground_image, (x, ground_level))

        # Dessine le sol
        # pygame.draw.rect(screen, ground_color, (0, ground_level, SCREEN_WIDTH, SCREEN_HEIGHT - ground_level))

        # Inverser l'image du joueur si la direction est vers la gauche
        if player_direction == -1:
            flipped_player = pygame.transform.flip(player, True, False)
            screen.blit(flipped_player, (player_x, player_y))
        else:
            screen.blit(player, (player_x, player_y))
            
    pygame.display.flip()
    pygame.display.update()
    # clock.tick(60)  # Limite la boucle de jeu à 60 FPS

# FIN EVENT HANDLER

# FIN GAME LOOP

pygame.quit()