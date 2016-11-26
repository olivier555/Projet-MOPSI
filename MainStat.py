"""Programme principal"""

import Alternant
import Collier
import Vecteur_Signe
import Simplexe
import copy
import Lambda
import time
import statistics


def main_stat():


    tex = []
    
    nb_perles = int(input("Veuillez rentrer votre nombre de perles : \n"))
    #nb_types = int(input("Veuillez rentrer votre nombre de types : \n"))
    nb_essai = 200
    
    moyenne = []
    ecart_type = []
    
    for nb_types in range(2, int(1 + nb_perles / 2)):
    
        tex = []
        for i in range(nb_essai):
            #t = time.time()
            
            collier = Collier.Collier()
            collier.collier_aleatoire(nb_types, nb_perles)
            #print("collier : ", collier.liste)
        
            vecteur_signe_initial = Vecteur_Signe.creer_vecteur_signe([-1] + [0] * (nb_perles - 1))
            simplexe_initial = Simplexe.creer_simplexe([vecteur_signe_initial])
        
            liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe_initial, collier)
            #print("simplexe 2 : ", liste_noeuds_voisins[0])
            simplexe = liste_noeuds_voisins[0]
            liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
            
            nb_iter = 2
        
            while len(liste_noeuds_voisins) == 2 and Lambda.fonction_lambda(simplexe.chaine[0], collier) != 0:
                if simplexe_initial == liste_noeuds_voisins[0]:
                    simplexe_initial = copy.deepcopy(simplexe)
                    simplexe = copy.deepcopy(liste_noeuds_voisins[1])
                else:
                    simplexe_initial = copy.deepcopy(simplexe)
                    simplexe = copy.deepcopy(liste_noeuds_voisins[0])
                #print("\n simplexe choisi : ",simplexe)
                liste_noeuds_voisins = Alternant.noeuds_voisins(simplexe, collier)
                nb_iter += 1
                #print("voisins : ", liste_noeuds_voisins)
        
            print(nb_iter)
            tex.append(nb_iter)
            """print("\n simplexe final : ", simplexe)
            print("collier : ", collier.liste)
            print(Lambda.fonction_lambda_liste(simplexe.chaine,  collier))"""
        moyenne.append(statistics.mean(tex))
        ecart_type.append(statistics.stdev(tex))
        print(statistics.mean(tex))
        print(statistics.stdev(tex), "\n")
            
        #print("temps moyen : ", sum(tex) / float(len(tex)))
    print("moyenne : ", moyenne)
    print("ecart-type : ", ecart_type) 
    
    