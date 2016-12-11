import pygame
import sys
import math
import time
import copy
import Collier
import Vecteur_Signe
import Lambda
import MethodeNaive

TAILLE = 600
NB_PERLES = 12
NB_TYPES = 4
RAYON_COLLIER = 200
RAYON_PERLE = int(math.pi * RAYON_COLLIER / (3 * (NB_PERLES - 1)))

#RAYON_PERLE = 20
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
BLEU_FONCE = (0, 0, 128)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROSE = (255, 200, 200)
GRIS = (125, 125, 125)
JAUNE = (0, 250, 250)
LISTE_COULEURS = [ROUGE, VERT, BLEU, ROSE, BLEU_FONCE, JAUNE, BLANC, GRIS]

collier = Collier.Collier()
collier.collier_aleatoire_jeu(NB_TYPES, NB_PERLES)

pygame.init()
fenetre = pygame.display.set_mode((TAILLE, TAILLE))


t = math.pi
centre_collier = [int(TAILLE/2), RAYON_COLLIER]
liste_positions = []
for i in range(collier.nb_perles):
    liste_positions.append((int(centre_collier[0] + RAYON_COLLIER * math.cos(t) - RAYON_PERLE), int(centre_collier[1] - RAYON_COLLIER * math.sin(t) - RAYON_PERLE)))
    t += math.pi / (collier.nb_perles - 1)
"""pygame.draw.lines(fenetre, NOIR, False, liste_positions, 4)
liste_surface_perle = []
for i in range(collier.nb_perles):
    surface = pygame.Surface((2 * RAYON_PERLE, 2 * RAYON_PERLE))
    pygame.draw.circle(surface, LISTE_COULEURS[collier.liste[i]], (RAYON_PERLE, RAYON_PERLE), RAYON_PERLE)
    surface.set_colorkey(NOIR)
    liste_surface_perle.append(surface)"""

perle_blanche = pygame.image.load("perleblanche.gif").convert_alpha()
perle_bleue = pygame.image.load("perlebleue.gif").convert_alpha()
perle_jaune = pygame.image.load("perlejaune.gif").convert_alpha()
perle_marron = pygame.image.load("perlemarron.gif").convert_alpha()
perle_orange = pygame.image.load("perleorange.gif").convert_alpha()
perle_rose = pygame.image.load("perlerose.gif").convert_alpha()
perle_rouge = pygame.image.load("perlerouge.gif").convert_alpha()
perle_verte = pygame.image.load("perleverte.gif").convert_alpha()
perle_violette = pygame.image.load("perleviolet.gif").convert_alpha()

liste_perles = [perle_blanche, perle_bleue, perle_jaune, perle_marron,
                perle_orange, perle_rose, perle_rouge, perle_verte,
                perle_violette]

coquillage_blanc = pygame.image.load("coblanc.gif").convert_alpha()
coquillage_bleu = pygame.image.load("cobleu.gif").convert_alpha()
coquillage_jaune = pygame.image.load("cojaune.gif").convert_alpha()
coquillage_marron = pygame.image.load("comarron.gif").convert_alpha()
coquillage_orange = pygame.image.load("coorange.gif").convert_alpha()
coquillage_rose = pygame.image.load("corose.gif").convert_alpha()
coquillage_rouge = pygame.image.load("corouge.gif").convert_alpha()
coquillage_vert = pygame.image.load("covert.gif").convert_alpha()
coquillage_violet = pygame.image.load("coviolet.gif").convert_alpha()

liste_coquillages = [coquillage_blanc, coquillage_bleu, coquillage_jaune,
                     coquillage_marron, coquillage_orange, coquillage_orange,
                     coquillage_rose, coquillage_rouge, coquillage_vert,
                     coquillage_violet]


liste_repartition = [1] * collier.nb_perles

pygame.mouse.set_visible(False)
image_curseur = pygame.image.load("curseur.gif").convert_alpha()
image_curseur = pygame.transform.scale(image_curseur, (50, 30))
#image_curseur = pygame.transform.flip(image_curseur, True, False)

image_voleur_0 = pygame.image.load("poisson1.gif").convert_alpha()
image_voleur_0 = pygame.transform.scale(image_voleur_0,(50, 50))

image_voleur_1 = pygame.image.load("poisson2.gif").convert_alpha()
image_voleur_1 = pygame.transform.scale(image_voleur_1,(50, 50))

position_image_voleur_0 = (30, 450)
position_image_voleur_1 = (30, 525)

#image_nuage = pygame.image.load("nuage.jpg").convert_alpha()
#image_nuage = pygame.transform.scale(image_nuage, (20, 20))


image_ciseaux = pygame.image.load("curseur.gif").convert_alpha()
image_ciseaux = pygame.transform.scale(image_ciseaux, (40, 60))

image_requin = pygame.image.load("curseur.gif").convert_alpha()
image_requin = pygame.transform.scale(image_requin, (40, 60))

image_prison = pygame.image.load("prison.png").convert_alpha()
image_prison = pygame.transform.scale(image_prison, (TAILLE, TAILLE))

image_gagnant = pygame.image.load("tresor.png").convert_alpha()
image_gagnant = pygame.transform.scale(image_gagnant,(TAILLE, TAILLE))

image_fond = pygame.image.load("fond.gif").convert_alpha()
image_fond = pygame.transform.scale(image_fond,(TAILLE, TAILLE))

image_corde = pygame.image.load("corde.gif").convert_alpha()
image_corde = pygame.transform.scale(image_corde,(RAYON_PERLE, int(RAYON_COLLIER * math.pi / (collier.nb_perles - 1))))



bulle_verte = pygame.image.load("chronov.gif").convert()
bulle_verte = pygame.transform.scale(bulle_verte, (20, 20))
bulle_verte.set_alpha(120)

bulle_rouge = pygame.image.load("chronor.gif").convert()
bulle_rouge = pygame.transform.scale(bulle_rouge, (20, 20))
bulle_rouge.set_alpha(120)

bulle_jaune = pygame.image.load("chronoj.gif").convert()
bulle_jaune = pygame.transform.scale(bulle_jaune, (20, 20))
bulle_jaune.set_alpha(120)


liste_image_corde = []
liste_fil_visible = []
liste_centre_fils = []
liste_rectangle = []
t = 180 / (2 * (collier.nb_perles - 1))
for i in range(collier.nb_perles - 1):
    position_x = int((liste_positions[i][0] + liste_positions[i+1][0])/2)
    position_y = int((liste_positions[i][1] + liste_positions[i+1][1])/2)
    liste_centre_fils.append((position_x, position_y))
    liste_fil_visible.append(True)
    image = pygame.transform.rotate(image_corde, t)
    rectangle = image.get_rect()
    rectangle.center = (position_x, position_y)
    liste_rectangle.append(rectangle)
    liste_image_corde.append(image)
    
    t += 180 / (collier.nb_perles - 1)
    

font = pygame.font.SysFont("mvboli", 36)
text = font.render("Level 1", 1, (10, 10, 120))
textpos = text.get_rect()
textpos.top = 30
textpos.left = 30

font_niveau_reussi = pygame.font.SysFont("mvboli", 50)
texte_niveau_reussi = font_niveau_reussi.render("Level 1 réussi !", 1, (10, 250, 10))
texte_niveau_reussi_rect = texte_niveau_reussi.get_rect()
texte_niveau_reussi_rect.center = (int(TAILLE / 2), int(TAILLE / 2))

rayon_clic = ((math.pi * RAYON_COLLIER) / (collier.nb_perles - 1) - RAYON_PERLE) / 2

nb_coupes = collier.nb_types

niveau_reussi = False

temps_niveau = 150
nb_coquillage = 10
t1 = math.pi / 2
centre_temps = [int(TAILLE / 2), int(TAILLE / 3)]
RAYON_TEMPS = 70
liste_positions_temps = []
for i in range(nb_coquillage):
    liste_positions_temps.append((int(centre_temps[0] + RAYON_TEMPS * math.cos(t1)), int(centre_temps[1] - RAYON_TEMPS * math.sin(t1))))
    t1 += 2 * math.pi / (nb_coquillage - 1) 

start = time.time()
temps_ecoule = False

def collier_fil_coupe(liste_fil_visible):
    """Renvoit la liste correspondant a la repartition
    de liste_fil_visible"""

    liste = [1]
    voleur = 1
    for bool in liste_fil_visible:
        if bool:
            liste.append(voleur)
        else:
            voleur = - voleur
            liste.append(voleur)
    return liste


def affiche_repartition(fenetre, liste_repartition, collier):
    """Affiche la repartition des perles entre les 2 joueurs"""

    espacement_perle_affiche = int(460 / collier.nb_perles)
    rayon_affiche_perle = int(espacement_perle_affiche / 3.5)
    vecteur_signe = Vecteur_Signe.creer_vecteur_signe(liste_repartition, collier)
    liste_voleur_repartition = Lambda.repartition_joueurs_types(vecteur_signe, collier)
    position_x_poubelle_0 = int(110 + 460 / 2)
    position_x_poubelle_1 = int(110 + 460 / 2)
    position_x_coussin = int(110)
    #image_nuage = pygame.transform.scale(image_nuage, (espacement_perle_affiche, espacement_perle_affiche))
    for type in range(collier.nb_types):
        nb_nuages = collier.liste.count(type)
        nb_perles_type_0 = liste_voleur_repartition[0][type]
        nb_perles_type_1 = liste_voleur_repartition[1][type]
        for j in range(int(nb_nuages / 2)):
            fenetre.blit(pygame.transform.scale(liste_coquillages[type], (espacement_perle_affiche, espacement_perle_affiche)), (position_x_coussin, 460))
            fenetre.blit(pygame.transform.scale(liste_coquillages[type], (espacement_perle_affiche, espacement_perle_affiche)), (position_x_coussin, 535))
            if nb_perles_type_0 > 0:
                position_cercle = (int(- RAYON_PERLE + position_x_coussin + espacement_perle_affiche / 2), int(- RAYON_PERLE + 460 + espacement_perle_affiche / 2))
                fenetre.blit(pygame.transform.scale(liste_perles[type],(espacement_perle_affiche, espacement_perle_affiche)), position_cercle)
                nb_perles_type_0 -= 1
            if nb_perles_type_1 > 0:
                position_cercle = (int(- RAYON_PERLE + position_x_coussin + espacement_perle_affiche / 2), int(- RAYON_PERLE + 535 + espacement_perle_affiche / 2))
                fenetre.blit(pygame.transform.scale(liste_perles[type],(espacement_perle_affiche, espacement_perle_affiche)), position_cercle)
                nb_perles_type_1 -= 1
            position_x_coussin += espacement_perle_affiche
        while nb_perles_type_0 > 0:
            position_cercle = (int(position_x_poubelle_0 + espacement_perle_affiche / 2), int(460 + espacement_perle_affiche / 2))
            fenetre.blit(pygame.transform.scale(liste_perles[type],(espacement_perle_affiche, espacement_perle_affiche)), position_cercle)
            nb_perles_type_0 -= 1
            position_x_poubelle_0 += espacement_perle_affiche
        while nb_perles_type_1 > 0:
            position_cercle = (int(- RAYON_PERLE + position_x_poubelle_1 + espacement_perle_affiche / 2), int(- RAYON_PERLE + 535 + espacement_perle_affiche / 2))
            fenetre.blit(pygame.transform.scale(liste_perles[type],(espacement_perle_affiche, espacement_perle_affiche)), position_cercle)
            nb_perles_type_1 -= 1
            position_x_poubelle_1 += espacement_perle_affiche

def affiche_coups_restants(fenetre, nb_coupes, nb_types):
    """affiche le nombre de cous possibles restant
    represente par des ciseaux"""

    position_x = 30
    position_y = 70
    for i in range(nb_coupes):
        fenetre.blit(image_requin, (position_x, position_y))
        position_x += 40

def affichage_chronometre(fenetre):
    """affiche le chronometre"""

    nb_coquillages_restant = int(nb_coquillage * (temps_niveau - time.time() + start) / temps_niveau)
    if nb_coquillages_restant < int(nb_coquillage / 3):
        for t in range(nb_coquillages_restant):
            fenetre.blit(bulle_rouge, liste_positions_temps[t])
    elif nb_coquillages_restant < int(2 * nb_coquillage / 3):
        for t in range(nb_coquillages_restant):
            fenetre.blit(bulle_jaune, liste_positions_temps[t])
    else:
        for t in range(nb_coquillages_restant):
            fenetre.blit(bulle_verte, liste_positions_temps[t])

    
def affichage_complet(fenetre, liste_positions, liste_repartition, nb_coupes, collier):
    """fonction permettant d'afficher tout le jeu"""

    fenetre.blit(image_fond, (0, 0))
    for i in range(collier.nb_perles - 1):
        if liste_fil_visible[i]:
            fenetre.blit(liste_image_corde[i], liste_rectangle[i])
    for i in range(collier.nb_perles):
        position = (liste_positions[i][0] - RAYON_PERLE, liste_positions[i][1] - RAYON_PERLE)
        fenetre.blit(pygame.transform.scale(liste_perles[collier.liste[i]], (2 * RAYON_PERLE, 2 * RAYON_PERLE)), position)
        
    affiche_coups_restants(fenetre, nb_coupes, collier.nb_types)
    affiche_repartition(fenetre, liste_repartition, collier)
    affichage_chronometre(fenetre)
    fenetre.blit(text, textpos)
    fenetre.blit(image_voleur_0, position_image_voleur_0)
    fenetre.blit(image_voleur_1, position_image_voleur_1)
    fenetre.blit(image_curseur, pygame.mouse.get_pos())

def affichage_temps_ecoule(fenetre):
    """affichage lorsque le temps est ecoule"""

    fenetre.blit(image_fond, (0, 0))
    fenetre.blit(image_prison, (0, 0))
    fenetre.blit(image_curseur, pygame.mouse.get_pos())

def affichage_niveau_reussi(fenetre):
    """affichage lorsque le joueur a reussit le niveau"""

    fenetre.blit(image_fond, (0, 0))
    fenetre.blit(image_gagnant,(0, 0))
    fenetre.blit(texte_niveau_reussi, texte_niveau_reussi_rect)
    fenetre.blit(image_curseur, pygame.mouse.get_pos())
    
    


while True: # main game loop

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            position_clic = pygame.mouse.get_pos()
            for i in range(collier.nb_perles - 1):
                distance_x = position_clic[0] - liste_centre_fils[i][0]
                distance_y = position_clic[1] - liste_centre_fils[i][1]
                if distance_x * distance_x + distance_y * distance_y < rayon_clic * rayon_clic:
                    if liste_fil_visible[i]:
                        if nb_coupes > 0:
                            liste_fil_visible[i] = False
                            nb_coupes -= 1
                    else:
                        liste_fil_visible[i] = True
                        nb_coupes += 1
                    liste_repartition = collier_fil_coupe(liste_fil_visible)
                    if MethodeNaive.decoupe_type_valable(collier, liste_repartition):
                        niveau_reussi = True
                    

    if time.time() - start >= temps_niveau:
        temps_ecoule = True
    if temps_ecoule and not niveau_reussi:
        affichage_temps_ecoule(fenetre)
    elif niveau_reussi:
        affichage_niveau_reussi(fenetre)
    else:
        affichage_complet(fenetre, liste_positions, liste_repartition, nb_coupes, collier)
    
        
    pygame.display.update()