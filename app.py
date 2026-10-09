from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

class Student(BaseModel):
    cgpa: float

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/script.js")
def javascript():
    return FileResponse("script.js")

@app.post("/predict")
def predict(student: Student):
    result = model.predict([[student.cgpa]])
    return {"prediction": round(float(result[0]), 2)}