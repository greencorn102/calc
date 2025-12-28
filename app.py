from fastapi import FastAPI
import joblib
import numpy as np
import os

app = FastAPI()

# Load once when server starts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "svm_model.pkl"))

@app.post("/predict")
def predict(features: list):
    x = np.array(features).reshape(1, -1)
    prediction = model.predict(x)
    return {"prediction": int(prediction[0])}


