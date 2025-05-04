from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pypdf import PdfReader, PdfWriter

# def get_llm(api_key):
#     return ChatOpenAI(api_key=api_key, temperature=0)
def get_llm():
    load_dotenv()
    api_key = os.getenv('api_key')
    
    #api_key = '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'
    os.environ['OPENAI_API_KEY'] = api_key

    # Initialize the LLM
    llm = ChatOpenAI(temperature=0)
    return llm

def fill_form(base_info, clinical_study_details):
    
    reader = PdfReader("FDA-1572.pdf")
    writer = PdfWriter()

    
    fields = reader.get_fields()
    print(fields.keys())  

    
    writer.append(reader)
    writer.update_page_form_field_values(
        writer.pages[0],
        {
            "Name_of_Clinical_Investigator": "John Doe",
            "Address_1": "123 Main St"
        },
    )

    with open("filled_form.pdf", "wb") as f:
        writer.write(f)

