"""Module lançant la fenetre de jeu avec la grille et les actions possibles"""

## Modules importes ##


import time
from PyQt4 import QtGui, QtCore
import Collier
import sys


## Variables globales ##


LISTE_PERLE = ["perle_1.png", "perle_2.png", "perle_3.png"]

TAILLE_BOUTON = 100


## Classe Interface ##


class Interface(QtGui.QDialog):
    """classe permettant d'utiliser une interface graphique pour jouer au jeu"""


    def __init__(self):

        super(Interface, self).__init__()

        self.init_ui()


    def init_ui(self):


        #Initialisation du jeu
        self.collier = Collier.Collier()
        self.collier.collier_aleatoire(3, 8)

        #Creation de la grille permettant l'affichage
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        #Rend le fond de la fenetre blanc
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Background, QtGui.QColor("white"))
        self.setPalette(self.palette)


        #Liste contenant les valeurs contenues dans la grille de jeu
        names = self.collier.chaine
        taille = 8

        #Liste des position de la grille d'affichage dedie aux cases du jeu
        positions = [(i, j) for i in range(1) for j in range(taille)]

        #Creation du liste qui contiendra tous les boutons
        #correspondant à des cases de jeu
        list_buttons = []
        #Boucle creant les boutons correspondant au case de jeu
        for position, name in zip(positions, names):

            if name == '':
                continue
                
            label = QtGui.QLabel() 
            label.setPixmap(QtGui.QPixmap(LISTE_PERLE[0]))
            grid.addWidget(label, *position)
            button = self.image_associe(name)
            grid.addWidget(button, *position)
            
             


        self.list_buttons = list_buttons

        self.move(50, 50)
        self.setWindowTitle("jeu")
        self.show()




    def image_associe(self, name):
        """Associe l'image correspondant a valeur"""
        button = QtGui.QPushButton()
        button.setIcon(QtGui.QIcon(LISTE_PERLE[int(name)]))
        button.setIconSize(QtCore.QSize(TAILLE_BOUTON, TAILLE_BOUTON))
        button.setFlat(True)


        return button


APP = QtGui.QApplication(sys.argv)
ex = Interface()
sys.exit(APP.exec_())
