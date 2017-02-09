"""Module principale permettant de lancer le programme"""

## Modules importes ##

import Menu
import Constant

import pygame
import sqlite3

## Main ##

GAME = sqlite3.connect("game.db")
CURSOR = GAME.cursor()

def main():
    """Lance le jeu et gere l'actualisation des scores dans le base de 
    donnees"""

    list_repartition = []
    list_time = []
    list_score = []


    CURSOR.execute("""SELECT red, orange, yellow, green, blue, violet, brown, 
    pink, white FROM necklace""")

    rows = CURSOR.fetchall()

    for row in rows:

        list_repartition.append(row)


    CURSOR.execute("""SELECT time FROM level""")
    rows = CURSOR.fetchall()

    for row in rows:

        list_time.append(row[0])


    CURSOR.execute("""SELECT stars FROM score""")
    rows = CURSOR.fetchall()

    for row in rows:
        list_score.append(row[0])


    CURSOR.execute("""SELECT number FROM score WHERE open = "FALSE" """)
    row = CURSOR.fetchone() 
    actual_level = row[0] - 1


    pygame.init()
    window = pygame.display.set_mode((Constant.WINDOW_SIZE, 
    Constant.WINDOW_SIZE))
    
    menu = Menu.Menu(actual_level, window, list_repartition, list_time, 
    list_score)

    var = menu.play()
    
    
    for lev in range(actual_level + 1, var[0] + 1):

        CURSOR.execute("""UPDATE score SET open = "TRUE" WHERE number = ? """, 
        (lev,))
    
    for star in range(len(var[1])):

        CURSOR.execute("""UPDATE score SET stars = ? WHERE number = ? """, 
        (var[1][star], star + 1,))

    GAME.commit()
