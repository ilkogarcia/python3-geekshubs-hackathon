from datetime import datetime
formato_fecha = '%d/%m/%Y'
print(datetime.today().strftime(formato_fecha))

fecha_nacimiento = input('Cuál es tu fecha de nacimiento (dd/mm/aaaa): ')
fecha_nacimiento = datetime.strptime(fecha_nacimiento, formato_fecha)
print(fecha_nacimiento)

def calcularEdad(fecha_nacimiento):
    fecha_hoy = datetime.today()
    edad = fecha_hoy - fecha_nacimiento.year - ((fecha_hoy.month, fecha_hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

print(calcularEdad(fecha_nacimiento) + 'años')