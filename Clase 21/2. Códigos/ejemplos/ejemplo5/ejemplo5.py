def ingresar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    profesion = input("Ingrese su profesión: ")
    return f"Nombre: {nombre}, Edad: {edad}, Profesión: {profesion}"

def main():
    # Nombre del archivo de texto
    archivo_nombre = 'carta.txt'
    
    # Abre el archivo en modo lectura y escritura ('r+' significa lectura y escritura)
    with open(archivo_nombre, 'r+') as archivo:
        # Lee todo el contenido del archivo
        contenido = archivo.read()
        print(contenido)
        # Busca corchetes [] y permite al usuario ingresar datos
        while '[]' in contenido:
            contenido = contenido.replace('[]', ingresar_datos(), 1)

        # Coloca el cursor al principio del archivo
        archivo.seek(0)

        # Escribe el contenido modificado de vuelta al archivo
        archivo.write(contenido)

main()