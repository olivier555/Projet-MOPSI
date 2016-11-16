"""Module gerant le simplexe"""

import Vecteur_Signe

class Simplexe:
    """Classe creeant les simplexes"""
    
    def __init__(self):
        """Cree le simplexe initiale"""

        self.chaine = []
        self.dimension = -1
        self.carrier_hemisphere = []


    def __eq__(self, other):
        """Definition de l'egalite entre 2 simplexe"""

        if self.dimension != other.dimension:
            return False
        for indice in range(self.dimension +1):
            if self.chaine[indice] != other.chaine[indice]:
                return False
        return True


    def __repr__(self):
        """permet d'utiliser print"""

        return str(self.chaine)


    def __str__(self):
        """permet d'utiliser print"""

        return str(self.chaine)


    def dimension_simplexe(self):
        """Permet de calculer la dimension du simplexe"""

        self.dimension = len(self.chaine) - 1

    def carrier_hemisphere_simplexe(self):
        """Permet de calculer le carrier hemisphere"""

        if self.dimension > -1:
            self.carrier_hemisphere = self.chaine[self.dimension].carrier_hemisphere
            
    def simplexe_moins(self, indice0):

        assert(indice0 <= self.dimension)
        nouvelle_chaine = [self.chaine[indice] for indice in range(len(self.chaine)) if indice != indice0]
        return creer_simplexe(nouvelle_chaine)


    def liste_facette(self):
        """retourne une liste contenant tous les simplexes etant facettes
        de simplexe"""

        liste_facette = []
        for indice in range(len(self.chaine)):
            liste_facette.append(self.simplexe_moins(indice))
        return liste_facette


def creer_simplexe(chaine):

    simplexe = Simplexe()
    simplexe.chaine = chaine
    simplexe.chaine.sort()
    simplexe.dimension_simplexe()
    simplexe.carrier_hemisphere_simplexe()    
    return simplexe