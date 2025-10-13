'''
def contar_iterativo (numero):
    for i in range(numero,-1,-1):
        print(i)

contar_iterativo(8)

def contar_recursivo(numero):
    if numero < 0 :
        return
    print(numero)
    contar_recursivo(numero - 1)

contar_recursivo(8)
'''

'''
def factorial_recursivo(numero):
    if numero == 0:
        return 1

    return numero * factorial_recursivo (numero -1)
print(factorial_recursivo(5))
'''
# Fibonacci

'''
def fibonacci (numero):
    if numero == 0:
        return 0
    if numero == 1 :
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

print(fibonacci(6))

# VisualGO.net   ---   Recursion tree

'''

# Forma Recursiva

def fibonacci (numero):
    a = 0
    b = 1
    for _ in range(numero):
        c = a + b
        a = b
        b = c
    return

print(fibonacci(6))

