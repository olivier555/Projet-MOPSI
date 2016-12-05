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
            
    def collier_aleatoire_jeu(self, nb_types, nb_perles):
        
        if nb_types == 1:
            self.liste = [0] * nb_perles
            self.nb_types = nb_types
            self.nb_perles = nb_perles
            self.repartition = [nb_perles]
        
        else:
        
            self.repartition = Outils.repartition_aleatoire_perle(nb_perles, nb_types)
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
        liste_collier = contenu.split("\n")
        caracteristique = liste_collier[0].split(' ')
        self.nb_types = int(caracteristique[0])
        self.nb_perles = int(caracteristique[2]) * int(caracteristique[1]) * int(caracteristique[0])
        print(len(liste_collier))
        liste_perles = liste_collier[1].split(' ')
        print(len(liste_perles))
        liste = []
        for i in range(self.nb_perles):
            liste.append(liste_perles[i])
        self.liste = liste
       
       