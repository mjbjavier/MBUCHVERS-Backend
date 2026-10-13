from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # <-- NUEVO: Herramienta de validación

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fila_clientes = [
    {"nombre": "Andrés", "motivo": "Soporte Técnico"},
    {"nombre": "Camila", "motivo": "Facturación"}
]

# --- NUEVO: Creamos el "Molde" de cómo debe lucir un cliente
class NuevoCliente(BaseModel):
    nombre: str
    motivo: str

@app.get("/clientes")
def obtener_clientes():
    return fila_clientes

@app.delete("/clientes/{nombre}")
def eliminar_cliente(nombre: str):
    for cliente in fila_clientes:
        if cliente["nombre"] == nombre:
            fila_clientes.remove(cliente)
            break
    return {"mensaje": f"{nombre} retirado"}

# --- NUEVO: La ruta POST para recibir nuevos clientes
@app.post("/clientes")
def agregar_cliente(cliente: NuevoCliente):
    # Convertimos el molde seguro de Pydantic a un diccionario normal
    fila_clientes.append(cliente.model_dump())
    return {"mensaje": f"{cliente.nombre} agregado exitosamente"}