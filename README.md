# LangChain Workflow Example

This project demonstrates a simple LangChain workflow that takes user input and presents three options to choose from.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:
```bash
python main.py
```

The program will:
1. Ask for your input
2. Present three options
3. Process your choice and provide a response

## Features

- Takes user input
- Presents three predefined options
- Uses LangChain to process the input and choice
- Provides a structured response based on the selected option 