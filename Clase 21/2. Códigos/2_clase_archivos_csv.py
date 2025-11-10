##################################
# leer un archivo CSV

""" # Abrir el archivo en modo lectura
with open('archivos/empleados.csv', 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()
    print(lineas)
    
    # Extraer los encabezados (la primera línea)
    encabezados = lineas[0].strip().split(',')
    print("Encabezados:", encabezados)
    
    # Extraer los datos de cada empleado
    datos = []
    for linea in lineas[1:]:  # Saltamos la primera línea que contiene los encabezados
        # print(linea)
        fila = linea.strip().split(',')  # Eliminamos espacios y separamos por comas
        datos.append(fila)
    
    print("Datos:")
    for fila in datos:
        print(fila)
        
### Breve explicación ###
# ✅ lineas = archivo.readlines(): Lee todas las líneas del archivo y las almacena en una lista.
# ✅ encabezados = lineas[0].strip().split(','): Obtiene la primera línea del archivo, elimina 
# los espacios en blanco a los extremos con strip(), y luego divide la línea en una lista de encabezados usando split(',').
# ✅ Luego, recorremos el resto de las líneas para obtener los datos de cada fila, aplicando el 
# mismo proceso de eliminación de espacios y división por comas. """
##################################



##################################
# escribir un archivo CSV

# Definimos los encabezados y los datos
""" encabezados = ["nombre", "edad", "departamento", "salario"]
datos = [
    ["Pedro", "25", "Marketing", "2000"],
    ["Julieta", "39", "Finanzas", "4500"],
    ["Jose", "45", "Desarrollo", "6000"]
]

# Abrir el archivo en modo escritura
with open('archivos/empleados_nuevo.csv', 'w') as archivo:
    # Escribir los encabezados, unidos por comas
    archivo.write(','.join(encabezados) + '\n')
    
    # Escribir cada fila de datos
    for fila in datos:
        archivo.write(','.join(fila) + '\n')


### Breve explicación ###
# ✅ ','.join(encabezados): Une los elementos de la lista encabezados en una cadena de texto separada por comas.
# ✅ archivo.write(... + '\n'): Escribe cada línea en el archivo y añade un salto de línea al final. """
##################################



##################################
# buscar un empleado por su nombre
""" # Función para buscar el salario de un empleado por su nombre sin usar librerías externas
def buscar_salario_por_nombre(archivo_csv, nombre_buscado):
    with open(archivo_csv, mode='r') as archivo:
        encabezados = archivo.readline().strip().split(',')  # Leer y saltar la fila de encabezados
        for linea in archivo:
            nombre, edad, departamento, salario = linea.strip().split(',')
            if nombre.lower() == nombre_buscado.lower():
                return salario
        return None

# Uso de la función
archivo_csv = 'archivos/empleados.csv'
nombre_buscado = input('Ingresa el nombre del empleado: ')
salario_empleado = buscar_salario_por_nombre(archivo_csv, nombre_buscado)

if salario_empleado:
    print(f'El salario de {nombre_buscado} es {salario_empleado}.')
else:
    print(f'No se encontró ningún empleado con el nombre {nombre_buscado}.') """
##################################



##################################
# interaccion con un archivo .csv de Kaggle ---> https://www.kaggle.com/datasets/gregorut/videogamesales
""" with open('archivos/vgsales.csv', 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()
    
    # Extraer los encabezados (la primera línea)
    encabezados = lineas[0].strip().split(',')
    print("Encabezados:", encabezados)
    
    # Extraer los datos de cada empleado
    datos = []
    for linea in lineas[1:]:  # Saltamos la primera línea que contiene los encabezados
        # print(linea)
        fila = linea.strip().split(',')  # Eliminamos espacios y separamos por comas
        datos.append(fila)
    
    print("Datos:")
    for fila in datos:
        print(fila)
        if fila[0] == "23": # para que muestre solo 23 filas
            break """
##################################


##################################
# interaccion con un archivo .csv de Kaggle y ordenar por Global_Sales (ventas globales)
""" with open('archivos/vgsales.csv', 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()
    
    # Extraer los encabezados
    encabezados = lineas[0].strip().split(',')
    print("Encabezados:", encabezados)
    
    # Procesar los datos
    datos = []
    for linea in lineas[1:]:
        fila = linea.strip().split(',')
        # Convertir Global_Sales a float para ordenar
        fila[-1] = float(fila[-1])  # Último elemento es Global_Sales
        datos.append(fila)
    
    # Función para obtener el valor de Global_Sales
    def obtener_global_sales(fila):
        return fila[-1]
    
    # Ordenar por Global_Sales (descendente) usando función definida
    datos_ordenados = sorted(datos, key=obtener_global_sales, reverse=True)
    
    print("\nTop 23 juegos por ventas globales:")
    contador = 0
    for fila in datos_ordenados:
        # Convertir todos los elementos a string para imprimir
        fila_str = []
        for item in fila:
            fila_str.append(str(item))
        print(fila_str)
        
        # Mostrar solo 23 filas
        contador += 1
        if contador >= 23:
            break """
##################################



##################################
# leer un archivo CSV
""" def csv_to_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            print(line)
            # Eliminamos cualquier espacio y el salto de línea, luego separamos por comas
            row = line.strip().split(',')
            # Convertimos cada elemento a entero
            matrix.append([int(value) for value in row])
    return matrix

# Ejemplo de uso
filename = 'numeros.csv'  # Reemplaza con el nombre de tu archivo CSV
matrix = csv_to_matrix(filename)
print(matrix) """
##################################