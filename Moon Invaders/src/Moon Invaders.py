import pygame, sys, os
from pygame.locals import *
from random import randint

class Score():
        def __init__(self, nombrePJ):
                self.puntaje = 0
                self.nombre = nombrePJ

        def __cmp__(self, otroScore):
                if self.puntaje < otroScore.puntaje:
                        resultado = -1
                if self.puntaje > otroScore.puntaje:
                        resultado = 1
                else:
                        resultado = 0
                return resultado


class Configuracion():
        def __init__(self, dificultad = 1):
                self.listaScores = []
                self.listaScoresCampania = []
                self.alto = 600
                self.ancho = 800
                self.ventana = pygame.display.set_mode((self.ancho, self.alto))
                pygame.display.set_caption("Moon Invaders")
                self.tiempo = 3
                self.pausa = False
                self.inicioPausa = 0
                self.duracionPausa = 0
                self.reloj = pygame.time.Clock()
                self.Fuente = pygame.font.SysFont("Arial", 30)
                self.dificultad = dificultad
                self.imagenControles = pygame.image.load("Imagenes/DistribucionTeclado.png")
                
        def pausar(self, tiempo):
                if not self.pausa:
                        self.pausa = not self.pausa
                        self.inicioPausa = tiempo
                else:
                        self.duracionPausa = tiempo - self.inicioPausa
                        self.pausa = not self.pausa
        
        def cargarListaScores(self):
                archivoScores = open("Scores.txt", "r")
                x = 0
                flag = True
                for linea in archivoScores.readlines():
                        if x%2 == 0:
                                scoreTemp = Score("")
                                scoreTemp.nombre = linea.rstrip()
                                x += 1
                        elif x%2 == 1:
                                scoreTemp.puntaje = int(float(linea.rstrip()))
                                x += 1
                                self.listaScores.append(scoreTemp)
                archivoScores.close()

        def cargarListaScoresCampania(self):
                archivoScores = open("ScoresCampania.txt", "r")
                x = 0
                flag = True
                for linea in archivoScores.readlines():
                        if x%2 == 0:
                                scoreTemp = Score("")
                                scoreTemp.nombre = linea.rstrip()
                                x += 1
                        elif x%2 == 1:
                                scoreTemp.puntaje = int(float(linea.rstrip()))
                                x += 1
                                self.listaScoresCampania.append(scoreTemp)
                archivoScores.close()
                
        def agregarScore(self, score):
                self.listaScores.append(score)

        def agregarScoreCampania(self, score):
                self.listaScoresCampania.append(score)
                
        def guardarListaScores(self):
                self.listaScores.sort(key = lambda score : score.puntaje, reverse = True)
                archivoScores = open("Scores.txt", "w")
                if len(self.listaScores) > 10:
                         for i in range(0, 10):
                                archivoScores.write(self.listaScores[i].nombre + '\n' + str(self.listaScores[i].puntaje) + '\n')
                else:
                        for score in self.listaScores:
                                archivoScores.write(score.nombre + '\n' + str(score.puntaje) + '\n')
                        archivoScores.close()

        def guardarListaScoresCampania(self):
                self.listaScoresCampania.sort(key = lambda score : score.puntaje, reverse = True)
                archivoScores = open("ScoresCampania.txt", "w")
                if len(self.listaScores) > 10:
                         for i in range(0, 10):
                                archivoScores.write(self.listaScoresCampania[i].nombre + '\n' + str(self.listaScoresCampania[i].puntaje) + '\n')
                else:
                        for score in self.listaScoresCampania:
                                archivoScores.write(score.nombre + '\n' + str(score.puntaje) + '\n')
                        archivoScores.close() 
                        
        def verScores(self): #terminar
                mostrando = True
                self.ventana.fill((0,0,0))
                while mostrando:
                        posicion = 1
                        nombres = self.Fuente.render("Nombre", 2, (255,0,0))
                        scores = self.Fuente.render("Score", 2, (255, 0, 0))
                        textoSalir_1 = self.Fuente.render("Presione escape", 2, (0, 0, 255))
                        textoSalir_2 = self.Fuente.render("para salir", 2, (0, 0, 255))
                        self.ventana.blit(nombres, (100, 40*posicion))
                        self.ventana.blit(scores, (400, 40*posicion))
                        self.ventana.blit(textoSalir_1, (550, 20*posicion))
                        self.ventana.blit(textoSalir_2, (550, 45*posicion))
                        for score in self.listaScores:
                                posicion += 1
                                textoScore = self.Fuente.render(score.nombre, 2, (255, 0, 0))
                                textoNombre = self.Fuente.render(str(score.puntaje), 2, (255, 0, 0))
                                self.ventana.blit(textoScore, (100, 40*posicion))
                                self.ventana.blit(textoNombre, (400, 40*posicion))
                        for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if evento.type == pygame.KEYDOWN:
                                        if evento.key == K_ESCAPE or evento.key == K_RETURN:
                                                mostrando=False
                        pygame.display.update()
                        
        def verScoresCampania(self): #terminar
                mostrando = True
                self.ventana.fill((0,0,0))
                while mostrando:
                        posicion = 1
                        nombres = self.Fuente.render("Nombre", 2, (255,0,0))
                        scores = self.Fuente.render("Score", 2, (255, 0, 0))
                        textoSalir_1 = self.Fuente.render("Presione escape", 2, (0, 0, 255))
                        textoSalir_2 = self.Fuente.render("para salir", 2, (0, 0, 255))
                        self.ventana.blit(nombres, (100, 40*posicion))
                        self.ventana.blit(scores, (400, 40*posicion))
                        self.ventana.blit(textoSalir_1, (550, 20*posicion))
                        self.ventana.blit(textoSalir_2, (550, 45*posicion))
                        for score in self.listaScoresCampania:
                                posicion += 1
                                textoScore = self.Fuente.render(score.nombre, 2, (255, 0, 0))
                                textoNombre = self.Fuente.render(str(score.puntaje), 2, (255, 0, 0))
                                self.ventana.blit(textoScore, (100, 40*posicion))
                                self.ventana.blit(textoNombre, (400, 40*posicion))
                        for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if evento.type == pygame.KEYDOWN:
                                        if evento.key == K_ESCAPE or evento.key == K_RETURN:
                                                mostrando=False
                        pygame.display.update()

        def mostrarControles(self):
                mostrando = True
                textoVolver = self.Fuente.render("Presione Escape para volver al menu", 1, (255, 0, 0))
                while mostrando:
                        self.ventana.blit(self.imagenControles, (0, 0))
                        self.ventana.blit(textoVolver, (0, 0))
                        for evento in pygame.event.get():
                                if evento.type == pygame.KEYDOWN:
                                        if evento.key == K_ESCAPE:
                                                mostrando = False
                        pygame.display.update()
                        
class Entrada():

        def __init__(self, config):
            self.lineas=0
            self.caracteres=['']
            self.fuente=pygame.font.Font(None,25)

            self.distancia=20
            self.posX=config.ancho/2
            self.posY=config.alto/2

        def teclas(self,evento):
            for accion in evento:
                if accion.type == KEYDOWN:
                    if accion.key==K_RETURN:
                        #self.caracteres.append('')
                        return
                        self.lineas+=1
                    elif accion.key == K_BACKSPACE:
                            if self.caracteres[self.lineas]=='' and self.lineas > 0:
                                self.caractereS[0:-1]
                                self.lineas-=1
                            else:
                                self.caracteres[self.lineas]=self.caracteres[self.lineas][0:-1]
                    else:
                            self.caracteres[self.lineas]=str(self.caracteres[self.lineas]+accion.unicode)

        def mensaje(self,superficie):
            superficie.fill((0,0,0))
            for self.lineas in xrange(len(self.caracteres)):
                Img_letra=self.fuente.render(self.caracteres[self.lineas],True,(200,200,0))
            superficie.blit(Img_letra,(self.posX,self.posY + self.distancia * self.lineas))

            
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=(255, 255, 255), (pos_x, pos_y)=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
 
class GameMenu():
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load("Imagenes/fondoMenu.jpg")
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item)#, '/home/nebelhom/.fonts/SHOWG.TTF')
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)
 
            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
 
    def run(self, config):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                            if item.is_mouse_selection(pygame.mouse.get_pos()):
                                        if item.text == "Salir":
                                                mainloop = False
                                        if item.text == "Iniciar Campania":
                                                menuDificultadItems = ('Facil', 'Dificil')
                                                menuDificultad = GameMenu(self.screen, menuDificultadItems)
                                                menuDificultad.run(config)
                                                campania(config, self.screen)
                                        if item.text == "Supervivencia":
                                                bucleDeJuego(config, self.screen)
                                        if item.text == "Score (Survival)":
                                                config.verScores()
                                        if item.text == "Score (Campaign)":
                                                config.verScoresCampania()
                                        if item.text == "Controles":
                                                config.mostrarControles()
                                        if item.text == "Facil":
                                                config.dificultad = 1
                                                mainloop = False
                                        if item.text == "Dificil":
                                                config.dificultad = 2
                                                mainloop = False
 

            # Redraw the background
            self.screen.blit(self.background_image, (0, 0))
 
            for item in self.items:
                if item.is_mouse_selection(pygame.mouse.get_pos()):
                    item.set_font_color((255, 0, 0))
                    item.set_italic(True)
                else:
                    item.set_font_color((0, 0, 255))
                    item.set_italic(False)
                self.screen.blit(item.label, item.position)
 
            pygame.display.flip()


class Personajes(pygame.sprite.Sprite):
        """Clase de los personajes"""
        def cargarImagenes(self):
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Arriba/personaje_quieto_arriba.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Arriba/personaje_caminando_arriba.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Arriba/personaje_caminando2_arriba.png")) #Del 0 al 2 son arriba
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Abajo/personaje_quieto_abajo.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Abajo/personaje_caminando_abajo.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Abajo/personaje_caminando2_abajo.png")) #Del 3 al 5 son abajo
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Izquierda/personaje_quieto_izquierda.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Izquierda/personaje_caminando_izquierda.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Izquierda/personaje_caminando2_izquierda.png")) #Del 6 al 8 son izquierda
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Derecha/personaje_quieto_derecha.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Derecha/personaje_caminando_derecha.png"))
                self.imagenPersonaje.append(pygame.image.load("Imagenes/Personaje/Derecha/personaje_caminando2_derecha.png")) #Del 9 al 11 son derecha
                
        def __init__(self, alto=600, ancho=800, nombrePJ = "", vida=100, velocidad=4):
                pygame.sprite.Sprite.__init__(self)
                self.scoreActual = Score(nombrePJ)
                self.imagenPersonaje = []
                self.cargarImagenes();
                self.rect = self.imagenPersonaje[0].get_rect()
                self.rect.centerx = ancho-100
                self.rect.centery = alto - (self.rect.bottom - self.rect.top)
                self.caminando = False
                self.ultimaCaminata = 0
                self.tiempoUltimaCaminata = 0
                self.vida = vida
                self.maxVida=100
                self.velocidad = velocidad
                self.listaDisparo = []
                self.listaCuracion=[]
                self.ultimoDisparo = -1
                self.ultimaCuracion = -5
                self.ultimoDisparoLaser=-5
                self.direccion = 'N' #Direcciones: Norte(N), Sur(S), Este(E), Oeste(O)
                self.Fuente = pygame.font.SysFont("Arial", 30)
                self.cooldownCuracion=0
                self.cooldownLaser=0
                self.listaBomba = []
                self.ultimaBomba = -5
                self.cooldownBomba = 0
                
        def reducirScore(self, puntos):
                self.scoreActual.puntaje -= puntos
                if self.scoreActual.puntaje <= 0:
                        self.scoreActual.puntaje = 0
                
        def aumentarScore(self, puntos):
                self.scoreActual.puntaje += puntos
        
        def dibujar(self, superficie, tiempo):
                if self.direccion == 'N':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 0 and self.ultimaCaminata < 3:
                                        superficie.blit(self.imagenPersonaje[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                        self.tiempoUltimaCaminata = tiempo
                                        if self.ultimaCaminata == 0:
                                               superficie.blit(self.imagenPersonaje[1], self.rect)
                                               self.ultimaCaminata = 1

                                        elif self.ultimaCaminata == 1:
                                               superficie.blit(self.imagenPersonaje[2], self.rect)
                                               self.ultimaCaminata = 2
                                        
                                        else:
                                               superficie.blit(self.imagenPersonaje[1], self.rect)
                                               self.ultimaCaminata = 1
                        else:
                                superficie.blit(self.imagenPersonaje[0], self.rect)
                                self.ultimaCaminata = 0
                        
                elif self.direccion == 'S':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 3 and self.ultimaCaminata < 6:
                                        superficie.blit(self.imagenPersonaje[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                       self.tiempoUltimaCaminata = tiempo
                                       if self.ultimaCaminata == 3:
                                               superficie.blit(self.imagenPersonaje[4], self.rect)
                                               self.ultimaCaminata = 4
                                       elif self.ultimaCaminata == 4:
                                               superficie.blit(self.imagenPersonaje[5], self.rect)
                                               self.ultimaCaminata = 5
                                       else:
                                               superficie.blit(self.imagenPersonaje[4], self.rect)
                                               self.ultimaCaminata = 4
                        else:
                                superficie.blit(self.imagenPersonaje[3], self.rect)
                                
                elif self.direccion == 'O':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 6 and self.ultimaCaminata < 9:
                                        superficie.blit(self.imagenPersonaje[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                       self.tiempoUltimaCaminata = tiempo
                                       if self.ultimaCaminata == 6:
                                               superficie.blit(self.imagenPersonaje[7], self.rect)
                                               self.ultimaCaminata = 7
                                       elif self.ultimaCaminata == 7:
                                               superficie.blit(self.imagenPersonaje[8], self.rect)
                                               self.ultimaCaminata = 8
                                       else:
                                               superficie.blit(self.imagenPersonaje[7], self.rect)
                                               self.ultimaCaminata = 7
                        else:
                                superficie.blit(self.imagenPersonaje[6], self.rect)

                elif self.direccion == 'E':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 9 and self.ultimaCaminata < 12:
                                        superficie.blit(self.imagenPersonaje[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                       self.tiempoUltimaCaminata = tiempo
                                       if self.ultimaCaminata == 9:
                                               superficie.blit(self.imagenPersonaje[10], self.rect)
                                               self.ultimaCaminata = 10
                                       elif self.ultimaCaminata == 10:
                                               superficie.blit(self.imagenPersonaje[11], self.rect)
                                               self.ultimaCaminata = 11
                                       else:
                                               superficie.blit(self.imagenPersonaje[10], self.rect)
                                               self.ultimaCaminata = 10
                        else:
                                superficie.blit(self.imagenPersonaje[9], self.rect)
                self.mostrarVida(superficie)
                self.mostrarCoolCuracion(superficie)
                self.mostrarCoolLaser(superficie)
                self.mostrarCoolBomba(superficie)
                
        def mostrarVida(self, superficie):
                texto_vida = self.Fuente.render("Vida: " + str(self.vida), 0, (255, 0, 0))
                superficie.blit(texto_vida, (5, 5))
                
        def mostrarCoolCuracion(self,superficie):
                texto_curacion = self.Fuente.render("| Curacion: " + str(self.cooldownCuracion), 0, (0, 255, 0))
                superficie.blit(texto_curacion, (150, 5))
        def mostrarCoolLaser(self,superficie):
                texto_laser = self.Fuente.render("| Laser: " + str(self.cooldownLaser), 0, (0, 255, 255))
                superficie.blit(texto_laser, (300, 5))
                
        def mostrarCoolBomba(self,superficie):
                        texto_bomba = self.Fuente.render("| Bomba: " + str(self.cooldownBomba), 0, (255, 100, 0))
                        superficie.blit(texto_bomba, (410, 5))
                
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
                aumento = Curacion(self.rect.centerx,self.rect.centery, 10)
                if tiempo >= self.ultimaCuracion + aumento.tiempoReutilizacion:
                        self.listaCuracion.append(aumento)
                                
        def recibirDanio(self, danio):
                self.vida -= danio
                
        def disparar(self, tiempo): 
                disparo = Disparo(self.rect.centerx, self.rect.centery, self.direccion,10,6)
                if tiempo >= self.ultimoDisparo + disparo.tiempoReutilizacion:
                        self.listaDisparo.append(disparo)
                        self.ultimoDisparo = tiempo
                        disparo.sonido.play()
                        
        def disparoLaser(self, tiempo):
                 disparo=Disparo(self.rect.centerx,self.rect.centery,self.direccion,2,16)
                 if tiempo >= self.ultimoDisparoLaser + disparo.tiempoReutilizacionLaser:
                        disparo.sonido = pygame.mixer.Sound("Sonidos\RafagaLaser.wav")
                        for d in range (1, 10):
                                otrodisparo=Disparo(self.rect.centerx,self.rect.centery,self.direccion,2, 5 + d )
                                self.listaDisparo.append(otrodisparo)
                        self.listaDisparo.append(disparo)
                        self.ultimoDisparoLaser = tiempo
                        self.cooldownLaser=disparo.tiempoReutilizacionLaser
                        disparo.sonido.play()
        
        
        def dispararBomba(self, tiempo):
                bomba =Bomba(self.rect.centerx, self.rect.centery)
                if tiempo >= self.ultimaBomba + bomba.tiempoReutilizacion:
                        self.listaBomba.append(bomba)
                        self.ultimaBomba = tiempo
                        self.cooldownBomba = bomba.tiempoReutilizacion
                        bomba.sonido.play()
                        
        def corregirCDS(self, segundosExtra):
                self.ultimaCuracion += segundosExtra
                self.ultimoDisparo += segundosExtra
                self.ultimoDisparoLaser += segundosExtra
                self.ultimaBomba += segundosExtra
        

                
class Curacion(pygame.sprite.Sprite):
        """Clase Curacion y aumento de Velocidad"""

        def __init__(self, posX, posY, cantAumento = 10, cantAumentoVelocidad = 5):
                pygame.sprite.Sprite.__init__(self)
                self.imagenCuracion = pygame.image.load("Imagenes\Curacion.png")
                self.rect = self.imagenCuracion.get_rect()
                self.rect.centerx = posX
                self.rect.centery = posY
                self.cantAumento = cantAumento
                self.cantAumentoVelocidad = cantAumentoVelocidad
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

        def aumentarEnemigo(self,antagonista,tiempo):
                antagonista.atributoEnemigo.vida+=self.cantAumento
                antagonista.atributoEnemigo.velocidad += self.cantAumentoVelocidad
                antagonista.ultimaCuracion=tiempo
                antagonista.cooldownCuracion=self.tiempoReutilizacion
                if antagonista.atributoEnemigo.vida>= antagonista.maxVida:
                        antagonista.atributoEnemigo.vida=antagonista.maxVida
                
        
        def dibujar(self, superficie):
                superficie.blit(self.imagenCuracion, (self.rect.centerx-9, self.rect.centery+5))

        def reducirVelocidad(self, jugador):
                jugador.velocidad -= self.cantAumentoVelocidad

        def reducirVelocidadEnemigo(self,antagonista):
                antagonista.atributoEnemigo.velocidad -= self.cantAumentoVelocidad
                
        def trayectoria(self, jugador):
                self.rect.centerx = jugador.rect.centerx
                self.rect.centery = jugador.rect.centery
                     
                     
class Bomba(pygame.sprite.Sprite):
        """Clase bomba"""
        def __init__(self, posX, posY):
                pygame.sprite.Sprite.__init__(self)
                self.imagenBomba = pygame.image.load("Imagenes/Bomba.png")
                self.rect = self.imagenBomba.get_rect()
                self.rect.centerx, self.rect.centery = posX, posY
                self.danio = 15
                self.usado = False
                self.tiempoReutilizacion = 6
                self.sonido = pygame.mixer.Sound("Sonidos\Explosion.wav")
                self.sonido.set_volume(1)
                
        def dibujar(self, superficie):
                superficie.blit(self.imagenBomba, self.rect)

        def trayectoria(self, posX, posY):
                self.rect.centerx, self.rect.centery = posX, posY                     


        
                
class Disparo(pygame.sprite.Sprite):
        """Clase del disparo"""
        
        def __init__(self, posX, posY, direccion,danio=10,velocidad=5):
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
                self.sonido = pygame.mixer.Sound("Sonidos\DisparoLaser.wav")
                self.sonido.set_volume(0.2)
                
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

class Antagonista(pygame.sprite.Sprite):
        """Clase Antagonista"""
        
        def __init__(self,posX,posY, tiempo, dificultad =1 ):
                self.atributoEnemigo=Enemigo(posX,posY)
                self.atributoEnemigo.vida=200
                self.cargarImagenes()
                self.atributoEnemigo.puntos = 500
                self.ultimoDisparo = tiempo
                self.listaCuracion=[]
                self.ultimaCuracion=tiempo-2
                self.cooldownCuracion=0
                self.maxVida=200
                self.rect=self.atributoEnemigo.rect
                self.ultimoDisparoLaser=tiempo-2
                self.caminando = False
                self.tiempoUltimaCaminata = 0
                self.ultimaCaminata = 0
                self.dificultad = dificultad
        def cargarImagenes(self):

                for imagen in self.atributoEnemigo.imagenEnemigo[:]:
                        self.atributoEnemigo.imagenEnemigo.remove(imagen)
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Arriba/antagonista_quieto_arriba.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Arriba/antagonista_caminando_arriba.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Arriba/antagonista_caminando2_arriba.png")) #Del 0 al 2 son arriba
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Abajo/antagonista_quieto_abajo.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Abajo/antagonista_caminando_abajo.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Abajo/antagonista_caminando2_abajo.png")) #Del 3 al 5 son abajo
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Izquierda/antagonista_quieto_izquierda.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Izquierda/antagonista_caminando_izquierda.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Izquierda/antagonista_caminando2_izquierda.png")) #Del 6 al 8 son izquierda
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Derecha/antagonista_quieto_derecha.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Derecha/antagonista_caminando_derecha.png"))
                self.atributoEnemigo.imagenEnemigo.append(pygame.image.load("Imagenes/Antagonista/Derecha/antagonista_caminando2_derecha.png")) #Del 9 al 11 son derecha
        
                
        def dibujar(self,superficie,tiempo):
                self.atributoEnemigo.dibujar(superficie,tiempo)

        def aumentarVida(self,tiempo):
                aumento = Curacion(self.rect.centerx,self.rect.centery,self.atributoEnemigo.vida)
                aumento.cantAumentoVelocidad=2
                aumento.cantAumento=10*self.dificultad
                aumento.duracionVelocidad=2
                aumento.tiempoReutilizacion=7
                if tiempo >= self.ultimaCuracion + aumento.tiempoReutilizacion:
                        self.listaCuracion.append(aumento)
                        
        def disparoLaser(self, tiempo):
                 disparo=Disparo(self.rect.centerx,self.rect.centery,self.atributoEnemigo.direccion,2*self.dificultad,16)
                 if tiempo >= self.ultimoDisparoLaser + disparo.tiempoReutilizacionLaser:
                        disparo.sonido = pygame.mixer.Sound("Sonidos\RafagaLaser.wav")
                        for d in range (1, 10):
                                otrodisparo=Disparo(self.rect.centerx,self.rect.centery,self.atributoEnemigo.direccion,2*self.dificultad, 5 + d )
                                self.atributoEnemigo.listaDisparo.append(otrodisparo)
                        self.atributoEnemigo.listaDisparo.append(disparo)
                        self.ultimoDisparoLaser = tiempo
                        disparo.sonido.play()
                        #self.cooldownLaser=disparo.tiempoReutilizacionLaser

        def corregirCDS(self, segundosExtra):
                self.ultimaCuracion += segundosExtra
                self.atributoEnemigo.ultimoDisparo += segundosExtra
                self.ultimoDisparoLaser += segundosExtra
                
class Enemigo(pygame.sprite.Sprite):
        
        """Clase de los enemigos basicos"""

        def __init__(self, posX, posY, dificultad = 1,  vida =100, velocidad = 2, puntos = 100, stuneado = False, ultimoStun=0):
                pygame.sprite.Sprite.__init__(self)
                self.vida = vida
                self.Fuente = pygame.font.SysFont("Arial", 20)
                self.direccion = 'S'
                self.imagenEnemigo = []
                self.cargarImagenes()
                self.rect = self.imagenEnemigo[0].get_rect()
                self.rect.centerx = posX
                self.rect.centery = posY
                self.velocidad = velocidad
                self.puntos = puntos
                self.listaDisparo = []
                self.ultimoDisparo = 0
                self.caminando = False
                self.tiempoUltimaCaminata = 0
                self.ultimaCaminata = 0
                self.stuneado = stuneado
                self.ultimoStun = ultimoStun
                self.dificultad = dificultad

        def cargarImagenes(self):
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Arriba/enemigo_quieto_arriba.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Arriba/enemigo_caminando_arriba.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Arriba/enemigo_caminando2_arriba.png")) #Del 0 al 2 son arriba
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Abajo/enemigo_quieto_abajo.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Abajo/enemigo_caminando_abajo.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Abajo/enemigo_caminando2_abajo.png")) #Del 3 al 5 son abajo
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Izquierda/enemigo_quieto_izquierda.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Izquierda/enemigo_caminando_izquierda.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Izquierda/enemigo_caminando2_izquierda.png")) #Del 6 al 8 son izquierda
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Derecha/enemigo_quieto_derecha.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Derecha/enemigo_caminando_derecha.png"))
                self.imagenEnemigo.append(pygame.image.load("Imagenes/Enemigo/Derecha/enemigo_caminando2_derecha.png")) #Del 9 al 11 son derecha

        def dibujar(self, superficie, tiempo):
                if self.direccion == 'N':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 0 and self.ultimaCaminata < 3:
                                        superficie.blit(self.imagenEnemigo[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                        self.tiempoUltimaCaminata = tiempo
                                        if self.ultimaCaminata == 0:
                                               superficie.blit(self.imagenEnemigo[1], self.rect)
                                               self.ultimaCaminata = 1

                                        elif self.ultimaCaminata == 1:
                                               superficie.blit(self.imagenEnemigo[2], self.rect)
                                               self.ultimaCaminata = 2
                                        
                                        else:
                                               superficie.blit(self.imagenEnemigo[1], self.rect)
                                               self.ultimaCaminata = 1
                        else:
                                superficie.blit(self.imagenEnemigo[0], self.rect)
                                self.ultimaCaminata = 0
                        
                elif self.direccion == 'S':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 3 and self.ultimaCaminata < 6:
                                        superficie.blit(self.imagenEnemigo[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                       self.tiempoUltimaCaminata = tiempo
                                       if self.ultimaCaminata == 3:
                                               superficie.blit(self.imagenEnemigo[4], self.rect)
                                               self.ultimaCaminata = 4
                                       elif self.ultimaCaminata == 4:
                                               superficie.blit(self.imagenEnemigo[5], self.rect)
                                               self.ultimaCaminata = 5
                                       else:
                                               superficie.blit(self.imagenEnemigo[4], self.rect)
                                               self.ultimaCaminata = 4
                        else:
                                superficie.blit(self.imagenEnemigo[3], self.rect)
                                
                elif self.direccion == 'O':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 6 and self.ultimaCaminata < 9:
                                        superficie.blit(self.imagenEnemigo[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                       self.tiempoUltimaCaminata = tiempo
                                       if self.ultimaCaminata == 6:
                                               superficie.blit(self.imagenEnemigo[7], self.rect)
                                               self.ultimaCaminata = 7
                                       elif self.ultimaCaminata == 7:
                                               superficie.blit(self.imagenEnemigo[8], self.rect)
                                               self.ultimaCaminata = 8
                                       else:
                                               superficie.blit(self.imagenEnemigo[7], self.rect)
                                               self.ultimaCaminata = 7
                        else:
                                superficie.blit(self.imagenEnemigo[6], self.rect)

                elif self.direccion == 'E':
                        if self.caminando and self.tiempoUltimaCaminata + 300 > tiempo and self.ultimaCaminata >= 9 and self.ultimaCaminata < 12:
                                        superficie.blit(self.imagenEnemigo[self.ultimaCaminata], self.rect)
                                        
                        elif self.caminando and self.tiempoUltimaCaminata + 300 <= tiempo:
                                       self.tiempoUltimaCaminata = tiempo
                                       if self.ultimaCaminata == 9:
                                               superficie.blit(self.imagenEnemigo[10], self.rect)
                                               self.ultimaCaminata = 10
                                       elif self.ultimaCaminata == 10:
                                               superficie.blit(self.imagenEnemigo[11], self.rect)
                                               self.ultimaCaminata = 11
                                       else:
                                               superficie.blit(self.imagenEnemigo[10], self.rect)
                                               self.ultimaCaminata = 10
                        else:
                                superficie.blit(self.imagenEnemigo[9], self.rect)
                self.mostrarVida(superficie)

        def mostrarVida(self, superficie):
                texto_vida = self.Fuente.render("Vida: " + str(self.vida), 0, (255, 0, 0))
                superficie.blit(texto_vida, (self.rect.left +5, self.rect.bottom ))

        def disparar(self, tiempo):
                disparo = Disparo(self.rect.centerx, self.rect.centery, self.direccion,10 * self.dificultad,5)
                disparo.tiempoReutilizacion += 2
                if tiempo > self.ultimoDisparo + disparo.tiempoReutilizacion:
                        self.listaDisparo.append(disparo)
                        self.ultimoDisparo = tiempo
                        disparo.sonido.play()

        def sigueVivo(self):
                if self.vida > 0:
                        return True
                else:
                        return False

        def moverIzquierda(self):
                if not self.stuneado:
                        self.rect.centerx -= self.velocidad
                        self.__movimiento()
                self.direccion = 'O'

        def moverDerecha(self):
                if not self.stuneado:
                        self.rect.centerx += self.velocidad
                        self.__movimiento()
                self.direccion = 'E'

        def moverArriba(self):
                if not self.stuneado:
                        self.rect.centery -= self.velocidad
                        self.__movimiento()
                self.direccion = 'N'

        def moverAbajo(self):
                if not self.stuneado:
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

                if self.stuneado:
                        self.caminando = False
                else:
                        self.caminando = True
                                
        def recibirDanio(self, danio):
                self.vida -= danio

        def stunear(self, tiempo):
                self.stuneado = True
                self.ultimoStun = tiempo

        def desStunear(self, tiempo):
                if self.stuneado and self.ultimoStun + 3 < tiempo:
                        self.stuneado = False

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
                return ((self.rect.left < jugador.rect.centerx and self.rect.right > jugador.rect.centerx and (self.direccion == 'S' or self.direccion == 'N')) or
                        (self.rect.top < jugador.rect.centery and self.rect.bottom > jugador.rect.centery and (self.direccion == 'E' or self.direccion == 'O')))
        
def crearListaEnemigos(listaEnemigos, cantidad, config):
        for i in range (0,cantidad):
                posx = randint(0, config.ancho)
                posy = randint(550, 600)
                enemigo = Enemigo(posx, posy, config.dificultad)
                listaEnemigos.append(enemigo)

                """ PRIMER NIVEL """
def primerNivel(jugador,tiempo_anterior,ventana, config):       
        imagenFondo = pygame.image.load("Imagenes\Fondo.jpg")
        ventana.blit(imagenFondo, (0, 0))
        tiempo = tiempo_anterior
        
        derechaApretada = False
        izquierdaApretada = False
        arribaApretada = False
        abajoApretada = False
        disparoApretado = False
        disparoLaserApretado=False
        
        listaEnemigos = []
        crearListaEnemigos(listaEnemigos, 3, config)
        while len (listaEnemigos)>0 and jugador.sigueVivo():
                while config.pausa:
                        tiempo_milesimas = pygame.time.get_ticks()
                        ventana.blit(config.imagenControles, (0, 0))
                        if tiempo <= tiempo_milesimas/1000:
                                tiempo += 1
                        for evento in pygame.event.get():
                                if evento.type == QUIT: #agregar la salida al menu y guardado de score
                                        jugador.vida = 0
                                if evento.type == pygame.KEYDOWN:
                                        if evento.key == K_p:
                                                config.pausar(tiempo)
                                                jugador.corregirCDS(config.duracionPausa)
                        pygame.display.update()
                        
                tiempo_milesimas = pygame.time.get_ticks()
                if tiempo <= tiempo_milesimas/1000:
##                        print tiempo
                        tiempo += 1
                        
                        if jugador.cooldownCuracion>0:    
        ##                        print jugador.cooldownCuracion
                                jugador.cooldownCuracion-=1

                        if jugador.cooldownLaser>0:
        ##                        print jugador.cooldownLaser
                                jugador.cooldownLaser-=1
                                
                        if jugador.cooldownBomba>0:
        ##                        print jugador.cooldownLaser
                                jugador.cooldownBomba-=1

                                
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
                                        jugador.caminando = True #ojo aca
                                elif evento.key == K_DOWN:
                                        abajoApretada = True
                                elif evento.key == K_1:
                                        jugador.aumentarVida(tiempo)
                                elif evento.key == K_2:
                                        disparoLaserApretado=True
                                elif evento.key == K_3:
                                        jugador.dispararBomba(tiempo)
                                elif evento.key ==K_SPACE:
                                        disparoApretado=True
                                elif evento.key == K_p:
                                        izquierdaApretada = False
                                        derechaApretada = False
                                        arribaApretada = False 
                                        abajoApretada = False
                                        config.pausar(tiempo)

                        if evento.type == pygame.KEYUP:
                                if evento.key == K_LEFT:
                                        izquierdaApretada = False
                                elif evento.key == K_RIGHT:
                                        derechaApretada = False
                                elif evento.key == K_UP:
                                        arribaApretada = False
                                        jugador.caminando = False #ojo aca
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
                
                if arribaApretada or abajoApretada or izquierdaApretada or derechaApretada:
                        jugador.caminando = True
                else:
                        jugador.caminando = False
                
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

                if len(jugador.listaBomba) > 0:
                        for bomba in jugador.listaBomba:
                                bomba.dibujar(ventana)
                                if len(listaEnemigos) > 0 and not bomba.usado:
                                        for enemigo in listaEnemigos:
                                                if bomba.rect.colliderect(enemigo.rect):
                                                        enemigo.recibirDanio(bomba.danio)
                                                        enemigo.stunear(tiempo)
                                                bomba.usado = True
                                if tiempo_milesimas > jugador.ultimaBomba*1000 + 100:
                                        jugador.listaBomba.remove(bomba)
                                        
                jugador.dibujar(ventana, tiempo_milesimas)

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

                if len(listaEnemigos) > 0:
                        for enemigo in listaEnemigos:
                                enemigo.dibujar(ventana, tiempo_milesimas)
                                if not enemigo.rect.colliderect(jugador.rect):  
                                        enemigo.mover(jugador)
                                for otroEnemigo in listaEnemigos:
                                        if not enemigo == otroEnemigo:
                                                if enemigo.rect.colliderect(otroEnemigo.rect):
                                                        enemigo.alejarse(otroEnemigo)
                                if not enemigo.sigueVivo():
                                        listaEnemigos.remove(enemigo)
                                        jugador.aumentarScore(enemigo.puntos)
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
                                if enemigo.stuneado:
                                        enemigo.desStunear(tiempo)  
                pygame.display.update()
                config.reloj.tick(40)
        for enemigo in listaEnemigos:
                for disparo in enemigo.listaDisparo:
                        enemigo.listaDisparo.remove(disparo)
                listaEnemigos.remove(enemigo)
        pygame.mixer.music.stop()
        return tiempo


        """ SEGUNDO NIVEL """

def segundoNivel(jugador,tiempo_anterior,ventana, config):
        imagenFondo = pygame.image.load("Imagenes\Fondo.jpg")
        ventana.blit(imagenFondo, (0, 0))
        tiempo = tiempo_anterior

        derechaApretada = False
        izquierdaApretada = False
        arribaApretada = False
        abajoApretada = False
        disparoApretado = False
        disparoLaserApretado=False

        antagonista=Antagonista(ancho/2,alto/2, tiempo, config.dificultad)
        while jugador.sigueVivo() and antagonista.atributoEnemigo.sigueVivo():
                while config.pausa:
                        tiempo_milesimas = pygame.time.get_ticks()
                        ventana.blit(config.imagenControles, (0, 0))
                        if tiempo <= tiempo_milesimas/1000:
                                tiempo += 1
                        for evento in pygame.event.get():
                                if evento.type == pygame.KEYDOWN:
                                        if evento.key == K_p:
                                                config.pausar(tiempo)
                                                jugador.corregirCDS(config.duracionPausa)
                                                antagonista.corregirCDS(config.duracionPausa)
                        pygame.display.update()

                tiempo_milesimas = pygame.time.get_ticks()
                if tiempo <= tiempo_milesimas/1000:
##                        print tiempo
                        tiempo += 1
                        
                        if jugador.cooldownCuracion>0:    
        ##                        print jugador.cooldownCuracion
                                jugador.cooldownCuracion-=1

                        if jugador.cooldownLaser>0:
        ##                        print jugador.cooldownLaser
                                jugador.cooldownLaser-=1
                        if jugador.cooldownBomba>0:
        ##                        print jugador.cooldownLaser
                                jugador.cooldownBomba-=1        
                                
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
                                        jugador.caminando = True #ojo aca
                                elif evento.key == K_DOWN:
                                        abajoApretada = True
                                elif evento.key == K_1:
                                        jugador.aumentarVida(tiempo)
                                elif evento.key == K_2:
                                        disparoLaserApretado=True
                                elif evento.key == K_3:
                                        jugador.dispararBomba(tiempo)
                                elif evento.key ==K_SPACE:
                                        disparoApretado=True
                                elif evento.key == K_p:
                                        config.pausar(tiempo)
                                        izquierdaApretada = False
                                        derechaApretada = False
                                        arribaApretada = False 
                                        abajoApretada = False     
                                        

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
             
                if arribaApretada or abajoApretada or izquierdaApretada or derechaApretada:
                        jugador.caminando = True
                else:
                        jugador.caminando = False

                if len(jugador.listaDisparo) > 0: #aca recorro la lista de disparos pendientes del jugador
                        for x in jugador.listaDisparo:
                                x.dibujar(ventana)
                                x.trayectoria()
                                if x.rect.colliderect(antagonista.atributoEnemigo.rect):
                                        antagonista.atributoEnemigo.recibirDanio(x.danio)
                                        jugador.listaDisparo.remove(x)
                                if x.rect.top < -20:
                                        jugador.listaDisparo.remove(x)
                                elif x.rect.bottom > alto+20:
                                        jugador.listaDisparo.remove(x)
                                elif x.rect.left < -20:
                                        jugador.listaDisparo.remove(x)
                                elif x.rect.right > ancho+20:
                                        jugador.listaDisparo.remove(x)
                   
                if len(jugador.listaBomba) > 0:
                        for bomba in jugador.listaBomba:
                                bomba.dibujar(ventana)
                                if bomba.rect.colliderect(antagonista.atributoEnemigo.rect) and not bomba.usado:
                                        antagonista.atributoEnemigo.recibirDanio(bomba.danio)
                                        antagonista.atributoEnemigo.stunear(tiempo)
                                bomba.usado = True
                                if tiempo_milesimas > jugador.ultimaBomba*1000 + 100:
                                        jugador.listaBomba.remove(bomba)

                jugador.dibujar(ventana, tiempo_milesimas)
                
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
                                        
                if antagonista.atributoEnemigo.sigueVivo():
                        antagonista.dibujar(ventana, tiempo_milesimas)
                        if antagonista.atributoEnemigo.stuneado:
                                antagonista.atributoEnemigo.desStunear(tiempo)
                        if not antagonista.atributoEnemigo.rect.colliderect(jugador.rect):
                                antagonista.atributoEnemigo.mover(jugador)
                        if tiempo>antagonista.ultimaCuracion+5:
                                antagonista.aumentarVida(tiempo)
                        if antagonista.atributoEnemigo.enRango(jugador):
                                antagonista.atributoEnemigo.disparar(tiempo)
                                antagonista.disparoLaser(tiempo)

                if len(antagonista.atributoEnemigo.listaDisparo) > 0:
                        for y in antagonista.atributoEnemigo.listaDisparo:
                                y.dibujar(ventana)
                                y.trayectoria()
                                if y.rect.colliderect(jugador.rect):
                                        jugador.recibirDanio(y.danio)
                                        antagonista.atributoEnemigo.listaDisparo.remove(y)
                                elif y.rect.top < 0:
                                        antagonista.atributoEnemigo.listaDisparo.remove(y)
                                elif y.rect.bottom > alto:
                                        antagonista.atributoEnemigo.listaDisparo.remove(y)
                                elif y.rect.left < 0:
                                        antagonista.atributoEnemigo.listaDisparo.remove(y)
                                elif y.rect.right > ancho:
                                        antagonista.atributoEnemigo.listaDisparo.remove(y)
                                        
                if len(antagonista.listaCuracion) >0:
                        for z in antagonista.listaCuracion:
                                z.dibujar(ventana)
                                z.trayectoria(antagonista)
                                if not z.usado:
                                        z.aumentarEnemigo(antagonista, tiempo)
                                        z.usado = True
                                elif antagonista.ultimaCuracion + z.duracionVelocidad <= tiempo:
                                        z.reducirVelocidadEnemigo(antagonista)
                                        antagonista.listaCuracion.remove(z)
                pygame.display.update()
                config.reloj.tick(40)
        if not antagonista.atributoEnemigo.sigueVivo():
                jugador.aumentarScore(antagonista.atributoEnemigo.puntos)
        return tiempo

def bucleDeJuego(config, ventana):
        nombrePJ = leerNombre(ventana, config)
        jugador=Personajes(config.alto/2, config.ancho/2, nombrePJ)
        tiempo_termino_nivel = int(pygame.time.get_ticks()/1000)
        nivel = 1;
        jugando = True
        while jugando: # asi es infinito
                tiempo_termino_nivel=primerNivel(jugador,tiempo_termino_nivel,ventana, config)
                tiempo_termino_nivel=segundoNivel(jugador,tiempo_termino_nivel+3,ventana, config)
                if not jugador.sigueVivo():
                        jugando = False
                else:
                        nivel+=1
                if nivel >= 5:
                        config.dificultad = 2
        flag=True
        Fuente = pygame.font.SysFont("Arial", 30) 
        textoFin=Fuente.render("FIN DEL JUEGO", 2, (255,0, 255))
        textoPuntos=Fuente.render("TU PUNTAJE ES: " + str(jugador.scoreActual.puntaje), 2, (255,0, 255))
        textoNivel=Fuente.render("NIVEL ALCANZADO: " + str(nivel), 2, (255,0, 255))
        textoContinuar=Fuente.render("PRESIONE ENTER PARA CONTINUAR", 1, (255,0, 0))
        while flag:
                for evento in pygame.event.get():
                        if evento.type == pygame.KEYDOWN:
                                if evento.key == K_RETURN:
                                        flag=False
                        if evento.type == QUIT: #agregar
                                config.agregarScore(jugador.scoreAcutal)
                                config.guardarListaScores
                                pygame.quit()
                                sys.exit()
                                
                                
                ventana.blit(textoFin,(ancho/2-100, alto/2-100))
                ventana.blit(textoPuntos,(ancho/2-200, alto/2))
                ventana.blit(textoNivel,(ancho/2-200, alto/2 +100))
                ventana.blit(textoContinuar,(ancho/2-200, alto/2 +200))
                pygame.display.update()
        config.agregarScore(jugador.scoreActual)
        config.guardarListaScores()

def campania(config, ventana):
        nombrePJ = leerNombre(ventana, config)
        jugador=Personajes(config.alto/2, config.ancho/2, nombrePJ)
        tiempo_termino_nivel = int(pygame.time.get_ticks()/1000)
        tiempo_termino_nivel=primerNivel(jugador,tiempo_termino_nivel,ventana, config)
        tiempo_termino_nivel=segundoNivel(jugador,tiempo_termino_nivel+3,ventana, config)
        Fuente = pygame.font.SysFont("Arial", 30) 
        if not jugador.sigueVivo():
                textoFin=Fuente.render("HAS MUERTO", 2, (255,0, 255))
                textoComentario=Fuente.render("la raza humana ha sido esclavizada por Nexarien", 2, (255,0, 255))
        else:
                textoFin=Fuente.render("HAS VENCIDO", 2, (255,0, 255))
                textoComentario=Fuente.render("has salvado a la raza humana", 2, (255,0, 255))
        textoContinuar=Fuente.render("PRESIONE ENTER PARA CONTINUAR", 1, (255,0, 0))
        flag = True
        while flag:
                for evento in pygame.event.get():
                        if evento.type == pygame.KEYDOWN:
                                if evento.key == K_RETURN:
                                        flag=False
                        if evento.type == QUIT: #agregar
                                jugador.reducirScore(pygame.time.get_ticks()/1000)
                                config.agregarScoreCampania(jugador.scoreActual)
                                config.guardarListaScoresCampania()
                                pygame.quit()
                                sys.exit()
                                
                                
                ventana.blit(textoFin,(ancho/2-100, alto/2-100))
                ventana.blit(textoComentario,(ancho/2-200, alto/2))
                ventana.blit(textoContinuar,(ancho/2-200, alto/2 +100))
                pygame.display.update()
        jugador.reducirScore(pygame.time.get_ticks()/1000)
        config.agregarScoreCampania(jugador.scoreActual)
        config.guardarListaScoresCampania()
        
def leerNombre(ventana, config):
        escritura=Entrada(config)
        Fuente = pygame.font.SysFont("Arial", 25) 
        textoFin=Fuente.render("Ingrese su nombre: ", 2, (0,0, 255))
        salir=False
        while not salir:
                eventos=pygame.event.get()
                for accion in eventos:
                        if accion.type==QUIT:
                                salir=True
                        if accion.type==KEYDOWN:
                                if accion.key==K_RETURN:
                                        salir=True
                escritura.teclas(eventos)
                escritura.mensaje(ventana)
                ventana.blit(textoFin, (config.ancho/2-75, config.alto/2-50))
                pygame.display.update()
        return str(escritura.caracteres).strip("['']")


"""""""""""""""""""""""""""MAIN"""""""""""""""""""""""""""""""""
pygame.init()
pygame.mixer.init()
config = Configuracion()
config.cargarListaScores()
config.cargarListaScoresCampania()
alto = config.alto
ancho = config.ancho
ventana = config.ventana
menu_items = ('Iniciar Campania', 'Supervivencia','Score (Campaign)', 'Score (Survival)', 'Controles' ,'Salir')#Menu
pygame.mixer.music.load("Sonidos\Musica lvl1.mp3") #musica de juego
pygame.mixer.music.play(-1, 2)

gm = GameMenu(ventana, menu_items)
gm.run(config)

pygame.quit()
sys.exit()
 
