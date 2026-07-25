# Load The Trained Model And Make predictions
# the libraried should be installed

# load the joblib version

import pandas as pd
from joblib import load

joblib_path = "/Users/pouniq/Lab/ML_codes/Deployment/model_dir/diabetes_logistic.joblib"

# LOAD THE SAVED MODEL
loaded_job_model = load(joblib_path)

new_data = pd.DataFrame(
    {
        "Pregnancies": [2],
        "Glucose": [120],
        "BloodPressure" : [70],
        "SkinThickness" : [25],
        "Insulin" : [80],
        "BMI" : [28.5],
        "DiabetesPedigreeFunction" : [0.45],
        "Age" : [35]
    }
)
new_data

pred = loaded_job_model.predict(new_data)
print(pred[0])
# not diabetic

# we can do that with pickle too
