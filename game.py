import pygame
from player import Player  

class Game:

    def __init__(self):
    # génère le joueur
        self.player = Player()
        self.pressed = {}