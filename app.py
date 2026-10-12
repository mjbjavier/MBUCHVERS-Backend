from enrutador import enrutar_cliente

nombre_sistema = "MBUCHVERS"

fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"}
]

print(f"Bienvenido a {nombre_sistema}.")

for persona in fila_clientes:
    enrutar_cliente(persona)