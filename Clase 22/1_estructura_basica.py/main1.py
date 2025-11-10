import pygame # importamos la libreria. Primero la debemos instalar

# de este modo inicializamos pygame
pygame.init()

# creamos la ventana
# sin toda la logica de abajo se abrira y se cerrara rapidamente
ventana = pygame.display.set_mode((800, 600))

# logica para mantener la ventana del juego siempre corriendo
corriendo = True

while corriendo:
    
    # realizaremos un for para recorrer los eventos
    for evento in pygame.event.get():
        # print(pygame.event.get())
        if evento.type == pygame.QUIT:
            corriendo = False
        
        # se va actualizando la pantalla
        pygame.display.update()

# se usa para cerrar correctamente todos los módulos de Pygame
pygame.quit()