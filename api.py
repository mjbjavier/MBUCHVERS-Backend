from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Inicializamos el servidor web
app = FastAPI()

# --- NUEVO: CONFIGURACIÓN DE SEGURIDAD CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # El asterisco significa: "Deja pasar a TODOS los navegadores"
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],
)
# ----------------------------------------------

# Nuestra base de datos simulada
fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"}
]

# Creamos el Endpoint (La ruta)
@app.get("/clientes")
def obtener_clientes():
    return fila_clientes