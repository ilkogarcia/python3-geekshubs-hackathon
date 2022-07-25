''''
Las funciones son bloques de código independientes
que contienen instrucciones relacionadas entre si
que se encargan de cumplir con una tarea.

VENTAJAS:
- Organizar el código en partes pequeñas.
- Permite la organización y usabilidad del código.
- Evita la repetición de instrucciones y facilita su reutilización.

DEFINICIÓN:
def <¡nombre_funcion>():
    <instrucciones>
'''

APELLIDO = "García" 

# Built-in function
print()


# User defined functions
def mifuncion():
    print("Mi primera funcion")
    nombre = "Ilko"
    print(nombre, APELLIDO)
mifuncion()

# print(nombre) # Dará error porque la variable es local en el ámbito de la función
print(APELLIDO) # No dará error porque es una variable global

print()
def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    print(f"El perimetro es {perimetro} {unidades}")

perimetro_cuadrado(25, "metros")

perimetro_cuadrado(lado=10, unidades="cm")


# Instrucción return para utilizar el resultado en el proceso
print()
def perimetro_cuadrado(lado):
    perimetro = lado * 4
    #return perimetro Cuando la función no devuelve un valor entonces se considera "None"

def area_cuadrado (lado):
    area = lado * lado
    return area

perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(lado=5)

print(f"Área: {area}, Perímetro: {perimetro}")

# En una función se pueden devolver varios resultados al mismo tiempo
print()
def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return area, perimetro

area, perimetro = calcular_cuadrado(lado=5)

#print(f"Área: {area}, Perímetro: {perimetro}")

resultado = calcular_cuadrado(lado=5)
print(resultado)


# La documentación de funciones en Python se conoce como docstring
def perimetro_cuadrado(lado):
    '''Calcular el perímetro de un cuadrado
    
    Esta función recibe el valor de un lado de un cuadrado y a partir 
    de este calcula y retorna su perímetro.

    Args:
        lado (int): medida del lado del cuadrado

    Returns:
        perimetro (int): perímetro del cuadrado
    '''

    perimetro = lado * 4
    return perimetro

perimetro_cuadrado(lado=5)
