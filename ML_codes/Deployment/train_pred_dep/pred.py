import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from joblib import load
import pandas as pd

def predict(model, input_data: dict):
    df = pd.DataFrame([input_data])
    predicted_value = model.predict(df)[0]
    return predicted_value
    
def main():
    try:
        load_dotenv()
        
        PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT"))
        MODEL_PATH = PROJECT_ROOT / os.getenv("MODEL_DIR") / os.getenv("MODEL_NAME")
        LOG_PATH = PROJECT_ROOT / os.getenv("LOG_DIR") / os.getenv("LOG_NAME")
        
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler(),  # terminal
                logging.FileHandler(LOG_PATH)  # file
            ],
        )
        
        
        model = load(MODEL_PATH)
        logging.info("model loaded")
        
        
        input_data = {
            "Pregnancies": 2,
            "Glucose": 120,
            "BloodPressure": 70 ,
            "SkinThickness": 35
            ,"Insulin": 96
            ,"BMI": 36,
            "DiabetesPedigreeFunction": 0.43,
            "Age": 29,
        }
        
        prediction = predict(model=model, input_data=input_data)
        if prediction == 1:
            logging.info("You Have diabetes")
        else:
            logging.info("You do NOT have diabetes")
        
    except Exception as e:
        print('prediction failed')
        logging.exception(f"prediction failed: {e}")
        raise
        
if __name__ == "__main__":
    main()