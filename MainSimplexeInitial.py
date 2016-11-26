"""Programme principal"""

import Alternant
import Collier
import Vecteur_Signe
import Simplexe
import copy
import Lambda

def creation_simplexes_initiaux(nb_types, nb_perles):
    """Creation des 2 simplexes initiaux la ou le chamin commence
    a dependre du collier"""

    chaine = []
    for i in range(1,nb_perles-nb_types):
        liste = [0]*(nb_perles-nb_types-1-i) + [-1]*i + [0]*(nb_types+1)
        vecteur_signe = Vecteur_Signe.creer_vecteur_signe(liste)
        chaine.append(vecteur_signe)
    simplexe_0 = Simplexe.creer_simplexe(chaine)
    #print(simplexe_0)
    vecteur_signe_1 = Vecteur_Signe.creer_vecteur_signe([-1]*(nb_perles-nb_types) + [0]*nb_types)
    chaine_1 = copy.deepcopy(chaine)
    chaine_1.append(vecteur_signe_1)
    #print(chaine_1)
    simplexe_1 = Simplexe.creer_simplexe(chaine_1)
    #print(simplexe_1)
    return [simplexe_0, simplexe_1]


def main_simplexe_initial():


    nb_perles = 24
    nb_types = 1
    collier = Collier.Collier()
    collier.collier_aleatoire(nb_types, nb_perles)
    #print("collier : ", collier.liste)

    simplexes_initiaux =  creation_simplexes_initiaux(nb_types, nb_perles)
    simplexe_initial = simplexes_initiaux[0]
    simplexe = simplexes_initiaux[1]
    #print("simplexe initial : ", simplexe_initial)
    #print("simplexe initial 2 : ", simplexe)
    
    liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
    
    nb_iter = 0

    while len(liste_noeuds_voisins) == 2 and Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier) != 0:
        #print(Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier))
        if simplexe_initial == liste_noeuds_voisins[0]:
            simplexe_initial = copy.deepcopy(simplexe)
            simplexe = copy.deepcopy(liste_noeuds_voisins[1])
        else:
            simplexe_initial = copy.deepcopy(simplexe)
            simplexe = copy.deepcopy(liste_noeuds_voisins[0])
        #print("\n simplexe choisi : ",simplexe)
        liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
        nb_iter += 1

    #print(Lambda.fonction_lambda(simplexe.chaine[simplexe.dimension], collier))
    #print("\n simplexe precedent : ", simplexe_initial)
    print("\n simplexe final : ", simplexe)
    print("collier : ", collier.liste)
    print("nombre d'iterations : ", nb_iter)