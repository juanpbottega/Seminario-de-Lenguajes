import pygame, sys
from pygame.locals import *

ancho = 800
alto = 600

class Personajes(pygame.sprite.Sprite):
        """Clase de los personajes"""
        vida = 100
        velocidad = 3
        direccion = 'N' #Direcciones: Norte(N), Sur(S), Este(E), Oeste(O)
        
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.ImagenPersonaje = pygame.image.load("Imagenes\Personaje.png")
                self.rect = self.ImagenPersonaje.get_rect()
                self.rect.centerx = ancho/2
                self.rect.centery = alto - 50
                self.vida = 100
                self.velocidad = 3
                self.listaDisparo = []
                self.direccion = 'N' #Direcciones: Norte(N), Sur(S), Este(E), Oeste(O)
        
        def dibujar(self, superficie):
                superficie.blit(self.ImagenPersonaje, self.rect)

        def moverIzquierda(self):
                self.rect.centerx -= self.velocidad
                self.__movimiento()
                self.direccion = 'O'
                #limite de pantalla()

        def moverDerecha(self):
                self.rect.centerx += self.velocidad
                self.__movimiento()
                self.direccion = 'E'
                #limite de pantalla()
        def moverArriba(self):
                self.rect.centery -= self.velocidad
                self.__movimiento()
                self.direccion = 'N'
		#limite pantalla()
        def moverAbajo(self):
                self.rect.centery += self.velocidad
                self.__movimiento()
                self.direccion = 'S'
                #limite patalla()
                
        def __movimiento(self):
                if self.sigueVivo():
                    if self.rect.bottom > alto:
                        self.rect.bottom = alto
                    elif self.rect.top < 0:
                        self.rect.top = 0
                    elif self.rect.left < 0:
                        self.rect.left = 0
                    elif self.rect.right > ancho:
                        self.rect.right = ancho
                
        def sigueVivo(self):
                if self.vida > 0:
                        return True
                else:
                        return False
        def disparar(self, superficie):
                disparo = Disparo(self.rect.centerx, self.rect.centery, self.direccion)
                self.listaDisparo.append(disparo)

                
class Disparo(pygame.sprite.Sprite):
        """Clase del disparo"""
        
        def __init__(self, posX, posY, direccion):
                pygame.sprite.Sprite.__init__(self)
                self.imagenDisparo = pygame.image.load("Imagenes\Disparo.png")
                self.rect = self.imagenDisparo.get_rect()
                self.rect.centerx = posX
                self.rect.centery = posY
                self.velocidad = 5
                self.direccion = direccion
                
        def trayectoria(self):
                if self.direccion == 'N':
                        self.rect.centery -= self.velocidad
                elif self.direccion == 'S':
                        self.rect.centery += self.velocidad
                elif self.direccion == 'E':
                        self.rect.centerx += self.velocidad
                elif self.direccion == 'O':
                        self.rect.centerx -= self.velocidad
                
        def dibujar(self, superficie):
                superficie.blit(self.imagenDisparo, self.rect)

        
"""""""""""""""""""""""""""MAIN"""""""""""""""""""""""""""""""""        
pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")
jugador = Personajes()
pygame.key.set_repeat(True)
imagenFondo = pygame.image.load("Imagenes\Fondo.jpg")
ventana.blit(imagenFondo, (0, 0))

while True:
        for evento in pygame.event.get():
                if evento.type == QUIT or not jugador.sigueVivo(): #agregar la salida al menu y guardado de score
                        pygame.quit()
                        sys.exit()
                if evento.type == pygame.KEYDOWN:
                        if evento.key == K_LEFT:
                                jugador.moverIzquierda()
                        elif evento.key == K_RIGHT:
                                jugador.moverDerecha()
                        elif evento.key == K_UP:
                                jugador.moverArriba()
                        elif evento.key == K_DOWN:
                                jugador.moverAbajo()
                        elif evento.key == K_SPACE:
                                pygame.key.set_repeat(False)
                                jugador.disparar(ventana)
                                pygame.key.set_repeat(True)
        ventana.blit(imagenFondo, (0, 0))
        jugador.dibujar(ventana)
        if len(jugador.listaDisparo) > 0: #aca recorro la lista de disparos pendientes
                for x in jugador.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.top < -20:
                                jugador.listaDisparo.remove(x)
                        elif x.rect.bottom > alto+20:
                                jugador.listaDisparo.remove(x)
                        elif x.rect.left < -20:
                                jugador.listaDisparo.remove(x)
                        elif x.rect.right > ancho+20:
                                jugador.listaDisparo.remove(x)

        pygame.display.update()
        
