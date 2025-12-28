from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input format
class AddInput(BaseModel):
    a: float
    b: float

# Define API endpoint
@app.post("/add")
def add_numbers(data: AddInput):
    result = data.a * data.b
    return {
        "a": data.a,
        "b": data.b,
        "sum": result
    }

