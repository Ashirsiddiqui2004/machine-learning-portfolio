from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------- MOCK MODEL --------
def fake_model_predict(text: str):
    """
    This simulates a trained ML model.
    """
    if "good" in text.lower() or "love" in text.lower():
        return 0.85
    return 0.15
# ----------------------------

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running (mock model)"}

@app.post("/predict")
def predict(data: TextInput):
    prediction = fake_model_predict(data.text)
    return {
        "input_text": data.text,
        "prediction": prediction
    }
