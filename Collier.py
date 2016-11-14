"""Module permettant de définir un collier"""

import Outils

class Collier:
    """Classe créant le collier"""
    
    def __init__(self):
        """Initialisation du collier"""

        self.chaine = []
        self.nb_types = 0
        self.nb_perles = 0


    def collier_aleatoire(self, nb_types, nb_perles):
        """Permet de construire un collier aleatoire"""

        repartition = Outils.repartition_perle(nb_perles, nb_types)
        for i in range(nb_types):
            self.chaine += [i]*repartition[i]
        Outils.random.shuffle(self.chaine)
        self.nb_types = nb_types
        self.nb_perles = nb_perles


    def collier_choisi(self, nb_types, nb_perles):
        """Permet de creer le collier souhaite"""

        repartition = Outils.repartition_perle(nb_perles, nb_types)
        print("Voici la répartition de vos types de perles : \n")
        for i in range(len(repartition)):
            str_reponse = 'Type ' + str(i) + ' : ' + str(repartition[i]) + ' \n'
            print (str_reponse)
        print("Veuillez entrer la forme du collier souhaité : \n")
        for i in range(nb_perles):
            str_demande = 'Veuillez entre votre ' + str(i+1) + 'ème perle : \n'
            perle = input(str_demande)
            self.chaine += perle


    def collier_fichier(self, fichier):
        """Permet d'importer un collier"""

        mon_fichier = open(fichier, "r")
        contenu = mon_fichier.read()
        chaine_collier = contenu.split(",")
        for i in range(len(chaine_collier)):
            self.chaine += chaine_collier[i]
       
       