# En el ordenamiento de burbuja, el primer bucle for i in range(n-1) 
# recorre el arreglo hasta la penúltima posición porque no es necesario 
# llegar hasta el último elemento en este bucle.

# range(n-1) en el bucle externo: El objetivo de este bucle externo es 
# controlar las pasadas necesarias para ordenar completamente el arreglo.
# Cada iteración coloca el elemento más grande restante en su lugar final. 
# Una vez que el último elemento está ordenado, no es necesario hacer otra pasada.
# Como la última comparación en cada pasada es entre los elementos n-2 y n-1, 
# la última pasada ya no necesita revisar el último elemento, de ahí el n-1.
# Si el bucle externo recorriera hasta n, haría una iteración adicional 
# innecesaria, ya que el último elemento estará ordenado después de las primeras n-1 pasadas.

# ordenamiento burbuja sin variable auxiliar
""" def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)
print(elementos) """



# ordenamiento burbuja con variable auxiliar
def ord_burbuja(arreglo):
    n = len(arreglo)
    
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                aux = arreglo[j+1]
                arreglo[j+1] = arreglo[j]
                arreglo[j] = aux

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)
print(elementos)



# ordenamiento burbuja con bucle while
""" def ord_burbuja(lista):
    n = len(lista)
    intercambiado = True  # Variable para verificar si hubo un intercambio
    while intercambiado:
        intercambiado = False  # Suponemos que no habrá intercambios
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                # Intercambiamos los elementos si están en el orden incorrecto
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True  # Hubo un intercambio
        n -= 1  # Reducimos el rango de comparación

numeros = [64, 34, 25, 12, 22, 11, 90]
ord_burbuja(numeros)
print(numeros) """