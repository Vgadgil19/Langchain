from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model = 'gpt-4.1-mini', max_tokens = 250, temperature = 0.5)

st.header("Research Assistant")
user_input = st.text_input("What is your question?")

if st.button("ASK"):
    result = model.invoke(user_input)
    st.write(result.content)