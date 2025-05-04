from function import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory.buffer import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import markdown
import os

def main(user_input):
  
    
    question = user_input
    print(question)
    


    with open("/Users/olaf/Columbia_Source/4511/CA4/data/markdown/FDA-3500_Stat_Sec_Ext_01-31-2025.md", "r", encoding="utf-8") as file:
        html_content = markdown.markdown(file.read())



    ind_qa_prompt = ChatPromptTemplate.from_template(f"""
    You are now acting as an expert in FDA IND (Investigational New Drug) applications. Your task is to automatically complete an IND application form provided in Markdown format, using the medication or clinical trial input information I provide.

    Please follow these steps:

    Carefully read the provided Markdown format IND application form and understand what needs to be filled in for each section.

    Carefully read the input information I provide and extract the essential data needed to fill out the form.

    Accurately complete each section of the form according to FDA IND application standards and regulations.

    If any required information is missing from the provided input, clearly identify the missing information using placeholders such as "[Missing Information]".

    Your output should be a fully completed Markdown format form.

    Here are the Markdown form and input information I provided:

    Markdown Form:

    {html_content}

    Input Information:

    {question}

    Based on the above, please return a fully completed Markdown form. If the input is not enough to fill the form, please return "[Missing Information]".
    """)

    llm = get_llm()
    # chain = LLMChain(llm=llm, prompt=ind_qa_prompt)
    chain = (
        RunnablePassthrough()  
        | ind_qa_prompt
        | llm
    )
    response = chain.invoke(user_input) 

    return response.content

