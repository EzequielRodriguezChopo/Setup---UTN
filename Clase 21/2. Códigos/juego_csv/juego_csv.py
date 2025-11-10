import pygame
import os

pygame.init()

# Pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejemplo PyGame + Archivo CSV sin módulo csv")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Jugador
player_size = 30
player_speed = 5

# Fuente
font = pygame.font.Font(None, 36)

# Archivo de puntajes
CSV_FILE = "puntajes.csv"


def guardar_puntaje(nombre, puntaje):
    """Guarda el puntaje como texto simple separado por coma"""
    nuevo = f"{nombre},{puntaje}\n"

    # Si no existe, crear con encabezado
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", encoding="utf-8") as f:
            f.write("Nombre,Puntaje\n")

    with open(CSV_FILE, "a", encoding="utf-8") as f:
        f.write(nuevo)


def cargar_puntajes():
    """Carga los puntajes en una lista y ordena de mayor a menor"""
    puntajes = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            lineas = f.readlines()[1:]  # Saltar encabezado
            for linea in lineas:
                linea = linea.strip()
                if linea:
                    nombre, puntaje = linea.split(",")
                    puntajes.append((nombre, int(puntaje)))

    # Ordenar: puntaje más alto primero
    puntajes.sort(key=lambda x: x[1], reverse=True)
    return puntajes


def mostrar_puntajes():
    screen.fill(WHITE)
    title = font.render("TOP 5 PUNTAJES:", True, BLACK)
    screen.blit(title, (50, 10))

    puntajes = cargar_puntajes()[:5]  # Solo los mejores 5

    y = 60
    for nombre, puntaje in puntajes:
        text = font.render(f"{nombre}: {puntaje}", True, BLACK)
        screen.blit(text, (50, y))
        y += 30

    pygame.display.flip()
    pygame.time.wait(3500)


def ingreso_nombre(puntaje):
    nombre = ""
    ingresando = True

    while ingresando:
        screen.fill(WHITE)

        msg = font.render("Perdiste! Ingresá tu nombre:", True, BLACK)
        screen.blit(msg, (50, 120))

        texto = font.render(nombre, True, RED)
        screen.blit(texto, (50, 170))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and nombre != "":
                    guardar_puntaje(nombre, puntaje)
                    mostrar_puntajes()
                    ingresando = False

                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]

                else:
                    if len(nombre) < 10:  # Limitar largo del nombre
                        nombre += event.unicode


def game_loop():
    player_x = WIDTH // 2
    player_y = HEIGHT // 2
    score = 0
    running = True

    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_x -= player_speed
        if keys[pygame.K_RIGHT]: player_x += player_speed
        if keys[pygame.K_UP]: player_y -= player_speed
        if keys[pygame.K_DOWN]: player_y += player_speed

        # Condición de derrota: tocar bordes
        if player_x < 0 or player_x + player_size > WIDTH or player_y < 0 or player_y + player_size > HEIGHT:
            ingreso_nombre(score)
            return  # Fin del juego → volver a inicio

        # Dibujar jugador
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

        # Actualizar puntaje
        score += 1
        texto = font.render(f"Puntaje: {score}", True, BLACK)
        screen.blit(texto, (10, 10))

        pygame.display.flip()
        clock.tick(30)


# Bucle principal
while True:
    game_loop()
