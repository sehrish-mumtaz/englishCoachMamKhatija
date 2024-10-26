import os
from datetime import datetime
import streamlit as st
from groq import Groq

# Set up Groq API client with your API key
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Define your Streamlit app
def main():
    st.title("Writing Assistant Chatbot")

    # Plan selection
    plans = {
        "30 Days Plan": 30,
        "45 Days Plan": 45,
        "60 Days Plan": 60,
    }
    plan_choice = st.selectbox("Select a Plan Duration", list(plans.keys()))
    selected_days = plans[plan_choice]

    start_date = datetime.today()
    day_of_plan = (datetime.today() - start_date).days + 1
    st.write(f"**Day {day_of_plan}**")

    # Today's writing topic
    topic = "Discuss the impact of technology on education."  # Example topic
    st.write(f"### Today's Topic: {topic}")

    # Input for essay
    essay_input = st.text_area("Write your essay below:")
    submit_button = st.button("Submit for Feedback")

    if submit_button:
        if essay_input:
            feedback = get_feedback(essay_input)
            st.write("### Feedback:")
            st.write(feedback)
        else:
            st.error("Please write your essay before submitting.")

def get_feedback(essay):
    # Call to Groq API to get feedback
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    "You are an expert academic writer with 40 years of experience in providing "
                    "concise but effective feedback. Instead of asking the student to do this and that, "
                    "you just say replace this with this to improve in a concise manner. You provide "
                    "concise grammar mistakes saying replace this with this along with mistake type. "
                    "You also provide specific replacement sentences for cohesion and abstraction, and "
                    "you point out all the vocab saying that replace this word with this. Analyze the "
                    "writing for grammar, cohesion, sentence structure, vocabulary, and the use of simple, "
                    "complex, and compound sentences, as well as the effectiveness of abstraction. "
                    "Provide detailed feedback on any mistakes and present an improved version of writing. "
                    "Don't use words such as dive, discover, uncover, etc. Follow academic style in writing. "
                    "Adjust the sentence according to English standards if needed, but do not add sentences "
                    "yourself. If user is of A1 level, return the output for beginners, A2 for average, "
                    "A3 for advance, and you can go till C1 level."
                ),
            },
            {
                "role": "user",
                "content": essay,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    main()
