CARGOFIJO = 7000
COSTOM3AGUA = 200
IVA = 0.21

bonificacion = 0
recargo = 0
cliente_residecial = 0
tipo_cliente = input("Ingrese el tipo de cliente: ")
consumo = int(input("Ingrese la cantidad de metros 3 consumidos"))

match tipo_cliente:
    case "Cliente Residencial":
        if consumo < 30 :
            bonificacion = 0.1
        elif consumo > 80 :
            recargo = 0.15
        print("Cliente Residencial")

    case "Cliente Comercial":
        if consumo > 300 :
            bonificacion = 0.12
        elif consumo > 150 :
            bonificacion = 0.08
        elif consumo < 50 :
            recargo = 0.05
        print("Cliente Comercial")
    
    case "Cliente Industrial":
        if consumo > 1000 :
            bonificacion = 0.3
        elif consumo > 500 :
            bonificacion = 0.2
        elif consumo < 200 :
            recargo = 0.1
        print("Cliente Industrial")

sub_total_consumo = CARGOFIJO + COSTOM3AGUA * consumo

if cliente_residecial == "Cliente Residencial" and sub_total_consumo < 35000:
    bonificacion = bonificacion + 0.05

print(f"El costo subtotal es de {sub_total_consumo}$")
print(f"La cantidad de bonificación que tiene es de {bonificacion * 100}%")
print(f"La cantidad de recargos que tiene es de {recargo * 100}%")
sub_total_recargo_bonificacion = sub_total_consumo - sub_total_consumo * bonificacion + sub_total_consumo * recargo
print(f"EL subtoral de consumo con recargos y bonificaciones es de {sub_total_recargo_bonificacion}$")
total_iva_aplicado = sub_total_recargo_bonificacion + sub_total_recargo_bonificacion * IVA
print(f"Total con iva aplicado {total_iva_aplicado}")