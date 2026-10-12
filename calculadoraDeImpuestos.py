# Algoritmo que me permite calcular impuestos según salario e hijos

# Entrada de datos
salario = float(input("Ingrese su salario en pesos: "))
hijos = input("¿Tiene hijos? (si / no): ").lower()

# Lógica para calcular el impuesto
if salario > 5000000:
    if hijos == "si":
        impuesto = salario * 0.20
        print(f"Debe pagar un impuesto del 20%. Valor: {impuesto:.2f} pesos")
    else:
        impuesto = salario * 0.30
        print(f"Debe pagar un impuesto del 30%. Valor: {impuesto:.2f} pesos")
elif 2000000 <= salario <= 5000000:
    impuesto = salario * 0.10
    print(f"Debe pagar un impuesto del 10%. Valor: {impuesto:.2f} pesos")
else:
    impuesto = 0
    print("No paga impuestos ")