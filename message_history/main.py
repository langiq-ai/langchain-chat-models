from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama.llms import OllamaLLM

chat_history = [
    SystemMessage(content="you like to correct grammar?"),
    HumanMessage(content="What is 100 divided by 10?"),
    AIMessage(content="I you waste no time you give straight answer : 10"),
    HumanMessage(content="What is 100 divided by 20?"),
]

# Initialize the OllamaLLM model with the specified version
model = OllamaLLM(model="llama3.2:1b")

while True:
    query = input("Enter your query: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    # Invoke the chain with a question and get the responses
    result = model.invoke(chat_history)
    response = result
    chat_history.append(AIMessage(content=response))
    # Print the responses
    print(f"AI: {response}")

print("============ Chat History ============")
for message in chat_history:
    print(message.content)