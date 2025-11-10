# abrimos el archivo
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        print(linea)
        # Divide la línea en nombre del producto y precio
        nombre_producto, precio_str = linea.strip().split(',')
        
        # Convierte el precio a un número decimal
        precio = float(precio_str)
        
        # Verifica si el precio es mayor que 20
        if precio > 30:
            print(f'{nombre_producto} cuesta más de $30 ({precio}).')