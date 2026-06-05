from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name:str
    math:int
    physics:int
    coding:int
    english:int

@app.post("/analyze")
def analyze(data: Student):

    avg = (
        data.math +
        data.physics +
        data.coding +
        data.english
    ) / 4

    if avg >= 80:
        category = "Excellent"
    elif avg >= 60:
        category = "Good"
    else:
        category = "Needs Improvement"

    return {
        "name": data.name,
        "average": avg,
        "category": category
    }