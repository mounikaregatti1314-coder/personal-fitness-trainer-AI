import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Fitness Trainer Pro", page_icon="💪", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #667eea, #764ba2);
}
.title {
    text-align:center;
    font-size:50px;
    color:white;
    font-weight:bold;
}
.subtitle {
    text-align:center;
    color:white;
    margin-bottom:30px;
}
.card {
    padding:20px;
    border-radius:20px;
    background:white;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="title">💪 AI Fitness Trainer Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart Health • Smart Life 🚀</p>', unsafe_allow_html=True)

# ---------------- MODEL ----------------
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def train_model():
    data = pd.DataFrame({
        "weight": [50, 60, 70, 80, 90],
        "age": [20, 25, 30, 35, 40],
        "calories": [1800, 2000, 2200, 2500, 2800]
    })
    X = data[["weight", "age"]]
    y = data["calories"]
    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

# ---------------- INPUT SECTION ----------------
st.markdown("### 🧾 Enter Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", 10, 60)

with col2:
    weight = st.number_input("⚖️ Weight (kg)", 30, 150)
    height = st.number_input("📏 Height (m)", 1.0, 2.5)

with col3:
    st.info("💡 Tip: Stay consistent for best results!")

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Smart Plan"):

    bmi = calculate_bmi(weight, height)
    calories = model.predict([[weight, age]])[0]

    if bmi < 18.5:
        goal = "Underweight"
        plan = "High calorie diet + strength training"
        progress = 30
    elif bmi < 25:
        goal = "Fit"
        plan = "Balanced diet + cardio"
        progress = 70
    else:
        goal = "Overweight"
        plan = "Fat loss + calorie deficit"
        progress = 50

    st.markdown("---")

    # ---------------- METRICS ----------------
    col1, col2, col3 = st.columns(3)

    col1.metric("📊 BMI", f"{bmi:.2f}")
    col2.metric("🔥 Calories", f"{int(calories)} kcal")
    col3.metric("🧠 Body Type", goal)

    # ---------------- PROGRESS BAR ----------------
    st.subheader("📈 Fitness Progress Level")
    st.progress(progress)

    # ---------------- PLAN ----------------
    st.markdown("### 🏃 Your Smart Plan")
    st.success(plan)

    # ---------------- EXTRA UI ----------------
    st.balloons()

    st.markdown("### 💡 Daily Tips")
    st.write("""
    - Drink 3-4 liters of water 💧  
    - Sleep at least 7-8 hours 😴  
    - Exercise regularly 🏃  
    """)