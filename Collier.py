
import Outils

class Collier:
    
    def __init__(self):
        
         self.chaine = []
         self.nb_types = 0
         self.nb_perles = 0
         
    def collier_aleatoire(self, nb_types,nb_perles):
        
        repartition = Outils.repartition_perle(nb_perles, nb_types)
        for i in range(nb_types):
            self.chaine += [i]*repartition[i]
        Outils.random.shuffle(self.chaine)
        self.nb_types = nb_types
        self.nb_perles = nb_perles
         