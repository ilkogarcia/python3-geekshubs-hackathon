'''
Mi primer programa en Python3 
'''

nombre = input('¿Cuál es tu nombre?: ')
print('Gracias ' + nombre + '...sigamos.')
primer_apellido = input('¿Cuál es tu primer apellido?: ')
print('vale... ahora dime')
segundo_apellido = input('¿Cuál es tu segundo apellido?: ')
print('Entonces tu nombre completo es: ')
print(nombre + ' ' + primer_apellido + ' ' + segundo_apellido)
print('')
edad = input('¿Qué edad tienes?: ')
if( int(edad) >= 18 ):
    print('vale ' + nombre + '. Entonces eres mayor de edad y podemos continuar.')
else:
    print('Lo sentimos mucho ' + nombre + ' aún eres menor de edad y no podemos continuar el proceso')
