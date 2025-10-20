def agregar(lista:list, elemento:any)->list:
    """
    Agrega un elemento nuevo al final de la lista.

    Argumentos:
        lista: list lista que se le agrega el elemento
        elemento: any elemento que se le agrega a la lista
    
    Retorno:
        Retorna la lista introducida con el elemento agregado.

    """

    lista += [elemento]

    return lista

# Uso practico de la funcion # 
variable = True
lista = ["salame", 2, "jorgito de chocolate", 25]

print(agregar(lista, variable))
