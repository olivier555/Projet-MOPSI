"""Classe permettant de generer le menu du jeu"""

## Modules importes ##

import pygame
import sys
import time

import Constantes
import Image
import Niveau


 
## Constantes globales ##
 
height = Constantes.TAILLE_FENETRE
 
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

blue = (49, 140, 231)
bright_blue = (38, 196, 236)

## Fonctions outils ##

def text_objects(text, font):
    """Cree un objet texte"""

    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, image, gameDisplay, action=None):
    """Cree un bouton"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:

        if click[0] == 1 and action != None:
            action()         

    gameDisplay.blit(image.surface, (x, y))
    smallText = pygame.font.SysFont("mvboli", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2) ), (y + (h / 2) ) )
    gameDisplay.blit(textSurf, textRect)

def button_level(msg, x, y, w, h, image, gameDisplay, star, nb_star, action=None):
    """Cree un bouton de niveau"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:

        if click[0] == 1 and action != None:
            action()         

    gameDisplay.blit(image.surface, (x, y))
    for st in range(nb_star):
        gameDisplay.blit(star.surface, (x + st * 25 + 25, y + 15))
    smallText = pygame.font.SysFont("mvboli", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + 15), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def display_background(gameDisplay, background, text, x, y):
    """Cree le fond de chaque page du menu"""

    gameDisplay.fill(white)
    gameDisplay.blit(background.surface, (0, 0))
    largeText = pygame.font.SysFont("mvboli", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    
        
## Classe menu ##

class Menu:
    """Classe permettant de generer un menu en fonction du nombre de niveaux debloques"""

    def __init__(self, nb_level, window, list_repartition, list_time, list_score):
        """Initialise la classe menu"""

        pygame.init()

        self.gameDisplay = window
        pygame.display.set_caption('Pearl Cut')

        self.clock = pygame.time.Clock()
        self.nb_level = nb_level
        self.list_repartition = list_repartition
        self.list_time = list_time
        self.list_score = list_score
        self.nb_level_tot = len(list_repartition)

        self.download_image()


    def download_image(self):
        """Charge les images necessaires a l'affichage du menu"""

        self.background = Image.Image("fond.gif", height, height)
        self.button_red = Image.Image(Image.LIST_BUTTON[0], 100, 50)
        self.button_orange = Image.Image(Image.LIST_BUTTON[1], 100, 50)
        self.button_yellow = Image.Image(Image.LIST_BUTTON[2], 100, 50)
        self.button_blue = Image.Image(Image.LIST_BUTTON[3], 100, 50)
        self.button_black = Image.Image(Image.LIST_BUTTON[4], 100, 50)
        self.padlock = Image.Image("padlock.jpg", 50, 50)
        self.star = Image.Image("star.gif", 20, 20)


    def play(self):
        """Execute le menu"""

        self.game_intro()
        pygame.quit()
        return (self.nb_level, self.list_score)
    
    def game_intro(self):
        """Lance le menu d'introduction"""

        self.gameExit = False
    
        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display_background(self.gameDisplay, self.background, "Pearl Cut", height / 2, 200)
            button("Level", 75, 450, 100, 50, self.button_yellow, self.gameDisplay, self.game_level)
            button("Rules", 250, 450, 100, 50, self.button_orange, self.gameDisplay, self.game_rules)
            button("Quit", 425, 450, 100, 50, self.button_red, self.gameDisplay, self.quitgame)
            

            pygame.display.update()
            self.clock.tick(15)

    
    def game_rules(self):
        """Donne les instructions du jeu"""

        while not self.gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display_background(self.gameDisplay, self.background, "Rules", height / 2, 100)
            button("Return", 450, 500, 100, 50, self.button_orange, self.gameDisplay, self.game_intro)

            pygame.display.update()
            self.clock.tick(60)
   

    
    def game_level(self):
        """Affiche les differents niveaux du jeu"""

        while not self.gameExit:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display_background(self.gameDisplay, self.background, "Level", height / 2, 100)

            for lev in range(self.nb_level):
                
                name_level = str(lev + 1) 
                button_level(name_level, 50 + lev % 4 * 130, 250 + lev // 4 * 60, 100, 50, self.button_blue, self.gameDisplay, self.star, self.list_score[lev], lambda:self.game(lev))
            
            for lev in range(self.nb_level, self.nb_level_tot):
    
                name_level = str(lev + 1)
                button(name_level, 50 + lev % 4 * 130, 250 + lev // 4 * 60, 100, 50, self.button_black, self.gameDisplay, None) 

            button("Menu", 450, 500, 100, 50, self.button_orange, self.gameDisplay, self.game_intro)

            pygame.display.update()
            self.clock.tick(60)


    def game(self, lev):
        """Lance un niveau du jeu"""

        level = Niveau.Niveau(self.gameDisplay, self.list_repartition[lev], self.list_time[lev])
        data = level.jouer()
        number = data[0]

        if (number == 1 or number == 2 or number == 3):

            if self.list_score[lev] < data[1]:

                self.list_score[lev] = data[1]

        if lev == self.nb_level - 1:

            if number == 1:

                self.nb_level += 1
                self.game_intro()
                
            if number == 2:

                self.nb_level += 1

                while number == 2:

                    level = Niveau.Niveau(self.gameDisplay, self.list_repartition[lev], self.list_time[lev])
                    number = level.jouer()   

            if number == 3 and lev != self.nb_level_tot - 1:

                self.nb_level += 1
                self.game(lev + 1)

            if number == 4:
    
                self.game_intro()

            while number == 5:

                level = Niveau.Niveau(self.gameDisplay, self.list_repartition[lev], self.list_time[lev])
                number = level.jouer()
        else:

            if number == 1:
    
                self.game_intro()

            if number == 2:

                while number == 2:

                    level = Niveau.Niveau(self.gameDisplay, self.list_repartition[lev], self.list_time[lev])
                    number = level.jouer()

            if number == 3 and lev != self.nb_level_tot - 1:

                self.game(lev + 1)

            if number == 4:

                self.game_intro()

            while number == 5:

                level = Niveau.Niveau(self.gameDisplay, self.list_repartition[lev], self.list_time[lev])
                number = level.jouer()

    def quitgame(self):
        """Quitte le menu"""

        self.gameExit = True


