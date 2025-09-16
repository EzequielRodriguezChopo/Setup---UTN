#Escribir una funcion que calcule el area de un rectangulo. La función recibe la base y la altura y retorna el area
'''
from math import pi

def calcular_area(base,altura):
    area = base * altura
    return area

base = float(input("Ingrese la Base: "))
altura = float(input("Ingrese la Altura: "))

area = calcular_area(base,altura)
print(area)
print(pi)
print(2%2)
'''
# Define una función que encuantre el maximo de ters numeros. La función debe aceptar tres argumentos 
# y devolver el numero mas grande.
'''
def maximo_numero(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num3:
#   elif num2 <= num1 and num2 <= num3:  ES REDUNDANTE
        return num2
    else:
        return num3

print(maximo_numero(3,5,6))
'''

# Diseñar una funcion que calcule la potencia de un número. La función debe recibir la base y 
# el exponente como argumentos y devolver el resultado

# Hecho una papa

# Crear una función que imprima la tabla de multiplicar de un número recibido como parametro.
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación.
# Por defecto es del 1 al 10.

def tabla_multiplicar (numero, inicio=1 , fin = 10):
    
    for i in range(inicio, fin + 1):
        resultado = i * numero
        print(f"Numero {numero} x {i} = {resultado}")

numero = int(input("Ingrese un número: "))
opcion = input("Desea ingresar el inicio y el fin? Si - No: ")

if(opcion == "Si"):
    inicio = int(input("Ingrese el inicio: "))
    fin = int(input("Ingrese el fin: "))
    tabla_multiplicar(numero, inicio, fin)
else:
    tabla_multiplicar(numero)
