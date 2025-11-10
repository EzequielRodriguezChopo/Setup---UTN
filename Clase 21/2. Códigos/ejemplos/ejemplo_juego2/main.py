# Juego sencillo de "Aventura en una Mazmorra" en el que el jugador se mueve por una cuadrícula y busca encontrar la salida.
# El estado del juego se guarda en un archivo, permitiendo al jugador cargar y continuar desde donde quedó.

# En este juego:

# - El jugador se mueve en una cuadrícula de 5x5 con las opciones norte, sur, este y oeste.
# - El objetivo es llegar a la posición de salida.
# - El estado del juego (posición actual del jugador) se guarda en un archivo de texto para poder cargar y continuar más tarde.

import json

# Configuración de la mazmorra
MAZMORRA = (5, 5)  # Tamaño de la cuadrícula
POSICION_SALIDA = (4, 4)  # Posición de la salida

def guardar_partida(posicion_jugador):
    with open("partida_guardada.json", "w") as archivo:
        json.dump({"posicion": posicion_jugador}, archivo)
    print("Partida guardada.")

def cargar_partida():
    try:
        with open("partida_guardada.json", "r") as archivo:
            data = json.load(archivo)
            return tuple(data["posicion"])
    except FileNotFoundError:
        print("No se encontró ninguna partida guardada. Iniciando una nueva partida.")
        return (0, 0)  # Posición inicial

def mover_jugador(posicion, direccion):
    x, y = posicion
    if direccion == "norte" and y > 0:
        y -= 1
    elif direccion == "sur" and y < MAZMORRA[1] - 1:
        y += 1
    elif direccion == "este" and x < MAZMORRA[0] - 1:
        x += 1
    elif direccion == "oeste" and x > 0:
        x -= 1
    else:
        print("Movimiento inválido.")
    return (x, y)

def juego():
    print("Bienvenido a la aventura en la mazmorra!")
    posicion_jugador = cargar_partida()

    while True:
        print(f"\nTu posición actual es: {posicion_jugador}")
        if posicion_jugador == POSICION_SALIDA:
            print("¡Felicidades, encontraste la salida!")
            break

        accion = input("¿Quieres moverte (norte, sur, este, oeste), guardar o salir?: ").lower()
        if accion in ["norte", "sur", "este", "oeste"]:
            posicion_jugador = mover_jugador(posicion_jugador, accion)
        elif accion == "guardar":
            guardar_partida(posicion_jugador)
        elif accion == "salir":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Comando no reconocido.")

# Iniciar el juego
juego()


# Explicación del código
# 1- Guardar y cargar partida: Utiliza JSON para guardar la posición del jugador en el 
# archivo partida_guardada.json. La función guardar_partida guarda la posición actual, 
# mientras que cargar_partida intenta cargar la posición desde el archivo o inicia desde 
# la posición (0, 0) si el archivo no existe.

# 2- Movimiento: La función mover_jugador ajusta la posición según el comando 
# (norte, sur, este, oeste). Verifica también que el jugador no se mueva fuera de 
# los límites de la cuadrícula.

# 3- Bucle del juego: El bucle principal permite al jugador moverse, guardar o salir del juego.