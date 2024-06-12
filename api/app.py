from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate 
from langchain.chat_models import ChatOpenAI #chat application
from langserve import add_routes #create route source between OPENAI, LLAMA API.
import uvicorn
import os
from langchain_community.llms import Ollama 
from dotenv import load_dotenv


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


##ollama llama2
llm=Ollama(model="llama2")

prompt=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")


add_routes(
    app,
    prompt | llm,
    path = "/poem"
)


if __name__=="__main__":
    uvicorn.run(app,
                host = "localhost", 
                port = 8000)
