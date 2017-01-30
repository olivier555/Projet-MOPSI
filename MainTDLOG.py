import Niveau
import Menu
import pygame
import Score

import sqlite3





def jouer_menu(n, fenetre, liste_repartition, liste_temps):

    menu = Menu.Menu(n, fenetre)
    menu.game_intro()
    jouer_niveau(menu.sortie, fenetre, liste_repartition, liste_temps)

def jouer_niveau(k, fenetre, liste_repartition, liste_temps):

    niveau = Niveau.Niveau(fenetre, liste_repartion[menu.sortie], liste_temps[menu.sortie])
    entier = niveau.jouer()
    if entier == 1:
        jouer_menu(k, fenetre, liste_repartion, liste_temps)
    if entier == 2:
        jouer_niveau(k, fenetre, liste_repartition, liste_temps)
    if entier == 3:
        jouer_niveau(k + 1, fenetre, liste_repartition, liste_temps)
    

def main():

    liste_repartition = []
    liste_temps = []
    liste_score = []
        
    
    Score.cursor.execute("""SELECT rouge, orange, jaune, vert, bleu, violet, marron, rose, blanc FROM necklace""")
    rows = Score.cursor.fetchall()
    for row in rows:
        liste_repartition.append(row)
    
    Score.cursor.execute("""SELECT time FROM level""")
    rows = Score.cursor.fetchall()
    for row in rows:
        liste_temps.append(row[0])
        
    Score.cursor.execute("""SELECT stars FROM score""")
    rows = Score.cursor.fetchall()
    for row in rows:
        liste_score.append(row[0])
        
    Score.cursor.execute("""SELECT number FROM score WHERE open = "FALSE" """)
    row = Score.cursor.fetchone() 
    actual_level = row[0]


    pygame.init()
    fenetre = pygame.display.set_mode((800, 600))
    
    t = Menu.Menu(actual_level, fenetre, liste_repartition, liste_temps)
    
    
    for level in range(actual_level, t + 1):
        Score.cursor.execute("""UPDATE score SET open = "TRUE" WHERE number = level """)
            
            
    
    