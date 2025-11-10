import json
import random
import os

ARCHIVO_DATOS = "puntuaciones.json"

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS) and os.path.getsize(ARCHIVO_DATOS) > 0:
        with open(ARCHIVO_DATOS, 'r') as f:
            return json.load(f)
    return []

def guardar_datos(puntuaciones):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(puntuaciones, f)

def es_numero_valido(entrada):
    return entrada.isdigit() and 1 <= int(entrada) <= 100

def jugar():
    nombre = input("\nIngresa tu nombre: ")
    numero = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    print("\n¡Adivina el número entre 1 y 100!")
    while not adivinado:
        entrada = input("Tu intento: ")
        if es_numero_valido(entrada):
            intento = int(entrada)
            intentos += 1
            if intento < numero:
                print("Más alto")
            elif intento > numero:
                print("Más bajo")
            else:
                adivinado = True
                print(f"\n¡Correcto! Lo adivinaste en {intentos} intentos")
        else:
            print("Por favor ingresa un número válido entre 1 y 100")
    
    return {"nombre": nombre, "intentos": intentos}

def mostrar_ranking():
    puntuaciones = cargar_datos()
    
    if not puntuaciones:
        print("\nNo hay puntuaciones registradas")
        return
    
    # Función local para obtener los intentos (reemplazo de lambda)
    def obtener_intentos(registro):
        return registro['intentos']
    
    puntuaciones_ordenadas = sorted(puntuaciones, key=obtener_intentos)
    top_5 = puntuaciones_ordenadas[:5]
    
    print("\n=== TOP 5 PUNTUACIONES ===")
    for i, puntuacion in enumerate(top_5, 1):
        print(f"{i}. {puntuacion['nombre']}: {puntuacion['intentos']} intentos")

def mostrar_creditos():
    print("\n=== CRÉDITOS ===")
    print("Desarrollado por: [Tu nombre]")
    print("Versión: 1.0")
    print("Usando Python y JSON para almacenamiento de datos")

def main():
    salir = False
    while not salir:
        print("\n=== JUEGO DE ADIVINANZAS ===")
        print("1. Jugar")
        print("2. Ver ranking")
        print("3. Créditos")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            resultado = jugar()
            puntuaciones = cargar_datos()
            puntuaciones.append(resultado)
            guardar_datos(puntuaciones)
            
        elif opcion == "2":
            mostrar_ranking()
            
        elif opcion == "3":
            mostrar_creditos()
            
        elif opcion == "4":
            salir = True
            print("\n¡Gracias por jugar!")
            
        else:
            print("\nOpción inválida. Por favor elige 1-4")


main()