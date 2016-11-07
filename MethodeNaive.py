"""Fichier permettant de trouver tous les partages valables
d'un collier donné"""

import Collier

def ajout_element(T, e):
    liste_ajout_element = [T[i]+[e] for i in range(len(T))]
    return liste_ajout_element
    
    
def ensemble_partie(S):

    if S == []:
        return [[]]
    T = S
    e = T.pop()
    PT = ensemble_partie(T)
    return ajout_element(PT, e) + PT
    
def selection_partie(PS, taille):
    return [e for e in PS if len(e) == taille]
  
    
    
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
    partage = [0]*nb_perles
    """while (not decoupe_type_valable(collier, partage) or not decoupe_nombre_valable(partage) or nb_coupes(partage) > nb_types):
        for i in range(nb_perles):
            partage[i] = 1 - 2 * Collier.Outils.random.randint(0, 1) """
    
    parties = ensemble_partie([i for i in range(nb_perles)])
    parties_bonne_taille = selection_partie(parties,int(nb_perles/2))
    print(len(parties_bonne_taille))
    ensemble_partage = []
    for m in parties_bonne_taille:
        partage = []
        for i in range(nb_perles):
            if i in m:
                partage.append(1)
            else:
                partage.append(-1)
        ensemble_partage.append(partage)
    partage_coupes_valable = [partage for partage in ensemble_partage if nb_coupes(partage) <= nb_types]
    partage_valable = [partage for partage in partage_coupes_valable if decoupe_type_valable(collier, partage)]
    liste_nombre_coupes = [nb_coupes(h) for h in partage_valable]
    print(len(liste_nombre_coupes))
    indice_minimum_coupes =  liste_nombre_coupes.index(min(liste_nombre_coupes))
    print(indice_minimum_coupes)
    print(liste_nombre_coupes)
    print("nombre de coupes : " + str(liste_nombre_coupes[indice_minimum_coupes]))
    print(partage_valable[indice_minimum_coupes])
    print(collier.chaine)
        
        