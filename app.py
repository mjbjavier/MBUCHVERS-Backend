nombre_sistema = "MBUCHVERS"

# Cada cliente ahora es un Diccionario {key: value}
fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"},
    {"nombre": "Javier", "motivo": "Ventas"},
    {"nombre": "Paola", "motivo": "Reclamo Severo"}
]

print(f"Bienvenido a {nombre_sistema}. Iniciando enrutamiento inteligente...\n")

for cliente in fila_clientes:
    # Evaluamos la propiedad 'motivo' de cada diccionario
    if cliente['motivo'] == "Reclamo Severo":
        print(f"🚨 URGENTE: {cliente['nombre']} transferido a RETENCIÓN (Motivo: {cliente['motivo']})")
    
    elif cliente['motivo'] == "Soporte Técnico":
        print(f"🔧 TÉCNICO: {cliente['nombre']} transferido a MESA DE AYUDA (Motivo: {cliente['motivo']})")
        
    else:
        print(f"✅ GENERAL: {cliente['nombre']} transferido a ASESOR COMERCIAL (Motivo: {cliente['motivo']})")

print("\nLa fila está vacía. Todos los clientes fueron enrutados.")