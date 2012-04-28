# menu.py
#
# The main menu for the game.

import pygame # import all pygame modules
pygame.init() # Initialize all pygame modules

class Menu():
    def __init__(self, size_x, size_y):
        self.background = pygame.Surface((size_x, size_y))
