'''
inventario = [
                ["Laptop", 15000.00, 10],
                ["Silla", 200.00, 50],
                ["Libro", 15.00, 100],
                ["Monitor", 300.00, 30]
]
'''
inventario=[]
opcion = 0

def cargar_producto(inventario):
    nombre_nuevo=input("\nIngrese el nombre del producto a ingresar: ")
    precio_nuevo=float(input("\nIngrese el precio del producto a ingresar: "))
    stock_nuevo=input("\nIngrese la cantidad de stock a ingresar: ")
    producto_nuevo=[nombre_nuevo,precio_nuevo,stock_nuevo]
    inventario.append(producto_nuevo)
    return inventario

def buscar_producto (inventario):
    producto_buscado = input("Ingrese el producto a buscar: ")
    for i in range(len(inventario)):
        if(producto_buscado == inventario[i][0]):
            return inventario[i]

def prod_mas_caro_mas_barato (inventario):
    barato=0.00
    caro=99999999999.00
    for i in range(len(inventario)):
        if inventario[i][1]<caro:
            caro = inventario[i][1]
            prod_mas_barato=inventario[i]
        if inventario[i][1]>barato:
            barato = inventario[i][1]
            prod_mas_caro=inventario[i]
    return(prod_mas_caro,prod_mas_barato)

def prod_mayor_a(inventario):
    productos_mayores=[]
    for i in range(len(inventario)):
        if inventario[i][1]>1500.00:
            productos_mayores.append(inventario[i])
    return productos_mayores

if len(inventario) == 0 :
    valor = 0

while(opcion != 6):

    print("\nMenu\n")
    print("1-Cargar Producto")
    print("2-Buscar Producto")
    print("3-Ordenar Inventario")
    print("4-Mostrar prodcuto más caro y más barato")
    print("5-Mostrar productos con precio mayor a 15000")
    print("6-Salir\n")

    opcion=input("Ingrese una opción: ")

    match(opcion):
        
        case "1":
            inventario=cargar_producto(inventario)
            print(f"\nEl nuevo inventario queda de la suiguiente manera {inventario}")
        
        case "2":
            if len(inventario) == 0:
                print("No hay productos disponibles para la operación solicitada")
            prod_encontrado = buscar_producto(inventario)
            print(f"\nEl producto encontrado es {prod_encontrado[0]} precio: {prod_encontrado[1]}$ cantidad: {prod_encontrado[2]}")
        
        case "3":
            print("")
        
        case "4":
            resultado = prod_mas_caro_mas_barato(inventario)
            print(f"\nEl producto con el precio más alta es {resultado[0]} y  el mas barato {resultado[1]}")
            
        case "5":
            print("Mostrat productos con precio mayor a 1500")
            productos_mayores_1500 = prod_mayor_a(inventario)
            print(f"\nLos prodctos mayores a 1500 son: {productos_mayores_1500}")
        case "6":
            break