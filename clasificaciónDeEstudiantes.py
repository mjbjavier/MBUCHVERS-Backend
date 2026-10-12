# Algoritmo que me permite clasificar la nota de un estudiante

# 1. Entrada de datos
nota = float(input("Ingrese la nota del estudiante (0 - 100): "))

# 2. Validación y clasificación
if nota < 0 or nota > 100:
    print("Nota inválida")
elif 90 <= nota <= 100:
    print("Excelente")
elif 80 <= nota <= 89:
    print("Muy bueno")
elif 70 <= nota <= 79:
    print("Aprobado")
elif 60 <= nota <= 69:
    print("Condicional")
else:
    print("Reprobado")