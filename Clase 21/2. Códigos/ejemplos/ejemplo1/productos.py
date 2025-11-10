# Abre el archivo en modo lectura
with open('productos.txt', 'r') as archivo:
    # leer y mostrar los productos
    productos = archivo.read()
    print(productos)

    # lo podemos mostrar con un for
    """ for linea in archivo:
        print(linea.strip())  # .strip() elimina los espacios en blanco y saltos de línea adicionales """
    
    # lo podemos mostrar con un for y readlines
    """ for linea in archivo.readlines():
        print(linea) """

# Cierra automáticamente el archivo después de salir del bloque "with"