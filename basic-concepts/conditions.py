'''
Uso de condiciones en Python.
Una condición es una instrucción que se ejecuta o no al cumplirse una condición.
Depende de una operación lógica.
'''

# Igual ==
print(1 == 1)

# Diferente !=
print(3 != 5)

# Menor <
print(8.1 < 10.5)

# Mayor > 
print(4 > 26)

# Menor o igual que <= 
print(8 <= 3)

# Mayor o igual que >=
print(2.1 >= 2)

# Cómo se usan los operadores lógicos
# operadores: is, and, or, not

estado_civil = "Casado"

if estado_civil == "Casado":
    print ("Esta casado")
elif estado_civil == "Divorsiado":
    print ("Está divorsiado")
else:
    print("Está soltero")

a = 1
b = 1

if a < b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")

c = True
if c:
    print("C es verdadero")
else:
    print("C es falso")

if type(c) is bool:
    print("C es booleano")
else:
    print("C es otro tipo de dato")

x = 10
y = 5
z = 1

if x > y and y > z:
    print("X es mayor que Z")
