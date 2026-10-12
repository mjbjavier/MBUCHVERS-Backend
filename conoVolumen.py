# Algoritmo que me permite saber el volumen de un cono
import math

# Declaramos la variable

def volumen_cono(r, h):
    """
    Calcula el volumen de un cono.
    Parámetros:
        r -> radio de la base
        h -> altura
    Retorna:
        Volumen del cono
    """
    # Creamos la estructura algoritmica de la formula
    V = (math.pi * r**2 * h) / 3
    return V

# Ejemplo
print("Volumen del cono:", volumen_cono(6, 20))