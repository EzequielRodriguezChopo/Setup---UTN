numeros = [10, 20, 30, 40, 50]
letras = ["a", "b", "c", "d"]

numeros.extend(letras)

print(f"Ambas listas combinadas{numeros}")

for i in range(3):
    numeros.pop(0)
    numeros.pop()
print(numeros)