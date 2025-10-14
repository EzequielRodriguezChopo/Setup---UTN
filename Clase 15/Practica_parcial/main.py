import funciones.aritmetica

#sumados = funciones.aritmetica.suma(2, 3)
#print(sumados)

def eliminar_primer_instancia(lista, elemento):
    

    for iterable in range(len(lista)):

        if elemento == lista[iterable]:
            
            lista = lista[iterable:]
            return lista
        else:

            pass

inventario = [
                ["Laptop", 15000.00, 10],
                ["Silla", 200.00, 50],
                ["Libro", 15.00, 100],
                ["Monitor", 300.00, 30]
]

def bubble_sort(inventario):
    longitud = len(inventario)
    for i in range(longitud-1):
        for j in range(longitud -1 -i):
            if inventario[j][1]<inventario[j+1][1]:
                aux = inventario[j+1][1]
                inventario[j+1][1]=inventario[j][1]
                inventario[j][1]=aux
    return inventario
inventario = bubble_sort(inventario)
print(inventario)