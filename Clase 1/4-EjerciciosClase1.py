'''
#/1
valorA = int(input("Ingrese el valor A: "))
valorB = int(input("Ingrese el valor B: "))

print(f"Valor A: {valorA}, valor B: {valorB}")

auxiliar = valorA
valorA = valorB
valorB = auxiliar

print(f"Valor A: {valorA}, valor B: {valorB}")
'''

'''
#2
numero = float(input("Ingrese un número flotante: "))
numeroEntero = int(numero)
numeroCadena = str(numero)
print(f" El numero ingresado es {numero}, del tipo {type(numero)}")
print(f" El numero ingresado es {numeroEntero}, del tipo {type(numeroEntero)}")
print(f" El numero ingresado es {numeroCadena}, del tipo {type(numeroCadena)}")
'''

'''
#3
nombre = "Ezequiel"
apellido = "Rodriguez"
edad = 37
print(f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años.")
'''

'''
#4
base = float(input("Ingrese la base del traingulo: "))
altura = float(input("Ingrese la altura del triangulo"))
area = base * altura / 2
print(f"El area del triangulo es de {area}")
'''

'''
#5
variable1 = 8
variable2 = 6.3
variable3 = 9
variable4 = 5.8
variable5 = 3

promedio = (variable1 + variable2 + variable3 + variable4 + variable5)/5

print(f"El valor del promedio es de {promedio}")
'''
'''
#6
cantidad = float(input("Ingrese la cantidad en metros: "))
cantidaEnCentimetros = cantidad * 100
cantidadEnMilimetros = cantidad * 1000
cantidadEnPlugadas = (cantidad * 100) / 2.54
print(f"La cantidad ingresada es {cantidad}")
print(f"La cantidad ingresada en centimetros es {cantidaEnCentimetros}")
print(f"La cantidad ingresada en milimetros es {cantidadEnMilimetros}")
print(f"La cantidad ingresada en pulgadas es {cantidadEnPlugadas}")
'''

'''
#7
edad1 = 25
edad2 = 26
edad3 = 25

if(edad1 == edad2 == edad3):
    print("Las tres edad son iguales")
else:
    print("Las tres esdades no son iguales")
'''

'''
#8
precio_a = 25
precio_b = 25

if precio_a < precio_b :
    print("El precio_a es mayor al precio_b")
elif precio_a > precio_b :
    print("El precio_b es mayor al precio_a")
else:
    print("Los precios son iguales")
'''

'''
#9

# palabra = "Perrito"
# print(f"La palabra mide {len(palabra)} letras")

palabra1 = "Perro"
palabra2 = "perros"

if len(palabra1) > len(palabra2):
    print("Palabra2 es mayor que Palabra1")
elif len(palabra1) < len(palabra2):
    print("Palabra2 es mayor que Palabra1")
else: 
    print("El tamaño de la palabras son iguales")
'''

'''
#10
x = 2
if x >= 10 and x <= 20 :
    print(f"El valor {x} esta entre el 10 y 20")
else:
    print(f"El valor {x} no esta entre 10 y 20")
'''

'''
#11
distancia_a = 25
distancia_b = 10

if distancia_a <= distancia_b :
    print("La distancia_a es menor e igual a la distancia_b")
else:
    print("La distancia_a es mayor a la distancia_b")
'''

'''
#12
numeroA = 3
numeroB = 9
numeroC = 21

if numeroC > numeroB :
    if numeroB > numeroA :
        print("Estan ordenados ascendentemente")
    else:
        print("No estan ordenados ascendentemente")
else:
    print("No estan ordenados ascendentemente")
'''

'''
#13
numero_n = 135
resultado = numero_n%3
#print(resultado)
if resultado == 0 and numero_n > 50 :
    print("El resultado es multiplo de 3 y mayor a 50")
else:
    print("El resultado no es multiplo de 3 o mayor a 50")
'''

print(7 == 7)