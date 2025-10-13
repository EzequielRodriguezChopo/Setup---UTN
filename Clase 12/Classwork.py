# Ya vieron un ejemplo de matriz

'''
numeros = [[12, 54, 435],
           [77, 87, 56],
           [1, 24, 65]]

def buscar_en_matriz(lista,numero):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if numero == lista[i][j]:
                return f"Fila: {i} - Columna: {j}"

resultado = buscar_en_matriz(numeros, 177)

if resultado == None:
    print("No se encontro el nnumero")
else:
    print(f"El numero 77 se encontro en la poscion {resultado}")
'''
# Muestre aquellos productos mayor o menor a 4000
# De esos productos cual es de mayor stock
# De estos productos cual es el de mayor precio
# MAXIMOS, MINIMOS, ORDENAMIENTO, FILTROS, QUE YO QUIERA AGEGAR UN ELEMENTO (def agregar)
# Borrar todos los productos, "Vaciar la Matriz"
# Va a pedir un menú:
# 0 - Agregar un producto
# 1 - Ver cual es el producto de mayor precio
# Ver si existe el "x" producto, sino existe, debe imprimir "No existe el producto"


######## Ejemplo parcial PONELE

'''

productos = [["Coca-Cola", 2500, 5],
             ["Hambuguesa", 5000, 8],
             ["Alfajor", 1500, 6]]
def buscar_en_matris(lista,producto):
    if len(productos) == 0:
        print("No hay productos en la lista")
        return None
    for i in range(len(lista)):
        if producto == lista[i][0]:
            print(f"Aca te mostraba los productos")
            pass   # "El profe borro todo juajaja"

def mostrar_maximo(productos):
    if len(productos)== 0:
        print("No hay productos en la lista")
        return None
    maximo = productos[0]

    for i in range(len(productos)):  # for i in range(1,len(productos)): "Asi no pregunta si Coca-Cola es Coca-Cola"
        if productos[i][1] > maximo[1]:
            maximo = productos[i]
    return maximo

resultado_maximo = mostrar_maximo(productos)
print(resultado_maximo)


'''

'''
# Ejercicio 1
# Crea un programa que encuentre el valor más grande en una matriz de enteros.
# Restricciones :
# No uses listas por compresión, métodos de listas(como, max()), ni funciones integradas salvo len() y range()
# Ejemplo: para un matriz:

matriz=[[5,3,2,8],
        [7,6,65,8],
        [22,63,8,90]
]

def valor_mas_grande(datos):

    if len(datos) == 0:
        return "Lista vacia"
    
    maximo = 0

    for i in range(len(datos)):
        for j in range(len(datos[i])):
            if maximo <= datos[i][j]:
                maximo = datos[i][j]
    return maximo
#print(len(matriz))
resultado = valor_mas_grande(matriz)
print(f"El resultado mas grande es {resultado}")
'''


'''
# Ejercicio 2
# Desarrollar una función que perciba por parametro una matriz (lista de listas de números)
# y un número especificado. La función debe buscar el número en toda la matriz y retornar True si existe.
# Si no existe, retornar False

matriz=[[5,3,2,8],
        [7,6,65,8],
        [22,63,8,90]
]

print("\nIngrese una opción\n")
print(" 1 - Ingresar valor")
print(" 2 - Salir \n")
opcion = int(input("Ingrese una opción: "))

while(opcion == 1):

    valor_buscado = int(input("\nIngrese un valor: "))

    def buscar_valor(datos, numero):

        if len(datos) == 0:
            return "Lista vacia"

        for i in range(len(datos)):
            for j in range(len(datos[i])):
                if datos[i][j] == numero :
                    return True
        return False

    resultado = buscar_valor(matriz,valor_buscado)

    print(f"\nEl resultado es : {resultado}")

    print("\nIngrese una opción\n")
    print(" 1 - Ingresar valor")
    print(" 2 - Salir \n")
    opcion = int(input("Ingrese una opción: "))

print("\nPrograma terminado\n")
'''

# Ejercicio 3
# Desarrollar una función que reciba una matriz (lista de lista de números) y un numero especifico.
# La función debe buscar el número en toda la matriz y retornar una lista con todas las posiciones donde se encuentra
# (como lista de fila y columna). Si el número no se encuantra en la matriz, imprimir el mensaje 
# "El número no se encuentra en la matriz".

matriz=[[5,36,2,82],
        [71,6,65,8],
        [22,6,8,90]
]

print("\nIngrese una opción\n")
print(" 1 - Ingresar valor")
print(" 2 - Salir \n")
opcion = int(input("Ingrese una opción: "))

while(opcion == 1):

    valor_buscado = int(input("\nIngrese un valor: "))

    def buscar_valor(datos, numero):

        if len(datos) == 0:
            return "Lista vacia"

        for i in range(len(datos)):
            for j in range(len(datos[i])):
                if datos[i][j] == numero :
                    return [i,j]
        return False

    resultado = buscar_valor(matriz,valor_buscado)
    if resultado == False:
        print("\nEl resultado no se encuantra en la matriz")
    else:
        print(f"\nEl resultado es se encuantra en la Fila: {resultado[0]} Columna: {resultado[1]}")

    print("\nIngrese una opción\n")
    print(" 1 - Ingresar valor")
    print(" 2 - Salir \n")
    opcion = int(input("Ingrese una opción: "))

print("\nPrograma terminado\n")