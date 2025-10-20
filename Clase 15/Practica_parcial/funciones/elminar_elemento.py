'''
Eliminar primera ocurrencia

Nombre de la función:
eliminar_primer_instancia(lista, elemento)

Objetivo:
Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.

Tarea:
Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.
Si el elemento no existe, retornar None y dejar la lista sin cambios.
Ejemplo: Si la lista es [5, 3, 5, 7] y se elimina 5, la lista queda [3, 5, 7] y se retorna 5.


'''

def eliminar_primer_instancia(inventario, elemento):
    

    for i in range(len(inventario)):

        if elemento == inventario[i]:
            
            inventario = inventario[:i] + inventario[i+1:]

            return inventario
        else:

            pass


lista = [5, 3, 5, 7]
variable = 5

print(eliminar_primer_instancia(lista, variable))