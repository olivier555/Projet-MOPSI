"""fichier contenant les fonctions permettant
d'obtenir la liste des partages"""


def ajout_element(liste, element):
    """T est une liste de liste
    Renvoit une liste de liste avec les listes contenues dans T
    concatenees avec element"""

    liste_element_ajoute = [liste[i]+[element] for i in range(len(liste))]
    return liste_element_ajoute


def ensemble_partie(liste):
    """Fonction recursive renvoyant toutes les parties de la liste S
    sous forme de liste"""

    #Cas d'arret
    if liste == []:
        #Renvoit de la liste vide
        return [[]]
    #Copie de liste afin de ne pas la modifier avec pop
    liste_copie = liste
    element = liste_copie.pop()
    #Appel recursif de la fonction pour une liste de taille len(liste)-1
    partie = ensemble_partie(liste_copie)
    #Renvoit de la liste des parties de
    return ajout_element(partie, element) + partie


def selection_partie(liste_partie, taille):
    """prend en argument une liste de liste et renvoit
    une liste contenant seulement les listes de partie de taille taille"""

    return [partie for partie in liste_partie if len(partie) == taille]
