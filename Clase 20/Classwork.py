"""
usuario1 = {"nombre": "Sara", "edad": 24, "documento": 27456877}
print(usuario1)

usuario2 = dict([("nombre", "Sara"),("edad", 24),("documento", 27456877)])
print(usuario2)

usuario3 = dict(nombre= "Pedro", edad= 27, documento= 27569877)
print(usuario3)

conjunto = {"casa",89,45,"Perro",45}

print(len(conjunto))
"""

#########################################

"""

usuario = {"nombre": "Sara", "edad": 24, "documento": 27456877}
print(usuario)

usuario["Nacionalidad"] = "Argentina"

# usuario["Profesion"] = input("Ingrese su profesion: ")

print(usuario["documento"])
print(usuario["nombre"])
print(usuario["edad"])

print(usuario)

# usuarios["usuario3"]["Lenguaje"] = ["Python", "Java", "Cobol"]  #

# usuarios["usuario3"]["Lenguaje"]

for clave in usuario:  # Imprimo solo las claves
    print(f"Los valores de las claves son: {clave}")

for clave in usuario.values():  # Imprimo solo valores
    print(f"Los valores de los valores, no claves son: {clave}")

for clave, valor in usuario.items():  # Imprimo clave y valor
    print(f"Clave: {clave.capitalize()}, Valor: {valor}")

print("Hola mundo")


"""


def ord_burbuja(arreglo):
    n = len(arreglo)
    print(n)

    for i in range(n - 1):  # <-- bucle padre
        for j in range(n - 1 - i):  # <-- bucle hijo
            if arreglo[j][1] > arreglo[j + 1][1]:
                aux = arreglo[j + 1]
                arreglo[j + 1] = arreglo[j]
                arreglo[j] = aux


elementos = [
    ["Laptop", 15000.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00, 30],
]
# elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)
print(elementos)
menor = float("-inf")
if menor < 10:
    print("Funciona")
else:
    print("No funciona")
