import logging

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Configure logging
# logging.basicConfig(level=logging.DEBUG)

# Define the template for the prompt
template = """Question: {question}

Answer: Let's think step by step."""


messages = [
    SystemMessage(content="Lets solve basic math problems, but you are a jerk "),
    HumanMessage(content="what is 100 divided by 10 ?"),
    AIMessage(content="i think you should know basic math"),
    HumanMessage(content="what is 100 divided by 20 ?"),
]

# Initialize the OllamaLLM model with the specified version
model = OllamaLLM(model="llama3.2:1b")

# Invoke the chain with a question and get the responses
responses = model.invoke(messages)

# Print the responses
print(responses)

