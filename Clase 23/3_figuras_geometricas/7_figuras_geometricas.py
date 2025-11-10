import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 600)) 

pygame.display.set_caption("Programación 1 - UTN Avellaneda")

# Definir colores
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    ventana.fill(negro)  # Limpiar pantalla
    
    # Dibujar un rectángulo
    pygame.draw.rect(ventana, rojo, (100, 450, 200, 100))
    
    # el parametro width es para generar un borde en el rectangulo
    # el parametro border_radius es para dar un border radius
    pygame.draw.rect(ventana, rojo, (50, 300, 200, 100), 10, 5)
    
    # Dibujar una línea
    pygame.draw.line(ventana, verde, (300, 100), (600, 100), 5)
    
    # Dibujar un círculo
    pygame.draw.circle(ventana, azul, (620, 240), 100)
    
    # Dibujar un ellipse
    pygame.draw.ellipse(ventana, rojo, (450, 250, 40, 190))
    
    # Dibujar un polígono
    puntos_poligono = [(50, 90), (70, 50), (250, 120), (320, 250), (150, 280)]
    pygame.draw.polygon(ventana, azul, puntos_poligono)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado
    pygame.display.flip()

pygame.quit()