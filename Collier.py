import Outils

class Collier:
    
    def __init__(self):
        
         self.chaine = []
         self.nb_types = 0
         self.nb_perles = 0
         
    def collier_aleatoire(self, nb_types, nb_perles):
        
        self.repartition = Outils.repartition_perle(nb_perles, nb_types)
        for i in range(nb_types):
            self.chaine += [i]*self.repartition[i]
        Outils.random.shuffle(self.chaine)
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
            self.chaine += perle
    
    def collier_fichier(self, fichier):
        
        monFichier = open(fichier, "r")
        contenu = monFichier.read()
        chaine_collier = contenu.split(",")
        for i in range(len(chaine_collier)):
            self.chaine += chaine_collier[i]
       
       