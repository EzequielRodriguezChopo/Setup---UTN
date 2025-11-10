import pygame # Importa la librería pygame

pygame.init() # Inicializa todos los módulos de PyGame

ventana = pygame.display.set_mode((800, 600)) # Crea la ventana principal del juego de 800 píxeles de ancho y 600 de alto

pygame.display.set_caption("Progrmación 1 - UTN Avellaneda") # Define el título de la ventana que aparece en la barra superior.

color_azul = (0, 0, 255) # Define un color azul en formato RGB (rojo, verde, azul).

# Crea un objeto Rect, que representa un rectángulo en la posición (300, 300), 
# de 50 píxeles de ancho y 50 de alto. Sirve para trabajar más cómodamente con posiciones y tamaños.
rectangulo = pygame.Rect(300, 300, 50, 50)
print(rectangulo)


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Dibujar un rectángulo relleno
    pygame.draw.rect(ventana, color_azul, (100, 100, 200, 150))

    # Dibujar un rectángulo con borde de grosor 5
    pygame.draw.rect(ventana, color_azul, (400, 100, 200, 150), 5)

    # Dibujar un rectángulo relleno con bordes redondeados
    pygame.draw.rect(ventana, color_azul, (500, 300, 200, 150), border_radius=10)
    
    # Dibujar un rectángulo mediante un objeto Rect
    pygame.draw.rect(ventana, color_azul, rectangulo)

    # actualiza toda la pantalla, mostrando cualquier cambio visual que hayas realizado en el búfer.
    pygame.display.flip()

pygame.quit()