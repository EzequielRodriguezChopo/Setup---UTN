
# 1
nombreDelCadete = input("¿Cúal es su nombre, cadete espacial? ")
print(f"Saludos, {nombreDelCadete}. El Guardián te pondra a prueba...")

# 2
print("Comienza: La prueba de fuerza --------------------")
numeroEntero1 = int(input("Ingrese un número entero: "))
numeroEntero2 = int(input("Ingrese otro número entero: "))
suma = numeroEntero1 + numeroEntero2
resta = numeroEntero1 - numeroEntero2
multiplicacion = numeroEntero1 * numeroEntero2
division = numeroEntero1 / numeroEntero2
print(f"La suma de los numeros ingresados es {suma}")
print(f"La resta de los numeros ingresados es {resta}")
print(f"La multiplicación de los numeros ingresados es {multiplicacion}")
print(f"La división de los numeros ingresados es {division}")

# 3
print("Comienza: La prueba lógica --------------------")
print(f"El primer número es mayor al segundo: {numeroEntero1 > numeroEntero2}")
print(f"El primer número es igual al segundo: {numeroEntero1 == numeroEntero2}")
print(f"El primer número es menor o es igual 10: {numeroEntero1 <= 10}")

# 4
print("Prueba final: La Puerta de escape --------------------")
print(f"Ambos valores son positivos: {numeroEntero1 > 0 and numeroEntero2 > 0}")
print(f"Al menos uno de los números es mayor que 100: {numeroEntero1 > 100 or numeroEntero2 > 100}")
print(f"El primer número NO es cero: {numeroEntero1 != 0}")

# Mision Secundaria
MINIMACANTIDADDECOMBUSTIBLE = 200
cantidaDeCombustibleCargado=float(input("Ingrese la cantidad de combustible que cargo: "))
diferencia = MINIMACANTIDADDECOMBUSTIBLE - cantidaDeCombustibleCargado
porcentage = cantidaDeCombustibleCargado*100/MINIMACANTIDADDECOMBUSTIBLE
print(f"Te sobra combustible: {diferencia < 0}")
print(f"Te falta combustible: {diferencia > 0}")
print(f"Esta perfecto la cantidad de combustible: {diferencia == 0}")
print(f"Usted cargo {porcentage}% del minimo de combustible.")

# Fin de la Mision
print(f"\"✨ Fin de la misión, {nombreDelCadete}. El Guardián Galáctico te deja pasar... ¡Has escapado!\"")