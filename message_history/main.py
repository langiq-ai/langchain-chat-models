import logging
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama.llms import OllamaLLM

# Configure logging
# logging.basicConfig(level=logging.INFO)

def initialize_model():
    return OllamaLLM(model="llama3.2:1b")

def get_user_input():
    return input("Enter your query: ")

def process_query(model, chat_history, query):
    chat_history.append(HumanMessage(content=query))
    try:
        result = model.invoke(chat_history)
        response = result
        chat_history.append(AIMessage(content=response))
        return response
    except Exception as e:
        logging.error(f"Error invoking model: {e}")
        return "An error occurred while processing your query."

def main():
    chat_history = [
        SystemMessage(content="you like to correct grammar?"),
        HumanMessage(content="What is 100 divided by 10?"),
        AIMessage(content="I you waste no time you give straight answer : 10"),
        HumanMessage(content="What is 100 divided by 20?"),
    ]

    model = initialize_model()

    while True:
        query = get_user_input()
        if query.lower() == "exit":
            break
        if not query.strip():
            print("Query cannot be empty. Please try again.")
            continue
        response = process_query(model, chat_history, query)
        print(f"AI: {response}")

    print("============ Chat History ============")
    for message in chat_history:
        print(message.content)

if __name__ == "__main__":
    main()