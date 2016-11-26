"""Programme principal"""

import Alternant
import Collier
import Vecteur_Signe
import Simplexe
import copy
import Lambda

def main_test_constant():


    nb_perles = 16
    nb_types = 1
    collier = Collier.Collier()
    collier.collier_aleatoire(nb_types, nb_perles)
    print("collier : ", collier.liste)

    vecteur_signe_initial = Vecteur_Signe.creer_vecteur_signe([-1]+[0]*(nb_perles - 1))
    simplexe_initial = Simplexe.creer_simplexe([vecteur_signe_initial])

    liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe_initial, collier)
    #print("simplexe 2 : ", liste_noeuds_voisins[0])
    simplexe = liste_noeuds_voisins[0]
    liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
    
    compteur = 0

    while len(liste_noeuds_voisins) == 2 and abs(Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier)) > nb_types:
        #print(Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier))
        if simplexe_initial == liste_noeuds_voisins[0]:
            simplexe_initial = copy.deepcopy(simplexe)
            simplexe = copy.deepcopy(liste_noeuds_voisins[1])
        else:
            simplexe_initial = copy.deepcopy(simplexe)
            simplexe = copy.deepcopy(liste_noeuds_voisins[0])
        print("\n simplexe choisi : ",simplexe)
        liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
        compteur += 1

    print(compteur)
    print("\n simplexe precedent : ", simplexe_initial)
    print("\n simplexe final : ", simplexe)
    print("collier : ", collier.liste)