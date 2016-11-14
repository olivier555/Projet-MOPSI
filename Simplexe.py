"""Module permettant de creer et gerer des simplexes"""

class Simplexe:
    """Classe créant un simplexe"""
    
    def __init__(self):
        """Initialisation du simplexe"""

        self.chaine = []
        self.taille = 0
        self.dimension = 0
        self.career_hemisphere = ' '
         
    def simplexe_initiale(self, nb_perles):
        """Fonction creant un simplexe initiale"""

        chaine_0 = [0] * nb_perles
        self.chaine = chaine_0
        self.taille = nb_perles
        
        
    def relation_ordre_partiel(self, other):
        """ si self < other au sens de R alors la fonction renvoie vraie"""

        for perle in range(self.taille):
            if abs(self.chaine[perle]) > abs(other.chaine[perle]):
                return False
            if self.chaine[perle] != 0:
                if self.chaine[perle] != other.chaine[perle]:
                    return False
        return True

    
    def dimension_simplexe(self):
        """Permet de calculer la dimension du simplexe"""

        compteur = 0
        for perle in range(self.taille):
            if self.chaine[perle] != 0:
                compteur += 1
        self.dimension = compteur 

    def concatenation(self, voleur):
        """Permet d'ajouter une valeur à la chaîne du simplexe"""

        self.chaine[self.dimension] = voleur
        self.dimension_simplexe()

    def voisins(self):
        """Trouve tous les voisins du simplexe"""

        if (self.dimension > 1):
            liste_voisins = []
            liste_position_perle = []
            liste_perle = []
            for perle in range(self.taille):
                if self.chaine[perle] != 0:
                    liste_perle.append(self.chaine[perle])
                    liste_position_perle.append(perle)
            for perle in range(len(liste_perle)):
                liste_vierge = [0] * self.taille
                liste_vierge[liste_position_perle[perle]] = liste_perle[perle]
                liste_voisins.append(liste_vierge)
            return liste_voisins
                
                
        
    
    
    def trouver_career_hemisphere(self):
        """Trouve le career hemisphere du simplexe"""
        
        hemisphere = ' '
        for perle in range(self.taille):
            if self.chaine[perle] == 1:
                hemisphere = '+'
            if self.chaine[perle] == -1:
                hemisphere = '-'
        self.career_hemisphere = hemisphere

        

        
       