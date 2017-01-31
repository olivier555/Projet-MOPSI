import Niveau
import Menu
import pygame
import sqlite3

game = sqlite3.connect("game.db")

cursor = game.cursor()


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

    cursor.execute("""SELECT rouge, orange, jaune, vert, bleu, violet, marron, rose, blanc FROM necklace""")
    rows = cursor.fetchall()
    for row in rows:
        liste_repartition.append(row)


    cursor.execute("""SELECT time FROM level""")
    rows = cursor.fetchall()
    for row in rows:
        liste_temps.append(row[0])

    cursor.execute("""SELECT stars FROM score""")
    rows = cursor.fetchall()
    for row in rows:
        liste_score.append(row[0])

    cursor.execute("""SELECT number FROM score WHERE open = "FALSE" """)
    row = cursor.fetchone() 
    actual_level = row[0] - 1


    pygame.init()
    fenetre = pygame.display.set_mode((800, 600))
    
    menu = Menu.Menu(actual_level, fenetre, liste_repartition, liste_temps, liste_score)
    t = menu.play()
    
    
    for lev in range(actual_level + 1, t[0] + 1):
        cursor.execute("""UPDATE score SET open = "TRUE" WHERE number = ? """, (lev,))
    
    for star in range(len(t[1])):
        cursor.execute("""UPDATE score SET stars = ? WHERE number = ? """, (t[1][star], star,))
    
    game.commit()
