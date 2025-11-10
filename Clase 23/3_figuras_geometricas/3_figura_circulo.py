import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Dibujar un círculo verde relleno
    pygame.draw.circle(ventana, (0, 255, 0), (400, 300), 50)

    # Dibujar un círculo con borde
    pygame.draw.circle(ventana, (0, 255, 0), (200, 300), 50, 2)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado.
    pygame.display.flip()

pygame.quit()