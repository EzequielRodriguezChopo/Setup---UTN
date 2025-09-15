'''
temperatura = 28

if not temperatura > 30 :   # if not (false)   # if true
    print(f"La temperatura es.... {temperatura}")
'''

'''
temperatura = 28

if not temperatura > 30 : print(f"La temperatura es.... {temperatura}")
print("Hola")
'''


'''
# Mirar si un numero es divisible por 2 o por 5

numero = int(input("Ingrese un numero "))
resultado2 = numero % 2
if resultado2 == 0:
    print("El numero es divisible por 2")
else:
    print("El resultado no es divisible por 2")
resultado5 = numero % 5
if resultado5 == 0:
    print("El numero es divisible por 5")
else:
    print("El resultado no es divisible por 5")

#-----------------------------------------------------------

if resultado2 == 0 or resultado5 == 0 :
    print("El resultado es divisible por 2 o por 5")
else:
    print("El resultado no es divisible por 2 o 5")
'''

#Verificar si un numero esta entre 10 y 20 o es negativo

'''
numero = int(input("Ingrese un numero: "))

if (numero > 10 and numero < 20) or numero < 0:
    print(f"El numero {numero} esta entre 10 y 20 o es negativo")
else:
    print(f"El numero {numero} no esta entre 10 y 20 o es no negativo")
'''

'''
A partir del ingreso de la altura en centimetros de un jugador de baloncesto, el programa
debera determinar la posicion del jugador en la cancha, considerando los siguientes
parametros:
Menos de 160cm: Base
Entre 160cm y 179cm : Escolta
Entre 180cm Y 199cmCM: Alero
200cm o más: Ala-Pivot O Pivot
'''
'''
altura = float(input("Ingrese la altua del jugador "))
if altura < 160:
    print("Su posición es Base")
elif altura >= 160 and altura <= 179 :
    print("Su posición es Escolta")
elif altura >= 180 and altura <= 199 :
    print("Su posición es Alero")
elif altura >= 200 :
    print("Su posición es Ala-Pivot o Pivot")
'''

'''
Calcular una nota que ingrese el usuario ente el 1 y el 10 inclusive, para luego
mostrar un mensaje segun el valor:
6,7,8,9, y 10   ---> Promocion directa, la nota es ...
4 y 5           ---> Aprobado, la nota es ...
1,2 y 3         ---> Desaprobado, la nota es ...
'''
'''
nota=int(input("Ingrese la nota del 1 a 10 "))
if nota >=1 and nota <=3:
    print(f"Desaprobado, la nota es {nota}")   
elif nota >=4 and nota <=5 :
    print(f"Aprobado, la nota es {nota}") 
elif nota >=6 and nota <=10 :
    print(f"Promocion directa, la nota es {nota}")

match nota:
    case 1 | 2 | 3:
        print(f"Desaprobado, la nota es {nota}") 
    case 4 | 5 :
        print(f"Aprobado, la nota es {nota}")
    case 6 | 7 | 8 | 9 | 10 :
        print(f"Promocion directa, la nota es {nota}")
    case _:
        print("Opción ingresada incorrecta")
'''
'''
Una agencia de viajes nos pide informar si hacemos viajes a lugares segun la estación del año.
En caso de hacerlo mostrar por print el mensaje "Se viaja", caso contrario mostrar "No se viaja".
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del Plata y Cataratas.
Si es otoño: se vaja a todos los lugares.
Si es primavera: Se viaja a todos los lugares menos Bariloche.
'''
estacionDelAño=input("Ingrese la estacion del año que quiere viajar: ")
opcionCliente=input("A donde desea viajar: ")
match estacionDelAño:
    case 'invierno' :
        if opcionCliente == 'Bariloche':
            print("Se viaja.")
        else:
            print("No se viaja.")
    case 'verano':
        if opcionCliente == 'Mar del Plata' or opcionCliente == 'Cataratas':
            print("Se viaja.")
        else:
            print("No se viaja.")
    case 'otoño':
        print("Se viaja")
    case 'primavera':
        if opcionCliente == 'Bariloche':
            print("No se viaja.")
        else:
            print("Se viaja.")
    case _:
        print("Estación ingresada incorrecta.")











































#     *23571113/   LABS-UTNFRA