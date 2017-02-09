"""Module contenant les fonctions outils necessaires au bon fonctionnement du 
jeu"""

## Modules importes ##

import random
import Necklace

## Fonctions outils ##

def random_repartition_pearl(nb_pearl, nb_type):
    """Renvoit un nombre de perles aleatoire par type repondant
    aux donnees du problemes"""
        
    random_cut = []
    half = int(nb_pearl / 2)
    
    for i in range (nb_type - 1):

        random_int = random.randint(1, half - 1)

        while (random_int in random_cut):

            random_int = random.randint(1, half - 1)

        random_cut.append(random_int)

    random_cut.sort()
    repartition = []
    repartition.append(2 * random_cut[0])

    for i in range (nb_type - 2):

        repartition.append(2 * (random_cut[i + 1] - random_cut[i]))

    repartition.append(2 * (half - random_cut[nb_type - 2]))

    return repartition


def valid_cut_type(necklace, sharing):
    """Renvoit sur la decoupe est valable c'est-a-dire que chaque part a le meme
     nombre de perles par type"""

    for types in range(necklace.nb_type):

        count_1 = 0
        count_2 = 0

        for pearl in range(len(sharing)):

            if necklace.list[pearl] == types:

                if sharing[pearl] == 1:

                    count_1 += 1

                else:

                    count_2 += 1

        if count_1 != count_2:

            return False

    return True

