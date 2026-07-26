from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict

# API: menu in restaurant, collection of endpoints
# EndPoints: items in the menu - individual services -- like http
# Get/Post: methods, how we gonna interact with them
# get --> show me what foods do you have
# post --> I want to order smth

app = FastAPI(title = "Ml prediction App")

class PredictionInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: int 
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    
    
# Machine learning Endpoints
@app.post("/predict_diabetes")
def predict_diabetes(input_data: PredictionInput):
    prediction = predict(input_data.model_dump())
    return {
        "prediction": int(prediction)
    }
    
