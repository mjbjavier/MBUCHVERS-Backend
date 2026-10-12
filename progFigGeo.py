import math

# Función para calcular área y volumen del triángulo (usaremos prisma triangular)
def triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    profundidad = float(input("Ingrese la profundidad (para el volumen): "))

    # Área del triángulo
    area = (base * altura) / 2

    # Volumen del prisma triangular
    volumen = area * profundidad

    print(f"Área del triángulo: {area}")
    print(f"Volumen del prisma triangular: {volumen}")

# Función para círculo (área del círculo y volumen de una esfera)
def circulo():
    radio = float(input("Ingrese el radio del círculo: "))

    area = math.pi * radio**2
    volumen = (4/3) * math.pi * radio**3  # esfera

    print(f"Área del círculo: {area}")
    print(f"Volumen de la esfera: {volumen}")

# Función para cono
def cono():
    radio = float(input("Ingrese el radio de la base del cono: "))
    altura = float(input("Ingrese la altura del cono: "))

    area_base = math.pi * radio**2
    generatriz = math.sqrt(radio**2 + altura**2)
    area_total = area_base + (math.pi * radio * generatriz)
    volumen = (1/3) * area_base * altura

    print(f"Área del cono: {area_total}")
    print(f"Volumen del cono: {volumen}")

# Función para cilindro
def cilindro():
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))

    area_base = math.pi * radio**2
    area_total = (2 * area_base) + (2 * math.pi * radio * altura)
    volumen = area_base * altura

    print(f"Área del cilindro: {area_total}")
    print(f"Volumen del cilindro: {volumen}")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ DE FIGURAS GEOMÉTRICAS ---")
        print("1. Triángulo (prisma)")
        print("2. Círculo (esfera)")
        print("3. Cono")
        print("4. Cilindro")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            triangulo()
        elif opcion == "2":
            circulo()
        elif opcion == "3":
            cono()
        elif opcion == "4":
            cilindro()
        elif opcion == "5":
            print("Saliendo del programa... ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar menú
menu()