añoActual = int(input("Ingrese el año actual: "))
mesActual = int(input("Ingrese el mes actual: "))
diaActual = int(input("Ingrese el día actual: "))
if(añoActual >=1900 and añoActual <=2100):
    if(mesActual >=0 and mesActual <=12):
        if(diaActual >=0 and diaActual <=31):
            añoDeNacimiento = int(input("Ingrese su año de nacimiento: "))
            mesDeNacimiento = int(input("Ingrese su mes de nacimiento: "))
            diaDeNacimiento = int(input("Dia de nacimiento: "))
            if(añoDeNacimiento >=1900 and añoDeNacimiento <=2100):
                if(mesDeNacimiento >=0 and mesDeNacimiento <=12):
                    if(diaDeNacimiento >=0 and diaDeNacimiento <=31):
                        
                        edad = añoActual - añoDeNacimiento

                        if(mesActual<mesDeNacimiento):      #/ Cuando entra al If es porque aún no cumplio años en este año,
                            edad -= 1                       #/ si es el mismo mes, pasa al "elif"
                        elif(diaActual<diaDeNacimiento):    #/ Entra si es el mesDeNacimiento es mayor al mes actual, o pasa lo de arriba
                            edad -= 1                       #/ Como no paso su fecha de cumpleaños, le restamos 1 a su edad
                        print(f"{edad}")
        
                    else:
                        print("El día ingresado es incorrecto")
                else:
                    print("El mes ingresado es incorrecto")
            else:
                print("El año ingresado es incorrecto")

        else:
            print("El día ingresado es incorrecto")
    else:
        print("El mes ingresado es incorrecto")
else:
    print("El año ingresado es incorrecto")
'''
if(añoActual >=1900 and añoActual <=2100):
    if(mesActual >=0 and mesActual <=12):
        if(diaActual >=0 and diaActual <=31):
            edad=8
        else:
            print("El día ingresado es incorrecto")
    else:
        print("El mes ingresado es incorrecto")
else:
    print("El año ingresado es incorrecto")
'''