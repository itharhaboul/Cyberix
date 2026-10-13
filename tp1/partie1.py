import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CyberiX")
clock = pygame.time.Clock()

player_x = 400
player_y = 300
player_size = 50
speed = 5 # la vitesse de player

monster_x = 100
monster_y = 50
monster_size = 50
monster_speed = 3 # vitesse de monster

running = True
while running:
    for event in pygame.event.get(): # montre tt la liste un par un (for)
        if event.type == pygame.QUIT: # si le player clique sur *
            running = False

    keys = pygame.key.get_pressed()  # pour on peux bouger le player dans les 4 direction
    if keys[pygame.K_RIGHT]:
        player_x = player_x + speed
    if keys[pygame.K_LEFT]:
        player_x = player_x - speed
    if keys[pygame.K_UP]:
        player_y = player_y - speed
    if keys[pygame.K_DOWN]:
        player_y = player_y + speed

    if player_x > 800 - player_size: # pour ne depasser pas le bord de windwz
        player_x = 800 - player_size
    if player_x < 0:    # le côté gauche est sorti de la fenêtre
        player_x = 0      # on le remet pile sur le bord gauche
    if player_y > 600 - player_size:
        player_y = 600 - player_size
    if player_y < 0:
        player_y = 0

    monster_x = monster_x + monster_speed    # combien la vitesse qui le monster bouge
    if monster_x > 800 - monster_size or monster_x < 0: # verfiction si il depasse le bord ou touche 
        monster_speed = -monster_speed      # le demi-tour

    screen.fill((180, 180, 180))  # color de windz
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, player_size, player_size)) # x,y,largeur,hauteur
    pygame.draw.rect(screen, (255, 0, 0), (monster_x, monster_y, monster_size, monster_size))
    pygame.display.flip()   # affichage
    clock.tick(60)

pygame.quit()