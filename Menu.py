"""Classe permettant de generer le menu du jeu"""

## Modules importes ##

import pygame

import Constant
import Image
import Level


 
## Constantes globales ##
 
HEIGHT = Constant.WINDOW_SIZE

WHITE = Constant.WHITE  
BLACK = Constant.BLACK

## Fonctions outils ##

def text_objects(text, font):
    """Cree un objet texte"""

    text_area = font.render(text, True, BLACK)
    return text_area, text_area.get_rect()


def button(msg, x, y, w, h, image, game_display, action=None):
    """Cree un bouton actif"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        if click[0] == 1 and action != None:

            action()         

    game_display.blit(image.area, (x, y))
    small_text = pygame.font.SysFont("mvboli", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ( (x + (w / 2) ), (y + (h / 2) ) )
    game_display.blit(text_surf, text_rect)


def button_level(msg, x, y, w, h, imag, game_display, st, nb_star, action=None):
    """Cree un bouton de Level"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        if click[0] == 1 and action != None:
            action()         

    game_display.blit(imag.area, (x, y))

    for star in range(nb_star):

        game_display.blit(st.area, (x + 25 + star * 25, y + 15))

    small_text = pygame.font.SysFont("mvboli", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + 15), (y + (h / 2)))
    game_display.blit(text_surf, text_rect)


def display_background(game_display, background, text, x, y):
    """Cree le fond de chaque page du menu"""

    game_display.fill(WHITE)
    game_display.blit(background.area, (0, 0))
    large_text = pygame.font.SysFont("mvboli", 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (x, y)
    game_display.blit(text_surf, text_rect)
    

## Classe Menu ##

class Menu:
    """Classe permettant de generer un menu en fonction du nombre de Levelx 
    debloques"""

    def __init__(self, nb_lev, window, list_repartition, list_time, list_score):
        """Initialise la classe menu"""

        pygame.init()

        self.game_display = window
        pygame.display.set_caption('Angry Sea')

        self.clock = pygame.time.Clock()
        self.nb_level = nb_lev
        self.list_repartition = list_repartition
        self.list_time = list_time
        self.list_score = list_score
        self.nb_level_tot = len(list_repartition)

        self.download_image()


    def download_image(self):
        """Charge les images necessaires a l'affichage du menu"""

        self.background = Image.Image("background.gif", HEIGHT, HEIGHT)
        self.button_red = Image.Image(Image.LIST_BUTTON[0], 100, 50)
        self.button_orange = Image.Image(Image.LIST_BUTTON[1], 100, 50)
        self.button_yellow = Image.Image(Image.LIST_BUTTON[2], 100, 50)
        self.button_blue = Image.Image(Image.LIST_BUTTON[3], 100, 50)
        self.button_black = Image.Image(Image.LIST_BUTTON[4], 100, 50)
        self.star = Image.Image("star.gif", 20, 20)


    def play(self):
        """Execute le menu"""

        self.game_intro()
        pygame.quit()
        return (self.nb_level, self.list_score)

    
    def game_intro(self):
        """Lance le menu d'introduction"""

        self.game_exit = False
    
        while not self.game_exit:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()

            display_background(self.game_display, self.background, "Angry Sea", 
            HEIGHT / 2, 200)

            button("Level", 75, 450, 100, 50, self.button_yellow, 
            self.game_display, self.game_level)

            button("Rules", 250, 450, 100, 50, self.button_orange, 
            self.game_display, self.game_rules)

            button("Quit", 425, 450, 100, 50, self.button_red, self.game_display
            ,self.quitgame)
            

            pygame.display.update()
            self.clock.tick(15)

    
    def game_rules(self):
        """Donne les instructions du jeu"""

        while not self.game_exit:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()

            display_background(self.game_display, self.background, "Rules", 
            HEIGHT / 2, 100)

            small_text = pygame.font.SysFont("mvboli", 50)
            msg = " Deux petits POISSONS veulent se partager un MAGNIFIQUE collier de perles trouvé au fond de l'océan. Mais pour cela, ils ne disposent que d'un nombre limité de petits coquillages tranchants. Penses-tu pouvoir relever le défi avant que la police du fond de l'océan ne t'attrape toi et tes deux petits poisons ? !"
            text_surf, text_rect = text_objects(msg, small_text)
            text_rect.center = (300, 200)
            self.game_display.blit(text_surf, text_rect)

            button("Return", 450, 500, 100, 50, self.button_orange, 
            self.game_display, self.game_intro)

            pygame.display.update()
            self.clock.tick(60)

    
    def game_level(self):
        """Affiche les differents Levelx du jeu"""

        while not self.game_exit:
    
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()

            display_background(self.game_display, self.background, "Level", 
            HEIGHT / 2, 100)

            for lev in range(self.nb_level):

                name_level = str(lev + 1) 

                button_level(name_level, 50 + lev % 4 * 130, 250 + lev // 4 * 60
                , 100, 50, self.button_blue, self.game_display, self.star, 
                self.list_score[lev], lambda:self.game(lev))

            for lev in range(self.nb_level, self.nb_level_tot):
    
                name_level = str(lev + 1)

                button(name_level, 50 + lev % 4 * 130, 250 + lev // 4 * 60, 100
                , 50, self.button_black, self.game_display, None) 

            button("Menu", 450, 500, 100, 50, self.button_orange, 
            self.game_display, self.game_intro)

            pygame.display.update()
            self.clock.tick(60)


    def game(self, lev):
        """Lance un Level du jeu"""

        level = Level.Level(self.game_display, self.list_repartition[lev], 
        self.list_time[lev], lev + 1)

        data = level.play()
        number = data[0]

        if (number == 1 or number == 2 or number == 3):

            if self.list_score[lev] < data[1]:

                self.list_score[lev] = data[1]
        
        if lev == self.nb_level - 1:

            while number == 4:

                level = Level.Level(self.game_display, 
                self.list_repartition[lev], self.list_time[lev], lev + 1)

                data = level.play()
                number = data[0]

            if number == 3:

                if self.nb_level < self.nb_level_tot :
                
                    self.nb_level += 1

                self.game_intro()
                
            if number == 1:

                self.nb_level += 1

                while number == 1:

                    level = Level.Level(self.game_display, 
                    self.list_repartition[lev], self.list_time[lev], lev + 1)

                    data = level.play()
                    number = data[0]   

            if number == 2 and lev != self.nb_level_tot - 1:

                self.nb_level += 1
                self.game(lev + 1)

            if number == 5:
    
                self.game_intro()

        else:

            while number == 4:

                level = Level.Level(self.game_display, 
                self.list_repartition[lev], self.list_time[lev], lev + 1)

                data = level.play()
                number = data[0]

            if number == 3:
    
                self.game_intro()

            if number == 1:

                while number == 1:

                    level = Level.Level(self.game_display, 
                    self.list_repartition[lev], self.list_time[lev], lev + 1)

                    data = level.play()
                    number = data[0]

            if number == 2 and lev != self.nb_level_tot - 1:

                self.game(lev + 1)

            if number == 5:

                self.game_intro()

        

    def quitgame(self):
        """Quitte le menu"""

        self.game_exit = True


