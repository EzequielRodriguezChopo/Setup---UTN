#numero = 5
#while condicion:
#    print("Hola mundo")

'''
numero = 5
while numero < 10 :
    print("Hola mundo", numero)
    numero +=1
'''

'''
respuesta = input("Ingrese si ")

while respuesta != "si": respuesta = input("Ingrese si ")
#while respuesta != "si":
 #   respuesta = input("Ingrese si ")
print("El usuario ingreso si")
'''

'''
numero = 5

while numero < 10 :
    print(f"El numero es {numero}")
    numero +=1          #Si en el while encontramos un BREAK!!! no va a entrar al else, ese seria el unico caso
else:  
    print("Termino el bucle")
'''

'''
tabla = 1  # representa la tabla del 1

while tabla <= 5:
    print(f"Tabla del {tabla}")
    multiplicador = 1

    while multiplicador <= 10:
        resultado = multiplicador * tabla
        print(f"{tabla} * {multiplicador} = {resultado}")
        multiplicador +=1
    print()
    tabla +=1
'''

'''
numero = 1

while numero < 100:
    numero += 1

    if numero == 10:
        break
print("While terminado")
'''

'''
bandera = True

while bandera == True:
    print("1. Imprimir Hola Mundo. ")
    print("2. Imprimir Chau Mundo. ")
    print("3. Salir del menu. ")
    
    opcion = input("Ingrese una opcion a realizar: ")

    if opcion == "1":
        print("### Hola Mundo ###")
    elif opcion == "2":
        print("### Chau Mundo ###")
    elif opcion == "3":
        #break
        bandera = False                         #OJOOOOOO!!!! FIJATE QUE DIFERENCIA TIENE EL BREAK SOLO A LO QUE ESTA ESCRITO AHORA!!!!!
        continue
    else:
        print("Opción invalida")
    print("Llegue al fin del bucle, vuelvo a iterar")
print("Fin del programa")
'''

'''
for i in range(10):
    print(i)
'''

'''
mensaje = "Hola mundo"
print(f"Mensaje posee {len(mensaje)} letras")
for i in range(len(mensaje)):
    print(i)
'''

'''
mensaje = "Hola mundo"
print(f"Mensaje posee {len(mensaje)} letras")

print(f"Letra en indice 3: {mensaje[3]}")

for i in range(len(mensaje)):
    print(mensaje[i])
'''

'''
mensaje = "Hola mundo"

for i in range(len(mensaje) - 1):
    print(mensaje[i])
'''

'''

inicio = 10
fin = 20
saltos = 2

for i in range (inicio,fin,saltos):
    print(i)
'''

'''
# Numeros impares
inicio = 0
fin = 20
saltos = 2

for i in range (inicio,fin,saltos):
    if i % 2 != 0 :
        print(i)
'''

#------------------------------------------------------------------------------------------


'''
# 1- Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

numero = 0

while numero <10:
    numero += 1
    print(numero)
'''

'''
# 2- Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
numero = 11

while numero > 1:
    numero -= 1
    print(numero)
'''

'''
# 3- Mostrar la suma de los números desde el 1 hasta el 10.

numero = 0
sumatoria = 0
while numero < 10:
    numero += 1
    sumatoria = numero + sumatoria
print(f"La sumatoria de numeros es {sumatoria}")
'''

'''
# 4- Mostrar la suma de los números pares desde el 1 hasta el 10.

numero = 0
sumatoriaPar = 0

while numero < 10 :

    numero +=1
    #print(numero)

    if numero % 2 == 0:
        #print(f"El numero es {numero} par")
        #print()
        sumatoriaPar = numero + sumatoriaPar
print(f"La sumatoria de numeros pares del 1 al 10 es {sumatoriaPar}")
'''

'''
# 5- Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
#  Mostrar la suma y el promedio por pantalla.

cantidadNumerosIngresados = 5
contador = 0
acumulador = 0

while contador < 5 :
    valor = int(input("Ingrese un valor: "))
    contador += 1
    acumulador = acumulador + valor

promedio = acumulador/5

print(f"El prmedio de los valores ingresados es {promedio}")
'''


'''

# 6- Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

respuesta = 'si'
contador = 0
acumulador = 0

while respuesta == 'si' :
    valor = int(input("Ingrese un valor: "))
    contador +=1
    acumulador = valor + acumulador
    respuesta = input("Si desea ingresar un numero ingrese si: ")

promedio = acumulador / contador

print(f"La suma de los valores ingresadas es {acumulador} y el promedio es {promedio}")
'''

'''
# 7- Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

pregunta = 'si'
suma_positivos = 0
producto_negativos = 1

while pregunta == 'si':
    valor = int(input("Ingrese un valor: "))
    if valor > 0 :
        suma_positivos = valor + suma_positivos
    if valor < 0 :
        producto_negativos = producto_negativos * valor
    pregunta = input("Desea seguir ingreando valores? si/no ")

print(f"La suma de los valor positivos es {suma_positivos}")
print(f"La multiplicación de los numeros negativos es {producto_negativos}")
'''

contador = 0
valor_menor = 0
valor_mayor = 0

while contador < 10:
    print(f"{contador}")
    contador += 1
    valor = int(input("Ingrese un valor "))
    if contador == 1 :
        valor_menor == valor
        valor_mayor == valor
    if valor < valor_menor :
        valor_menor = valor
    if valor > valor_mayor:
        valor_mayor = valor
print(f"El valor menor es {valor_menor}")
print(f"El menor valor es {valor_mayor}")
