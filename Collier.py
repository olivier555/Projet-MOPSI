import Outils

class Collier:
    
    def __init__(self):
        
         self.liste = []
         self.nb_types = 0
         self.nb_perles = 0
         
    def collier_aleatoire(self, nb_types, nb_perles):
        
        if nb_types == 1:
            self.liste = [0] * nb_perles
            self.nb_types = nb_types
            self.nb_perles = nb_perles
            self.repartition = [nb_perles]
        
        else:
        
            self.repartition = Outils.repartition_perle(nb_perles, nb_types)
            for i in range(nb_types):
                self.liste += [i]*self.repartition[i]
            Outils.random.shuffle(self.liste)
            self.nb_types = nb_types
            self.nb_perles = nb_perles
        
    def collier_choisi(self, nb_types, nb_perles):

        
        repartition = Outils.repartition_perle(nb_perles, nb_types)
        print("Voici la repartition de vos types de perles : \n")
        for i in range(len(repartition)):
            str_reponse = "Type " + str(i) + " : " + str(repartition[i]) + " perles \n"
            print (str_reponse)
        print("Veuillez entrer la forme du collier que vous souhaitez avoir : \n")
        for i in range(nb_perles):
            str_demande = "Veuillez entre votre " + str(i+1) + "eme perle : \n"
            perle = input(str_demande)
            self.liste += perle
    
    def collier_fichier(self, fichier):
        
        monFichier = open(fichier, "r")
        contenu = monFichier.read()
        liste_collier = contenu.split(",")
        for i in range(len(liste_collier)):
            self.liste += liste_collier[i]
       
       