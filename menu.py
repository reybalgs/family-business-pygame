# menu.py
#
# The main menu for the game.

import pygame # import all pygame modules
pygame.init() # Initialize all pygame modules

class Button():
    # A button in the main menu.
    # 
    # Accepts size (x,y), text and what event it calls.
    def __init__(self, size_x, size_y, text, event):
        """
        Initialization function for a button
        """
         

class Menu():
    def __init__(self, size_x, size_y):
        self.background = pygame.Surface((size_x, size_y))
