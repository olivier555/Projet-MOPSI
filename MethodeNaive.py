"""Permet de trouver le partage equitable grace a une methode naive"""

import Collier
import ObtentionListePartage


    
def decoupe_nombre_valable(partage):
    """Verifie que le nombre de perles par voleur est le meme"""
    
    compteur_1 = 0
    compteur_2 = 0
    for perle in range(len(partage)):
        if partage[perle] == 1:
            compteur_1 += 1
        else:
            compteur_2 += 1
    return compteur_1 == compteur_2


def decoupe_type_valable(collier, partage):
    """Verifie que le nombre de perles par type par voleur est le même"""

    for type in range(collier.nb_types):
        compteur_1 = 0
        compteur_2 = 0
        for perle in range(len(partage)):
            if collier.chaine[perle] == type:
                if partage[perle] == 1:
                    compteur_1 += 1
                else:
                    compteur_2 += 1
        if compteur_1 != compteur_2:
            return False
    return True


def nombres_coupes(partage):
    """Calcule le nombre de coupes pour un partage"""

    nb_coupes = 0
    for i in range(1, len(partage)):
        if partage[i - 1] != partage[i]:
            nb_coupes += 1
    return nb_coupes


def methode_naive_1():
    """Calcule un partage equitable par methode naive"""
    
    collier = Collier.Collier()
    type_demande = ' '
    nb_perles = 1
    type_de_generation = ' '

    while (type_demande != "oui" and type_demande !="non"):
        str_demande = "Voulez-vous importer un fichier ? \n "
        type_demande = input(str_demande)

    if type_demande == "oui":
        name_fichier = input("Veuillez entrer le nom de votre fichier : \n")
        collier.collier_fichier(name_fichier)
        nb_perles = int(input("Rentrez votre nombre de perles : \n"))
        nb_types = int(input("Rentrez votre nombre de types : \n"))

    if type_demande == "non":
        while (int(nb_perles) % 2 != 0):
            nb_perles = int(input("Rentrez votre nombre de perles : \n"))
        nb_types = int(input("Rentrez votre nombr-e de types : \n"))
        while (nb_types > nb_perles / 2):
            nb_types = int(input("Rentrez votre nombre de types : \n"))
        while (type_de_generation != "aleatoire" and type_de_generation !="design"):
            type_de_generation = input("Taper 'aleatoire' si vous souhaitez un collier aleatoire et 'design' si vous souhaitez confectionner votre collier : \n")
        if type_de_generation == 'aleatoire':
            collier.collier_aleatoire(nb_types, nb_perles)
        if type_de_generation == 'design':
            collier.collier_choisi(nb_types, nb_perles)

    partage = [0]*nb_perles
    while (not decoupe_type_valable(collier, partage) or not decoupe_nombre_valable(partage) or nombres_coupes(partage) > nb_types):
        for i in range(nb_perles):
            partage[i] = 1 - 2 * Collier.Outils.random.randint(0, 1) 
    print(partage)
    print(' ')
    print(collier.chaine)
        
        