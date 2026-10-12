nombre_sistema = "MBUCHVERS"

# Cada cliente ahora es un Diccionario {key: value}
fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"},
    {"nombre": "Javier", "motivo": "Ventas"},
    {"nombre": "Paola", "motivo": "Reclamo Severo"}
]

print(f"Bienvenido a {nombre_sistema}. Sistema en línea.")

# Extraemos propiedades específicas del diccionario usando corchetes y la 'Key'
for cliente in fila_clientes:
    print(f"Asignando a: {cliente['nombre']} | Motivo: {cliente['motivo']}")

print("La fila está vacía. Todos los clientes fueron atendidos.")