"""Fichier contenant la fonction lambda pour un vecteur_signe
ainsi que pour une liste de simlexe"""

## Modules importes

from Collier import Collier
import Vecteur_Signe
import copy

def fonction_m_complet(liste):
    """fonction calculant m d'une liste complet (sans 0)
    definit comme le nombre d'alternance entre 0 et 1
    et de signe le premier element du vecteur_signe"""

    signe = liste[0]
    val_abs = 0
    for i in range(len(liste) - 1):
        if liste[i] != liste[i+1]:
            val_abs += 1
    return signe * val_abs


def fonction_m(vecteur_signe):
    """fonction calculant m pour tout vecteur_signe definit comme
    maxabs(m(vecteur_signe_complet)|vecteur_signe inclut dans vecteur_signe complet"""
    
    indice_non_nul = len(vecteur_signe.liste)

    if 1 in vecteur_signe.liste and -1 in vecteur_signe.liste:
        indice_non_nul = min(vecteur_signe.liste.index(-1),vecteur_signe.liste.index(1))
    elif 1 in vecteur_signe.liste:
        indice_non_nul = vecteur_signe.liste.index(1)
    elif -1 in vecteur_signe.liste:
        indice_non_nul = vecteur_signe.liste.index(-1)
    while indice_non_nul < len(vecteur_signe.liste) and vecteur_signe.liste[indice_non_nul] == 0:
        indice_non_nul += 1


    #Creation de vecteur_signe_complet un vecteur_signe complet contenant vecteur_signe
    #et ayant le maximum d'alternances possibles
    liste_copie = copy.deepcopy(vecteur_signe.liste)

    for i in range(indice_non_nul - 1, -1, -1):
        liste_copie[i] = - liste_copie[i + 1]

    for i in range(indice_non_nul + 1, len(vecteur_signe.liste)):
        if liste_copie[i] == 0:
            liste_copie[i] = - liste_copie[i - 1]

    return fonction_m_complet(liste_copie)


def repartition_joueurs_types(vecteur_signe, collier):
    """fonction renvoyant une double liste contenant
    le nombre de perles que chaque joueur a par type"""

    liste_joueur_1 = [0] * collier.nb_types
    liste_joueur_2 = [0] * collier.nb_types
    liste_perles_joueur = [liste_joueur_1, liste_joueur_2]
    for i in range(collier.nb_perles):
        if vecteur_signe.liste[i] == 1:
            liste_perles_joueur[0][collier.liste[i]] += 1
        if vecteur_signe.liste[i] == -1:
            liste_perles_joueur[1][collier.liste[i]] += 1
    return liste_perles_joueur


def fonction_lambda(vecteur_signe, collier):
    """calcule la fonction lambda d'un vecteur_signe"""

    valeur_m = fonction_m(vecteur_signe)
            
    if abs(valeur_m) > collier.nb_types:
        return  valeur_m

    repartition_perles_types = repartition_joueurs_types(vecteur_signe, collier)
    #print(repartition_perles_types)
    for i in range(collier.nb_types):
        moitie = int(collier.repartition[i] / 2)
        if repartition_perles_types[0][i] > moitie:
            return (i + 1)
        if repartition_perles_types[1][i] > moitie:
            return - (i + 1)
    return 0


def fonction_lambda_liste(liste_vecteur_signe, collier):
    """Renvoit une liste contenant les valeurs de la fonction lambda
    pour chaque vecteur_signe de la liste"""

    return [fonction_lambda(vecteur_signe, collier) for vecteur_signe in liste_vecteur_signe]
