from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import chat 
import form
# Load environment variables
# api_key = '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'

# os.environ['OPENAI_API_KEY'] = api_key

# # Initialize the LLM
# llm = ChatOpenAI(temperature=0)

# # Define the prompt template
# prompt = ChatPromptTemplate.from_template("""
#     User Input: {user_input}
    
#     Please choose one of the following options:
#     1. {option1}
#     2. {option2}
#     3. {option3}
    
#     Your choice (1, 2, or 3):
#     """)

def main():
    # Get user input
    choice = input("Please enter your choice: ")
    base_info = {
        'drug_name': 'Aspirin',
        'study_phase': 'Phase 1',
        'submission_type':'New Drug Application',
        'IND_num': '123456',
        'sponsor_org': 'Columbia University',
        'point_contact_name': 'John Doe',
        'point_contact_email': 'john.doe@columbia.edu',
        'phone_num': '1234567890'
        }
    while choice != "1" and choice != "2" and choice != "3":
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Please enter your choice: ")

    if choice == "1":
        user_input = input("Please enter your question or request: ")
        output = chat.main(user_input)
        print(output)

    elif choice == "2":
        output = form.main(base_info)
        print(output)
    elif choice == "3":
        user_input = input("Please enter your request: ")
    
    # Define the three options
    # options = {
    #     "option1": "Q&A",
    #     "option2": "Fill Form",
    #     "option3": "Doc Generation"
    # }
    
    # # Create the chain
    # chain = prompt | llm
    
    # # Run the chain
    # response = chain.invoke({
    #     "user_input": user_input,
    #     **options
    # })
    
    # print("\nResponse:")
    # print(response.content)

if __name__ == "__main__":
    main() 
