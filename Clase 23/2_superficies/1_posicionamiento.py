import pygame

# Inicializa Pygame
pygame.init()

# Establece el tamaño de la ventana
ventana = pygame.display.set_mode((800, 600))
print(ventana) # para mostrar que la ventana es una Superficie (Surface)

# Establece el título de la ventana
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

# Fuente para mostrar las coordenadas
fuente = pygame.font.Font(None, 36)

# Se puede especificar una fuente especifica:
# fuente = pygame.font.Font("zombie_zone.ttf", 36)


# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Rellena la ventana con un color de fondo
    ventana.fill((0, 0, 0))
    
    # Obtiene la posición del ratón
    pos_x, pos_y = pygame.mouse.get_pos()
    
    # Renderiza las coordenadas como texto
    texto = fuente.render(f"Posición del ratón: ({pos_x}, {pos_y})", True, (255, 255, 255), (100, 25, 55))
    
    # Dibuja el texto en la ventana
    # blit() se usa para dibujar una superficie sobre otra. 
    # Es una de las funciones más importantes para mostrar 
    # gráficos en pantalla, ya que permite colocar imágenes, 
    # texto o cualquier otro elemento visual en posiciones 
    # específicas dentro de la superficie principal o en 
    # cualquier otra superficie.
    # surface_destino.blit(superficie_origen, posicion)
    ventana.blit(texto, (20, 20))
    
    # Actualiza la pantalla
    pygame.display.flip()


pygame.quit()