frutas = ["manzana", "banana", "naranja", "uva"]
print(f"Frutas original= {frutas}")

frutas.append("pera")
print(f"Agregue al final pera= {frutas}")

frutas.insert(1,"kiwi")
print(f"Insertamos Kiwi wn el indice 1= {frutas}")

frutas.remove("banana")
print(f"Removi banana= {frutas}")

frutas.sort()
print("Ordene de menor a mayor frutas= {frutas}")

frutas.reverse()
print(f"Inverti la lista= {frutas}")

print(f'Las veces que aparece Uva es: {frutas.count("uva")}')

frutas1 = frutas.copy()

print(f"La copia de frutas es: {frutas1}")

frutas1.clear()
print(f"Frutas1 vaciada= {frutas1}")