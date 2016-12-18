"""Fichier contenant la definition de la classe niveau"""

## Modules importes

import pygame
import math
import Collier
import Image
import Constantes
import time
import Vecteur_Signe
import sys


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
        position_x_0 = liste_position_perles[i][0]
        position_x_1 = liste_position_perles[i + 1][0]
        position_x = int((position_x_0 + position_x_1)/2)
        position_y_0 = liste_position_perles[i][1]
        position_y_1 = liste_position_perles[i + 1][1]
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
    for bool in liste_fil_visible:
        if bool:
            liste.append(voleur)
        else:
            voleur = - voleur
            liste.append(voleur)
    return liste
    
def position_chrono(temps_niveau):
    
    t1 = math.pi / 2
    centre_temps = [int(Constantes.TAILLE_FENETRE / 2), int(Constantes.TAILLE_FENETRE / 3)]
    liste_positions_temps = []
    for i in range(Constantes.NB_BULLE):
        liste_positions_temps.append((int(centre_temps[0] + Constantes.RAYON_TEMPS * math.cos(t1)), int(centre_temps[1] - Constantes.RAYON_TEMPS * math.sin(t1))))
        t1 += 2 * math.pi / (Constantes.NB_BULLE) 
        
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
        self.rayon_clic = (perimetre / (self.collier.nb_perles - 1) - self.rayon_perle) / 2
        self.nb_coupes = 0
        self.espacement_perle_affiche = int(460 / self.collier.nb_perles)

        self.liste_repartition = [0] * self.collier.nb_perles

        self.liste_position_temps = position_chrono(self.temps_niveau)
        
        self.liste_image_chrono = [Image.Image(Image.LISTE_CHRONO[0], 20, 20), Image.Image(Image.LISTE_CHRONO[1], 20, 20), Image.Image(Image.LISTE_CHRONO[2], 20, 20)]
        self.charger_image()

    def charger_image(self):
        """Charge les images necessaires a l'affichage du jeu"""

        self.curseur = Image.Image("curseur.gif", 50, 30)
        self.liste_image_chrono = [Image.Image(Image.LISTE_CHRONO[0], 20, 20), Image.Image(Image.LISTE_CHRONO[1], 20, 20), Image.Image(Image.LISTE_CHRONO[2], 20, 20)]
        self.prison = Image.Image("prison.png", Constantes.TAILLE_FENETRE, Constantes.TAILLE_FENETRE)
        self.tresor = Image.Image("tresor.png", Constantes.TAILLE_FENETRE, Constantes.TAILLE_FENETRE)
        self.fond = Image.Image("fond.gif", Constantes.TAILLE_FENETRE, Constantes.TAILLE_FENETRE)
        self.liste_coquillages = []
        for i in range(self.collier.nb_types):
            self.liste_coquillages.append(Image.Image(Image.LISTE_COQUILLAGES[i], self.espacement_perle_affiche, self.espacement_perle_affiche))
        self.voleur_0 = Image.Image("poisson1.gif", 50, 50)
        self.voleur_1 = Image.Image("poisson2.gif", 50, 50)
        self.position_image_voleur_0 = (30, 450)
        self.position_image_voleur_1 = (30, 525)
        font = pygame.font.SysFont(None, 50)
        self.texte_niveau = font.render("Level 1", 1, (10, 10, 120))
        self.texte_niveau_rect = self.texte_niveau.get_rect()
        self.texte_niveau_rect.top = 30
        self.texte_niveau_rect.left = 30
        
        
        self.texte_niveau_reussi = font.render("Level 1 réussi !", 1, (10, 250, 10))
        self.texte_niveau_reussi_rect = self.texte_niveau_reussi.get_rect()
        self.texte_niveau_reussi_rect.center = (int(Constantes.TAILLE_FENETRE / 2), int(Constantes.TAILLE_FENETRE / 2))
    
    def affiche_repartition(self):
        """Affiche la repartition des perles entre les 2 joueurs"""

        liste_voleur_repartition = [[0] * self.collier.nb_types, [0] * self.collier.nb_types]
        for i in range(self.collier.nb_perles):
            if self.liste_repartition[i] == 1:
                liste_voleur_repartition[0][collier.liste[i]] += 1
            if self.liste_repartition[i] == -1:
                liste_voleur_repartition[1][collier.liste[i]] += 1
        position_x_poubelle_0 = int(110 + 460 / 2)
        position_x_poubelle_1 = int(110 + 460 / 2)
        position_x_coussin = int(110)
        for type in range(self.collier.nb_types):
            nb_nuages = self.collier.liste.count(type)
            nb_perles_type_0 = liste_voleur_repartition[0][type]
            nb_perles_type_1 = liste_voleur_repartition[1][type]
            for j in range(int(nb_nuages / 2)):
                self.fenetre.blit(self.liste_coquillages[type].surface, (position_x_coussin, 460))
                self.fenetre.blit(self.liste_coquillages[type].surface, (position_x_coussin, 535))
                if nb_perles_type_0 > 0:
                    position_cercle = (int(- self.rayon_perle + position_x_coussin + self.espacement_perle_affiche / 2), int(- self.rayon_perle + 460 + self.espacement_perle_affiche / 2))
                    self.fenetre.blit(pygame.transform.scale(self.liste_surface_perle[type],(int(0.7 * self.espacement_perle_affiche), int(0.7 * self.espacement_perle_affiche))), position_cercle)
                    nb_perles_type_0 -= 1
                if nb_perles_type_1 > 0:
                    position_cercle = (int(- self.rayon_perle + position_x_coussin + self.espacement_perle_affiche / 2), int(- self.rayon_perle + 535 + self.espacement_perle_affiche / 2))
                    self.fenetre.blit(pygame.transform.scale(self.liste_surface_perle[type],(int(0.7 * self.espacement_perle_affiche), int(0.7 * self.espacement_perle_affiche))), position_cercle)
                    nb_perles_type_1 -= 1
                position_x_coussin += self.espacement_perle_affiche
            while nb_perles_type_0 > 0:
                position_cercle = (int(position_x_poubelle_0 + espacement_perle_affiche / 2), int(460 + espacement_perle_affiche / 2))
                self.fenetre.blit(pygame.transform.scale(self.liste_surface_perle[type],(int(0.7 * self.espacement_perle_affiche), int(0.7 * self.espacement_perle_affiche))), position_cercle)
                nb_perles_type_0 -= 1
                position_x_poubelle_0 += self.espacement_perle_affiche
            while nb_perles_type_1 > 0:
                position_cercle = (int(- self.rayon_perle + position_x_poubelle_1 + self.espacement_perle_affiche / 2), int(- self.rayon_perle + 535 + self.espacement_perle_affiche / 2))
                self.fenetre.blit(pygame.transform.scale(self.liste_surface_perle[type],(int(0.7 * self.espacement_perle_affiche), int(0.7 * self.espacement_perle_affiche))), position_cercle)
                nb_perles_type_1 -= 1
                position_x_poubelle_1 += self.espacement_perle_affiche
    
    def affiche_coups_restants(self):
        """affiche le nombre de cous possibles restant
        represente par de ciseaux"""
    
        position_x = 30
        position_y = 70
        for i in range(self.nb_coupes):
            self.fenetre.blit(self.curseur, (position_x, position_y))
            position_x += 40
    
    def affichage_chronometre(self, start):
        """affiche le chronometre"""
    
        nb_bulle_restante = int(Constantes.NB_BULLE * (self.temps_niveau - time.time() + start) / self.temps_niveau)
        if nb_bulle_restante < int(Constantes.NB_BULLE / 3):
            for t in range(nb_bulle_restante):
                self.fenetre.blit(self.liste_image_chrono[2].surface, liste_position_temps[t])
        elif nb_bulle_restante < int(2 * Constantes.NB_BULLE / 3):
            for t in range(nb_bulle_restante):
                self.fenetre.blit(self.liste_image_chrono[1].surface, self.liste_position_temps[t])
        else:
            for t in range(nb_bulle_restante):
                self.fenetre.blit(self.liste_image_chrono[0].surface, self.liste_position_temps[t])
    
        
    def affichage_complet(self, start):
        """fonction permettant d'afficher tout le jeu"""
    
        self.fenetre.blit(self.fond.surface, (0, 0))
        for i in range(self.collier.nb_perles - 1):
            if self.liste_corde_visible[i]:
                self.fenetre.blit(self.liste_surface_corde[i], self.liste_rectangle_corde[i])
        for i in range(self.collier.nb_perles):
            position = (self.liste_positions_perles[i][0] - self.rayon_perle, self.liste_positions_perles[i][1] - self.rayon_perle)
            self.fenetre.blit(pygame.transform.scale(self.liste_surface_perle[self.collier.liste[i]], (2 * self.rayon_perle, 2 * self.rayon_perle)), position)
            
        self.affiche_coups_restants()
        self.affiche_repartition()
        self.affichage_chronometre(start)
        self.fenetre.blit(self.texte_niveau, self.texte_niveau_rect)
        self.fenetre.blit(self.voleur_0.surface, self.position_image_voleur_0)
        self.fenetre.blit(self.voleur_1.surface, self.position_image_voleur_1)
        self.fenetre.blit(self.curseur.surface, pygame.mouse.get_pos())
    
    def affichage_temps_ecoule(self):
        """affichage lorsque le temps est ecoule"""
    
        self.fenetre.blit(self.fond, (0, 0))
        self.fenetre.blit(self.prison, (0, 0))
        self.fenetre.blit(self.curseur, pygame.mouse.get_pos())
    
    def affichage_niveau_reussi(self):
        """affichage lorsque le joueur a reussit le niveau"""
    
        self.fenetre.blit(self.fond.surface, (0, 0))
        self.fenetre.blit(self.tresor.surface,(0, 0))
        self.fenetre.blit(self.texte_niveau_reussi, self.texte_niveau_reussi_rect)
        self.fenetre.blit(self.curseur, pygame.mouse.get_pos())

    def jouer(self):
        
        start =  time.time()
        temps_ecoule = False
        niveau_reussi = False

        while True: # main game loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    position_clic = pygame.mouse.get_pos()
                    for i in range(self.collier.nb_perles - 1):
                        distance_x = position_clic[0] - (self.liste_positions_perles[i][0] + self.liste_positions_perles[i + 1][0] + 2 * self.rayon_perle) / 2
                        distance_y = position_clic[1] - (self.liste_positions_perles[i][0] + self.liste_positions_perles[i + 1][0] + 2 * self.rayon_perle) / 2
                        if distance_x * distance_x + distance_y * distance_y < self.rayon_clic * self.rayon_clic:
                            if self.liste_fil_visible[i]:
                                if self.nb_coupes > 0:
                                    self.liste_fil_visible[i] = False
                                    self.nb_coupes -= 1
                            else:
                                self.liste_fil_visible[i] = True
                                self.nb_coupes += 1
                            self.liste_repartition = collier_fil_coupe(liste_fil_visible)
                            if MethodeNaive.decoupe_type_valable(collier, liste_repartition):
                                niveau_reussi = True
                            
        
            if time.time() - start >= self.temps_niveau:
                temps_ecoule = True
            if temps_ecoule and not niveau_reussi:
                self.affichage_temps_ecoule()
            elif niveau_reussi:
                self.affichage_niveau_reussi()
            else:
                self.affichage_complet(start)
            
                
            pygame.display.update()