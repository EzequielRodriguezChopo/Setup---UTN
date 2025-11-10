# Abre el archivo en modo lectura
with open('empleados.txt', 'r') as archivo:
    # Lee las líneas del archivo
    lineas = archivo.readlines()
    print(lineas)

    # Inicializa una lista vacía para almacenar los datos
    datos_empleados = []

    # Procesa cada línea del archivo
    for linea in lineas:
        # Divide la línea en campos utilizando la coma como separador
        campos = linea.strip().split(',')
        if linea == lineas[0]:
            pass
        else:
            nombre = campos[0]
            inasistencias = int(campos[1])
            sueldo = float(campos[2])
        
            # Agrega los datos a la lista
            datos_empleados.append((nombre, inasistencias, sueldo))
        
    for empleado in datos_empleados:
        nombre, inasistencias, sueldo = empleado
        print(f"Nombre: {nombre}, Inasistencias: {inasistencias}, Sueldo: ${sueldo:.2f}")