import pygame, sys
from pygame.locals import *
from random import randint

class Personajes(pygame.sprite.Sprite):
        """Clase de los personajes"""
        def cargarImagenes(self, imagenPersonaje):
                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Arriba/personaje_quieto_arriba.png"))
##                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Arriba/presonaje_caminando_arriba.png")
##                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Arriba/presonaje_caminando_arriba2.png")
                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Abajo/personaje_quieto_abajo.png"))
##                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Abajo/personaje_caminando_abajo.png"))
##                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Abajo/personaje_caminando2_abajo.png"))
                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Izquierda/personaje_quieto_izquierda.png"))
                imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Derecha/personaje_quieto_derecha.png"))
                
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.imagenPersonaje = []
                self.cargarImagenes(self.imagenPersonaje);
##                self.imagenPersonaje = pygame.image.load("Imagenes\Personaje.png")
                self.rect = self.imagenPersonaje[0].get_rect()
                self.rect.centerx = ancho/2
                self.rect.centery = alto - 50
                self.vida = 100
                self.maxVida=100
                self.velocidad = 5
                self.listaDisparo = []
                self.listaCuracion=[]
                self.ultimoDisparo = -1
                self.ultimaCuracion = -5
                self.ultimoDisparoLaser=-5
                self.direccion = 'N' #Direcciones: Norte(N), Sur(S), Este(E), Oeste(O)
                self.Fuente = pygame.font.SysFont("Arial", 30)
                self.cooldownCuracion=0
                self.cooldownLaser=0
        
        def dibujar(self, superficie):
                if self.direccion == 'N':
                        superficie.blit(self.imagenPersonaje[0], self.rect)
                elif self.direccion == 'S':
                        superficie.blit(self.imagenPersonaje[1], self.rect)
                elif self.direccion == 'O':
                        superficie.blit(self.imagenPersonaje[2], self.rect)
                elif self.direccion == 'E':
                        superficie.blit(self.imagenPersonaje[3], self.rect)
                self.mostrarVida(superficie)
                self.mostrarCoolCuracion(superficie)
                self.mostrarCoolLaser(superficie)
                
        def mostrarVida(self, superficie):
                texto_vida = self.Fuente.render("Vida: " + str(self.vida), 0, (255, 0, 0))
                superficie.blit(texto_vida, (5, 5))
                
        def mostrarCoolCuracion(self,superficie):
                texto_curacion = self.Fuente.render("Curacion: " + str(self.cooldownCuracion), 0, (255, 255, 0))
                superficie.blit(texto_curacion, (150, 5))
        def mostrarCoolLaser(self,superficie):
                texto_laser = self.Fuente.render("Laser: " + str(self.cooldownLaser), 0, (0, 255, 255))
                superficie.blit(texto_laser, (300, 5))
                
        def mover(self, izq, der, arr, aba):
                if izq:
                        self.moverIzquierda()
                elif der:
                        self.moverDerecha()
                elif arr:
                        self.moverArriba()
                elif aba:
                        self.moverAbajo()
           
        def moverIzquierda(self):
                self.rect.centerx -= self.velocidad
                self.__movimiento()
                self.direccion = 'O'

        def moverDerecha(self):
                self.rect.centerx += self.velocidad
                self.__movimiento()
                self.direccion = 'E'

        def moverArriba(self):
                self.rect.centery -= self.velocidad
                self.__movimiento()
                self.direccion = 'N'

        def moverAbajo(self):
                self.rect.centery += self.velocidad
                self.__movimiento()
                self.direccion = 'S'
                
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
                if self.vida > 1:
                        return True
                else:
                        return False
                
        def aumentarVida(self,tiempo):
                aumento = Curacion(self.rect.centerx,self.rect.centery,self.vida)
                if tiempo >= self.ultimaCuracion + aumento.tiempoReutilizacion:
                        self.listaCuracion.append(aumento)
                                
        def recibirDanio(self, danio):
                self.vida -= danio
                
        def disparar(self, tiempo): 
                disparo = Disparo(self.rect.centerx, self.rect.centery, self.direccion,10,6)
                
                if tiempo >= self.ultimoDisparo + disparo.tiempoReutilizacion:
                        self.listaDisparo.append(disparo)
                        self.ultimoDisparo = tiempo
                        
        def disparoLaser(self, tiempo):
                 disparo=Disparo(self.rect.centerx,self.rect.centery,self.direccion,2,16)
                 if tiempo >= self.ultimoDisparoLaser + disparo.tiempoReutilizacionLaser:
                        for d in range (1, 10):
                                otrodisparo=Disparo(self.rect.centerx,self.rect.centery,self.direccion,2, 5 + d )
                                self.listaDisparo.append(otrodisparo)
                        self.listaDisparo.append(disparo)
                        self.ultimoDisparoLaser = tiempo
                        self.cooldownLaser=disparo.tiempoReutilizacionLaser
        

                
class Curacion(pygame.sprite.Sprite):
        """Clase Curacion y aumento de Velocidad"""

        def __init__(self, posX, posY, vida):
                pygame.sprite.Sprite.__init__(self)
                self.imagenCuracion = pygame.image.load("Imagenes\Curacion.png")
                self.rect = self.imagenCuracion.get_rect()
                self.rect.centerx = posX
                self.rect.centery = posY
                self.cantAumento = 10
                self.cantAumentoVelocidad = 5
                self.duracionVelocidad = 3
                self.usado = False
                self.tiempoReutilizacion=5
              
        def aumentar(self, jugador, tiempo):
                jugador.vida+=self.cantAumento
                jugador.velocidad += self.cantAumentoVelocidad
                jugador.ultimaCuracion=tiempo
                jugador.cooldownCuracion=self.tiempoReutilizacion
                if jugador.vida>= jugador.maxVida:
                        jugador.vida=jugador.maxVida
                
        
        def dibujar(self, superficie):
                superficie.blit(self.imagenCuracion,self.rect)

        def reducirVelocidad(self, jugador):
                jugador.velocidad -= self.cantAumentoVelocidad
                
        def trayectoria(self, jugador):
                self.rect.centerx = jugador.rect.centerx
                self.rect.centery = jugador.rect.centery
                     
                     
                     


        
                
class Disparo(pygame.sprite.Sprite):
        """Clase del disparo"""
        
        def __init__(self, posX, posY, direccion,danio,velocidad):
                pygame.sprite.Sprite.__init__(self)
                
                if direccion == 'N' or direccion == 'S':
                        self.imagenDisparo = pygame.image.load("Imagenes/Disparo_laser_vertical.png")
                else:
                        self.imagenDisparo = pygame.image.load("Imagenes/Disparo_laser_horizontal.png")
                        
                self.rect = self.imagenDisparo.get_rect()
                self.rect.centerx = posX
                self.rect.centery = posY
                self.danio = danio
                self.velocidad = velocidad
                self.direccion = direccion
                self.tiempoReutilizacion = 1
                self.tiempoReutilizacionLaser = 5
                
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



class Enemigo(pygame.sprite.Sprite):
        
        """Clase de los enemigos basicos"""

        def __init__(self, posX, posY):
                pygame.sprite.Sprite.__init__(self)
                self.vida = 100
                self.Fuente = pygame.font.SysFont("Arial", 20)
                self.direccion = 'S'
                self.imagenEnemigo = pygame.image.load("Imagenes/Enemigo1.png")
                self.rect = self.imagenEnemigo.get_rect()
                self.rect.centerx = posX
                self.rect.centery = posY
                self.velocidad = 2
                self.listaDisparo = []
                self.ultimoDisparo = 0

        def dibujar(self, superficie):
                superficie.blit(self.imagenEnemigo, self.rect)
                self.mostrarVida(superficie)

        def mostrarVida(self, superficie):
                texto_vida = self.Fuente.render("Vida: " + str(self.vida), 0, (255, 0, 0))
                superficie.blit(texto_vida, (self.rect.left +5, self.rect.bottom ))

        def disparar(self, tiempo):
                disparo = Disparo(self.rect.centerx, self.rect.centery, self.direccion,10,5)
                if tiempo > self.ultimoDisparo + disparo.tiempoReutilizacion:
                        self.listaDisparo.append(disparo)
                        self.ultimoDisparo = tiempo

        def sigueVivo(self):
                if self.vida > 0:
                        return True
                else:
                        return False

        def moverIzquierda(self):
                self.rect.centerx -= self.velocidad
                self.__movimiento()
                self.direccion = 'O'

        def moverDerecha(self):
                self.rect.centerx += self.velocidad
                self.__movimiento()
                self.direccion = 'E'

        def moverArriba(self):
                self.rect.centery -= self.velocidad
                self.__movimiento()
                self.direccion = 'N'

        def moverAbajo(self):
                self.rect.centery += self.velocidad
                self.__movimiento()
                self.direccion = 'S'

                
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

        def mover(self, jugador):
                if abs(self.rect.centerx - jugador.rect.centerx) < abs(self.rect.centery - jugador.rect.centery):
                        if self.rect.centerx >= jugador.rect.right:
                                self.moverIzquierda()
                        elif self.rect.centerx <= jugador.rect.left:
                                self.moverDerecha()
                        elif self.rect.centerx < jugador.rect.right and self.rect.centerx > jugador.rect.left and self.rect.centery > jugador.rect.centery:
                                self.moverArriba()
                        elif self.rect.centerx < jugador.rect.right and self.rect.centerx > jugador.rect.left and self.rect.centery < jugador.rect.centery:
                                self.moverAbajo()
                else:
                        if self.rect.centery <= jugador.rect.top:
                                self.moverAbajo()
                        elif self.rect.centery >= jugador.rect.bottom:
                                self.moverArriba()
                        elif self.rect.centery <= jugador.rect.bottom and self.rect.centery >= jugador.rect.top and self.rect.centerx > jugador.rect.centerx:
                                self.moverIzquierda()
                        elif self.rect.centery <= jugador.rect.bottom and self.rect.centery >= jugador.rect.top and self.rect.centerx < jugador.rect.centerx:
                                self.moverDerecha()
                                
        def recibirDanio(self, danio):
                self.vida -= danio

        def alejarse(self, otroenemigo):
                if self.rect.centerx > otroenemigo.rect.centerx:
                        self.moverDerecha()
                elif self.rect.centerx < otroenemigo.rect.centerx:
                        self.moverDerecha()
                elif self.rect.centerx == otroenemigo.rect.centerx:
                        if self.rect.centery < otroenemigo.rect.centery:
                                self.moverArriba()
                        else:
                                self.moverAbajo()
                if self.rect.centery > otroenemigo.rect.centery:
                        self.moverAbajo()
                elif self.rect.centery < otroenemigo.rect.centery:
                        self.moverArriba()
                elif self.rect.centery == otroenemigo.rect.centery:
                        if self.rect.centerx < otroenemigo.rect.centerx:
                                self.moverIzquierda()
                        else:
                                self.moverDerecha()
            

        def enRango(self, jugador):
                return ((enemigo.rect.left < jugador.rect.centerx and enemigo.rect.right > jugador.rect.centerx and (self.direccion == 'S' or self.direccion == 'N')) or
                        (enemigo.rect.top < jugador.rect.centery and enemigo.rect.bottom > jugador.rect.centery and (self.direccion == 'E' or self.direccion == 'O')))
        
def crearListaEnemigos(listaEnemigos, cantidad):
        for i in range (0,cantidad):
                posx = randint(100, ancho-100)
                posy = randint(100, alto-100)
                enemigo = Enemigo(posx, posy)
                listaEnemigos.append(enemigo)
        
"""""""""""""""""""""""""""MAIN"""""""""""""""""""""""""""""""""        
pygame.init()
ancho = 1024
alto = 768
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")


imagenFondo = pygame.image.load("Imagenes\Fondo.jpg")
ventana.blit(imagenFondo, (0, 0))

jugador = Personajes()
tiempo = 5

derechaApretada = False
izquierdaApretada = False
arribaApretada = False
abajoApretada = False
disparoApretado = False
disparoLaserApretado=False

listaEnemigos = []
crearListaEnemigos(listaEnemigos, 3)

while jugador.sigueVivo():
        tiempo_milesimas = pygame.time.get_ticks()/1000
        if tiempo == tiempo_milesimas:
##                print tiempo
                tiempo += 1
                
                if jugador.cooldownCuracion>0:    
##                        print jugador.cooldownCuracion
                        jugador.cooldownCuracion-=1

                if jugador.cooldownLaser>0:
##                        print jugador.cooldownLaser
                        jugador.cooldownLaser-=1
                        
        for evento in pygame.event.get():
                if evento.type == QUIT: #agregar la salida al menu y guardado de score
                        pygame.quit()
                        sys.exit()
                if evento.type == pygame.KEYDOWN:
                        if evento.key == K_LEFT:
                                izquierdaApretada = True
                        elif evento.key == K_RIGHT:
                                derechaApretada = True
                        elif evento.key == K_UP:
                                arribaApretada = True
                        elif evento.key == K_DOWN:
                                abajoApretada = True
                        elif evento.key == K_1:
                                jugador.aumentarVida(tiempo)
                        elif evento.key == K_2:
                                disparoLaserApretado=True
                        elif evento.key ==K_SPACE:
                                disparoApretado=True
                                

                if evento.type == pygame.KEYUP:
                        if evento.key == K_LEFT:
                                izquierdaApretada = False
                        elif evento.key == K_RIGHT:
                                derechaApretada = False
                        elif evento.key == K_UP:
                                arribaApretada = False
                        elif evento.key == K_DOWN:
                                abajoApretada = False     
                        elif evento.key == K_2 :
                                disparoLaserApretado=False
                        elif evento.key ==K_SPACE:
                                disparoApretado=False
                        
                      
        if disparoLaserApretado:      
                jugador.disparoLaser(tiempo)                  
        elif disparoApretado:
                jugador.disparar(tiempo)
                        
        jugador.mover(izquierdaApretada, derechaApretada, arribaApretada, abajoApretada)
        ventana.blit(imagenFondo, (0, 0))
        jugador.dibujar(ventana)

        if len(listaEnemigos) > 0:
                for enemigo in listaEnemigos:
                        enemigo.dibujar(ventana)
                        enemigo.mover(jugador)
                        for otroEnemigo in listaEnemigos:
                                if not enemigo == otroEnemigo:
                                        if enemigo.rect.colliderect(otroEnemigo.rect):
                                                enemigo.alejarse(otroEnemigo)
                        if not enemigo.sigueVivo():
                                listaEnemigos.remove(enemigo)
                        elif enemigo.enRango(jugador):
                                enemigo.disparar(tiempo)
                        if len(enemigo.listaDisparo) > 0:
                                for y in enemigo.listaDisparo:
                                        y.dibujar(ventana)
                                        y.trayectoria()
                                        if y.rect.colliderect(jugador.rect):
                                                jugador.recibirDanio(y.danio)
                                                enemigo.listaDisparo.remove(y)
                                        elif y.rect.top < 0:
                                                enemigo.listaDisparo.remove(y)
                                        elif y.rect.bottom > alto:
                                                enemigo.listaDisparo.remove(y)
                                        elif y.rect.left < 0:
                                                enemigo.listaDisparo.remove(y)
                                        elif y.rect.right > ancho:
                                                enemigo.listaDisparo.remove(y)
        
        if len(jugador.listaDisparo) > 0: #aca recorro la lista de disparos pendientes del jugador
                for x in jugador.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if len(listaEnemigos) > 0:
                                enemigoGolpeado = False
                                for enemigo in listaEnemigos:
                                        if not enemigoGolpeado:
                                                if x.rect.colliderect(enemigo.rect):
                                                        enemigoGolpeado = True
                                                if enemigoGolpeado:
                                                        enemigo.recibirDanio(x.danio)
                                                        jugador.listaDisparo.remove(x)
                        if x.rect.top < -20:
                                jugador.listaDisparo.remove(x)
                        elif x.rect.bottom > alto+20:
                                jugador.listaDisparo.remove(x)
                        elif x.rect.left < -20:
                                jugador.listaDisparo.remove(x)
                        elif x.rect.right > ancho+20:
                                jugador.listaDisparo.remove(x)

                                
        if len(jugador.listaCuracion) > 0:
                for z in jugador.listaCuracion:
                        z.dibujar(ventana)
                        z.trayectoria(jugador)
                        if not z.usado:
                                z.aumentar(jugador, tiempo)
                                z.usado = True
                        elif jugador.ultimaCuracion + z.duracionVelocidad <= tiempo:
                                z.reducirVelocidad(jugador)
                                jugador.listaCuracion.remove(z)

        
        pygame.display.update()
        
pygame.quit()
sys.exit()
