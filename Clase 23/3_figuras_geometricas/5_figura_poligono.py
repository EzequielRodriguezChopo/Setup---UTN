import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Dibujar un triángulo relleno azul       [ (x, y),     (x, y),     (x, y)  ]
    pygame.draw.polygon(ventana, (0, 0, 255), [(400, 50), (500, 200), (300, 200)])

    # Dibujar un pentágono con borde rojo
    pygame.draw.polygon(ventana, (255, 0, 0), [(100, 300), (150, 400), (200, 350), (150, 250), (50, 250)], 5)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado en el búfer.
    pygame.display.flip()

pygame.quit()