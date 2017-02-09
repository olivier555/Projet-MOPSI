"""Module chargeant les images servant à l'affichage"""

## Modules importes

import pygame

## Listes globales ##

LIST_PERL = ["pearlred.gif", "pearlorange.gif", "pearlyellow.gif", 
"pearlgreen.gif", "pearlblue.gif", "pearlviolet.gif", "pearlpink.gif", 
"pearlwhite.gif", "pearlbrown.gif"]

LIST_SHELL = ["shellred.gif", "shellorange.gif", "shellyellow.gif", 
"shellgreen.gif", "shellblue.gif", "shellviolet.gif", "shellpink.gif", 
"shellwhite.gif", "shellbrown.gif"]

LIST_CHRONO = ["timergreen.gif", "timeryellow.gif", "timerred.gif"]

LIST_BUTTON = ["buttonred.gif", "buttonorange.gif", "buttonyellow.gif",
               "buttonblue.gif", "buttonblack.gif"]

## Classe Image ##

class Image:
    """Classe permettant de charger une image a la bonne taille et au bon
    format"""

    def __init__(self, name, width, height):
        """Initialise la classe Image"""

        area = pygame.image.load(name).convert_alpha()
        self.area = pygame.transform.scale(area, (width, height))
