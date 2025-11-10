import pygame

# Inicializar PyGame
pygame.init()

# Crear la pantalla principal (una superficie también)
screen = pygame.display.set_mode((800, 600))
print(screen)

# Crear una superficie de 50x50 píxeles
square_surface = pygame.Surface((50, 50))
square_surface.fill((255, 0, 0))  # Pintar la superficie de rojo, sino le ponemos color por defecto es negro
# print(dir(pygame.Surface)) # vemos todos los metodos y atributos que tiene la clase Surface
square_surface_rect = square_surface.get_rect()
print(square_surface_rect)      #### Estas dos lineas por ahora esan al pedo, esta y la ultima !!!!!!!!!!

# Bucle principal del juego
corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

    # Dibujar la superficie en la pantalla principal
    screen.fill((0, 0, 0))  # Limpiar la pantalla con color negro
    screen.blit(square_surface, (100, 100))  # Mostrar la superficie en (100, 100)
    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()


# Sobre la superficie square_surface entonces ahora podriamos hacer figuras, cargar imagenes, poner texto
# al igual que con la superficie screen, que tambien es una superficie.

# square_surface_rect = square_surface.get_rect()
# Esta línea obtiene un objeto Rect que corresponde al área de la superficie. 
# Un Rect es útil para manejar la posición y las colisiones de la superficie 
# en la pantalla. El Rect tiene propiedades como x, y, width, height, y otras como left, right, top, y bottom.
