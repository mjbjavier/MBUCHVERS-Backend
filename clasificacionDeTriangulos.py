# Algoritmo que me permite identificar tipos de triangulo
# Declaramos las variables
a = float(input ('Ingrese el lado a del triangulo: '))
b = float(input ('Ingrese el lado b del triangulo: '))
c = float(input ('Ingrese el lado c del triangulo: '))

# Creamos la estructura if else
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Equilatero')
    elif a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Las medidas no forman un triangulo')

