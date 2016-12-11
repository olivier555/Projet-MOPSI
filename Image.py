"""Fichier chargeant les images servant à l'affichage"""

## Modules importes

import pygame
import Constantes

pygame.init()
fenetre = pygame.display.set_mode((100, 100))

taille_fenetre = Constantes.TAILLE_FENETRE

CURSEUR = pygame.image.load("requin2.png").convert_alpha()
CURSEUR = pygame.transform.scale(CURSEUR, (50, 30))
CURSEUR = pygame.transform.flip(CURSEUR, True, False)

VOLEUR_0 = pygame.image.load("poisson-bleu.jpg").convert_alpha()
VOLEUR_0 = pygame.transform.scale(VOLEUR_0,(50, 50))

VOLEUR_1 = pygame.image.load("poisson-rouge.jpg").convert_alpha()
VOLEUR_1 = pygame.transform.scale(VOLEUR_1,(50, 50))

NUAGE = pygame.image.load("nuage.jpg").convert_alpha()
NUAGE = pygame.transform.scale(NUAGE, (20, 20))

CISEAUX = pygame.image.load("ciseaux.png").convert_alpha()
CISEAUX = pygame.transform.scale(CISEAUX, (40, 60))

REQUIN = pygame.image.load("requin2.png").convert_alpha()
REQUIN = pygame.transform.scale(REQUIN, (40, 60))

PRISON = pygame.image.load("prison.png").convert_alpha()
PRISON = pygame.transform.scale(PRISON, (taille_fenetre, taille_fenetre))

TRESOR = pygame.image.load("tresor.png").convert_alpha()
TRESOR = pygame.transform.scale(TRESOR,(taille_fenetre, taille_fenetre))

FOND = pygame.image.load("fond-marin.jpg").convert_alpha()
FOND = pygame.transform.scale(FOND,(taille_fenetre, taille_fenetre))

CORDE = pygame.image.load("corde.gif").convert_alpha()
#CORDE = pygame.transform.scale(CORDE,(RAYON_PERLE, int(RAYON_COLLIER * math.pi / (collier.nb_perles - 1))))

BULLE_VERTE = pygame.image.load("bulle_verte.png").convert()
BULLE_VERTE = pygame.transform.scale(BULLE_VERTE, (20, 20))

BULLE_ROUGE = pygame.image.load("bulle_orange.png").convert()
BULLE_ROUGE = pygame.transform.scale(BULLE_ROUGE, (20, 20))

BULLE_JAUNE = pygame.image.load("bulle_jaune.png").convert()
BULLE_JAUNE = pygame.transform.scale(BULLE_JAUNE, (20, 20))

font = pygame.font.SysFont("mvboli", 36)
text = font.render("Level 1", 1, (10, 10, 120))
textpos = text.get_rect()
textpos.top = 30
textpos.left = 30

font_niveau_reussi = pygame.font.SysFont("mvboli", 50)
texte_niveau_reussi = font_niveau_reussi.render("Level 1 réussi !", 1, (10, 250, 10))
texte_niveau_reussi_rect = texte_niveau_reussi.get_rect()
texte_niveau_reussi_rect.center = (int(TAILLE / 2), int(TAILLE / 2))