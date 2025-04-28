from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model
model = joblib.load('bitcoin_price_movement_model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define input format
class InputData(BaseModel):
    day_of_week: int
    day: int
    month: int

# Define predict endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    # Return result
    return {"prediction": int(prediction)}