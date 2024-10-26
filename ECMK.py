import streamlit as st
from datetime import datetime
import os
from groq import Groq

# Set up Groq API client with your API key
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define Streamlit app
st.title("Writing Assistant Chatbot")
st.write("Welcome to the Writing Assistant!")

# Define plans
plans = {
    "30 Days Plan": 30,
    "45 Days Plan": 45,
    "60 Days Plan": 60,
}

# Plan selection
plan_choice = st.selectbox("Select a Plan Duration", list(plans.keys()))
selected_days = plans[plan_choice]

# Track the current day in the plan
start_date = datetime.today()  # Start date
day_of_plan = (datetime.today() - start_date).days + 1  # Calculate the current day
st.write(f"**Day {day_of_plan}**")

# Adjusted Progress Calculation
if selected_days > 0:
    progress = day_of_plan / selected_days  # Calculate progress
else:
    progress = 0  # Default value if no days are selected

st.progress(progress)  # Show progress

st.write(f"You are {progress:.2f} through the {plan_choice}.")
