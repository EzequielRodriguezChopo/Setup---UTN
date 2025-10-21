'''
datos = [1,2,3,4,5,6]

print(datos)

datos.append(55)
print(datos)

#datos.clear()  # Solo la vacia, no la borra, oasea sigue estando en la misma posicion de memoria
#print(datos)

datos1 = datos.copy()
print(datos1)

#print(id(datos))
#print(id(datos1))

datos.append(77)
print(datos)
print(datos1)



datos1 = datos # AL HACER ESTO FIJATE QUE AMBAS SE MODIFICAN A LA VEZ,
               # PORQUE APUNTAN A LA MIMSA POSICION DE MEORIA
print(datos1)

#print(id(datos))
#print(id(datos1))

datos.append(77)
print(datos)
print(datos1)

'''
##############################################################################################
'''

datos = [1,2,3,4,[65,87],5]

print(datos)

datos1 = datos.copy()
print(datos1)

datos.append(77)
datos[4][0]="chau"
print(datos)
print(datos1)
# Fijate que aca pasa lo mismo, el copy no copia el "77", porqu es un copia superficial
# peeero, si modifica las sublistas dentro an ambos datos y dato1, pero no copia el 77, OJOTA

'''

###########################################################################3

'''
datos = [1,2,3,4,5,"Hola","Chau", 2, 2, 77]

print(datos)

#print(datos.count(5))
#print(datos)

#datos.extend("Python")
#print(datos)   #    [1, 2, 3, 4, 5, 'Hola', 'Chau', 2, 2, 77, 'P', 'y', 't', 'h', 'o', 'n']

datos.extend([65,78,56,12,3])   #Agrego varias cosas de una sola vez
print(datos)

'''

##############################################################################


'''

datos = [1,2,77,4,5,"Hola","Chau", 2, 2, 77]
print(datos)
print(datos.index(77,3))  # Arranca a partir del indice 3 y busca el 77, me devuelve la posción

'''
#################################################################
'''
datos = [1,2,77,88,"Hola","Chau", 4, 5, 77]
print(datos)

datos.insert(2,"Python") # Inserta en tal (2) posición que querramos ("Python")
print(datos)


datos.insert(40,"Python") # Lo agrega al final de la lista
print(datos)

'''

##########################################################################
'''
datos = [1,2,77,88,"Hola","Chau", 4, 5, 77]
print(datos)

print(datos.pop()) # Así elimina el ultimo utim de la lista
print(datos)

print(datos.pop(1)) # Borra lo que esta en el indice 1, y te lo devuelve
print(datos)

#print(datos.pop(88)) # Rompe como loco, le puse un indice que no existe
#print(datos)
'''

################################################################

'''
datos = [1,2,77,88,"Hola","Chau", 4, 5, 77,87]
print(datos)

datos.remove(87) 
print(datos)
'''
#####################################################################

'''
datos = [1,2,77,88, 4, 5, 77,87]
datos1 = [1,2,77,88, 4, 5, 77,87]
print(datos)

datos.sort()
print(datos)
datos1.sort(reverse = True) 
print(datos1)
'''

##########################################################################
# Ejemplo post recreo

lista = [1,2,3,4,5]

print(sum(lista)) # Hace la sumatoria de lo que esta dentro, solo numeros

# any() Devuelve True o False, despendiendo de los true y false
# all() Solo devuelve True si todo es verdadero

nombres = ["Ana","Luis","Carlos","Valeria"]

print(list(enumerate(nombres))) #Lo tuvo que pasar a lista (Te devuelve "DUPLAS")

for i, nombre in enumerate(nombres):
    print(f"En la posición {i} esta {nombre}")

print("\n")

for i, nombre in enumerate(nombres, start=77):
    print(f"En la posición {i} esta {nombre}")

apellidos = ["Martinez","Marino","Rodriguez","Zotti"]
edad = [23,34,42]
ciudades = ["BsAs","BsAs","BsAs","BsAs"]
print(f"\n{list(zip(nombres,apellidos,edad,ciudades))}\n")
for n,a,b,c in zip(nombres,apellidos,edad,ciudades):
    print(f"Nombre: {n}, Apellido: {a}, Edad: {b}, Ciudad: {c}")