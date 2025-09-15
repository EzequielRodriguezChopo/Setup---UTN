def sumar(a:int, b:float):
    """
    Esta funcion hace una suma
    # Argumentos
        - a = Es un numero
        - b = Es otro numero
    """
    return a + b

def restar(a=0, b=0):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):

    if b == 0:
        return "Error: division por 0"
    else:
        return a/b
