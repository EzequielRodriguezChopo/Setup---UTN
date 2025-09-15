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