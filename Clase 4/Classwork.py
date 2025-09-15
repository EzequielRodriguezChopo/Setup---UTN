# Mostrar los numeros descendentes desde el 10 al 1

#for i in range(10):
#    print(i)
'''
numero = 10

for i in range(0, 10 , 1):
    print(i)

for i in range(10, 0 , -1):
    print(i)
'''
'''
----------------------------inicio = 10
----------------------------fin = 20
----------------------------saltos = 2

----------------------------for i in range (inicio,fin,saltos):
----------------------------    print(i)
'''


'''
cantidad_temperaturas = int(input("Ingrese la cantidad de productos: "))
variable = 10

for i in range(cantidad_temperaturas):
    temperatura = int(input("Ingrese el valor del producto: "))
    if variable < temperatura :
        variable = temperatura
print(f"El valor maximo es: {variable}")

cantidad_temperaturas = int(input("Ingrese la cantidad de temperaturas: "))
variable = float("inf")

for i in range(cantidad_temperaturas):
    temperatura = int(input("Ingrese el valor de temperatura: "))
    if variable > temperatura :
        variable = temperatura
print(f"El valor minimo es: {variable}")

# Con la tecla F2 podes modificar todas las variables seleccionando la variable que queres!!!!!
# variable = float("inf") le asignamos el valor + infinito
# variable = float("-inf") le asignamos el valor - infinito
'''
'''
cantidad_temperaturas = int(input("Ingrese la cantidad de temperaturas: "))
valor_minimo = float("inf")
valor_maximo = float("-inf")

for i in range(cantidad_temperaturas):
    
    temperatura = int(input("Ingrese el valor de la temperatura: "))
    
    if valor_maximo < temperatura :
        valor_maximo = temperatura
    
    if valor_minimo > temperatura :
        valor_minimo = temperatura

print(f"El valor maximo es: {valor_maximo}")
print(f"El valor minimo es: {valor_minimo}")
'''
'''
opcion = ""
valor_salida = "Salir"

while opcion != valor_salida :
    print("Menu principal")
    print("1. Jugar")
    print("2. Opciones")
    print("Escribe 'Salir' para cerrar el menú.")

    opcion = input("Elige una opción: ")

    if opcion == "Jugar":
        print("Ingresando al juego...")
    elif opcion == "Opciones":
        print("Ingresando a opciones...")
    elif opcion == valor_salida :
        print("Cerrrando menu...")
    else:
        print("Opción no validda. Vuelva a intentarlo.")
'''
'''
usuario_correcto = "martin"
clave_correcta = "clave123"

usuario_ingresado = input("Ingrese su usuario: ")
clave_ingresada = input("Ingrese su clave")

while usuario_ingresado != usuario_correcto or clave_correcta != clave_ingresada :
    
    print("Credenciales incorrectas.")
    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = input("Ingrese su clave")

print("Credenciales correctas.")
'''
'''
# Ingrese una una temperatura en 0° y 50° (Ejemplo de validación)

temperatura = int(input("Ingrese la temperatura (entre 0° y 50°):"))

while temperatura <= 0 or temperatura >= 50:
    temperatura = int(input("Rango invalido, ingrese la temperatura (entre 0° y 50°):"))

print("Temperatura valida.")
'''
'''
# Ingresa una nota entre 0 y 10

nota = int(input("Ingrese la nota (entre 0 y 10):"))

while nota < 0 or nota > 10:
    nota = int(input("Nota invalida, ingrese la nota (entre 0° y 50°):"))

print("Nota valida.")
'''

'''
fruta_ingresada = input("Ingrese un tipo de fruta: ('Banana', 'Manzana', 'Naranja') ")

while fruta_ingresada != 'Banana' and fruta_ingresada != 'Manzana' and fruta_ingresada != 'Naranja' :
    print("Fruta invalida")
    fruta_ingresada = input("Ingrese un tipo de fruta: ('Banana', 'Manzana', 'Naranja') ")

print("Fruta valida")
'''
'''
fruta_ingresada = input("Ingrese un tipo de fruta: ('Banana', 'Manzana', 'Naranja') ")
cantidad = int(input("Ingrese la cantidad "))

while (fruta_ingresada != 'Banana' and fruta_ingresada != 'Manzana' and fruta_ingresada != 'Naranja') or \
(cantidad >=1 or cantidad <= 10):
#(0 < cantidad < 10) :
    print("Fruta invalida")
    fruta_ingresada = input("Ingrese un tipo de fruta: ('Banana', 'Manzana', 'Naranja') ")

print("Fruta valida")
'''

'''
# numero_ingresado = int(input("Ingrese un numero: "))  ESTO ROMPE, LA IDEA ES QUE NO ROMPA....
validar_ingreso = False  #BANDERA
ingreso_validado = 0

while not validar_ingreso : # validar_ingreso == False
    #print("Hola")
    #validar_ingreso = True    #CAMBIO LA BANDERA PARA TERMINAR EL WHILE !!!!!!!!!!!!
    ingreso_numerico = input("Ingrese un número: ")
    for i in range(len(ingreso_numerico)):
        match ingreso_numerico[i]:
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
                validar_ingreso = False
                ingreso_validado = ingreso_validado + ingreso_numerico[i]
            case _:
                validar_ingreso = True
                break

ingreso_casteado = int(ingreso_validado)
print(f"Ingreso validado y casteado: {ingreso_casteado}")
print(type(ingreso_casteado))
'''

clave = 123456
#print(type(clave))
clave_ingresada = int(input("Ingrese su clave numerica: "))
contador = 1
while clave_ingresada != clave :
    print(f"Clave invalida. Intentos restantes {3-contador}")
    clave_ingresada = int(input("Ingrese su clave numerica: "))
    contador +=1
    if(contador == 3): break

if clave_ingresada == clave :
    print("Clave correcta")
else: 
    print("Clave incorrecta. No tiene más intentos")