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


def list_perle(collier, rayon_perle, list_positions):
    """Renvoit la list contenant toutes les surfaces
    correspondant aux perles du collier et met a jour
    les positions correspondantes dans list_positions"""

    angle = math.pi
    position_centre_x = int(Constantes.TAILLE_FENETRE / 2)
    position_centre_y = Constantes.RAYON_COLLIER
    centre_collier = [position_centre_x, position_centre_y]
    list_surface = []
    for i in range(collier.nb_perles):
        rayon_x = Constantes.RAYON_COLLIER * math.cos(angle)
        position_x = int(centre_collier[0] + rayon_x - rayon_perle)
        rayon_y = - Constantes.RAYON_COLLIER * math.sin(angle)
        position_y = int(centre_collier[1] + rayon_y - rayon_perle)
        list_positions.append((position_x, position_y))
        angle += math.pi / (collier.nb_perles - 1)
        perle = Image.Image(Image.LIST_PERL[collier.liste[i]],
                            2 * rayon_perle, 2 * rayon_perle)
        list_surface.append(perle.surface)
    return list_surface


def list_rope(nb_perles, rayon_perle, list_position_perles, list_rectangle):
    """Renvoit la list contenant toutes les surfaces
    correspondant aux ropes du collier et met a jour
    les rectangles correspondant dans list_rectangle"""

    list_surface = []
    perimetre = math.pi * Constantes.RAYON_COLLIER
    taille = (rayon_perle, int(perimetre / (nb_perles - 1)))
    image_rope = Image.Image("rope.gif", taille[0], taille[1])
    angle = 180 / (2 * (nb_perles - 1))
    for i in range(nb_perles - 1):
        position_x_0 = list_position_perles[i][0] + rayon_perle
        position_x_1 = list_position_perles[i + 1][0] + rayon_perle
        position_x = int((position_x_0 + position_x_1)/2)
        position_y_0 = list_position_perles[i][1] + rayon_perle
        position_y_1 = list_position_perles[i + 1][1] + rayon_perle
        position_y = int((position_y_0 + position_y_1)/2)
        perimetre = math.pi * Constantes.RAYON_COLLIER
        taille = (rayon_perle, int(perimetre / (nb_perles - 1)))
        surface = Image.Image("rope.gif", taille[0], taille[1])
        surface = pygame.transform.rotate(image_rope.surface, angle)
        rectangle = surface.get_rect()
        rectangle.center = (position_x, position_y)
        list_rectangle.append(rectangle)
        list_surface.append(surface)
        angle += 180 / (nb_perles - 1)
    return list_surface


def collier_fil_coupe(list_fil_visible):
    """Renvoit la list correspondant a la repartition
    de list_fil_visible"""

    list = [1]
    voleur = 1
    for booleen in list_fil_visible:
        if booleen:
            list.append(voleur)
        else:
            voleur = - voleur
            list.append(voleur)
    return list

def position_chrono(temps_niveau):
    """renvoit la list des positions des bulles du chronometre"""

    courbe = math.pi / 2
    centre_temps = [int(Constantes.TAILLE_FENETRE / 2),
                    int(Constantes.TAILLE_FENETRE / 3)]
    list_positions_temps = []
    rayon = Constantes.RAYON_TEMPS
    for i in range(Constantes.NB_BULLE):
        position_x = int(centre_temps[0] + rayon * math.cos(courbe))
        position_y = int(centre_temps[1] - rayon * math.sin(courbe))
        list_positions_temps.append((position_x, position_y))
        courbe += 2 * math.pi / (Constantes.NB_BULLE)
    return list_positions_temps


## Definition de la classe Niveau


class Niveau:
    """Classe contenant tous les parametres relatifs a un niveau"""

    def __init__(self, fenetre, repartition, temps_niveau, number):
        """Initialise les parametres du niveau"""

        self.collier = Collier.Collier()
        self.collier.collier_repartition(repartition)

        self.temps_niveau = temps_niveau

        self.fenetre = fenetre

        self.nb_etoiles = 3

        self.number = number
        perimetre = math.pi * Constantes.RAYON_COLLIER
        radius_0 = perimetre / (3 * (self.collier.nb_perles - 1))
        self.rayon_perle = int(min(35, radius_0))
        self.list_positions_perles = []
        self.list_surface_perle = list_perle(self.collier,
                                               self.rayon_perle,
                                               self.list_positions_perles)
        self.list_rectangle_rope = []
        self.list_surface_rope = list_rope(self.collier.nb_perles,
                                               self.rayon_perle,
                                               self.list_positions_perles,
                                               self.list_rectangle_rope)
        self.list_rope_visible = [True] * (self.collier.nb_perles - 1)
        longueur = perimetre / (self.collier.nb_perles - 1)
        self.rayon_clic = (longueur - self.rayon_perle) / 2
        self.nb_coupes = self.collier.nb_types
        self.espacement_perle_affiche = int((5 / 6) * Constantes.TAILLE_FENETRE / (self.collier.nb_perles + 1))

        self.list_repartition = [0] * self.collier.nb_perles

        self.list_position_temps = position_chrono(self.temps_niveau)

        self.charger_image()

    def charger_image(self):
        """Charge les images necessaires a l'affichage du jeu"""

        self.curseur = Image.Image("curseur.gif", 50, 30)
        taille = Constantes.TAILLE_FENETRE
        self.list_image_chrono = [Image.Image(Image.LIST_CHRONO[0], 20, 20),
                                   Image.Image(Image.LIST_CHRONO[1], 20, 20),
                                   Image.Image(Image.LIST_CHRONO[2], 20, 20)]
        self.prison = Image.Image("prison.png", 800, 600)
        self.tresor = Image.Image("tresor.png", int(taille / 3), int(taille / 3))
        self.fond = Image.Image("fond.gif", 800, 600)
        self.etoile = Image.Image("star.gif", 100, 100)
        self.list_coquillages = []
        for i in range(self.collier.nb_types):
            chemin = Image.LIST_SHELL[i]
            taille_coquillage = int(1.8  * self.rayon_perle)
            self.list_coquillages.append(Image.Image(chemin,
                                                      taille_coquillage,
                                                      taille_coquillage))
        self.list_perle_repartition = []
        taille_perle_repartition = int(1.4 * self.rayon_perle)
        for i in range(self.collier.nb_types):
            image = Image.Image(Image.LIST_PERL[i],
                                taille_perle_repartition,
                                taille_perle_repartition)
            self.list_perle_repartition.append(image.surface)
        taille_6 = int((1 / 6) * taille)
        self.voleur_0 = Image.Image("poisson1.gif", taille_6, taille_6)
        self.voleur_1 = Image.Image("poisson2.gif", taille_6, taille_6)
        self.voleur_defaite_0 = Image.Image("poisson1.gif", 200, 200)
        self.voleur_defaite_1 = Image.Image("poisson2.gif", 200, 200)
        self.position_image_voleur_0 = (0, 4 * taille_6)
        self.position_image_voleur_1 = (0, 5 * taille_6)
        font_0 = pygame.font.SysFont("mvboli", 50)
        font_1 = pygame.font.SysFont("mvboli", 15)
        self.txt_niveau = font_0.render("Level " + str(self.number), 1, (10, 10, 120))
        self.txt_niveau_rect = self.txt_niveau.get_rect()
        self.txt_niveau_rect.top = 30
        self.txt_niveau_rect.left = 30

        black = Constantes.NOIR
        txt = "Level " + str(self.number) + " succeeded !"
        self.txt_niveau_reussi = font_0.render(txt, 1, black)
        self.txt_niveau_reussi_rect = self.txt_niveau_reussi.get_rect()
        demi_fenetre = int(taille / 2)
        self.txt_niveau_reussi_rect.center = (demi_fenetre, 50)

        self.button_menu = Image.Image(Image.LIST_BUTTON[0], 50, 50)
        self.button_level = Image.Image(Image.LIST_BUTTON[1], 100, 50)
        self.button_new_level = Image.Image(Image.LIST_BUTTON[2], 100, 50)
        self.txt_menu = font_1.render("Menu", 1, black)
        self.txt_menu_rect_0 = self.txt_menu.get_rect()
        self.txt_menu_rect_0.center = (400, 400)
        self.txt_menu_rect_1 = self.txt_menu.get_rect()
        self.txt_menu_rect_1.center = (425, 525)
        self.txt_level = font_1.render("Restart", 1, black)
        self.txt_level_rect_0 = self.txt_level.get_rect()
        self.txt_level_rect_0.center = (210, 400)
        self.txt_level_rect_1 = self.txt_level.get_rect()
        self.txt_level_rect_1.center = (150, 525)
        self.txt_new_level = font_1.render("Next level", 1, black)
        self.txt_new_level_rect = self.txt_new_level.get_rect()
        self.txt_new_level_rect.center = (300, 525)

    def affiche_repartition(self):
        """Affiche la repartition des perles entre les 2 joueurs"""

        list_voleur_repartition = [[0] * self.collier.nb_types,
                                    [0] * self.collier.nb_types]
        for i in range(self.collier.nb_perles):
            if self.list_repartition[i] == 1:
                list_voleur_repartition[0][self.collier.liste[i]] += 1
            if self.list_repartition[i] == -1:
                list_voleur_repartition[1][self.collier.liste[i]] += 1
        taille = Constantes.TAILLE_FENETRE
        position_x_poubelle_0 = int(110 + 460 / 2 + self.espacement_perle_affiche / 2)
        position_x_poubelle_1 = int(110 + 460 / 2 + self.espacement_perle_affiche / 2)
        position_x_coussin = int(taille / 6 + self.espacement_perle_affiche / 2)
        rayon = self.rayon_perle
        espacement = int(1.8  * self.rayon_perle)
        position_y_0 = int((9 / 12) * taille)
        position_y_1 = int((11 / 12) * taille)
        for type in range(self.collier.nb_types):
            nb_coquillages = self.collier.liste.count(type)
            nb_perles_type_0 = list_voleur_repartition[0][type]
            nb_perles_type_1 = list_voleur_repartition[1][type]
            for j in range(int(nb_coquillages / 2)):
                pos_shell_0 = (int(position_x_coussin - espacement /2),
                               int(position_y_0 - espacement / 2))
                pos_shell_1 = (int(position_x_coussin - espacement / 2),
                               int(position_y_1 - espacement / 2))
                self.fenetre.blit(self.list_coquillages[type].surface,
                                  pos_shell_0)
                self.fenetre.blit(self.list_coquillages[type].surface,
                                  pos_shell_1)
                if nb_perles_type_0 > 0:
                    position_x = position_x_coussin - 0.7 * self.rayon_perle
                    position_y = position_y_0 - 0.7 * self.rayon_perle
                    position_cercle = (int(position_x), int(position_y))
                    self.fenetre.blit(self.list_perle_repartition[type],
                                      position_cercle)
                    nb_perles_type_0 -= 1
                if nb_perles_type_1 > 0:
                    position_x = position_x_coussin - 0.7 * self.rayon_perle
                    position_y = position_y_1 - 0.7 * self.rayon_perle
                    position_cercle = (int(position_x), int(position_y))
                    self.fenetre.blit(self.list_perle_repartition[type],
                                      position_cercle)
                    nb_perles_type_1 -= 1
                position_x_coussin += self.espacement_perle_affiche
            while nb_perles_type_0 > 0:
                position_x = position_x_poubelle_0 - 0.7 * self.rayon_perle
                position_y = position_y_0 - 0.7 * self.rayon_perle
                position_cercle = (int(position_x), int(position_y))
                self.fenetre.blit(self.list_perle_repartition[type],
                                  position_cercle)
                nb_perles_type_0 -= 1
                position_x_poubelle_0 += self.espacement_perle_affiche
            while nb_perles_type_1 > 0:
                position_x = position_x_poubelle_1 - 0.7 * self.rayon_perle
                position_y = position_y_1 - 0.7 * self.rayon_perle
                position_cercle = (int(position_x), int(position_y))
                self.fenetre.blit(self.list_perle_repartition[type],
                                  position_cercle)
                nb_perles_type_1 -= 1
                position_x_poubelle_1 += self.espacement_perle_affiche

    def affiche_coups_restants(self):
        """affiche le nombre de cous possibles restant
        represente par de ciseaux"""

        position_x = 30
        position_y = 100
        for i in range(self.nb_coupes):
            self.fenetre.blit(self.curseur.surface, (position_x, position_y))
            position_x += 40

    def affichage_chronometre(self, start):
        """affiche le chronometre"""

        temps = self.temps_niveau - time.time() + start
        nb_bulle = Constantes.NB_BULLE
        nb_bulle_restante = int(nb_bulle * temps / self.temps_niveau) + 1
        if nb_bulle_restante > int(2 * nb_bulle / 3) + 1:
            for i in range(nb_bulle_restante):
                self.fenetre.blit(self.list_image_chrono[0].surface,
                                  self.list_position_temps[i])
        elif nb_bulle_restante <= int(2 * nb_bulle / 3) + 1 and nb_bulle_restante > int(nb_bulle / 3):
            self.nb_etoiles = 2
            for i in range(nb_bulle_restante):
                self.fenetre.blit(self.list_image_chrono[1].surface,
                                  self.list_position_temps[i])
        else:
            self.nb_etoiles = 1
            for i in range(nb_bulle_restante):
                self.fenetre.blit(self.list_image_chrono[2].surface,
                                  self.list_position_temps[i])

    def affichage_complet(self, start):
        """fonction permettant d'afficher tout le jeu"""

        self.fenetre.blit(self.fond.surface, (0, 0))

        for i in range(self.collier.nb_perles - 1):
            if self.list_rope_visible[i]:
                self.fenetre.blit(self.list_surface_rope[i],
                                  self.list_rectangle_rope[i])
        for i in range(self.collier.nb_perles):
            self.fenetre.blit(self.list_surface_perle[i],
                              self.list_positions_perles[i])

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
        self.fenetre.blit(self.button_level.surface, (160, 375))
        self.fenetre.blit(self.button_menu.surface, (375, 375))
        self.fenetre.blit(self.txt_menu, self.txt_menu_rect_0)
        self.fenetre.blit(self.txt_level, self.txt_level_rect_0)
        self.fenetre.blit(self.curseur.surface, pygame.mouse.get_pos())

    def affichage_niveau_reussi(self):
        """affichage lorsque le joueur a reussit le niveau"""

        self.fenetre.blit(self.fond.surface, (0, 0))
        self.fenetre.blit(self.tresor.surface, (200, 225))
        self.fenetre.blit(self.txt_niveau_reussi, self.txt_niveau_reussi_rect)
        self.fenetre.blit(self.button_level.surface, (100, 500))
        if self.number < 20:
            self.fenetre.blit(self.button_new_level.surface, (250, 500))
            self.fenetre.blit(self.txt_new_level, self.txt_new_level_rect)
        self.fenetre.blit(self.button_menu.surface, (400, 500))
        self.fenetre.blit(self.txt_menu, self.txt_menu_rect_1)
        self.fenetre.blit(self.txt_level, self.txt_level_rect_1)
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
                            centre_0_x = self.list_positions_perles[i][0]
                            centre_1_x = self.list_positions_perles[i + 1][0]
                            somme_x = centre_0_x + centre_1_x + 2 * rayon
                            distance_x = position_clic[0] - somme_x / 2
                            centre_0_y = self.list_positions_perles[i][1]
                            centre_1_y = self.list_positions_perles[i + 1][1]
                            somme_y = centre_0_y + centre_1_y + 2 * rayon
                            distance_y = position_clic[1] - somme_y / 2
                            distance_x_carre = distance_x * distance_x
                            distance_y_carre = distance_y * distance_y
                            distance_carre = distance_x_carre + distance_y_carre
                            if distance_carre < self.rayon_clic * self.rayon_clic:
                                if self.list_rope_visible[i]:
                                    if self.nb_coupes > 0:
                                        self.list_rope_visible[i] = False
                                        self.nb_coupes -= 1
                                else:
                                    self.list_rope_visible[i] = True
                                    self.nb_coupes += 1
                                self.list_repartition = collier_fil_coupe(self.list_rope_visible)
                                if MethodeNaive.decoupe_type_valable(self.collier, self.list_repartition):
                                    niveau_reussi = True
                    elif niveau_reussi:
                        if position_clic[0] > 100 and position_clic[0] < 200:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 1 
                                niveau_actif = False
                        if self.number < 20:
                            if position_clic[0] > 250 and position_clic[0] < 350:
                                if position_clic[1] > 500 and position_clic[1] < 550:
                                    sortie = 2  
                                    niveau_actif = False
                        if position_clic[0] > 400 and position_clic[0] < 450:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 3
                                niveau_actif = False
                    else:
                        if position_clic[0] > 150 and position_clic[0] < 250:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 4
                                niveau_actif = False
                        if position_clic[0] > 400 and position_clic[0] < 450:
                            if position_clic[1] > 500 and position_clic[1] < 550:
                                sortie = 5
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

        data = [sortie, self.nb_etoiles]
        return data
