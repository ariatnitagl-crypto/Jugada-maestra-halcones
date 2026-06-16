from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models # El archivo que creamos recién

app = FastAPI()

# Esto permite que el Frontend se conecte sin errores
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Servidor de Los Halcones funcionando"}

# RESPUESTA A PREGUNTA 1: ¿Quiénes deben y quiénes están al día?
@app.get("/pagos/estado")
def obtener_estado_pagos():
    # Por ahora devolvemos datos de prueba, luego los traeremos de la DB
    return [
        {"nombre": "Juan Pérez", "categoria": "Infantil", "estado": "Pagado"},
        {"nombre": "Diego Soto", "categoria": "Juvenil", "estado": "Pendiente"},
        {"nombre": "Luis Jara", "categoria": "Adulto", "estado": "Pagado"}
    ]

# RESPUESTA A PREGUNTA 2: Asistencia promedio por categoría
@app.get("/asistencia/promedio")
def obtener_asistencia():
    return {
        "Infantil": "85%",
        "Juvenil": "70%",
        "Adulto": "60%"
    }

# RESPUESTA A PREGUNTA 3: Ingreso este mes vs anterior
@app.get("/finanzas/comparativa")
def obtener_comparativa():
    return {
        "mes_actual": 450000,
        "mes_anterior": 420000,
        "diferencia": "+7.1%"
    }