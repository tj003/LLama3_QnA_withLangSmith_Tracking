import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Define prompt with the correct variable
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "Question: {input}")
])

# Streamlit UI
st.title("LangChain App with Ollama - LLAMA3")
input_text = st.text_input("What question do you have in mind?")

# Ollama setup
llm = OllamaLLM(model="llama3")
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Invoke only when input is provided
if input_text:
    response = chain.invoke({"input": input_text})
    st.write(response)
