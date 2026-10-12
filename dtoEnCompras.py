# Algoritmo que me permite dar DTO por valor de compra
# Declaramos las variables
total = float(input ('Ingrese el valor total de la compra: '))
pago = input('Forma de pago, efectivo / tarjeta: ').lower() 


# Creamos la estructura if else
if total > 500000 and pago == 'efectivo':
    descuento = total * 0.15
elif total > 300000 or pago == 'tarjeta':
    descuento = total * 0.10
else:
    descuento = total
    
print(f'El descuento de la compra {total} es {descuento}')
