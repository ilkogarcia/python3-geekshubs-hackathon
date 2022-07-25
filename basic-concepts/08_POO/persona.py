class Persona:
    atributo = 123

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Estoy en el constructor")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños # {self.edad} {self.nombre}")

class Empleado(Persona):
    def __init__(self, horas_totales, nombre, edad):
        super(Empleado, self).__init__(nombre,edad)
        self.horas_totales = horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado hoy, un total de: {horas_trabajadas} horas")
        print(f"Su acumulado de horas totales trabajadas es: {self.horas_totales} horas")
        

paco = Empleado(nombre="Paco", edad=20, horas_totales=30)
paco.trabajar(horas_trabajadas=8)
paco.cumplir_anios()




pedro = Persona("Pedro", 20)
print(pedro.nombre)
print(pedro.edad)
print("Pedro es un objeto de clase:", type(pedro))
print(pedro.atributo)

print()

pedro.cumplir_anios()

print()

paco = Persona("Paco", 50)
print(paco.nombre)
print(paco.edad)
print("Paco es un objeto de clase: ", type(paco))
print(paco.atributo)

print()
# 2 objetos de una misma clase no son iguales porque ocupan espacios diferentes de memoria
print ("¿Son Pedro y Paco iguales?", pedro == paco) 

