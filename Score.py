"""Module permettant de creer la base de donnees"""

## Module importe ##

import sqlite3

## Creation de la base de donnees ##

GAME = sqlite3.connect("GAME.db")
CURSOR = GAME.cursor()


CURSOR.execute("""DROP TABLE IF EXISTS necklace""")
CURSOR.execute("""DROP TABLE IF EXISTS level""")
CURSOR.execute("""DROP TABLE IF EXISTS score""")



CREATION_NECKLACE = """
CREATE TABLE necklace (
number INTEGER PRIMARY KEY,
red INTEGER,
orange INTEGER,
yellow INTEGER,
green INTEGER,
blue INTEGER,
violet INTEGER,
brown INTEGER,
pink INTEGER,
white INTEGER);"""

CREATION_LEVEL = """
CREATE TABLE level (
time INTEGER,
number INTEGER, FOREIGN KEY(number) REFERENCES necklace(number));"""

CREATION_SCORE = """
CREATE TABLE score(
open BOOL,
stars INTEGER,
number INTEGER, FOREIGN KEY(number) REFERENCES level(number));"""

GAME.execute(CREATION_LEVEL)
GAME.execute(CREATION_SCORE)
GAME.execute(CREATION_NECKLACE)
GAME.commit()


NECKLACE_DATA = [ (1, 2, 2, 0, 0, 0, 0, 0, 0, 0), (2, 2, 4, 0, 0, 0, 0, 0, 0, 0)
, (3, 2, 2, 2, 0, 0, 0, 0, 0, 0), (4, 2, 2, 4, 0, 0, 0, 0, 0, 0), 
(5, 2, 4, 4, 0, 0, 0, 0, 0, 0), (6, 2, 2, 2, 2, 0, 0, 0, 0, 0), 
(7, 2, 2, 2, 4, 0, 0, 0, 0, 0), (8, 2, 4, 4, 4, 0, 0, 0, 0, 0), 
(9, 2, 2, 2, 2, 2, 0, 0, 0, 0), (10, 2, 2, 2, 2, 4, 0, 0, 0, 0), 
(11, 2, 4, 4, 4, 4, 0, 0, 0, 0), (12, 2, 2, 2, 2, 2, 2, 0, 0, 0)]

CURSOR.executemany("""
INSERT INTO necklace(number, red, orange, yellow, green, blue, violet, brown, 
pink, white)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", NECKLACE_DATA)

LEVEL_DATA = [ (10, 1), (10, 2), (15, 3), (15, 4), (15, 5), (20, 6), (20, 7), 
(20, 8), (25, 9), (25, 10), (25, 11), (30, 12) ]

CURSOR.executemany("""
INSERT INTO level(time, number)
    VALUES(?, ?)""", LEVEL_DATA)

SCORE_DATA = [ ("TRUE", 0, 1), ("FALSE", 0, 2), ("FALSE", 0, 3), ("FALSE", 0, 4)
, ("FALSE", 0, 5), ("FALSE", 0, 6), ("FALSE", 0, 7), ("FALSE", 0, 8), 
("FALSE", 0, 9), ("FALSE", 0, 10), ("FALSE", 0, 11), ("FALSE", 0, 12) ]

CURSOR.executemany("""
INSERT INTO score(open, stars, number)
    VALUES(?, ?, ?)""", SCORE_DATA)

GAME.commit() 
