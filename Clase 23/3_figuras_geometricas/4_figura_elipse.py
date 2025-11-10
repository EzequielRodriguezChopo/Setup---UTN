import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Dibujar una elipse amarilla rellena       (x , y, ancho, alto)
    pygame.draw.ellipse(ventana, (255, 255, 0), (50, 200, 200, 100))

    # Dibujar una elipse con borde
    pygame.draw.ellipse(ventana, (255, 255, 0), (100, 400, 200, 100), 3)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado en el búfer.
    pygame.display.flip()

pygame.quit()