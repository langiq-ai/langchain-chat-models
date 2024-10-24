# langchain-chat-models

## Overview
This project demonstrates the use of LangChain models to create a chat application. It utilizes various LangChain libraries to build and execute a prompt-response chain.

## Requirements
To install the necessary dependencies, run:
```sh
pip install -r requirements.txt
```
### Usage
The main script main.py sets up a chat prompt template and uses the Ollama LLM to generate responses.  
### Example
To run the example provided in main.py, execute:
```bash
python main.py
```
### Code Explanation
The script performs the following steps:
1. Imports necessary modules.
2. Defines a chat prompt template.
3. Initializes the Ollama LLM with a specific model.
4. Creates a chain combining the prompt and the model.
5. Invokes the chain with a sample question.
6. Prints the response.

### Dependencies
The project relies on the following libraries:
- `pytest`
- `langchain`
- `langchain-openai`
- `langchain-community`
- `langchain-experimental`
- `langgraph`
- `streamlit`
- `langchain-cli`
- `langsmith`
- `langchain-ollama`
- `python-dotenv`

### License
This project is licensed under the MIT License.
