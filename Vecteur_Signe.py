"""Module permettant de creer et gerer les vecteurs signes"""

import copy

class Vecteur_Signe:
    """Classe créant un vecteur signe"""
    
    def __init__(self, nb_perles):
        """Initialisation du vecteur signe"""

        self.liste = [0] * nb_perles
        self.taille = nb_perles
        self.carrier_hemisphere = [-1, 0]


    def __lt__(self, other):
        """ si self < other au sens de R alors la fonction renvoie vraie"""

        for perle in range(self.taille):
            if abs(self.liste[perle]) > abs(other.liste[perle]):
                return False
            if self.liste[perle] != 0:
                if self.liste[perle] != other.liste[perle]:
                    return False
        return True
    
    def __eq__(self, other):
        """Definition de l'egalite entre 2 vecteurs signes"""

        if self.taille != other.taille:
            return False
        for indice in range(self.taille):
            if self.liste[indice] != other.liste[indice]:
                return False
        return True


    def __ne__(self, other):
        """Definition de la non egalite entre 2 vecteurs signes"""

        return not self == other


    def __repr__(self):
        """Permet d'utiliser print sur la classe"""

        return str(self.liste)


    def __str__(self):
        """Permet d'utiliser print sur la classe"""

        return str(self.liste)

    def ajout_copie(self, voleur, position):
        """Permet d'ajouter une valeur à la chaîne du vecteur_signe"""

        nouveau_vecteur_signe = copy.deepcopy(self)
        nouveau_vecteur_signe.liste[position] = voleur
        nouveau_vecteur_signe.trouver_carrier_hemisphere()
        return nouveau_vecteur_signe

    
    def trouver_carrier_hemisphere(self):
        """Trouve le carrier hemisphere du vecteur_signe"""
        
        hemisphere = [0, 0]
        for perle in range(self.taille):
            if self.liste[perle] == 1:
                hemisphere[1] = 1
            if self.liste[perle] == -1:
                hemisphere[1] = -1
            if self.liste[perle] != 0:
                hemisphere[0] = perle
        self.carrier_hemisphere = hemisphere

        

def creer_vecteur_signe(liste):

    vecteur_signe = Vecteur_Signe(len(liste))
    vecteur_signe.liste = liste
    vecteur_signe.trouver_carrier_hemisphere()
    return vecteur_signe        
       