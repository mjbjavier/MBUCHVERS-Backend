from fastapi import FastAPI

# Inicializamos el servidor web
app = FastAPI()

# Nuestra base de datos simulada
fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"}
]

# Creamos el Endpoint (La ruta)
@app.get("/clientes")
def obtener_clientes():
    return fila_clientes