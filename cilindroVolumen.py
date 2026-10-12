# Algoritmo que me permite saber el volumen de un cilindro
import math

# Declaramos las variable
def volumen_cilindro(r, h):
    """
    Calcula el volumen de un cilindro.
    Parámetros:
        r -> radio de la base
        h -> altura
    Retorna:
        Volumen del cilindro
    """
    # Creamos la estructura algoritmica de la formula
    V = math.pi * r**2 * h
    return V

# Ejemplo
print("Volumen del cilindro:", volumen_cilindro(5, 20))  