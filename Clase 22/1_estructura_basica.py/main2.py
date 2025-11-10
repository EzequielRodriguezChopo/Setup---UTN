import pygame # importamos la libreria. Primero la debemos instalar

# constantes del tamaño de la ventana
ANCHO = 800
ALTO = 600

# constante nombre de la ventana
NOMBRE_JUEGO = "Chucky: el programador de malbolge" 

# constante icono de la ventana
# ICONO = pygame.image.load("logo.png") 

# de este modo inicializamos pygame
pygame.init()

# creamos la ventana
# sin toda la logica de abajo se abrira y se cerrara rapidamente
ventana = pygame.display.set_mode((ANCHO, ALTO))
# ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN) # para pantalla completa
# ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE) # para pantalla redimensionable
# ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.NOFRAME) # para pantalla sin bordes


# Establecer el ícono de la ventana
pygame.display.set_caption(NOMBRE_JUEGO)

# Establecer el ícono de la ventana
# pygame.display.set_icon(ICONO)


# logica para mantener la ventana del juego siempre corriendo
corriendo = True

while corriendo:
    
    # realizaremos un for para recorrer los eventos
    for evento in pygame.event.get():
        # print(pygame.event.get())
        if evento.type == pygame.QUIT:
            corriendo = False
        
        
        pygame.display.update()

pygame.quit()