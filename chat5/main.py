import logging
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Define the template for the prompt
template = """Question: {question}

Answer: Let's think step by step."""

# Create a ChatPromptTemplate from the template
prompt = ChatPromptTemplate.from_template(template)

# Initialize the OllamaLLM model with the specified version
model = OllamaLLM(model="llama3.2:1b")

# Create a chain by combining the prompt and the model
chain = prompt | model

# Invoke the chain with a question and get the responses
responses = chain.invoke({"question": "What is LangChain?"})

# Print the responses
print(responses)