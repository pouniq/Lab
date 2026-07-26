from fastapi import FastAPI    # it is like a waiter in a restaurant  that taked order to the chef
from pydantic import BaseModel # it just validate our input data




# create fastapi application

app = FastAPI(title = 'test run fastapi')

# GET end point
# we use this to get things from the server
# like in our case we use that to get the 
# prediction.
@app.get("/greet")
def Home():
    return {'message': 'welcome to my App'}

# request body schema
class user(BaseModel):
    name: str
    age: int


# POST end point
# we use this to tell our API server something 
# like the user test data that we want to predict
@app.post("/user")
def create_user(user: user):
    return {
        "status": "success",
        "message": f"{user.name} and the age is {user.age}"
    }
    
    
# mock machine learning endpoint
class PredictionInput(BaseModel):
    age: int
    bmi: float
    glucose: float
    
@app.post("/predict")
def predict(input_data: PredictionInput):
    if input_data.glucose > 140 or input_data.bmi > 35:
        prediction = "High Risk"
    else :
        prediction = "Low Risk"
    return {
        "prediction": prediction,
        "model": "mock model",
        "input" : input_data
    }