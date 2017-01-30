"""Module permettant de creer la base de donnees"""

import sqlite3


game = sqlite3.connect("game.db")

cursor = game.cursor()

cursor.execute("""DROP TABLE IF EXISTS necklace""")
cursor.execute("""DROP TABLE IF EXISTS level""")
cursor.execute("""DROP TABLE IF EXISTS score""")


creation_necklace = """
CREATE TABLE necklace (
number INTEGER PRIMARY KEY,
rouge INTEGER,
orange INTEGER,
jaune INTEGER,
vert INTEGER,
bleu INTEGER,
violet INTEGER,
marron INTEGER,
rose INTEGER,
blanc INTEGER);"""

creation_level = """
CREATE TABLE level (
time INTEGER,
number INTEGER, FOREIGN KEY(number) REFERENCES necklace(number));"""

creation_score = """
CREATE TABLE score(
open BOOL,
stars INTEGER,
number INTEGER, FOREIGN KEY(number) REFERENCES level(number));"""

game.execute(creation_level)
game.execute(creation_score)
game.execute(creation_necklace)
game.commit()

necklace_data = [ (1, 2, 2, 0, 0, 0, 0, 0, 0, 0), (2, 2, 4, 0, 0, 0, 0, 0, 0, 0), (3, 2, 2, 2, 0, 0, 0, 0, 0, 0), (4, 2, 2, 4, 0, 0, 0, 0, 0, 0), (5, 2, 4, 4, 0, 0, 0, 0, 0, 0), (6, 2, 2, 2, 2, 0, 0, 0, 0, 0), (7, 2, 2, 2, 4, 0, 0, 0, 0, 0), (8, 2, 4, 4, 4, 0, 0, 0, 0, 0), (9, 2, 2, 2, 2, 2, 0, 0, 0, 0), (10, 2, 2, 2, 2, 4, 0, 0, 0, 0), (11, 2, 4, 4, 4, 4, 0, 0, 0, 0), (12, 2, 2, 2, 2, 2, 2, 0, 0, 0)]

cursor.executemany("""
INSERT INTO necklace(number, rouge, orange, jaune, vert, bleu, violet, marron, rose, blanc)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", necklace_data)

level_data = [ (10, 1), (10, 2), (15, 3), (15, 4), (15, 5), (20, 6), (20, 7), (20, 8), (25, 9), (25, 10), (25, 11), (30, 12) ]

cursor.executemany("""
INSERT INTO level(time, number)
    VALUES(?, ?)""", level_data)

score_data = [ ("TRUE", 0, 1), ("FALSE", 0, 2), ("FALSE", 0, 3), ("FALSE", 0, 4), ("FALSE", 0, 5), ("FALSE", 0, 6), ("FALSE", 0, 7), ("FALSE", 0, 8), ("FALSE", 0, 9), ("FALSE", 0, 10), ("FALSE", 0, 11), ("FALSE", 0, 12) ]

cursor.executemany("""
INSERT INTO score(open, stars, number)
    VALUES(?, ?, ?)""", score_data)

game.commit() 
