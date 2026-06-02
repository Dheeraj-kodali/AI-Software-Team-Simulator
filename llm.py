from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=st.secrets["GROQ_API_KEY"],
    temperature=0.2
)