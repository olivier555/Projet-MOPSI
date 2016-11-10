"""Fichier contenant la fonction lambda pour un simplexe
ainsi que pour une liste de simlexe"""


def fonction_m_complet(simplexe):
    """fonction calculant m d'un simplexe complet (sans 0)
    definit comme le nombre d'alternance entre 0 et 1
    et de signe le premier element du simplexe"""

    signe = simplexe[0]
    val_abs = 0
    for i in range(len(simplexe) - 1):
        if simplexe[i] != simplexe[i+1]:
            val_abs += 1
    return signe * val_abs


def fonction_m(simplexe):
    """fonction calculant m pour tout simplexe definit comme
    maxabs(m(simplexe_complet)|simplexe inclut dans simplexe complet"""

    indice_non_nul = 0
    while simplexe[indice_non_nul] == 0:
        indice_non_nul += 1

    #Creation de simplexe_complet un simplexe complet contenant simplexe
    #et ayant le maximum d'alternances possibles
    simplexe_complet = simplexe

    for i in range(indice_non_nul - 1, -1, -1):
        simplexe_complet[i] = - simplexe_complet[i + 1]

    for i in range(indice_non_nul + 1, len(simplexe)):
        if simplexe_complet[i] == 0:
            simplexe_complet[i] = - simplexe_complet[i - 1]

    return fonction_m_complet(simplexe_complet)


def repartition_perles_types(simplexe, collier):
    """fonction renvoyant une double liste contenant
    le nombre de perles que chaque joueur a par type"""

    liste = [0] * collier.nb_types
    liste_nb_perles = [liste, liste]
    for i in range(collier.nb_perles):
        if simplexe[i] == 1:
            liste_nb_perles[0][collier.chaine[i]] += 1
        if simplexe[i] == -1:
            liste_nb_perles[-1][collier.chaine[i]] += 1
    return liste_nb_perles


def fonction_lambda(simplexe, collier):
    """calcule la fonction lambda d'un simplexe"""

    valeur_m = fonction_m(simplexe)

    if abs(valeur_m) > collier.nb_types:
        return valeur_m

    repartition_perles_type = repartition_perles_types(simplexe, collier)
    if abs(valeur_m) > collier.nb_types:
        for i in range(collier.nb_types):
            moitie = int(collier.repartition[i] / 2)
            if repartition_perles_type[0][i] > moitie:
                return i
            if repartition_perles_type[1][i] > moitie:
                return - i
    return 0


def fonction_lambda_liste(liste_simplexe, collier):
    """Renvoit une liste contenant les valeurs de la fonction lambda
    pour chaque simplexe de la liste"""

    return [fonction_lambda(simplexe, collier) for simplexe in liste_simplexe]
