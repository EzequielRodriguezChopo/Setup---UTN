#DEPURACION: Es checkear un error
#Abstraccion: La funcion es una caja negra que le ingreso algo y sale otra cosa
# control + B elimina el cuadro izquierdo
# Hasta ayer vimos programacion orientada a estructuras
# Estamos aprendiendo ahora programación funcional

'''
def saludar ():    # Esto se llama CABECERA o FIRMA de la función
    saludo = "Estoy saludadndo desde la función"
    print(saludo)

saludar()

print("Termino nuestro épico programa")
'''

'''
def saludar ():    # Esto se llama CABECERA o FIRMA de la función
    saludo = "Estoy saludadndo desde la función"
    return saludo

saludar()

print(saludar())
print("Termino nuestro épico programa")
'''

'''
def saludar_con_nombre (nombre):                    # Los parametros que estan en CABECERA de la función se llaman "parametros formales"
    saludo = f"Hola, como andas {nombre}?"
    return saludo

saludar_con_nombre( "Tomas")                        # En la llamada de la función se llama "parametros actuales"

variable = saludar_con_nombre( "Ezequiel")          # En la llamada de la función se llama "parametros actuales"
print(variable)

name = input("Ingrese su nombre: ")
variable = saludar_con_nombre(name)          # En la llamada de la función se llama "parametros actuales"
print(variable)

print("Termino nuestro épico programa")             #Lo que sale le debe llegar lo mismo a la función, sino se rompe
'''

'''
def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

def restar(num1, num2, tp):
    resultado = num1 - num2 - tp
    return resultado

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

pi=3.14

suma = sumar(numero1,numero2)
resta = restar(num1 = numero2 , num2 = numero1, tp=pi)

print(f"El valor de la suma es {suma}")
print(f"El valor de la resta es {resta}")
'''

'''
def sumar(num1=0, num2=0):          #Para que no rompa le mandamos un 0 y no rompe nunca
    resultado = num1 + num2
    return resultado

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

suma = sumar(numero1)


print(f"El valor de la suma es {suma}")
'''


'''
def sumar(num1=0, num2=0):          #Para que no rompa le mandamos un 0 y no rompe nunca
    resultado = num1 + num2
    return resultado

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

suma = sumar(numero1,numero2)

print(f"El valor de la suma es {suma}")
'''

############################# FUNCIONES INCORPORADAS DEL LENGUAJE #################################
'''
print("Hola",end="-")
print("Chau")
'''

'''
x = 5

def ejemplo():
    y = 10
    print(x)
    print(y)

ejemplo()
'''
        # EL "=" es el operador de la asignación         
#           a = 5
      # El "a" es el puntero

# El puntero apunta a:
#   PyOjb
#   id=145
#   value=5
#   Type=int
'''
y = 1

def ejemplo(y):
    y = 10
    print(id(y))

ejemplo(y)

print(id(y))
'''

# Algo mutable seria una lista:  (Es mutable porque cambio el valor, pero no cambio su "id") ESO ES MUTABILIDAD
                                        # Un valor comun se puede modificar y cambia su "ID" NO ES MUTABLE
'''
lista = [1, 2, 3]

print(lista)
print(id(lista))

def agregar_elemento(lista, e):
    lista.append(e)                 # Agrega dentro un nuevo elemento
                                    # Una lista tiene funciones para modificar su valor, sin modificar su ID
                                    # Aquellos que son inmutables son los char, int, float
agregar_elemento(lista, 4)

print(lista)
print(id(lista))
'''


########################## DOCUMENTACION ######################################

# Documentacion se llama "DOCSTRING" lo que esta entre """ """

'''
def sumar(numero_a,numero_b):
    """    Breve explicación de lo que hace
    Que parametros acepta
    Que devuelve"""
    suma = numero_a + numero_b
    return suma
'''

'''
def sumar(numero1: int | float, numero2 : int) -> int | float:     # Se lama sugerencia de tipos
    """   
    *Esta funcion suma dos números* \n
    # Argumentos 
        - numero1: primer numero a sumar 
        - numero2: segundo entero a sumar 
    retorno:
        - resultado de la suma de numero1 y numero2
    """
    suma = numero1 + numero2
    return suma

sumar(4,3)              # Pone el cursor sobre sumar y fijate como queda documentado, unluuuuujo
'''

def saludar_nombre(nombre:str):
    saludo = f"Hola como andas {nombre}"           # Como sugerimos que es un str, al poner un punto en {nombre.}
                                                    # te aparecen todos los metodos de string
    return saludo

print(saludar_nombre("Valeria"))
