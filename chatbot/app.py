from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate #here we provide initial prompt template for our chatbot.
from langchain_core.output_parsers import StrOutputParser #this is default output parser of the LLM response.

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true" # Tracing to capture all the monitoring results.
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") #helps us to store the results.


## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

## streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic you want")


## OpenAI LLM 
llm = ChatOpenAI(model="gpt-3.5-turbo")

## Output Parser
output_parser = StrOutputParser()

##Final step: Create a Chain of Prompt, LLM, and Output_parser.
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))