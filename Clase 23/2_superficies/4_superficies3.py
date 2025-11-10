import pygame

# Inicializar PyGame
pygame.init()

# Configurar la ventana principal
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

# Colores
BLANCO = (255, 255, 255)

# Crea un objeto Clock para limitar los FPS del juego. Permite controlar cuántas veces por segundo se actualiza la pantalla.
clock = pygame.time.Clock()

# Crea una superficie para nuestro sprite
# Crea una superficie nueva (como una "mini pantalla") de 100x100 píxeles 
# que se puede dibujar sobre la ventana. Puede usarse para dibujar cosas encima, 
# como sprites personalizados.
superficie_sprite = pygame.Surface((100, 100))  # Superficie de 100x100 píxeles
##### SPRITE ES UNA IMAGEN, OSEA UN PERSONAJE !!!!!!
# superficie_sprite.fill(BLANCO) # para poner el color de la superficie a blanco

# Cargar imagen (si no tienes una imagen, creará un cuadrado rojo)
try:
    # Intenta cargar la imagen
    imagen_sprite = pygame.image.load("mario.png")
    #imagen_sprite = pygame.image.load("d:/Tecnicatura en Programación/Clase 23/2_superficies/mario.png")
    print(imagen_sprite)
    # print(imagen_sprite) # para ver que es una superficie
    # Ajustar el tamaño de la imagen al tamaño de la superficie
    imagen_sprite = pygame.transform.scale(imagen_sprite, (85, 100))
except FileNotFoundError:
    # Si no hay imagen, dibuja un cuadrado rojo
    imagen_sprite = pygame.Surface((100, 100))
    imagen_sprite.fill((255, 0, 0))  # Color rojo

# Copiar la imagen a la superficie
superficie_sprite.blit(imagen_sprite, (0, 0))

sprite_rect = imagen_sprite.get_rect()
# Se coloca el sprite inicialmente en la posición (50, 50) en la pantalla.
sprite_rect.x = 50
sprite_rect.y = 50

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Borra el contenido de la ventana llenándola de blanco.
    ventana.fill(BLANCO)
    
    # Dibuja la superficie completa con el sprite ya "pegado" en (100, 150).
    ventana.blit(superficie_sprite, (100, 150))
    
    # Luego dibuja la imagen directamente en la posición actual (sprite_rect), que mas arriba la definimos sprite_rect.x = 50 - sprite_rect.y = 50.
    ventana.blit(imagen_sprite, sprite_rect)

    # Mueve el sprite un píxel a la derecha y un píxel hacia abajo en cada iteración del bucle. Se mueve en diagonal.
    sprite_rect.x += 1
    sprite_rect.y += 1
    
    pygame.display.flip() # actualiza toda la pantalla.
    clock.tick(30) # limita la velocidad del juego a 30 cuadros por segundo.

pygame.quit() # Termina y libera los recursos de PyGame.


'''
PS D:\Tecnicatura en Programación> cd '.\Clase 23\'                                                                                                       
PS D:\Tecnicatura en Programación\Clase 23> cd .\2_superficies\
PS D:\Tecnicatura en Programación\Clase 23\2_superficies> python .\4_superficies3.py
'''