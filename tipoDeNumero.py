# Algoritmo que me permite determinar el tipo de numero util para un inventario de bodega
# Declaramos las variables
num = int(input('Ingrese el numero a verificar: '))

# Creamos la estructura if else
if num > 0:
    print(f'{num} es positivo')
elif num < 0:
    print(f'{num} es negativo')
else:
    print(f'{num} es cero')
    
if num % 2 == 0:
    print(f'{num} es par')
else:
    print(f'{num} es impar')
    
if num % 8 == 0:
    print(f'{num} es multiplo de 8')
else:
    print(f'{num} no es multiplo de 8')
    
