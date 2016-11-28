import pygame
import sys
import math
import Collier

TAILLE = 600
ROUGE = (255,0,0)
VERT = (0,255,0)
BLEU = (0,0,255)
BLEU_FONCE = (0,0,128)
BLANC = (255,255,255)
NOIR = (0,0,0)
ROSE = (255,200,200)
LISTE_COULEURS = [ROUGE, VERT, BLEU, BLEU_FONCE, ROSE]

collier = Collier.Collier()
collier.collier_aleatoire(3, 10)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((TAILLE, TAILLE))
DISPLAYSURF.fill(BLANC)
pygame.display.set_caption('Hello World!')
#pygame.draw.rect(DISPLAYSURF, BLUE, (200, 150, 100, 50))
t = math.pi
centre_cercle = [int(TAILLE/2), 200]
liste_positions = []
for i in range(collier.nb_perles):
    liste_positions.append((int(centre_cercle[0] + 200 * math.cos(t)), int(centre_cercle[1] - 200 * math.sin(t))))
    t += math.pi / (collier.nb_perles - 1)
pygame.draw.lines(DISPLAYSURF, NOIR, False, liste_positions, 4)
for i in range(collier.nb_perles):
    pygame.draw.circle(DISPLAYSURF, LISTE_COULEURS[collier.liste[i]], liste_positions[i], 20)

pygame.mouse.set_visible(False)
cursor_picture = pygame.image.load("ciseaux.png").convert_alpha()
cursor_picture = pygame.transform.scale(cursor_picture,(15, 30))

while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            DISPLAYSURF.fill(BLANC)
            pygame.draw.lines(DISPLAYSURF, NOIR, False, liste_positions, 4)
            for i in range(collier.nb_perles):
                pygame.draw.circle(DISPLAYSURF, LISTE_COULEURS[collier.liste[i]], liste_positions[i], 20)
            
    DISPLAYSURF.blit(cursor_picture, pygame.mouse.get_pos())
    pygame.display.update()