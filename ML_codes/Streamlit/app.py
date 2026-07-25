import streamlit as st
# it is only used for demos and prototypes
from predictor import predict

# set page configurations
st.set_page_config(
    page_title="diabetes prediction app",
    page_icon= "🦶",
    layout='centered'
    
)

st.title("diabetes prediction test")
st.write('enter patient details & click **predict**')
st.subheader("Patients details")

col1, col2 = st.columns(2)

with col1:

    # first value is min
    # second value is max
    # third values is default value
    pregnancies = st.number_input("Pregnancies", 0, 10, 2)
    glucose = st.number_input("Glucose", 0, 400, 120)
    BloodPressure = st.number_input("BloodPressure", 0, 200, 70)
    SkinThickness = st.number_input("SkinThickness", 0, 100, 25)
with col2:
    Insulin = st.number_input("Insulin", 0, 900, 80)
    BMI = st.number_input("BMI", 0.0, 70.0, 28.5)
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", 0.0, 3.0 , 0.45)
    Age = st.number_input("Age", 1, 100, 20)


if st.button("Predict 👈"):
    input_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": BloodPressure ,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age,
    }
    prediction = predict(input_data=input_data)
    st.divider()
    if prediction == 1:
        st.error("the patient have diabetes")
    else:
        st.success("the patient is healthy and do not have diabetes")

