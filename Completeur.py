import copy
import Collier
import Vecteur_Signe
from Lambda import repartition_joueurs_types

def complete(vecteur_signe, collier):
    """renvoit la liste complete de maniere equitable"""

    liste = copy.deepcopy(Vecteur_Signe.liste)
    repartition_joueurs_types = repartition_joueurs_types(vecteur_signe, collier)
    for indice in range(collier.nb_perles):
        if liste[indice] == 0:
            if repartition_joueurs_types[0][indice] < repartition_joueurs_types[1][indice]:
                liste[indice] = 1
                repartition_joueurs_types[0][indice] += 1
            else:
                liste[indice] = -1
                repartition_joueurs_types[1][indice] += 1
    return liste
                