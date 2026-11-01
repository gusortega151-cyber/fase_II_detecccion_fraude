from fastapi import FastAPI
from typing import List
import pickle
import pandas as pd

app = FastAPI(title="API de Predicción de Fraude", description="API para modelo de ML")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"mensaje": "La API del modelo está funcionando correctamente."}

#Como mejora le decimos a FastAPI que espere una Lista de diccionarios para evaluar mas de un caso a la vez
@app.post("/predict")
def predict(data: List[dict]):
    df = pd.DataFrame(data)
    predicciones = model.predict(df)
    #Convertimos el array de resultados a lista para que JSON lo pueda leer
    return {"predicciones": predicciones.tolist()}