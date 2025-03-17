import streamlit as st

def calculate_bmi(weight, height):
    if height == 0:
        return "Height cannot be zero!"
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"Your BMI is {bmi:.2f}. Category: {category}"

# Streamlit UI
st.title("BMI Calculator 💪")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m)", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    result = calculate_bmi(weight, height)
    st.success(result)
