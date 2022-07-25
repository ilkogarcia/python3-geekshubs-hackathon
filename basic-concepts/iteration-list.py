'''
Cómo podemos iterar por los elementos de una lista en Python
'''

lenguajes = ["python", "java", "golang", "php", "angular"]
for lenguaje in lenguajes:
    print (lenguaje)

print("")

# Otra forma de iterar usando los indices
for index in range(len(lenguajes)):
    print("Indice:", index)
    print("Elemento:", lenguajes[index])

print()

# En este caso usaremos los ciclos while para iterar en una lista
i = 0
while i < len(lenguajes):
    print(i, lenguajes[i])
    i += 1

