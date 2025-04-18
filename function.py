from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def get_llm(key):
    api_key = key
    #api_key = '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'

    os.environ['OPENAI_API_KEY'] = api_key

    # Initialize the LLM
    llm = ChatOpenAI(temperature=0)
    return llm

