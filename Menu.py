"""Classe permettant de generer le menu du jeu"""

## Modules importes ##

import pygame
import sys
import time
import Image
import Niveau


 
## Constantes globales ##
 
display_width = 800
display_height = 600
 
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
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def bouton_actif(msg, x, y, w, h, ic, ac, gameDisplay, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2) ), (y + (h / 2) ) )
    gameDisplay.blit(textSurf, textRect)

def bouton_non_actif(msg, x, y, w, h, ic, gameDisplay):

    pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2) ), (y + (h / 2) ) )
    gameDisplay.blit(textSurf, textRect)

        
## Classe menu ##

class Menu:
    """Classe permettant de generer un menu en fonction du nombre de niveaux debloques"""

    def __init__(self, nb_niveau, fenetre, liste_repartition, liste_temps):
    
        pygame.init()
        self.gameDisplay = fenetre
        pygame.display.set_caption('Pearl Cut')
        self.clock = pygame.time.Clock()
        self.nb_niveau = nb_niveau
        self.liste_repartition = liste_repartition
        self.liste_temps = liste_temps
        self.game_intro()
        

    
    def game_intro(self):


        gameExit = False
    
        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            self.gameDisplay.fill(white)
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = text_objects("Pearl Cut", largeText)
            TextRect.center = ( (display_width / 2), (display_height / 2) )
            self.gameDisplay.blit(TextSurf, TextRect)
    

            bouton_actif("Quit", 600, 450, 100, 50, red, bright_red, self.gameDisplay, self.quitgame)
            bouton_actif("Niveau", 100, 450, 100, 50, green, bright_green, self.gameDisplay, self.game_niveau)
            bouton_actif("Règles", 400, 450, 100, 50, blue, bright_blue, self.gameDisplay, self.game_regles)

            
            pygame.display.update()
            self.clock.tick(15)
            
            
    
    
    def game_regles(self):

        gameExit = False
    
        while not gameExit:
    
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            self.gameDisplay.fill(white)
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = text_objects("Règles", largeText)
            TextRect.center = ( (display_width / 2), (display_height / 2) )
            self.gameDisplay.blit(TextSurf, TextRect)

            bouton_actif("Quit", 600, 450, 100, 50, red, bright_red, self.gameDisplay, self.quitgame)
            bouton_actif("Menu", 300, 450, 100, 50, green, bright_green, self.gameDisplay, self.game_intro)
            bouton_actif("Tuto", 100, 450, 100, 50, red, bright_red, self.gameDisplay, self.game_tuto)
            
            pygame.display.update()
            self.clock.tick(60)
            

    
    def game_niveau(self):

    
        gameExit = False
    
        while not gameExit:

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            self.gameDisplay.fill(white)
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = text_objects("Niveau", largeText)
            TextRect.center = ( (display_width / 2), (display_height / 4) )
            self.gameDisplay.blit(TextSurf, TextRect)

            for niveau in range(self.nb_niveau):
    
                nom_niveau = "Niveau " + str(niveau + 1)
                bouton_actif(nom_niveau, 100 + niveau % 4 * 110, 250 + niveau // 4 * 60, 100, 50, green, bright_green, self.gameDisplay, lambda:self.game(niveau))
            
            for niveau in range(self.nb_niveau, 12):
    
                nom_niveau = "Niveau " + str(niveau + 1)
                bouton_non_actif(nom_niveau, 100 + niveau % 4 * 110, 250 + niveau // 4 * 60, 100, 50, green, self.gameDisplay) 
    
            bouton_actif("Menu", 300, 460, 100, 50, green, bright_green, self.gameDisplay, self.game_intro)
            
            
            pygame.display.update()
            self.clock.tick(60)


    
    def game(self, niv):

        level = Niveau.Niveau(self.gameDisplay, self.liste_repartition[niv], self.liste_temps[niv])
        entier = level.jouer()
        if niv == self.nb_niveau - 1:
            if entier == 1:
                self.nb_niveau += 1
                self.game_intro()
            if entier == 2:
                self.nb_niveau += 1
                while entier == 2:
                    level = Niveau.Niveau(self.gameDisplay, self.liste_repartition[niv], self.liste_temps[niv])
                    entier = level.jouer()
            if entier == 3:
                self.nb_niveau += 1
                self.game(niv + 1)
            if entier == 4:
                self.game_intro()
            while entier == 5:
                level = Niveau.Niveau(self.gameDisplay, self.liste_repartition[niv], self.liste_temps[niv])
                entier = level.jouer()
        else:
            if entier == 1:
                self.game_intro()
            if entier == 2:
                while entier == 2:
                    level = Niveau.Niveau(self.gameDisplay, self.liste_repartition[niv], self.liste_temps[niv])
                    entier = level.jouer()
            if entier == 3:
                self.game(niv + 1)
            if entier == 4:
                self.game_intro()
            while entier == 5:
                level = Niveau.Niveau(self.gameDisplay, self.liste_repartition[niv], self.liste_temps[niv])
                entier = level.jouer()




    def quitgame(self):

        print(self.nb_niveau)
        a = self.nb_niveau
        pygame.quit()
        return(a)
        
    
    def game_tuto(self):
        
        pygame.quit()

        


