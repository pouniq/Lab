import requests

# fast API endpoint
API_URL = "http://127.0.0.1:8000/predict_diabetes"
payload = {
    "Pregnancies": 2,
    "Glucose": 140,
    "BloodPressure": 100,
    "SkinThickness": 30,
    "Insulin": 80,
    "BMI": 25,
    "DiabetesPedigreeFunction": 0.344,
    "Age": 27
}

# send Post request
response = requests.post(API_URL, json=payload)
print("Status Code" , response.status_code)
print("Response JSON", response.json())
