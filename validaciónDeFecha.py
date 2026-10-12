# Algoritmo que valida una fecha y detecta años bisiestos

# Entrada de datos
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

# Verificar si el año es bisiesto
bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Días máximos por mes
if mes in [1, 3, 5, 7, 8, 10, 12]:
    dias_mes = 31
elif mes in [4, 6, 9, 11]:
    dias_mes = 30
elif mes == 2:
    dias_mes = 29 if bisiesto else 28
else:
    dias_mes = 0  # mes inválido

# Validación de la fecha
if mes < 1 or mes > 12:
    print("Fecha inválida: el mes no existe ")
elif dia < 1 or dia > dias_mes:
    print(f"Fecha inválida: el mes {mes} tiene como máximo {dias_mes} días ")
else:
    print(f"La fecha {dia}/{mes}/{anio} es válida ")
    if mes == 2 and bisiesto:
        print("Nota: Este año es bisiesto, febrero tiene 29 días ")