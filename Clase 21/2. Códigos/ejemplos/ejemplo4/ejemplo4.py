with open('datos.csv', 'r') as archivo:
    cabeceras = archivo.readline().strip().split(',')
    print(cabeceras)
    for linea in archivo:
        valores = linea.strip().split(',')        
        print(valores)