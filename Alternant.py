"""fichier contenant les fonctions permettant de trouver
si des listes sont alternantes"""

import Simplexe
import Lambda
import copy

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


def alternant_simplexe(simplexe, collier):
    """Renvoit un entier caracterisant l'alternance du simplexe"""

    liste_lambda = Lambda.fonction_lambda_liste(simplexe.chaine, collier)
    if liste_lambda != [0]:
        return alternant(liste_lambda)


def etre_noeud(simplexe, collier):
    """Booleen indiquant si simplexe est bien un noeud ie si il
    verifie l'une des 3 conditions"""
    
    alternant = alternant_simplexe(simplexe, collier)
    dimension = simplexe.dimension
    carrier_hemisphere = simplexe.carrier_hemisphere

    if dimension == carrier_hemisphere[0] - 1 and alternant == carrier_hemisphere[1]:
        return True

    if dimension == carrier_hemisphere[0] and alternant == 0:
        for facette in simplexe.liste_facette():
            if alternant_simplexe(facette, collier) == carrier_hemisphere[1]:
                return True

    if dimension == carrier_hemisphere[0] and alternant != 0:
        return True

    return False


def noeuds_voisins(simplexe, collier):

    alternant = alternant_simplexe(simplexe, collier)
    dimension = simplexe.dimension
    carrier_hemisphere = simplexe.carrier_hemisphere
    
    
    
    #print("simplexe : ", simplexe)
    #print("alternant : ", alternant)
    #print("dimension : ", dimension)
    #print("carrier hemisphere : i", carrier_hemisphere[0]," et epsilon ", carrier_hemisphere[1])
    
    liste_lambda = Lambda.fonction_lambda_liste(simplexe.chaine, collier)
    #print("liste_lambda : ")
    #print(liste_lambda)
    if 0 in liste_lambda:
        indice = liste_lambda.index(0)
        simplexe_final = Simplexe.creer_simplexe([simplexe.chaine[indice]])
        return [simplexe_final, simplexe]

    liste_voisins = []

    if dimension == carrier_hemisphere[0] and dimension > 0:
        for facette in simplexe.liste_facette():
            #print("facette : ", facette)
            #print("carrier hemisphere : ", facette.carrier_hemisphere)
            if etre_noeud(facette, collier):
                if alternant_simplexe(facette, collier) == carrier_hemisphere[1]:
                    liste_voisins.append(facette)

    if alternant != 0:
        if dimension == carrier_hemisphere[0]:
            chaine_copie = copy.deepcopy(simplexe.chaine)
            nouveau_vecteur_signe = simplexe.chaine[dimension].ajout_copie(alternant, dimension +1)
            chaine_copie.append(nouveau_vecteur_signe)
            supfacette = Simplexe.creer_simplexe(chaine_copie)
            liste_voisins.append(supfacette)
        else:
            chaine_copie1 = copy.deepcopy(simplexe.chaine)
            chaine_copie2 = copy.deepcopy(simplexe.chaine)
            if simplexe.chaine[0].liste.count(0) != len(simplexe.chaine[0].liste) - 1:
                nouveau_vecteur_signe1 = copy.deepcopy(simplexe.chaine[0])
                nouveau_vecteur_signe2 = copy.deepcopy(simplexe.chaine[0])
                liste_indice_difference = [j for j in range(len(simplexe.chaine[0].liste)) if simplexe.chaine[0].liste[j] != 0]
                nouveau_vecteur_signe1.liste[liste_indice_difference[0]] = 0
                nouveau_vecteur_signe2.liste[liste_indice_difference[1]] = 0
                nouveau_vecteur_signe1.trouver_carrier_hemisphere()
                nouveau_vecteur_signe2.trouver_carrier_hemisphere()
                chaine_copie1.append(nouveau_vecteur_signe1)
                chaine_copie2.append(nouveau_vecteur_signe2)
                supfacette1 = Simplexe.creer_simplexe(chaine_copie1)
                supfacette2 = Simplexe.creer_simplexe(chaine_copie2)
                liste_voisins.append(supfacette1)
                liste_voisins.append(supfacette2)
            if  simplexe.chaine[dimension].liste.count(0) == (collier.nb_perles -carrier_hemisphere[0]):
                nouveau_vecteur_signe1 = copy.deepcopy(simplexe.chaine[dimension])
                nouveau_vecteur_signe2 = copy.deepcopy(simplexe.chaine[dimension])
                for indice in range(carrier_hemisphere[0] + 1 ):
                    if simplexe.chaine[dimension].liste[indice] == 0:
                        nouveau_vecteur_signe1.liste[indice] = 1
                        nouveau_vecteur_signe2.liste[indice] = -1
                        nouveau_vecteur_signe1.trouver_carrier_hemisphere()
                        nouveau_vecteur_signe2.trouver_carrier_hemisphere()
                        chaine_copie1.append(nouveau_vecteur_signe1)
                        chaine_copie2.append(nouveau_vecteur_signe2)
                        supfacette1 = Simplexe.creer_simplexe(chaine_copie1)
                        supfacette2 = Simplexe.creer_simplexe(chaine_copie2)
                        liste_voisins.append(supfacette1)
                        liste_voisins.append(supfacette2)
            for i in range(len(simplexe.chaine) - 1):
                if simplexe.chaine[i].liste.count(0) != simplexe.chaine[i+1].liste.count(0) + 1:
                    nouveau_vecteur_signe1 = copy.deepcopy(simplexe.chaine[i])
                    nouveau_vecteur_signe2 = copy.deepcopy(simplexe.chaine[i])
                    liste_indice_difference = [j for j in range(len(simplexe.chaine[i].liste)) if simplexe.chaine[i].liste[j] != simplexe.chaine[i+1].liste[j]]
                    nouveau_vecteur_signe1.liste[liste_indice_difference[0]] = simplexe.chaine[i+1].liste[liste_indice_difference[0]]
                    nouveau_vecteur_signe2.liste[liste_indice_difference[1]] = simplexe.chaine[i+1].liste[liste_indice_difference[1]]
                    nouveau_vecteur_signe1.trouver_carrier_hemisphere()
                    nouveau_vecteur_signe2.trouver_carrier_hemisphere()
                    chaine_copie1.append(nouveau_vecteur_signe1)
                    chaine_copie2.append(nouveau_vecteur_signe2)
                    supfacette1 = Simplexe.creer_simplexe(chaine_copie1)
                    supfacette2 = Simplexe.creer_simplexe(chaine_copie2)
                    liste_voisins.append(supfacette1)
                    liste_voisins.append(supfacette2)

    #print("voisins : ", liste_voisins)
    return liste_voisins
    