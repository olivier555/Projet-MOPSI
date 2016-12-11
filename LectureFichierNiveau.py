"""Fichier contenant les fonctions permettant de lire les fichiers
textes contenant les informations sur les niveaux"""

def lecture_fichier(fichier, liste_repartition, liste_temps):
    """fonction lisant un fichier texte afin de completer
    les 2 listes passes en argument"""

    monFichier = open(fichier, "r")
    contenu = monFichier.read()
    liste_niveau = contenu.split("\n")
    for niveau in liste_niveau:
        parametre = niveau.split(',')
        liste_temps.append(int(parametre[1]))
        repartition_string = parametre[0].split(' ')
        repartition_int = []
        for string in repartition_string:
            repartition_int.append(int(string))
        liste_repartition.append(repartition_int)
    monFichier.close()