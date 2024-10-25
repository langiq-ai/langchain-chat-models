import logging
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Configure logging
# logging.basicConfig(level=logging.DEBUG)

def initialize_model():
    return OllamaLLM(model="llama3.2:1b")

def create_prompt_template():
    template = """Question: {question}

Answer: Let's think step by step."""
    return ChatPromptTemplate.from_template(template)

def invoke_chain(chain, question):
    try:
        responses = chain.invoke({"question": question})
        return responses
    except Exception as e:
        logging.error(f"Error invoking chain: {e}")
        return "An error occurred while processing your query."

def main():
    prompt = create_prompt_template()
    model = initialize_model()
    chain = prompt | model

    question = "What is LangChain?"
    responses = invoke_chain(chain, question)
    print(responses)

if __name__ == "__main__":
    main()