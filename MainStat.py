"""Programme principal"""

import Alternant
import Collier
import Vecteur_Signe
import Simplexe
import copy
import Lambda
import time
import statistics
import MainSimplexeInitial


def main_stat():


    tex = []
    
    #nb_perles = int(input("Veuillez rentrer votre nombre de perles : \n"))
    #nb_types = int(input("Veuillez rentrer votre nombre de types : \n"))
    nb_essai = 30
    
    moyenne = []
    ecart_type = []
    
    for nb_types in range(10, 12):
    
        tex = []
        for i in range(nb_essai):
            t = time.time()
            nb_perles = 4 * nb_types 
                
            collier = Collier.Collier()
            collier.collier_aleatoire(nb_types, nb_perles)
        
            simplexes_initiaux =  MainSimplexeInitial.creation_simplexes_initiaux(nb_types, nb_perles, collier)
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
        
            print(nb_iter)
            tex.append(nb_iter)
            """print("\n simplexe final : ", simplexe)
            print("collier : ", collier.liste)
            print(Lambda.fonction_lambda_liste(simplexe.chaine,  collier))"""
        moyenne.append(statistics.mean(tex))
        ecart_type.append(statistics.stdev(tex))
        print(statistics.mean(tex))
        print(statistics.stdev(tex), "\n")
            
        print("temps moyen : ", sum(tex) / float(len(tex)))
    print("moyenne : ", moyenne)
    print("ecart-type : ", ecart_type) 
    
    