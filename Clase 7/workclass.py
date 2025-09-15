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

