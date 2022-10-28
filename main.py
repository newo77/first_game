import pygame
from game import Game
from player import Player

pygame.init()

#créer une class qui représente le jeu


# créer une classe qui représente le joueur


# générer fenetre

pygame.display.set_caption("Comet Fall Game") # titre
screen = pygame.display.set_mode((1080,720)) # définis la taille de la fenetre (largeur -> hauteur)


# import de l'arrière plan

background = pygame.image.load('assets/bg.jpg')

#charge le jeu

game = Game()

#charge le joueur

player = Player()

running = True



# boucle 

while running:

    # applique le background 0,0 corresponds a largeur hauteur

    screen.blit(background, (0,-200)) 


    screen.blit(game.player.image, game.player.rect)

    # vérifie si je vais à gauche ou a droite

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width <= screen.get_width():
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
        game.player.move_left()     


   

    # met a jour l'écran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
       
        # fermeture de fenetre

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Détecte la touche du clavier

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
          