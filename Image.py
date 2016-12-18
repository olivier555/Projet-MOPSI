"""Fichier chargeant les images servant à l'affichage"""

## Modules importes

import pygame
import Constantes

LISTE_PERLES = ["perlerouge.gif", "perleorange.gif", "perlejaune.gif", 
"perleverte.gif", "perlebleue.gif", "perleviolette.gif", "perlerose.gif", 
"perleblanche.gif", "perlemarron.gif"]

LISTE_COQUILLAGES = ["corouge.gif", "coorange.gif", "cojaune.gif", "covert.gif",
"cobleu.gif", "coviolet.gif", "corose.gif", "coblanc.gif", "comarron.gif"]

LISTE_CHRONO = ["chronov.gif", "chronoj.gif", "chronor.gif"]

class Image:
    
    def __init__(self, nom, taille_x, taille_y):
        surface = pygame.image.load(nom).convert_alpha()
        self.surface = pygame.transform.scale(surface, (taille_x, taille_y))

# PRISON = pygame.image.load("prison.png").convert_alpha()
# PRISON = pygame.transform.scale(PRISON, (taille_fenetre, taille_fenetre))
# 
# TRESOR = pygame.image.load("tresor.png").convert_alpha()
# TRESOR = pygame.transform.scale(TRESOR,(taille_fenetre, taille_fenetre))
# 
# FOND = pygame.image.load("fond.gif").convert_alpha()
# FOND = pygame.transform.scale(FOND,(taille_fenetre, taille_fenetre))
# 
# CORDE = pygame.image.load("corde.gif").convert_alpha()
# CORDE = pygame.transform.scale(CORDE,(RAYON_PERLE, int(RAYON_COLLIER * math.pi / (collier.nb_perles - 1))))

# PERLE_BLANCHE = pygame.image.load("perleblanche.gif").convert_alpha()
# PERLE_BLEUE = pygame.image.load("perlebleue.gif").convert_alpha()
# PERLE_JAUNE = pygame.image.load("perlejaune.gif").convert_alpha()
# PERLE_MARRON = pygame.image.load("perlemarron.gif").convert_alpha()
# PERLE_ORANGE = pygame.image.load("perleorange.gif").convert_alpha()
# PERLE_ROSE = pygame.image.load("perlerose.gif").convert_alpha()
# PERLE_ROUGE = pygame.image.load("perlerouge.gif").convert_alpha()
# PERLE_VERTE = pygame.image.load("perleverte.gif").convert_alpha()
# PERLE_VIOLETTE = pygame.image.load("perleviolet.gif").convert_alpha()
# 
# 
# 
# COQUILLAGE_BLANC = pygame.image.load("coblanc.gif").convert_alpha()
# COQUILLAGE_BLEU = pygame.image.load("cobleu.gif").convert_alpha()
# COQUILLAGE_JAUNE = pygame.image.load("cojaune.gif").convert_alpha()
# COQUILLAGE_MARRON = pygame.image.load("comarron.gif").convert_alpha()
# COQUILLAGE_ORANGE = pygame.image.load("coorange.gif").convert_alpha()
# COQUILLAGE_ROSE = pygame.image.load("corose.gif").convert_alpha()
# COQUILLAGE_ROUGE = pygame.image.load("corouge.gif").convert_alpha()
# COQUILLAGE_VERT = pygame.image.load("covert.gif").convert_alpha()
# COQUILLAGE_VIOLET = pygame.image.load("coviolet.gif").convert_alpha()



# BULLE_VERTE = pygame.image.load("chronov.gif").convert()
# BULLE_VERTE = pygame.transform.scale(BULLE_VERTE, (20, 20))
# 
# BULLE_ROUGE = pygame.image.load("chronor.gif").convert()
# BULLE_ROUGE = pygame.transform.scale(BULLE_ROUGE, (20, 20))
# 
# BULLE_JAUNE = pygame.image.load("chronoj.gif").convert()
# BULLE_JAUNE = pygame.transform.scale(BULLE_JAUNE, (20, 20))font = pygame.font.SysFont("mvboli", 36)
# text = font.render("Level 1", 1, (10, 10, 120))
# textpos = text.get_rect()
# textpos.top = 30
# textpos.left = 30
# 
# font_niveau_reussi = pygame.font.SysFont("mvboli", 50)
# texte_niveau_reussi = font_niveau_reussi.render("Level 1 réussi !", 1, (10, 250, 10))
# texte_niveau_reussi_rect = texte_niveau_reussi.get_rect()
# texte_niveau_reussi_rect.center = (int(taille_fenetre / 2), int(taille_fenetre / 2))

# 
