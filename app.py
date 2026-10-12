nombre_sistema = "MBUCHVERS"

# 1. DEFINIMOS LA FUNCIÓN (Construimos la máquina)
# Le decimos que necesita recibir un 'cliente' para poder trabajar
def enrutar_cliente(cliente):
    if cliente['motivo'] == "Reclamo Severo":
        print(f"🚨 URGENTE: {cliente['nombre']} transferido a RETENCIÓN")
    elif cliente['motivo'] == "Soporte Técnico":
        print(f"🔧 TÉCNICO: {cliente['nombre']} transferido a MESA DE AYUDA")
    else:
        print(f"✅ GENERAL: {cliente['nombre']} transferido a ASESOR COMERCIAL")

# 2. BASE DE DATOS DE CLIENTES
fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"}
]

print(f"Bienvenido a {nombre_sistema}.")

# 3. EL BUCLE QUE LLAMA A LA FUNCIÓN (Apretamos el botón)
for persona in fila_clientes:
    enrutar_cliente(persona) # Aquí invocamos la máquina y le pasamos los datos