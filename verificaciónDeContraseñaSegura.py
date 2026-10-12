# Algoritmo que me permite verificar si una contraseña es segura

# Entrada de datos
password = input("Ingrese su contraseña: ")

# Verificación de condiciones
condicion_longitud = len(password) >= 8
condicion_numero = any(char.isdigit() for char in password)
condicion_mayuscula = any(char.isupper() for char in password)

# Validación
if condicion_longitud and condicion_numero and condicion_mayuscula:
    print("Contraseña válida")
else:
    print("Contraseña inválida")
    if not condicion_longitud:
        print("- Debe tener al menos 8 caracteres")
    if not condicion_numero:
        print("- Debe contener al menos un número")
    if not condicion_mayuscula:
        print("- Debe contener al menos una letra mayúscula")