# Algoritmo que me permite controlar acceso
# Declaramos las variables
tipo = input('Es empleado o visitante: ').lower()
carnet = input('Tiene carnet ? si / no: ').lower()
cita = input('Tiene cita ? si / no: ')


# Creamos la estructura if else
if (tipo == 'empleado' and  carnet == 'si') or (tipo == 'visitante' and cita == 'si'):
    print('Acceso permitido, bienbenido')
else: 
    print('No puede ingresar')