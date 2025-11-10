import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Dibujar un arco naranja
    pygame.draw.arc(ventana, (255, 165, 0), (300, 200, 200, 100), 0, 3.14, 5)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado.
    pygame.display.flip()

pygame.quit()


# Recordar:
# 180 grados = PI radianes, 360 grados = 2*PI radianes, 90 grados = PI/2 radianes, etc.