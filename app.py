from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load once when server starts
model = joblib.load("svm_model.pkl")

@app.post("/predict")
def predict(features: list):
    x = np.array(features).reshape(1, -1)
    prediction = model.predict(x)
    return {"prediction": int(prediction[0])}
