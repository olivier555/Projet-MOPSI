"""Programme principal"""

import time
import Alternant
import Collier
import Vecteur_Signe
import Simplexe
import copy
import Lambda

def creation_simplexes_initiaux(nb_types, nb_perles, collier):
    """Creation des 2 simplexes initiaux la ou le chamin commence
    a dependre du collier"""

    chaine = []
    for i in range(1,nb_perles-nb_types):
        liste = [0]*(nb_perles-nb_types-1-i) + [-1]*i + [0]*(nb_types+1)
        vecteur_signe = Vecteur_Signe.creer_vecteur_signe(liste, collier)
        chaine.append(vecteur_signe)
    simplexe_0 = Simplexe.creer_simplexe(chaine)
    vecteur_signe_1 = Vecteur_Signe.creer_vecteur_signe([-1]*(nb_perles-nb_types) + [0]*nb_types, collier)
    chaine_1 = copy.deepcopy(chaine)
    chaine_1.append(vecteur_signe_1)
    simplexe_1 = Simplexe.creer_simplexe(chaine_1)
    return [simplexe_0, simplexe_1]


def main_simplexe_initial(nb_perles, nb_types):


    collier = Collier.Collier()
    collier.collier_aleatoire(nb_types, nb_perles)

    simplexes_initiaux =  creation_simplexes_initiaux(nb_types, nb_perles, collier)
    simplexe_initial = simplexes_initiaux[0]
    simplexe = simplexes_initiaux[1]
    #print("simplexe initial : ", simplexe_initial)
    #print("simplexe initial 2 : ", simplexe)
    
    liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
    
    nb_iter = 0

    bool = True
    while len(liste_noeuds_voisins) == 2 and bool:
        #print(Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier))
        #t = time.time()
        if simplexe_initial == liste_noeuds_voisins[0]:
            simplexe_initial = copy.deepcopy(simplexe)
            simplexe = copy.deepcopy(liste_noeuds_voisins[1])
        else:
            simplexe_initial = copy.deepcopy(simplexe)
            simplexe = copy.deepcopy(liste_noeuds_voisins[0])
        #print("temps de comparaison : ",time.time() - t)
        #print("\n simplexe choisi : ",simplexe)
        #print([vecteur_signe.nombre_zeros for vecteur_signe in simplexe.chaine])
        #t = time.time()
        liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
        #print("temps de recherche voisin : ",time.time() - t)
        nb_iter += 1
        bool = 0 not in [vec.valeur_lambda for vec in simplexe.chaine]

    #print(Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier))
    #print("\n simplexe precedent : ", simplexe_initial)
    print("\n simplexe final : ", simplexe)
    print("collier : ", collier.liste)
    print("nombre d'iterations : ", nb_iter)
    return nb_iter