"""Classe permettant de generer le menu du jeu"""

## Modules importes ##

import pygame
import sys
import time

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

    def __init__(self, nb_niveau):
    
        pygame.init()
        self.gameDisplay = pygame.display.set_mode( (display_width, display_height) )
        pygame.display.set_caption('Pearl Cut')
        self.clock = pygame.time.Clock()
        self.nb_niveau = nb_niveau
        self.game_intro()
    
        
    
    def game_intro(self):
    
        intro = True
    
        while intro:
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
                bouton_actif(nom_niveau, 100 + niveau * 110, 340, 100, 50, green, bright_green, self.gameDisplay, self.game)
            
            for niveau in range(self.nb_niveau, 6):
    
                nom_niveau = "Niveau " + str(niveau + 1)
                bouton_non_actif(nom_niveau, 100 + (niveau - 3) * 110, 400, 100, 50, green, self.gameDisplay) 
    
            bouton_actif("Menu", 300, 460, 100, 50, green, bright_green, self.gameDisplay, self.game_intro)
            
            
            pygame.display.update()
            self.clock.tick(60)

    
    def game(self):

        repartition = [2, 2, 2, 4]
        niveau = Niveau.Niveau(self.gameDisplay, repartition, 50) 
        niveau.jouer()
        niveau.affichage_complet()


    def quitgame(self):

        pygame.quit()

menu = Menu(3)
