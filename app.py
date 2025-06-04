from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from Inference import predict, predict_from_dict

app = FastAPI()

class InputData(BaseModel):
    Pclass: int = Field(..., description="Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)")
    Sex: int = Field(..., description="Sex (0 = female, 1 = male)")
    Age: float = Field(..., description="Age in years (0-100)")
    SibSp: int = Field(..., description="Number of siblings/spouses aboard")
    Parch: int = Field(..., description="Number of parents/children aboard")
    Fare: float = Field(..., description="Fare paid (in dollars)")
    Embarked: int = Field(..., description="Port of Embarkation (0 = S, 1 = C, 2 = Q)")

@app.post("/predict")
async def make_prediction(input_data: InputData):
    input_dict = input_data.model_dump()
    prediction = predict_from_dict(input_dict)  
    return {"prediction": prediction}

