import random

def repartition_aleatoire_perle(nb_perles, nb_types):
    """Renvoit un nombre de perles aleatoires par types repondant
    aux donnees du problemes"""
        
    decoupe_aleatoire = []
    moitie = int(nb_perles / 2)
    

    for i in range (nb_types - 1):
        int_aleatoire = random.randint(1, moitie-1)
        while (int_aleatoire in decoupe_aleatoire):
            int_aleatoire = random.randint(1, moitie-1)
        decoupe_aleatoire.append(int_aleatoire)
    decoupe_aleatoire.sort()
    repartition = []
    repartition.append(2 * decoupe_aleatoire[0])
    for i in range (nb_types - 2):
        repartition.append(2 * (decoupe_aleatoire[i+1] - decoupe_aleatoire[i]))
    repartition.append(2 * (moitie - decoupe_aleatoire[nb_types - 2]))
        
    return repartition


def repartition_perle(nb_perles, nb_types):
    """renvoit la repartition correspondant a nb_perles et nb_types
    avec le meme nombre de perle pour chaque type"""

    moitie = int(nb_perles / 2)
    
    valeur = moitie / nb_types
    if valeur - int(valeur) < 0.5:
        return [2 * int(valeur)] * (nb_types - 1) + [nb_perles -2 * int(valeur) * (nb_types - 1)]
    else:
        return [2 * (int(valeur) + 1)] * (nb_types - 1) + [nb_perles -2 * (int(valeur) + 1) * (nb_types - 1)]

