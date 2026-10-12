# Algoritmo que determina si un banco aprueba un crédito

# Entrada de datos
ingresos = float(input("Ingrese los ingresos del cliente en pesos: "))
reporte = input("¿Tiene reportes negativos? (si / no): ").lower()
avalista = input("¿Tiene avalista? (si / no): ").lower()

# Verificación de condiciones
if ingresos > 3000000 and reporte == "no":
    print("Crédito aprobado : ingresos altos y sin reportes negativos.")
elif 2000000 <= ingresos <= 3000000 and avalista == "si":
    print("Crédito aprobado : ingresos medios pero con avalista.")
else:
    print("Crédito negado : no cumple las condiciones.")