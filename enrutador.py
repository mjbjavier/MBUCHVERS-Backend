# 1. DEFINIMOS LA FUNCIÓN (Construimos la máquina)
# Le decimos que necesita recibir un 'cliente' para poder trabajar
def enrutar_cliente(cliente):
    if cliente['motivo'] == "Reclamo Severo":
        print(f"🚨 URGENTE: {cliente['nombre']} transferido a RETENCIÓN")
    elif cliente['motivo'] == "Soporte Técnico":
        print(f"🔧 TÉCNICO: {cliente['nombre']} transferido a MESA DE AYUDA")
    else:
        print(f"✅ GENERAL: {cliente['nombre']} transferido a ASESOR COMERCIAL")
