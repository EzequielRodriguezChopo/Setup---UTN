añoDeNacimiento = int(input("Ingrese el año en que nacio: "))
edad = 2025 - añoDeNacimiento
cumplioAños=input("Usted cumplio años? Si / No : ")
if(cumplioAños != "Si" and cumplioAños != "No"):
    print(f" \"{cumplioAños}\" ,no es una respuesta correcta, intente de nuevo, gracias")
else:
    if(cumplioAños=="No"):
        edad -= 1
    print(f"Usted tiene {edad} años")