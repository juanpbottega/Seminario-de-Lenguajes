import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prueba")

imagen = pygame.image.load("Imagenes\ovni.png")
posX = 270
posY = 300

velocidad = 5
blanco = (255, 255, 255)

while True:
    ventana.fill(blanco)
    ventana.blit(imagen,(posX, posY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                    posX -= velocidad
            elif event.key == K_RIGHT:
                    posX += velocidad
                
    pygame.display.update()
