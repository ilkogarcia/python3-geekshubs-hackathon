'''
Vamos a practicar con las estructuras de datos.
Las estructuras de datos son las formas que tiene
el lenguaje para organizar los datos, y nos permiten
realizan operaciones de manipulación, extracción,
búsqueda e inserción de manera eficiente.

Alguas estructuras de datos en Python son mutables,
lo que significa que sus elementos pueden ser modificados
despues de su creación.
'''

# ******
# Listas, se representan entre corchetes [elem_1, elem_2,..., elem_n]
# Son estructuras ordenadas, mutables y permiten duplicados

from turtle import update


lenguajes = ["python", "java", "golang"] # Declaración de una lista
print(lenguajes)

longitud_lista = len(lenguajes) # La función len nos dará la longitud de la lista
print(longitud_lista) 

print(lenguajes[0]) # Imprime la primera posición de una lista
print(lenguajes[-1]) # Imprime la última posición de una lista
print(lenguajes[-longitud_lista]) # Imprime la primara posición de una lista

print(lenguajes[0:2]) # Imprime lo elementos uno y dos de la lista

lista = [1, 2.0, True, "python", 1] #Las listas permiten duplicados y elementos de diferentes tipos
print(lista)

programacion = [lenguajes, "dedicación", "practica"] # Las listas pueden contener otras listas (listas anidadas)
print(programacion)
print(programacion[0][0])

lenguajes[0] = "dart" # Los elementos de una lista son mutables y por tanto pueden modificarse
print(lenguajes)

lenguajes.append("python") # Agregar elementos al final de una lista mediante append
print(lenguajes)

otros_lenguajes = ["C", "C++"]
lenguajes.extend(otros_lenguajes) # Extender una lista con otro lista usando extend
print(lenguajes)

lenguajes.append(otros_lenguajes) # Agregar una lista como un elemento de otra lista (listas anidadas)
print(lenguajes)


# ******
# Tuplas, se representan entre paréntesis (elem_1, elem_2,..., elem_n)
# Son estructuras ordenadas, inmutables y permiten duplicados

paises_europa = ("Portugal", "España", "Francia", "Alemania")
print(paises_europa)
paises_europa[0]
paises_europa[-1]

paises_asia = "China", "India", "Pakistan"
print(paises_asia)
paises_asia[0]
paises_asia[-1]

# paises_europa[-1] = "Marruecos" Daría error porque las tuplas no soportan la asignación de nuevas variables

paises_mundo = paises_europa + paises_asia # Varias tuplas se pueden concatenar
print(paises_mundo)


# ******
# Diccionarios, se representan entre llaves {llave: valor}
# Son estructuras no ordenadas, mutables y que no permiten duplicados
# contienen pares de llave y valor separados por dos punto y cada par de elemento por una coma

usuario = {
    "nombre": "Ilko",
    "apellido": "García",
    "edad": 47
}
print(usuario)
print(usuario["nombre"])

usuario["anio_nacimiento"] = 1994 # En un diccionario es posible agregar nuevos pares de llave:valor
print(usuario)

usuario["anio_nacimiento"] = 1974 # Un diccionario no permite duplicados por lo que actualizará los valores
print(usuario)

usuario["padres"] = ["Luis García", "Esperanza Pérez"] # Los diccionarios pueden contener listas
print(usuario)

print(usuario.items()) # Nos devolverá una lista con todas las tuplas del diccionario
print(usuario.keys()) # Nos devolverá una lista con las llaves dentro del diccionario
print(usuario.values()) # Nos devolverá una lista con los valores dentro del diccionario

usuario.clear() # Con esto haremos que el diccionario quede vacio
print(usuario)


# ******
# Sets, se representan entre llaves {elem_1, elem_2,..., elem_n}
# Son estructuras no ordenadas, mutables y contienen elementos únicos (no duplicados)

set1 = {1, 2, 3}
print(set1)

# set1[0] Esto debería dar un error

set2 = {1, 1, 1, 2, 3}
print(set2)

set3 = {1, 2.0, "texto"}
print(set3)

set1.add(4) # En un set se puede agregar elementos nuevos
print(set1)
print(len(set1))

set1.update([4, 5, 6]) # Un set puede actualizarse con ultiples elementos nuevos
print(set1)
print(len(set1))

set1.discard(2) # Es sencillo eliminar del set un elemento de esta manera
print(set1)
print(len(set1))

set1.remove(3) # También se puede usar esta otra manera para eliminar un elemento
print(set1)
print(len(set1))

set1.clear() # Con este método podemos vaciar el set
print(set1)

