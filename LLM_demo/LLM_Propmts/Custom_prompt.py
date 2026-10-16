from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

st.title("AI Tutor")
st.write("Learn any topic in customized way with AI Tutor.")

topic = st.text_input("Enter topic to learn:")
level = st.selectbox(" Select Difficulty :", ['Beginner', 'Intermediate', 'Advance'])
style = st.selectbox("Choose Explaination Style :" , ['Step-by-step', 'Research Oriented', 'Storytelling'])

template = load_prompt('template.json')


model = ChatOpenAI(model = 'gpt-4.1-mini', temperature=1.5, max_tokens = 300)

if st.button("ASK"):
    if topic.strip():
        prompt = template.invoke({'topic' : topic, 'level' : level, 'style' : style})
        with st.spinner("Generating response..."):
            result = model.invoke(prompt)
            st.markdown(result.content)
    else:
        st.warning("Please enter a topic to learn!")
