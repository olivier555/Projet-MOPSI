"""Module permettant de creer un collier"""

## Modules importes ##

import random

## Classe Necklace ##

class Necklace:
    """Classe permettant de creer un collier a partir d'un nombre de perles et 
    de types fixé"""
    
    def __init__(self):
        """Initialise la classe Necklace"""

        self.list = []
        self.nb_type = 0
        self.nb_pearl = 0


    def necklace_repartition(self, repartition):
        """Cree un collier a partir de la liste repartition
        donnant le nombre de perles par type"""

        self.nb_type = len(repartition)
        self.list = []

        for i in range(self.nb_type):

            self.list += [i] * repartition[i]
    
        random.shuffle(self.list)
        self.nb_pearl = len(self.list)