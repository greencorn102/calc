from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "svm_model.pkl"))

class PredictInput(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: PredictInput):
    x = np.array(data.features).reshape(1, -1)
    prediction = model.predict(x)
    return {"prediction": int(prediction[0])}
