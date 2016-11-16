"""Fichier permettant de trouver tous les partages valables
d'un collier donné"""

## Modules importees


import Collier
import ObtentionListePartage


## Fonction outils de la methode naive


def decoupe_nombre_valable(partage):
    
    compteur_1 = 0
    compteur_2 = 0
    for perle in range(len(partage)):
        if partage[perle] == 1:
            compteur_1 += 1
        else:
            compteur_2 += 1
    return compteur_1 == compteur_2
        

def decoupe_type_valable(collier, partage):
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
    
def nb_coupes(partage):
    nb_coupes = 0
    for i in range(1, len(partage)):
        if partage[i - 1] != partage[i]:
            nb_coupes += 1
    return nb_coupes

def methode_naive():
    
    collier = Collier.Collier()
    nb_perles = int(input("Rentrez votre nombre de perles : \n"))
    nb_types = int(input("Rentrez votre nombre de types : \n"))
    collier.collier_aleatoire(nb_types, nb_perles)
    nb_coupe = 1
    demi = int(nb_perles/2)
    liste_partage = ObtentionListePartage.liste_partage(nb_perles)
    partage_coupes_valable = [partage for partage in liste_partage if nb_coupes(partage) <= nb_types]
    partage_valable = [partage for partage in partage_coupes_valable if decoupe_type_valable(collier, partage)]
    liste_nombre_coupes = [nb_coupes(h) for h in partage_valable]
    indice_minimum_coupes =  liste_nombre_coupes.index(min(liste_nombre_coupes))
    print(indice_minimum_coupes)
    print(liste_nombre_coupes)
    print("nombre de coupes : " + str(liste_nombre_coupes[indice_minimum_coupes]))
    print(partage_valable[indice_minimum_coupes])
    print(collier.chaine)
        
        