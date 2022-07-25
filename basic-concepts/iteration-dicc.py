'''
Cómo podemos iterar dentro de un diccionario de datos en Python
'''


lenguaje = {
    "nombre": "python",
    "creador": "Guido van Rossum",
    "año":  1997
}

for llave in lenguaje:
    print("llave:", llave)
    print("valor:", lenguaje[llave])

print()
for elemet in lenguaje.keys():
    print(elemet)

print()
for elemet in lenguaje.values():
    print(elemet)

print()
for llave, valor in lenguaje.items():
    print(llave, valor)

print()
for element in lenguaje.items():
    print(element)

