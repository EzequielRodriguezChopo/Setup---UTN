import pygame

# Inicializar PyGame
pygame.init()

# Configurar la ventana principal
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Programación 1 - UTN Avellaneda")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Crear una superficie secundaria
# Las superficies son como lienzos donde podemos dibujar
superficie_secundaria = pygame.Surface((200, 200))
superficie_secundaria.fill(ROJO)  # Llenar la superficie con color rojo

# Dibujar un círculo en la superficie secundaria
pygame.draw.circle(superficie_secundaria, AZUL, (100, 100), 50)
pygame.draw.circle(superficie_secundaria, ROJO, (200, 200), 50 , 20)
# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Limpiar la ventana principal con color blanco
    ventana.fill(BLANCO)

    # Obtener la posición del mouse
    pos_mouse = pygame.mouse.get_pos()

    # Dibujar la superficie secundaria en la posición del mouse
    # El centro de la superficie seguirá al mouse
    ventana.blit(superficie_secundaria, (pos_mouse[0] - 100, pos_mouse[1] - 100))

    # Dibujar un rectángulo verde directamente en la ventana principal
    pygame.draw.rect(ventana, VERDE, (50, 50, 100, 100))
    pygame.draw.circle(ventana, ROJO, (400, 300), 50 , 10)
    # Actualizar la pantalla
    pygame.display.flip()
