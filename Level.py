"""Fichier contenant la definition de la classe level"""

## Modules importes


import math
import time
import sys
import pygame

import Necklace
import Image
import Constant
import Tools


## Fonctions outils


def list_pearl(necklace, radius_pearl, list_positions):
    """Renvoit la list contenant toutes les areas
    correspondant aux pearl du necklace et met a jour
    les positions correspondantes dans list_positions"""

    angle = math.pi
    position_center_x = int(Constant.WINDOW_SIZE / 2)
    position_center_y = Constant.RADIUS_NECKLACE
    center_necklace = [position_center_x, position_center_y]
    list_area = []
    for i in range(necklace.nb_pearl):
        radius_x = Constant.RADIUS_NECKLACE * math.cos(angle)
        position_x = int(center_necklace[0] + radius_x - radius_pearl)
        radius_y = - Constant.RADIUS_NECKLACE * math.sin(angle)
        position_y = int(center_necklace[1] + radius_y - radius_pearl)
        list_positions.append((position_x, position_y))
        angle += math.pi / (necklace.nb_pearl - 1)
        pearl = Image.Image(Image.LIST_PERL[necklace.list[i]],
                            2 * radius_pearl, 2 * radius_pearl)
        list_area.append(pearl.area)
    return list_area


def list_rope(nb_pearl, radius_pearl, list_position_pearl, list_rectangle):
    """Renvoit la list contenant toutes les areas
    correspondant aux areas des rope du necklace et met a jour
    les rectangles correspondant dans list_rectangle"""

    list_area = []
    perimeter = math.pi * Constant.RADIUS_NECKLACE
    size = (radius_pearl, int(perimeter / (nb_pearl - 1)))
    image_rope = Image.Image("rope.gif", size[0], size[1])
    angle = 180 / (2 * (nb_pearl - 1))
    for i in range(nb_pearl - 1):
        position_x_0 = list_position_pearl[i][0] + radius_pearl
        position_x_1 = list_position_pearl[i + 1][0] + radius_pearl
        position_x = int((position_x_0 + position_x_1)/2)
        position_y_0 = list_position_pearl[i][1] + radius_pearl
        position_y_1 = list_position_pearl[i + 1][1] + radius_pearl
        position_y = int((position_y_0 + position_y_1)/2)
        perimeter = math.pi * Constant.RADIUS_NECKLACE
        size = (radius_pearl, int(perimeter / (nb_pearl - 1)))
        area = Image.Image("rope.gif", size[0], size[1])
        area = pygame.transform.rotate(image_rope.area, angle)
        rectangle = area.get_rect()
        rectangle.center = (position_x, position_y)
        list_rectangle.append(rectangle)
        list_area.append(area)
        angle += 180 / (nb_pearl - 1)
    return list_area


def necklace_rope_coupe(list_rope_visible):
    """Renvoit la list correspondant a la repartition
    de list_rope_visible"""

    list = [1]
    thief = 1
    for booleen in list_rope_visible:
        if booleen:
            list.append(thief)
        else:
            thief = - thief
            list.append(thief)
    return list


def position_chrono(time_level):
    """renvoit la list des positions des bubbles du chronometer"""

    curve = math.pi / 2
    center_time = [int(Constant.WINDOW_SIZE / 2),
                   int(Constant.WINDOW_SIZE / 3)]
    list_position_time = []
    radius = Constant.RADIUS_TIME
    for i in range(Constant.NB_BUBBLE):
        position_x = int(center_time[0] + radius * math.cos(curve))
        position_y = int(center_time[1] - radius * math.sin(curve))
        list_position_time.append((position_x, position_y))
        curve += 2 * math.pi / (Constant.NB_BUBBLE)
    return list_position_time


## Definition de la classe level


class Level:
    """Classe contenant tous les parametres relatifs a un level"""

    def __init__(self, window, repartition, time_level, number):
        """Initialise les parametres du level"""

        self.necklace = Necklace.Necklace()
        self.necklace.necklace_repartition(repartition)

        self.time_level = time_level

        self.window = window

        self.nb_star = 3

        self.number = number
        perimeter = math.pi * Constant.RADIUS_NECKLACE
        radius_0 = perimeter / (3 * (self.necklace.nb_pearl - 1))
        self.radius_pearl = int(min(35, radius_0))
        self.list_position_pearl = []
        self.list_area_pearl = list_pearl(self.necklace,
                                               self.radius_pearl,
                                               self.list_position_pearl)
        self.list_rectangle_rope = []
        self.list_area_rope = list_rope(self.necklace.nb_pearl,
                                               self.radius_pearl,
                                               self.list_position_pearl,
                                               self.list_rectangle_rope)
        self.list_rope_visible = [True] * (self.necklace.nb_pearl - 1)
        longueur = perimeter / (self.necklace.nb_pearl - 1)
        self.radius_clic = (longueur - self.radius_pearl) / 2
        self.nb_cut = self.necklace.nb_type - repartition.count(0)
        num = (5 / 6) * Constant.WINDOW_SIZE
        den = self.necklace.nb_pearl + 1
        self.spacing_pearl_display = int(num / den)

        self.list_repartition = [0] * self.necklace.nb_pearl

        self.list_position_time = position_chrono(self.time_level)

        self.load_image()


    def load_image(self):
        """Charge les images necessaires a l'affichage du jeu"""

        self.cursor = Image.Image("cursor.gif", 50, 30)
        size = Constant.WINDOW_SIZE
        self.list_image_chrono = [Image.Image(Image.LIST_CHRONO[0], 20, 20),
                                   Image.Image(Image.LIST_CHRONO[1], 20, 20),
                                   Image.Image(Image.LIST_CHRONO[2], 20, 20)]
        self.prison = Image.Image("jail.png", 800, 600)
        self.treasure = Image.Image("treasure.png", int(size / 3),
                                    int(size / 3))
        self.fond = Image.Image("background.gif", 800, 600)
        self.star = Image.Image("star.gif", 100, 100)
        self.list_shell = []
        for i in range(self.necklace.nb_type):
            chemin = Image.LIST_SHELL[i]
            size_shell = int(1.8  * self.radius_pearl)
            self.list_shell.append(Image.Image(chemin,
                                               size_shell,
                                               size_shell))
        self.list_pearl_repartition = []
        size_pearl_repartition = int(1.4 * self.radius_pearl)
        for i in range(self.necklace.nb_type):
            image = Image.Image(Image.LIST_PERL[i],
                                size_pearl_repartition,
                                size_pearl_repartition)
            self.list_pearl_repartition.append(image.area)
        size_6 = int((1 / 6) * size)
        self.thief_0 = Image.Image("fish1.gif", size_6, size_6)
        self.thief_1 = Image.Image("fish2.gif", size_6, size_6)
        self.thief_defeat_0 = Image.Image("fish1.gif", 200, 200)
        self.thief_defeat_1 = Image.Image("fish2.gif", 200, 200)
        self.position_image_thief_0 = (0, 4 * size_6)
        self.position_image_thief_1 = (0, 5 * size_6)
        font_0 = pygame.font.SysFont("mvboli", 50)
        font_1 = pygame.font.SysFont("mvboli", 15)
        self.txt_level = font_0.render("Level " + str(self.number), 1,
                                       (10, 10, 120))
        self.txt_level_rect = self.txt_level.get_rect()
        self.txt_level_rect.top = 30
        self.txt_level_rect.left = 30

        black = Constant.BLACK
        txt = "Level " + str(self.number) + " succeeded !"
        self.txt_level_succed = font_0.render(txt, 1, black)
        self.txt_level_succed_rect = self.txt_level_succed.get_rect()
        demi_window = int(size / 2)
        self.txt_level_succed_rect.center = (demi_window, 50)

        self.button_menu = Image.Image(Image.LIST_BUTTON[0], 50, 50)
        self.button_level = Image.Image(Image.LIST_BUTTON[1], 100, 50)
        self.button_new_level = Image.Image(Image.LIST_BUTTON[2], 100, 50)
        self.txt_menu = font_1.render("Menu", 1, black)
        self.txt_menu_rect_0 = self.txt_menu.get_rect()
        self.txt_menu_rect_0.center = (400, 400)
        self.txt_menu_rect_1 = self.txt_menu.get_rect()
        self.txt_menu_rect_1.center = (425, 525)
        self.txt_restart = font_1.render("Restart", 1, black)
        self.txt_restart_rect_0 = self.txt_restart.get_rect()
        self.txt_restart_rect_0.center = (210, 400)
        self.txt_restart_rect_1 = self.txt_restart.get_rect()
        self.txt_restart_rect_1.center = (150, 525)
        self.txt_new_level = font_1.render("Next level", 1, black)
        self.txt_new_level_rect = self.txt_new_level.get_rect()
        self.txt_new_level_rect.center = (300, 525)

    def display_repartition(self):
        """Affiche la repartition des pearl entre les 2 joueurs"""

        list_thief_repartition = [[0] * self.necklace.nb_type,
                                    [0] * self.necklace.nb_type]
        for i in range(self.necklace.nb_pearl):
            if self.list_repartition[i] == 1:
                list_thief_repartition[0][self.necklace.list[i]] += 1
            if self.list_repartition[i] == -1:
                list_thief_repartition[1][self.necklace.list[i]] += 1
        size = Constant.WINDOW_SIZE
        position_x_bin_0 = int(110 + 460 / 2 + self.spacing_pearl_display / 2)
        position_x_bin_1 = int(110 + 460 / 2 + self.spacing_pearl_display / 2)
        position_x_shell = int(size / 6 + self.spacing_pearl_display / 2)
        radius = self.radius_pearl
        spacing = int(1.8  * self.radius_pearl)
        position_y_0 = int((9 / 12) * size)
        position_y_1 = int((11 / 12) * size)
        for type in range(self.necklace.nb_type):
            nb_shell = self.necklace.list.count(type)
            nb_pearl_type_0 = list_thief_repartition[0][type]
            nb_pearl_type_1 = list_thief_repartition[1][type]
            for j in range(int(nb_shell / 2)):
                pos_shell_0 = (int(position_x_shell - spacing /2),
                               int(position_y_0 - spacing / 2))
                pos_shell_1 = (int(position_x_shell - spacing / 2),
                               int(position_y_1 - spacing / 2))
                self.window.blit(self.list_shell[type].area,
                                  pos_shell_0)
                self.window.blit(self.list_shell[type].area,
                                  pos_shell_1)
                if nb_pearl_type_0 > 0:
                    position_x = position_x_shell - 0.7 * self.radius_pearl
                    position_y = position_y_0 - 0.7 * self.radius_pearl
                    position_circle = (int(position_x), int(position_y))
                    self.window.blit(self.list_pearl_repartition[type],
                                      position_circle)
                    nb_pearl_type_0 -= 1
                if nb_pearl_type_1 > 0:
                    position_x = position_x_shell - 0.7 * self.radius_pearl
                    position_y = position_y_1 - 0.7 * self.radius_pearl
                    position_circle = (int(position_x), int(position_y))
                    self.window.blit(self.list_pearl_repartition[type],
                                      position_circle)
                    nb_pearl_type_1 -= 1
                position_x_shell += self.spacing_pearl_display
            while nb_pearl_type_0 > 0:
                position_x = position_x_bin_0 - 0.7 * self.radius_pearl
                position_y = position_y_0 - 0.7 * self.radius_pearl
                position_circle = (int(position_x), int(position_y))
                self.window.blit(self.list_pearl_repartition[type],
                                  position_circle)
                nb_pearl_type_0 -= 1
                position_x_bin_0 += self.spacing_pearl_display
            while nb_pearl_type_1 > 0:
                position_x = position_x_bin_1 - 0.7 * self.radius_pearl
                position_y = position_y_1 - 0.7 * self.radius_pearl
                position_circle = (int(position_x), int(position_y))
                self.window.blit(self.list_pearl_repartition[type],
                                  position_circle)
                nb_pearl_type_1 -= 1
                position_x_bin_1 += self.spacing_pearl_display


    def display_hit_left(self):
        """Affiche le nombre de coups possibles restant
        represente par des coquillage"""

        position_x = 30
        position_y = 100
        for i in range(self.nb_cut):
            self.window.blit(self.cursor.area, (position_x, position_y))
            position_x += 40


    def display_chronometer(self, start):
        """Affiche le chronometre"""

        timer = self.time_level - time.time() + start
        nb_bubble = Constant.NB_BUBBLE
        nb_bubble_restante = int(nb_bubble * timer / self.time_level) + 1
        bool1 = nb_bubble_restante <= int(2 * nb_bubble / 3) + 1
        bool2 = nb_bubble_restante > int(nb_bubble / 3)
        if nb_bubble_restante > int(2 * nb_bubble / 3) + 1:
            for i in range(nb_bubble_restante):
                self.window.blit(self.list_image_chrono[0].area,
                                  self.list_position_time[i])
        elif bool1 and bool2:
            self.nb_star = 2
            for i in range(nb_bubble_restante):
                self.window.blit(self.list_image_chrono[1].area,
                                  self.list_position_time[i])
        else:
            self.nb_star = 1
            for i in range(nb_bubble_restante):
                self.window.blit(self.list_image_chrono[2].area,
                                  self.list_position_time[i])


    def display_complete(self, start):
        """Fonction permettant d'afficher tout le jeu"""

        self.window.blit(self.fond.area, (0, 0))

        for i in range(self.necklace.nb_pearl - 1):
            if self.list_rope_visible[i]:
                self.window.blit(self.list_area_rope[i],
                                 self.list_rectangle_rope[i])
        for i in range(self.necklace.nb_pearl):
            self.window.blit(self.list_area_pearl[i],
                             self.list_position_pearl[i])

        self.display_hit_left()
        self.display_repartition()
        self.display_chronometer(start)
        self.window.blit(self.txt_level, self.txt_level_rect)
        self.window.blit(self.thief_0.area, self.position_image_thief_0)
        self.window.blit(self.thief_1.area, self.position_image_thief_1)
        self.window.blit(self.cursor.area, pygame.mouse.get_pos())

    def display_time_finished(self):
        """Affichage lorsque le temps est ecoule"""

        self.window.blit(self.fond.area, (0, 0))
        self.window.blit(self.thief_defeat_0.area, (50, 150))
        self.window.blit(self.thief_defeat_1.area, (350, 150))
        self.window.blit(self.prison.area, (0, 0))
        self.window.blit(self.button_level.area, (160, 375))
        self.window.blit(self.button_menu.area, (375, 375))
        self.window.blit(self.txt_menu, self.txt_menu_rect_0)
        self.window.blit(self.txt_restart, self.txt_restart_rect_0)
        self.window.blit(self.cursor.area, pygame.mouse.get_pos())

    def display_level_succed(self):
        """Affichage lorsque le joueur a reussi le niveau"""

        self.window.blit(self.fond.area, (0, 0))
        self.window.blit(self.treasure.area, (200, 225))
        self.window.blit(self.txt_level_succed, self.txt_level_succed_rect)
        self.window.blit(self.button_level.area, (100, 500))
        if self.number < 20:
            self.window.blit(self.button_new_level.area, (250, 500))
            self.window.blit(self.txt_new_level, self.txt_new_level_rect)
        self.window.blit(self.button_menu.area, (400, 500))
        self.window.blit(self.txt_menu, self.txt_menu_rect_1)
        self.window.blit(self.txt_restart, self.txt_restart_rect_1)
        if self.nb_star == 3:
            self.window.blit(self.star.area, (100, 100))
            self.window.blit(self.star.area, (250, 100))
            self.window.blit(self.star.area, (400, 100))
        elif self.nb_star == 2:
            self.window.blit(self.star.area, (175, 100))
            self.window.blit(self.star.area, (325, 100))
        else:
            self.window.blit(self.star.area, (250, 100))
        self.window.blit(self.cursor.area, pygame.mouse.get_pos())
        

    def play(self):
        """Fonction permettant de jouer le niveau"""

        start = time.time()
        time_finished = False
        level_succed = False
        exit = 0
        level_active = True

        while level_active: # main game loop

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos_clic = pygame.mouse.get_pos()
                    if not level_succed and not time_finished:
                        radius = self.radius_pearl
                        for i in range(self.necklace.nb_pearl - 1):
                            center_0_x = self.list_position_pearl[i][0]
                            center_1_x = self.list_position_pearl[i + 1][0]
                            sum_x = center_0_x + center_1_x + 2 * radius
                            distance_x = pos_clic[0] - sum_x / 2
                            center_0_y = self.list_position_pearl[i][1]
                            center_1_y = self.list_position_pearl[i + 1][1]
                            sum_y = center_0_y + center_1_y + 2 * radius
                            distance_y = pos_clic[1] - sum_y / 2
                            distance_x_square = distance_x * distance_x
                            distance_y_square = distance_y * distance_y
                            distance_square = distance_x_square + distance_y_square
                            if distance_square < self.radius_clic * self.radius_clic:
                                if self.list_rope_visible[i]:
                                    if self.nb_cut > 0:
                                        self.list_rope_visible[i] = False
                                        self.nb_cut -= 1
                                else:
                                    self.list_rope_visible[i] = True
                                    self.nb_cut += 1
                                self.list_repartition = necklace_rope_coupe(self.list_rope_visible)
                                if Tools.valid_cut_type(self.necklace, self.list_repartition):
                                    level_succed = True
                    elif level_succed:
                        if pos_clic[0] > 100 and pos_clic[0] < 200:
                            if pos_clic[1] > 500 and pos_clic[1] < 550:
                                exit = 1 
                                level_active = False
                        if self.number < 20:
                            if pos_clic[0] > 250 and pos_clic[0] < 350:
                                if pos_clic[1] > 500 and pos_clic[1] < 550:
                                    exit = 2  
                                    level_active = False
                        if pos_clic[0] > 400 and pos_clic[0] < 450:
                            if pos_clic[1] > 500 and pos_clic[1] < 550:
                                exit = 3
                                level_active = False
                    else:
                        if pos_clic[0] > 160 and pos_clic[0] < 260:
                            if pos_clic[1] > 375 and pos_clic[1] < 425:
                                exit = 4
                                level_active = False
                        if pos_clic[0] > 375 and pos_clic[0] < 475:
                            if pos_clic[1] > 375 and pos_clic[1] < 425:
                                exit = 5
                                level_active = False

            if time.time() - start >= self.time_level:
                time_finished = True
            if time_finished and not level_succed:
                self.display_time_finished()
            elif level_succed:
                self.display_level_succed()
            else:
                self.display_complete(start)

            pygame.display.update()

        data = [exit, self.nb_star]
        return data
