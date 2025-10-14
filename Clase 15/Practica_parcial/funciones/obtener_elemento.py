'''
Obtener indice

Nombre de la función:

obtener_indice(lista, elemento)

Objetivo:
Encontrar el índice de la primera ocurrencia de un elemento en la lista.

Tarea:
Buscar en la lista el elemento recibido y retornar su posición (índice).
Si el elemento no existe en la lista, retornar -1.

'''
def obtener_indice(lista, elemento):
    
    for indice in range(len(lista)):

        if elemento == lista[indice]:
            
            resultado = indice

            return resultado

        else:

            resultado = -1
    
    print('Valor no encontrado, por lo tanto se entrega: ')
    return resultado       

lista = [1, 2 , 3 , 4 , 5 , 6] # Lista Ejemplo

variable = 2 # Elemento ejemplo
#variable = input('Introduce un valor, para agregar: ') # caso que el usuario quiera buscar algun valor en la lista
# Este caso solo funciona con String, sino entra ya con validaciones

print(obtener_indice(lista, variable))


