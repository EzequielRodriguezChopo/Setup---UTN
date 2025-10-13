# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# Validaciones a realizar: 
# Que el programa no rompa al ingresar un valor no numerico
# Que el ingreso contenga un '.' cómo máximo

'''

def validar_ingreso_flotante()-> float:
    ingreso_valido = False
    ingreso = input("Ingrese un número: ")
    while not ingreso_valido:
        contador_comas = 0
        primer_vuelta = True
        for i in range(len(ingreso)):
            match ingreso[i]:
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    ingreso_valido = True
                case "-": 
                    if not primer_vuelta:
                        print("Ingreso invalido.")
                        ingreso = input("Ingrese un número: ")
                        ingreso_valido = False
                        break
                case ".":
                    contador_comas += 1
                    if contador_comas > 1:
                        print("Ingreso invalido.")
                        ingreso = input("Ingrese un número: ")
                        ingreso_valido = False
                        break
                case _:
                    print("Ingreso invalido.")
                    ingreso = input("Ingrese un número: ")
                    ingreso_valido = False
                    break
            if primer_vuelta:
                primer_vuelta = False
    return float(ingreso)

ingreso_validado = validar_ingreso_flotante()
print("Ingreso validado: ", ingreso_validado)

'''

# Definir una función que reciba como parametro un str y devuelva la cantidad de LETRAS que contiene dicha cadena
# EJ: contar_letras("Hola mundo") -> 9 letras
# EJ: contar_letras("Hola                mundo") -> 9 letras
# EJ: contar_letras("Hola     124    mundo") -> 9 letras
'''
def contar_letras (palabra : str):
    cantidad_letras = 0
    for i in range(len(palabra)):
#  if(mensaje[i])>= "a" and mensaje[i]<="z") or(mensaje[i])>= "A" and mensaje[i]<="Z")   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
        #if(palabra[i]!=" "):
        #    cantidad_letras +=1
        #elif ord(palabra[i]) >= 48 and ord(palabra[i]<= 57):
        #    cantidad_letras -=1
'''
    return cantidad_letras

palabras = input("Ingrese una palabra: ")

cantidad_de_letras = contar_letras(palabras)

print(cantidad_de_letras)
'''

# Definir una función que reciba como parametro un str y devuelva la cantidad de palabras que contiene dicha cadena
# EJ: contar_palabras("Hola mundo") -> 2 Palabras
# EJ: contar_palabras("Hola                mundo") -> 2 Palabras
# EJ: contar_palabras("Hola     124    mundo") -> 3 Palabras
'''

def contar_palabras(mensaje):
    cantidad_palabras = 0
    contador_letras = 0
    for i in range(len(mensaje)):
        if (mensaje[i] != " "):
            contador_letras +=1
        else:
            if(contador_letras > 0):
                cantidad_palabras = 1 + cantidad_palabras
            contador_letras = 0
    return cantidad_palabras

cadena = input("Ingrese una cadena de texto: ")
total_palabras = int(contar_palabras(cadena))
print(total_palabras)
'''

# Tarea 1:
# Definir una función que reciba como parametro un str y, para cada palabra dentro del texto, 
# imprima la cantidad de vocales que contiene
# EJ: contar_vocales("Hola mundo") -> 4 vocales

################################################################################################################
'''
# Definir una función que reciba como parámetro un str y devuelva la cantidad de LETRAS que contiene dicha cadena.

# EJ: contar_letras("Hola mundo") -> 9 letras 
# EJ: contar_letras("Hola              mundo  ") -> 9 letras
# EJ: contar_letras("Hola    124          mundo  ") -> 9 letras

def validar_caracter_alfabetico(caracter: str)-> bool:
    if (caracter >= "a" and caracter <="z") or (caracter >= "A" and caracter<="Z"):
        return True
    return False

def contar_letras(mensaje:str) -> int:
    contador_letras = 0
    for i in range(len(mensaje)):
        if validar_caracter_alfabetico(mensaje[i]):
            contador_letras += 1
    return contador_letras

mensaje_ingresado = input("Ingrese su mensaje: ")

cantidad_letras_en_mensaje = contar_letras(mensaje_ingresado)
print(f"mensaje ingresado: {mensaje_ingresado} \n letras en mensaje: {cantidad_letras_en_mensaje}")
'''
################################################################################################################
'''
# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# Validaciones a realizar: 
# Que el valor retornado no sea un a cadena vacía -> ""
# Que el valor retornado no sea una cadena con solo espacios -> "  "

def validar_ingreso_cadena()-> str:
    ingreso_valido = False
    ingreso = input("Ingrese una cadena: ")
    while not ingreso_valido:
        contador_espacios = 0
        if ingreso == "": 
            ingreso = input("Ingreso invalido. Ingrese una cadena: ")
        else:
            for i in range(len(ingreso)):
                if ingreso[i] == " ":
                    contador_espacios += 1
            if contador_espacios == len(ingreso):
                ingreso = input("Ingreso invalido. Ingrese una cadena: ")
            else: 
                ingreso_valido = True
    return ingreso

ingreso_validado = validar_ingreso_cadena()
print("Ingreso validado: ", ingreso_validado)
'''
################################################################################################################
'''
# Definir una función que reciba como parámetro un str y devuelva la cantidad de PALABRAS que contiene dicha cadena.

# EJ: contar_palabras("Hola mundo") -> 2 palabras 
# EJ: contar_palabras("Hola              mundo  ") -> 2 palabras
# EJ: contar_palabras("Hola    124          mundo  ") -> 3 palabras
# EJ: contar_palabras("Hola    124          mundo  ") -> 2 palabras

def validar_caracter_alfabetico(caracter: str)-> bool:
    if (caracter >= "a" and caracter <="z") or (caracter >= "A" and caracter<="Z"):
        return True
    return False

def contar_palabras(mensaje:str) -> int:
    contador_palabras = 0
    dentro_de_palabra = False
    for i in range(len(mensaje)):
        if mensaje[i] != " " and not dentro_de_palabra:
            dentro_de_palabra = True
            contador_palabras += 1
        elif mensaje[i] == " ":
            dentro_de_palabra = False
    return contador_palabras

print(contar_palabras(""))
'''

'''
# Tarea 1:
# Definir una función que reciba como parametro un str y, para cada palabra dentro del texto, 
# imprima la cantidad de vocales que contiene
# EJ: contar_vocales("Hola mundo") -> 4 vocales
'''