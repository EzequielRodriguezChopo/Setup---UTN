##### apertura de archivos #####
# ----- Para abrir ----- #
"""print(open("archivos/archivo.txt", mode="r"))
# esto imprimira <_io.TextIOWrapper name='archivos/archivo.txt' mode='r' encoding='cp1252'>
# es una representación del objeto de archivo que se crea cuando abres un archivo.
# ✅ _io.TextIOWrapper es la clase del objeto, que maneja la lectura y escritura de archivos de texto.
# ✅ name='archivos/archivo.txt' es el nombre del archivo.
# ✅ mode='r' indica que el archivo se abrió en modo lectura (r).
# ✅ encoding='cp1252' muestra la codificación que se usa para leer el archivo.

#  VIENE DE from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
"""


# ----- Para leer ----- #
file = open("archivos/archivo.txt", mode="r", encoding="utf-8")
# Si es "r+" seria read and write y "a" para anexar

texto = file.read()
# Le estamos diciendo que lo que hay en file, lo lea y lo guarde en una variable llamada texto, read puede recibir un parametro, por ejemplo file.read(10) y eso significa que va a leer hasta esa posición.
# Una vez que lo leyo y lo guardo, puedo hacer lo que quiera, por ejemplo recorre con un FOR


for i in texto:
    print(i, end="-")

# O imprimirlo por pantalla
print(texto)

# Tambien podemos especificar cuantos caracteres queremos mostrar
# print(file.read(5))  # se deben comentar las otras lineas

# print(file.mode)  # Podemos ver en que modo abrimos el archivo
# print(file.name)  # Tambien podemos ver el nombre con la ruta del archivo
# print(file.closed)  # Nos dice si el archivo fue cerrado.

# file.close()  # Cerramos el archivo, pero como ya guardamos lo que leimos en la variable texto, podemos usarla igual

# file.read(5) # si quiero utilizar el file aca no se podra, porque ya se cerro. NO confundir con la variable texto que ya es un string

# print(f"Aca ya cerramos el archivo, pero podemos manipularlo igual ---> {texto}")

# ----- Para leer linea a linea ----- #
""""""
""" file = open("archivos/archivo.txt", "r")

linea_texto = file.readline() 
print(linea_texto)

linea_texto = file.readline(5) # mostrara solo los 5 primeros de la linea
print(linea_texto)

file.close() """

# -- ejemplito con readline -- #
""" file = open("archivos/archivo.txt", "r")

continuar = True
while continuar:
    
    linea_texto = file.readline()
    
    if not linea_texto:
        print("\nFin del archivo!")
        continuar = False
    
    else:
        print("\nLínea actual:", linea_texto.strip())
    
    respuesta = input("\n¿Deseas leer la siguiente línea? (s/n): ").lower()

    if respuesta != 's':
        continuar = False """


# ----- Para leer todas las lineas ----- #
""" file = open("archivos/archivo.txt", "r")

lineas_texto = file.readlines() # Lee la informacion que hay en el archivo LINEA a LINEA y la almacena en una lista

file.close()

print(lineas_texto) # Imprimira todas las lineas y las guardara en una lista
print(lineas_texto[1]) # Imprimira la segunda linea, que es la que esta en el indice 1.

# Imprime las líneas una por una
for linea in lineas_texto:
    print(linea) """


# ----- metodo seek ----- #
""" file = open("archivos/archivo.txt", "r")

file.seek(5)
lineas_texto = file.read()
print(lineas_texto) 
file.close()"""


# ----- metodo seekable ----- #
""" file = open("archivos/archivo.txt", "r")
print(file.seekable())
file.close() """


# ----- metodo tell ----- #
""" file = open("archivos/archivo.txt", "r")
datos = file.read(38)
posicion = file.tell()
print(f"Posición actual del puntero: {posicion}")
file.close() """


# ----- metodo fileno ----- #
""" file = open("archivos/archivo.txt", "r")
datos = file.read()
descriptor  = file.fileno()
print(descriptor)
file.close() """


# ----- creacion de un archivo con el modo "x" ----- #
""" file = open("archivos/contactos.txt", "x")
file.write("Hola como andas")
file.close()

# como tratar el error cuando el archivo ya existe
try:
    file = open("archivos/contactos.txt", "x")
except FileExistsError:
    print("El archivo ya existe") """


# ----- creacion de un archivo con el modo "w" ----- #
""" file = open("archivos/empleados.txt", "w")
file.close() """


# ----- escritura en un archivo ----- #
""" file = open("archivos/agregar_datos.txt", "w")
file.write("Ingresamos datos.\n")
file.write("Aca ingresamos mas datos.\n")
file.write("Otra linea de datos.\n")
file.close() """

# ejemplo
""" # Datos de empleados
empleados = [
    {"nombre": "Juan Pérez", "puesto": "Gerente", "salario": 60000},
    {"nombre": "María Gómez", "puesto": "Analista de Datos", "salario": 45000},
    {"nombre": "Pedro Rodríguez", "puesto": "Programador", "salario": 55000},
]

file = open("archivos/empleados.txt", "w")
for empleado in empleados:
    file.write(f"Nombre: {empleado['nombre']}\n")
    file.write(f"Puesto: {empleado['puesto']}\n")
    file.write(f"Salario: {empleado['salario']}\n")
    file.write("\n")

print(f"Los datos de los empleados se han escrito con exito.")

file.close() """


# ----- escritura en un archivo con el modo "a" ----- #
""" # primero lo probaremos con "w" y luego con "a"
file = open("archivos/personas.txt", "w")
file.write("Mariana.\n")
file.write("Pedro.\n")
# file.write("Juan.\n")
# file.write("Ana.\n")
file.close() """


# ----- escritura en un archivo utilizando writelines ----- #
""" lista_paises = ["Argentina\n", "Bolivia\n", "Paraguay\n", "Peru\n", "Chile\n"]
file = open("archivos/con_writelines.txt", "w")
file.writelines(lista_paises)
file.close() """


# ----- abrir un archivo para varias operaciones ----- #
# si intentamos escribir en un archivo, pero lo abrimos en modo lectura, arrojara un error
# file = open("archivos/prueba.txt", "r")
# file.write("Ingresamos datos")
# file.close()

# si intentamos leer en un archivo, pero lo abrimos en modo escritura, arrojara un error
""" file = open("archivos/prueba2.txt", "w")
file.read()
file.close() """

# podemos solucionar esto con el "+"
""" file = open("archivos/prueba.txt", "r+")
file.write("Ingresamos datos")
file.close() """


# ----- manejadores de contexto ----- #
""" with open("segundo-archivo.txt", "w+") as file:
    file.write("Abriendo, escribiendo y cerrando con with")

var = file.read()
print(var) """


# ----- eliminando un archivo de nuestro sistema ----- #
""" import os

with open("archivo_a_borrar.txt", "w+") as file:
    file.write("Este archivo lo vamos a borrar!")

# os.remove("archivo_a_borrar.txt") # descomentar para ver que se borra """


# ----- archivos json ----- #
# leer un archivo json
import json

# sin context manager
""" file = open("archivos/datos.json", "r")
content = file.read()
print(type(content))

data = json.loads(content)
print(type(data))
print(data)
print(data["edad"])
file.close() """

# con context manager y uso de loads
""" with open("archivos/datos.json", "r") as file:
    content = file.read()
    data = json.loads(content)
    print(type(data))
    print(data) """

# con context manager y uso de load
""" with open("archivos/datos.json", "r") as archivo:
    datos = json.load(archivo)  # Cargar el contenido del archivo JSON

# Ahora 'datos' contiene el contenido del archivo JSON como un diccionario de Python
print(datos)

# la diferencia entre json.load() y json.loads() está en el tipo de fuente desde donde se lee el JSON:
# - json.load()
#   Espera un objeto tipo archivo (como el que se obtiene con open()).
#   Se usa cuando vamos a leer JSON desde un archivo real.
# - json.loads()
#   Espera un string de texto que contenga JSON.
#   Se usa cuando tenemos el contenido JSON en una cadena (por ejemplo, descargado de internet o leído desde otro formato). """


#### ----------------- ####
# ejemplo extra.
""" # traemos dato de una API, los guardamos en una archivo json y luego los leemos.
import requests # para esto tenemos que instalarla, con el comando pip install requests, desde la terminal
# API de geolocalizacion
response = requests.get('http://ip-api.com/json/152.168.182.81')
data = json.loads(response.content)
# print(data)
with open('datos_ip.json', 'w+') as archivo:
    json.dump(data, archivo, indent=4)
    archivo.seek(0) # tenemos que volver el archivo al principio.
    datos = json.load(archivo)
    print(datos) """

# Se puede hacer con otro context manager sino.
""" with open('datos_ip.json', 'r') as archivo:
    datos = json.load(archivo)
    print(datos) """
#### ----------------- ####


#### ----------------- ####
# Ejemplo 1: crear un archivo json
""" # importamos la libreria json
import json

# creamos un diccionario de datos de usuarios
usuarios = {
    1: {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 30,
        'email': 'juan@example.com'
    },
    2: {
        'nombre': 'María',
        'apellido': 'Gómez',
        'edad': 25,
        'email': 'maria@example.com'
    },
    3: {
        'nombre': 'Pedro',
        'apellido': 'López',
        'edad': 35,
        'email': 'pedro@example.com'
    }
}

# imprimimos para ver en la consola como queda la estructura
print(usuarios)

with open("archivos/usuarios.json", 'w') as file:
    json.dump(usuarios, file, indent=4) # Serializa un objeto python como un objeto json. """
#### ----------------- ####


#### ----------------- ####
# Ejemplo 2: crear un archivo json
""" import json

# 1. Crear una lista de diccionarios (datos Python)
productos = [
    {
        "id": 101,
        "nombre": "Teclado mecánico",
        "precio": 59.99,
        "stock": True,
        "colores": ["negro", "blanco", "RGB"]
    },
    {
        "id": 202,
        "nombre": "Ratón inalámbrico",
        "precio": 29.95,
        "stock": False,
        "colores": ["negro", "gris"]
    },
    {
        "id": 303,
        "nombre": "Monitor 24 pulgadas",
        "precio": 159.00,
        "stock": True,
        "colores": None  # Ejemplo de valor nulo
    }
]


# 2. Guardar en un archivo .json
with open("productos.json", "w", encoding="utf-8") as archivo:
    json.dump(productos, archivo, indent=4, ensure_ascii=False)

print("\nArchivo 'productos.json' creado exitosamente!") """


# ensure_ascii=False --> Permite caracteres no-ASCII (ñ, acentos, etc.)
# json.dumps() --> Convierte objeto Python → cadena JSON (s de string)
# json.dump()	Escribe objeto Python → archivo JSON


# Regla mnemotécnica:
# dumps() = "dump string" → Salida en texto (s al final = string).
# dump() = "dump file" → Salida en archivo (sin s)


# otro ejemplo sencillo y rapido
""" import json

datos = [{"nombre": "Carlos", "edad": 30}, {"nombre": "Luisa", "edad": 25}]

# 1. dumps(): Python → String JSON
json_string = json.dumps(datos)
print(json_string)
print(type(json_string))

# 2. dump(): Python → Archivo JSON
with open("usuarios.json", "w") as archivo:
    json.dump(datos, archivo)  # Crea el archivo "usuarios.json" """
