from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PrendaModel(BaseModel):
    Prenda: str

@app.post("/tarea-2")
async def tarea_2(prenda: PrendaModel):
    return {"Respuesta": f"Prenda agregada: {prenda.Prenda}"}