import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for prediction

def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    

def main():
    # Set page title and icon
    st.set_page_config(page_title='Diabetes Prediction Web App', page_icon='🩺')

    # Set custom CSS styling
    st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    .center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    .stApp {
        background: linear-gradient(to bottom, red, #00bfff);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background-color: black;
        color: #ffffff;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    # Centered title using HTML markup
    st.markdown('<h1 style="text-align:center;">Diabetes Prediction Web App</h1>', unsafe_allow_html=True)

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()


