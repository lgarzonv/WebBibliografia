from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
#CORS: Habilitar peticiones desde clientes que no están en mi dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    all_credentials= True, 
    allow_methods=["*"],
    allow_headers=["*"],

)
@app.get("/sumar")
def sumar_numeros(a:float, b:float):
    return a+b

    