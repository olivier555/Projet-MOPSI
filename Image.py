"""Fichier chargeant les images servant à l'affichage"""

## Modules importes

import pygame
import Constantes

LIST_PERL = ["perlerouge.gif", "perleorange.gif", "perlejaune.gif", 
"perleverte.gif", "perlebleue.gif", "perleviolette.gif", "perlerose.gif", 
"perleblanche.gif", "perlemarron.gif"]

LIST_SHELL = ["corouge.gif", "coorange.gif", "cojaune.gif", "covert.gif",
"cobleu.gif", "coviolet.gif", "corose.gif", "coblanc.gif", "comarron.gif"]

LIST_CHRONO = ["chronov.gif", "chronoj.gif", "chronor.gif"]

LIST_BUTTON = ["buttonred.gif", "buttonorange.gif", "buttonyellow.gif",
               "buttonblue.gif", "buttonblack.gif"]

class Image:
    
    def __init__(self, nom, taille_x, taille_y):
        surface = pygame.image.load(nom).convert_alpha()
        self.surface = pygame.transform.scale(surface, (taille_x, taille_y))
