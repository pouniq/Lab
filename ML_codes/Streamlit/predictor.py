import os
import logging
from pathlib import Path

import pandas as pd
import numpy as np
from dotenv import load_dotenv
from joblib import load

# load env content
load_dotenv()

PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT"))
MODEL_PATH = PROJECT_ROOT / os.getenv("MODEL_DIR") / os.getenv("MODEL_NAME")
LOG_PATH = PROJECT_ROOT / os.getenv("LOG_DIR")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # terminal
        logging.FileHandler(LOG_PATH)  # file
    ],
)

# loading the trained model
logging.info("loading trained model...")
model = load(MODEL_PATH)
logging.info("model imported.")


# NOTE; model is loaded only once not for every prediction
def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return prediction


# input_data = {
#     "Pregnancies": 3,
#     "Glucose": 130,
#     "BloodPressure": 80 ,
#     "SkinThickness": 24,
#     "Insulin": 92,
#     "BMI": 36,
#     "DiabetesPedigreeFunction": 0.23,
#     "Age": 36,
# }

# model_prediction = predict(input_data=input_data)

# logging.info(f'prediction is done \n your result {model_prediction}')
# after you test the usage of it you should always comment this out 
# everytime
