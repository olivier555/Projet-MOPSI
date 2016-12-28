"""Fichier contenant la definition de la classe niveau"""

## Modules importes


import math
import time
import sys
import pygame
import Collier
import Image
import Constantes
import MethodeNaive


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
        perle = Image.Image(Image.LISTE_PERLES[collier.liste[i]],
                            2 * rayon_perle, 2 * rayon_perle)
        liste_surface.append(perle.surface)
    return liste_surface


def liste_corde(nb_perles, rayon_perle, liste_position_perles, liste_rectangle):
    """Renvoit la liste contenant toutes les surfaces
    correspondant aux cordes du collier et met a jour
    les rectangles correspondant dans liste_rectangle"""

    liste_surface = []
    perimetre = math.pi * Constantes.RAYON_COLLIER
    taille = (rayon_perle, int(perimetre / (nb_perles - 1)))
    image_corde = Image.Image("corde.gif", taille[0], taille[1])
    angle = 180 / (2 * (nb_perles - 1))
    for i in range(nb_perles - 1):
        position_x_0 = liste_position_perles[i][0] + rayon_perle
        position_x_1 = liste_position_perles[i + 1][0] + rayon_perle
        position_x = int((position_x_0 + position_x_1)/2)
        position_y_0 = liste_position_perles[i][1] + rayon_perle
        position_y_1 = liste_position_perles[i + 1][1] + rayon_perle
        position_y = int((position_y_0 + position_y_1)/2)
        perimetre = math.pi * Constantes.RAYON_COLLIER
        taille = (rayon_perle, int(perimetre / (nb_perles - 1)))
        surface = Image.Image("corde.gif", taille[0], taille[1])
        surface = pygame.transform.rotate(image_corde.surface, angle)
        rectangle = surface.get_rect()
        rectangle.center = (position_x, position_y)
        liste_rectangle.append(rectangle)
        liste_surface.append(surface)
        angle += 180 / (nb_perles - 1)
    return liste_surface


def collier_fil_coupe(liste_fil_visible):
    """Renvoit la liste correspondant a la repartition
    de liste_fil_visible"""

    liste = [1]
    voleur = 1
    for booleen in liste_fil_visible:
        if booleen:
            liste.append(voleur)
        else:
            voleur = - voleur
            liste.append(voleur)
    return liste

def position_chrono(temps_niveau):
    """renvoit la liste des positions des bulles du chronometre"""

    courbe = math.pi / 2
    centre_temps = [int(Constantes.TAILLE_FENETRE / 2),
                    int(Constantes.TAILLE_FENETRE / 3)]
    liste_positions_temps = []
    rayon = Constantes.RAYON_TEMPS
    for i in range(Constantes.NB_BULLE):
        position_x = int(centre_temps[0] + rayon * math.cos(courbe))
        position_y = int(centre_temps[1] - rayon * math.sin(courbe))
        liste_positions_temps.append((position_x, position_y))
        courbe += 2 * math.pi / (Constantes.NB_BULLE)
    return liste_positions_temps


## Definition de la classe Niveau


class Niveau:
    """Classe contenant tous les parametres relatifs a un niveau"""

    def __init__(self, fenetre, repartition, temps_niveau):
        """Initialise les parametres du niveau"""

        self.collier = Collier.Collier()
        self.collier.collier_repartition(repartition)

        self.temps_niveau = temps_niveau

        self.fenetre = fenetre

        self.nb_etoiles = 3

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
        self.liste_corde_visible = [True] * (self.collier.nb_perles - 1)
        longueur = perimetre / (self.collier.nb_perles - 1)
        self.rayon_clic = (longueur - self.rayon_perle) / 2
        self.nb_coupes = self.collier.nb_types
        self.espacement_perle_affiche = int((5 / 6) * Constantes.TAILLE_FENETRE / (self.collier.nb_perles + 1))

        self.liste_repartition = [0] * self.collier.nb_perles

        self.liste_position_temps = position_chrono(self.temps_niveau)

        self.charger_image()

    def charger_image(self):
        """Charge les images necessaires a l'affichage du jeu"""

        self.curseur = Image.Image("curseur.gif", 50, 30)
        taille = Constantes.TAILLE_FENETRE
        self.liste_image_chrono = [Image.Image(Image.LISTE_CHRONO[0], 20, 20),
                                   Image.Image(Image.LISTE_CHRONO[1], 20, 20),
                                   Image.Image(Image.LISTE_CHRONO[2], 20, 20)]
        self.prison = Image.Image("prison.png", taille, taille)
        self.tresor = Image.Image("tresor.png", int(taille / 3), int(taille / 3))
        self.fond = Image.Image("fond.gif", taille, taille)
        self.etoile = Image.Image("etoile.gif", 100, 100)
        self.liste_coquillages = []
        for i in range(self.collier.nb_types):
            chemin = Image.LISTE_COQUILLAGES[i]
            taille_coquillage = self.espacement_perle_affiche
            self.liste_coquillages.append(Image.Image(chemin,
                                                      taille_coquillage,
                                                      taille_coquillage))
        self.liste_perle_repartition = []
        taille_perle_repartition = int(1.4 * self.rayon_perle)
        for i in range(self.collier.nb_types):
            image = Image.Image(Image.LISTE_PERLES[i],
                                taille_perle_repartition,
                                taille_perle_repartition)
            self.liste_perle_repartition.append(image.surface)
        taille_6 = int((1 / 6) * taille)
        self.voleur_0 = Image.Image("poisson1.gif", taille_6, taille_6)
        self.voleur_1 = Image.Image("poisson2.gif", taille_6, taille_6)
        self.voleur_defaite_0 = Image.Image("poisson1.gif", 200, 200)
        self.voleur_defaite_1 = Image.Image("poisson2.gif", 200, 200)
        self.position_image_voleur_0 = (0, 4 * taille_6)
        self.position_image_voleur_1 = (0, 5 * taille_6)
        font = pygame.font.SysFont("mvboli", 50)
        self.txt_niveau = font.render("Level 1", 1, (10, 10, 120))
        self.txt_niveau_rect = self.txt_niveau.get_rect()
        self.txt_niveau_rect.top = 30
        self.txt_niveau_rect.left = 30

        vert = Constantes.VERT
        self.txt_niveau_reussi = font.render("Level 1 réussi !", 1, vert)
        self.txt_niveau_reussi_rect = self.txt_niveau_reussi.get_rect()
        demi_fenetre = int(taille / 2)
        self.txt_niveau_reussi_rect.center = (demi_fenetre, 50)

        self.rect_1 = pygame.Rect(70, 500, 120, 50)
        self.rect_2 = pygame.Rect(240, 500, 120, 50)
        self.rect_3 = pygame.Rect(410, 500, 120, 50)
        self.rect_4 = pygame.Rect(150, 500, 120, 50)
        self.rect_5 = pygame.Rect(330, 500, 120, 50)

    def affiche_repartition(self):
        """Affiche la repartition des perles entre les 2 joueurs"""

        liste_voleur_repartition = [[0] * self.collier.nb_types,
                                    [0] * self.collier.nb_types]
        for i in range(self.collier.nb_perles):
            if self.liste_repartition[i] == 1:
                liste_voleur_repartition[0][self.collier.liste[i]] += 1
            if self.liste_repartition[i] == -1:
                liste_voleur_repartition[1][self.collier.liste[i]] += 1
        taille = Constantes.TAILLE_FENETRE
        position_x_poubelle_0 = int(110 + 460 / 2)
        position_x_poubelle_1 = int(110 + 460 / 2)
        position_x_coussin = int(taille / 6)
        rayon = self.rayon_perle
        espacement = self.espacement_perle_affiche
        position_y_0 = int((9 / 12) * taille - espacement / 2)
        position_y_1 = int((11 / 12) * taille - espacement / 2)
        for type in range(self.collier.nb_types):
            nb_coquillages = self.collier.liste.count(type)
            nb_perles_type_0 = liste_voleur_repartition[0][type]
            nb_perles_type_1 = liste_voleur_repartition[1][type]
            for j in range(int(nb_coquillages / 2)):
                self.fenetre.blit(self.liste_coquillages[type].surface,
                                  (position_x_coussin, position_y_0))
                self.fenetre.blit(self.liste_coquillages[type].surface,
                                  (position_x_coussin, position_y_1))
                if nb_perles_type_0 > 0:
                    position_x = position_x_coussin - rayon + espacement / 2
                    position_y = 460 - rayon + espacement / 2
                    position_cercle = (int(position_x), int(position_y))
                    self.fenetre.blit(self.liste_perle_repartition[type],
                                      position_cercle)
                    nb_perles_type_0 -= 1
                if nb_perles_type_1 > 0:
                    position_x = position_x_coussin - rayon + espacement / 2
                    position_y = 535 - rayon + espacement / 2
                    position_cercle = (int(position_x), int(position_y))
                    self.fenetre.blit(self.liste_perle_repartition[type],
                                      position_cercle)
                    nb_perles_type_1 -= 1
                position_x_coussin += self.espacement_perle_affiche
            while nb_perles_type_0 > 0:
                position_x = position_x_poubelle_0 - rayon + espacement / 2
                position_y = 460 - rayon + espacement / 2
                position_cercle = (int(position_x), int(position_y))
                self.fenetre.blit(self.liste_perle_repartition[type],
                                  position_cercle)
                nb_perles_type_0 -= 1
                position_x_poubelle_0 += espacement
            while nb_perles_type_1 > 0:
                position_x = position_x_poubelle_1 - rayon + espacement / 2
                position_y = 535 - rayon + espacement / 2
                position_cercle = (int(position_x), int(position_y))
                self.fenetre.blit(self.liste_perle_repartition[type],
                                  position_cercle)
                nb_perles_type_1 -= 1
                position_x_poubelle_1 += espacement

    def affiche_coups_restants(self):
        """affiche le nombre de cous possibles restant
        represente par de ciseaux"""

        position_x = 30
        position_y = 70
        for i in range(self.nb_coupes):
            self.fenetre.blit(self.curseur.surface, (position_x, position_y))
            position_x += 40

    def affichage_chronometre(self, start):
        """affiche le chronometre"""

        temps = self.temps_niveau - time.time() + start
        nb_bulle = Constantes.NB_BULLE
        nb_bulle_restante = int(nb_bulle * temps / self.temps_niveau) + 1
        if nb_bulle_restante < int(nb_bulle / 3):
            for i in range(nb_bulle_restante):
                self.fenetre.blit(self.liste_image_chrono[2].surface,
                                  self.liste_position_temps[i])
        elif nb_bulle_restante < int(2 * nb_bulle / 3):
            self.nb_etoiles = 2
            for i in range(nb_bulle_restante):
                self.fenetre.blit(self.liste_image_chrono[1].surface,
                                  self.liste_position_temps[i])
        else:
            self.nb_etoile = 1
            for i in range(nb_bulle_restante):
                self.fenetre.blit(self.liste_image_chrono[0].surface,
                                  self.liste_position_temps[i])

    def affichage_complet(self, start):
        """fonction permettant d'afficher tout le jeu"""

        self.fenetre.blit(self.fond.surface, (0, 0))

        for i in range(self.collier.nb_perles - 1):
            if self.liste_corde_visible[i]:
                self.fenetre.blit(self.liste_surface_corde[i],
                                  self.liste_rectangle_corde[i])
        for i in range(self.collier.nb_perles):
            self.fenetre.blit(self.liste_surface_perle[i],
                              self.liste_positions_perles[i])

        self.affiche_coups_restants()
        self.affiche_repartition()
        self.affichage_chronometre(start)
        self.fenetre.blit(self.txt_niveau, self.txt_niveau_rect)
        self.fenetre.blit(self.voleur_0.surface, self.position_image_voleur_0)
        self.fenetre.blit(self.voleur_1.surface, self.position_image_voleur_1)
        self.fenetre.blit(self.curseur.surface, pygame.mouse.get_pos())

    def affichage_temps_ecoule(self):
        """affichage lorsque le temps est ecoule"""

        self.fenetre.blit(self.fond.surface, (0, 0))
        self.fenetre.blit(self.voleur_defaite_0.surface, (50, 150))
        self.fenetre.blit(self.voleur_defaite_1.surface, (350, 150))
        self.fenetre.blit(self.prison.surface, (0, 0))
        pygame.draw.rect(self.fenetre, Constantes.ROUGE, self.rect_4)
        pygame.draw.rect(self.fenetre, Constantes.VERT, self.rect_5)
        self.fenetre.blit(self.curseur.surface, pygame.mouse.get_pos())

    def affichage_niveau_reussi(self):
        """affichage lorsque le joueur a reussit le niveau"""

        self.fenetre.blit(self.fond.surface, (0, 0))
        self.fenetre.blit(self.tresor.surface, (200, 225))
        self.fenetre.blit(self.txt_niveau_reussi, self.txt_niveau_reussi_rect)
        pygame.draw.rect(self.fenetre, Constantes.ROUGE, self.rect_1)
        pygame.draw.rect(self.fenetre, Constantes.VERT, self.rect_2)
        pygame.draw.rect(self.fenetre, Constantes.ROSE, self.rect_3)
        if self.nb_etoiles == 3:
            self.fenetre.blit(self.etoile.surface, (100, 100))
            self.fenetre.blit(self.etoile.surface, (250, 100))
            self.fenetre.blit(self.etoile.surface, (400, 100))
        elif self.nb_etoiles == 2:
            self.fenetre.blit(self.etoile.surface, (175, 100))
            self.fenetre.blit(self.etoile.surface, (325, 100))
        else:
            self.fenetre.blit(self.etoile.surface, (250, 100))
        self.fenetre.blit(self.curseur.surface, pygame.mouse.get_pos())
        

    def jouer(self):
        """fonction permettant de jouer au niveau"""

        start = time.time()
        temps_ecoule = False
        niveau_reussi = False
        sortie = 0
        niveau_actif = True

        while niveau_actif: # main game loop

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    position_clic = pygame.mouse.get_pos()
                    if not niveau_reussi and not temps_ecoule:
                        rayon = self.rayon_perle
                        for i in range(self.collier.nb_perles - 1):
                            centre_0_x = self.liste_positions_perles[i][0]
                            centre_1_x = self.liste_positions_perles[i + 1][0]
                            somme_x = centre_0_x + centre_1_x + 2 * rayon
                            distance_x = position_clic[0] - somme_x / 2
                            centre_0_y = self.liste_positions_perles[i][1]
                            centre_1_y = self.liste_positions_perles[i + 1][1]
                            somme_y = centre_0_y + centre_1_y + 2 * rayon
                            distance_y = position_clic[1] - somme_y / 2
                            distance_x_carre = distance_x * distance_x
                            distance_y_carre = distance_y * distance_y
                            distance_carre = distance_x_carre + distance_y_carre
                            if distance_carre < self.rayon_clic * self.rayon_clic:
                                if self.liste_corde_visible[i]:
                                    if self.nb_coupes > 0:
                                        self.liste_corde_visible[i] = False
                                        self.nb_coupes -= 1
                                else:
                                    self.liste_corde_visible[i] = True
                                    self.nb_coupes += 1
                                self.liste_repartition = collier_fil_coupe(self.liste_corde_visible)
                                if MethodeNaive.decoupe_type_valable(self.collier, self.liste_repartition):
                                    niveau_reussi = True
                    elif niveau_reussi:
                        if position_clic[0] > 70 and position_clic[0] < 190:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 1
                                niveau_actif = False
                        if position_clic[0] > 240 and position_clic[0] < 360:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 2
                                niveau_actif = False
                        if position_clic[0] > 410 and position_clic[0] < 530:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 3
                                niveau_actif = False
                    else:
                        if position_clic[0] > 150 and position_clic[0] < 270:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 1
                                niveau_actif = False
                        if position_clic[0] > 330 and position_clic[0] < 450:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 2
                                niveau_actif = False
                        
                        

            if time.time() - start >= self.temps_niveau:
                temps_ecoule = True
            if temps_ecoule and not niveau_reussi:
                self.affichage_temps_ecoule()
            elif niveau_reussi:
                self.affichage_niveau_reussi()
            else:
                self.affichage_complet(start)

            pygame.display.update()

        return sortie
