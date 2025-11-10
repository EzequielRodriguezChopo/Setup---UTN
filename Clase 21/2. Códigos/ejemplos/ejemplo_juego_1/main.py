import random

def iniciar_registro(nombre, numero_secreto):
    """Inicia el registro del juego con el nombre del jugador y el número secreto."""
    with open("intentos.txt", "a") as archivo:
        archivo.write(f"Jugador: {nombre}\n")
        archivo.write(f"Número secreto: {numero_secreto}\n")

def guardar_intento(intento):
    """Guarda cada intento en el archivo de texto."""
    with open("intentos.txt", "a") as archivo:
        archivo.write(f"Intento: {intento}\n")

def guardar_resultado(nombre, intentos, resultado):
    """Guarda el resultado final del juego en el archivo de texto."""
    with open("intentos.txt", "a") as archivo:
        archivo.write(f"Jugador: {nombre} | Resultado: {resultado} en {intentos} intentos\n")
        archivo.write("---- Fin del Juego ----\n\n")

def jugar():
    nombre = input("Por favor, ingresa tu nombre: ")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print(f"¡Hola, {nombre}! Bienvenido al juego de Adivina el Número.")
    print("Estoy pensando en un número entre 1 y 100.")

    # Iniciar registro en archivo
    iniciar_registro(nombre, numero_secreto)

    continuar = True
    while continuar:
        try:
            intento = int(input("Adivina el número: "))
            intentos += 1
            guardar_intento(intento)

            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print(f"¡Felicidades, {nombre}! Adivinaste el número en {intentos} intentos.")
                guardar_resultado(nombre, intentos, "Ganó")
                continuar = False
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    print("Gracias por jugar.")

# Ejecutar el juego
jugar()