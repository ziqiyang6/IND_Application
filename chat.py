from function import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory.buffer import ConversationBufferMemory
from langchain.chains import LLMChain
def main(user_input):

    api_key = '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'
    question = user_input
    ind_qa_prompt = ChatPromptTemplate.from_template("""
    System:  
    You are an expert in IND (Investigational New Drug) applications, intimately familiar with FDA regulations (e.g., 21 CFR Part 312), international submission requirements, common pitfalls, timelines, and best practices.

    User Question:  
    {question}
                                                     
    Conversation history so far:
    {history}

    Please answer as an IND application specialist in clear, professional English. Be sure to cover:  
    - A complete list of core documents (e.g., CMC package, nonclinical study reports, clinical protocol)  
    - Key submission steps and expected timelines  
    - Common pitfalls and critical considerations  
    - Relevant FDA guidance or regulatory citations  
    - Practical, experience‑based recommendations  
    """)

    llm = get_llm(api_key)
    memory = ConversationBufferMemory(memory_key="history", return_messages=False)
    chain = LLMChain(llm=llm, prompt=ind_qa_prompt, memory=memory)
    response = chain.invoke(question)

    return response['text']