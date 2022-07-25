# Cómo se usan los ciclos for en Python

for letra in "Ilko García Pérez":
    print("Elemento:", letra)

print("Uso de brake en ciclos for:")
# Uso de brake en ciclos for
lenguajes = ["python", "java", "golang"]
for elemento in lenguajes:
    print(elemento)
    if elemento == "java":
        break

print("Uso de continue en ciclos for:")
# Uso de continue en ciclos for
lenguajes = ["python", "java", "golang"]
for elemento in lenguajes:
    if elemento == "java":
        continue
    print(elemento)

print("Uso de rangos en ciclos for:")
# Uso de rangos en ciclos for

# Cuando usamos range() con un solo numero N, el rango es de 0 a N-1
for element in range(5):
    print(element)

# Uso range() con un par de número, N1 y N2. El rango es de N1 a N2-1
for element in range(18, 25):
    print(element)
