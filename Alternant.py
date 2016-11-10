"""fichier contenant les fonctions permettant de trouver
si des listes sont alternantes"""

def alternant(liste):
    """ fonction permettant de savoir si liste est +alternating (renvoit +1),
    -alternating (renvoit -1) ou rien (renvoit 0)"""

    liste_abs = [abs(element) for element in liste]
    liste_abs_sorted = sorted(liste_abs)
    for i in range(len(liste) - 1):
        if liste_abs_sorted[i] == liste_abs_sorted[i + 1]:
            return 0
    liste_sorted = []
    for element in liste_abs_sorted:
        if element in liste:
            liste_sorted.append(element)
        else:
            liste_sorted.append(- element)
    for i in range (len(liste) - 1):
        if liste_sorted[i] * liste_sorted[i + 1] >= 0:
            return 0
    return int(liste_sorted[0] / liste_abs_sorted[0])
