'''
nombre = "Ezequiel"
apellido = "Rodriguez"
edad = int(input("Ingrese su edad "))


nombreCompleto = nombre + " " + apellido

print (f"{nombre} {apellido} {edad}")
print (nombre + " " + apellido)
print (nombreCompleto)
print (nombre,apellido)
print (nombre,apellido, sep="@@@")
'''
'''
a = 8
b = 4

print(a,b)

auxiliar = a
a = b
b = auxiliar
                # Si mantengo apretado la tecla "Alt" pudo mover la linea hacia donde quiero
print(a,b)      # shift + alt + flecha para abajo "Copia una linea"
'''

variable1 = int(input("Ingrese un valor: "))
variable2 = float(input("Ingrese un valor: "))
variable3 = int(input("Ingrese un valor: "))
variable4 = float(input("Ingrese un valor: "))
variable5 = int(input("Ingrese un valor: "))

promedio = (variable1 + variable2 + variable3 + variable4 + variable5) / 5

print(f"El valor de promedio de los 5 valores es: {promedio}")