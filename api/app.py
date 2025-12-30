from fastapi import FastAPI, UploadFile
from pathlib import Path
import joblib

app = FastAPI(title="DocIntel AI")

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "document_model.pkl"

# Load model once on startup
model = joblib.load(MODEL_PATH)

@app.get("/")
def health_check():
    return {"status": "DocIntel AI is running"}

@app.post("/predict")
async def predict(file: UploadFile):
    content = (await file.read()).decode("utf-8")
    prediction = model.predict([content])[0]
    return {
        "filename": file.filename,
        "prediction": prediction
    }
