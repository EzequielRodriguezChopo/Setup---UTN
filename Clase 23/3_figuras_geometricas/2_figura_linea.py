import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Progrmación 1 - UTN Avellaneda")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    pygame.draw.line(ventana, (255, 0, 0), (50, 50), (300, 300), 3)
    
    pygame.draw.line(ventana, (0, 0, 255), (230, 150), (500, 450), 5)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado.
    pygame.display.flip()

pygame.quit()