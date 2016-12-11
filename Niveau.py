"""Fichier contenant la definition de la classe niveau"""

## Modules importes

import pygame
import math
import Collier
import Image
import Constantes

## Fonctions outils

def liste_perle(collier, rayon_perle, liste_positions):
    """Renvoit la liste contenant toutes les surfaces
    correspondant aux perles du collier et met a jour
    les positions correspondantes dans liste_positions"""

    angle = math.pi
    position_centre_x = int(Constantes.TAILLE_FENETRE / 2)
    position_centre_y = Constantes.RAYON_COLLIER
    centre_collier = [position_centre_x, position_centre_y]
    liste_surface = []
    for i in range(collier.nb_perles):
        rayon_x = Constantes.RAYON_COLLIER * math.cos(angle)
        position_x = int(centre_collier[0] + rayon_x - rayon_perle)
        rayon_y = - Constantes.RAYON_COLLIER * math.sin(angle)
        position_y = int(centre_collier[1] + rayon_y - rayon_perle)
        liste_positions.append((position_x, position_y))
        angle += math.pi / (collier.nb_perles - 1)
        surface = pygame.Surface((2 * rayon_perle, 2 * rayon_perle))
        couleur = Constantes.LISTE_COULEURS[collier.liste[i]]
        position_centre = (rayon_perle, rayon_perle)
        pygame.draw.circle(surface, couleur, position_centre, rayon_perle)
        surface.set_colorkey(Constantes.NOIR)
        liste_surface.append(surface)
    return liste_surface


def liste_corde(nb_perles, rayon_perle, liste_position_perles, liste_rectangle):
    """Renvoit la liste contenant toutes les surfaces
    correspondant aux cordes du collier et met a jour
    les rectangles correspondant dans liste_rectangle"""

    liste_surface = []
    angle = 180 / (2 * (nb_perles - 1))
    for i in range(nb_perles - 1):
        position_x_0 = liste_position_perles[i][0]
        position_x_1 = liste_position_perles[i + 1][0]
        position_x = int((position_x_0 + position_x_1)/2)
        position_y_0 = liste_position_perles[i][1]
        position_y_1 = liste_position_perles[i + 1][1]
        position_y = int((position_y_0 + position_y_1)/2)
        perimetre = math.pi * Constantes.RAYON_COLLIER
        taille = (rayon_perle, int(perimetre / (nb_perles - 1)))
        surface = pygame.transform.scale(Image.CORDE, taille)
        surface = pygame.transform.rotate(surface, angle)
        rectangle = surface.get_rect()
        rectangle.center = (position_x, position_y)
        liste_rectangle.append(rectangle)
        liste_surface.append(surface)
        angle += 180 / (nb_perles - 1)
    return liste_surface


## Definition de la classe Niveau


class Niveau:
    """Classe contenant tous les parametres relatifs a un niveau"""

    def __init__(self, repartition, temps_niveau):
        """Initialise les parametres du niveau"""

        self.collier = Collier.Collier()
        self.collier.collier_repartition(repartition)
        self.temps_niveau = temps_niveau
        perimetre = math.pi * Constantes.RAYON_COLLIER
        self.rayon_perle = int(perimetre / (3 * (self.collier.nb_perles - 1)))
        self.liste_positions_perles = []
        self.liste_surface_perle = liste_perle(self.collier,
                                               self.rayon_perle,
                                               self.liste_positions_perles)
        self.liste_rectangle_corde = []
        self.liste_surface_corde = liste_corde(self.collier.nb_perles,
                                               self.rayon_perle,
                                               self.liste_positions_perles,
                                               self.liste_rectangle_corde)
        liste_corde_visible = [True] * (self.collier.nb_perles - 1)
        rayon_clic = (perimetre / (collier.nb_perles - 1) - RAYON_PERLE) / 2

    def jouer(self, fenetre