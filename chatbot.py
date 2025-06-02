import sys
import time
import asyncio
import matplotlib.pyplot as plt
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_community.document_loaders import TextLoader

# Initialize the model
model = OllamaLLM(model="llama3")

# Optimized prompt
template = """
You are a friendly mental health chatbot. Your job is to offer emotional support with **short and relevant** responses.

Use retrieved knowledge to **improve** responses, but keep it concise.

### Conversation History:
{context}

### User Question:
{question}

### Your Response (Rules):
1. Keep responses **short & relevant**.
2. Avoid overly long explanations.
3. Use a **friendly and caring tone**.
"""

prompt = ChatPromptTemplate.from_template(template)

# Load external knowledge
def initialize_vector_db():
    try:
        loader = TextLoader("mental_health_resources.txt")  
        docs = loader.load()

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        vector_store = Chroma.from_documents(docs, embeddings)
        
        retriever = vector_store.as_retriever(search_kwargs={"k": 1})  
        
        return retriever
    except Exception as e:
        print(f"Error initializing vector database: {e}")
        return None

retriever = initialize_vector_db()

response_times = []

async def generate_response(conversation_history, user_input):
    """Generates an **asynchronous** chatbot response for **faster processing**."""

    if retriever is None:
        return "Error: Retriever not initialized."

    start_time = time.time()  

    retrieved_docs = await asyncio.to_thread(retriever.invoke, user_input) if retriever else []
    retrieved_texts = "\n".join([doc.page_content for doc in retrieved_docs])

    input_text = prompt.format(context=conversation_history, question=user_input, retrieved_docs=retrieved_texts)

    try:
        full_response = await asyncio.to_thread(model.invoke, input_text)
    except Exception as e:
        full_response = f"Error: {e}"
    
    end_time = time.time()
    response_times.append(end_time - start_time)

    # Adjust response length dynamically
    word_count = len(user_input.split())
    if word_count <= 2:
        response = full_response.split(".")[0]  # Only first sentence
    elif word_count <= 5:
        response = " ".join(full_response.split(".")[:2])  # First two sentences
    else:
        response = full_response  # Full response for deep queries

    # Stream words faster
    sys.stdout.write("\nChatbot: ")
    sys.stdout.flush()
    for word in response.split():
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        await asyncio.sleep(0.02)  # Reduced delay for speed
    sys.stdout.write("\n")
    sys.stdout.flush()
    
    return response

def plot_response_times():
    """Plots chatbot response times."""
    if not response_times:
        print("No response times recorded.")
        return
    
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(response_times) + 1), response_times, marker='o', linestyle='-', color='b')
    plt.xlabel("Interaction Number")
    plt.ylabel("Response Time (seconds)")
    plt.title("Chatbot Response Time Over Conversation")
    plt.grid(True)
    plt.show()

async def chat():
    """Handles real-time chat asynchronously."""
    conversation_history = ""
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nChatbot: Take care! 💙")
            plot_response_times()
            break
        response = await generate_response(conversation_history, user_input)
        conversation_history += f"User: {user_input}\nChatbot: {response}\n"

if __name__ == "__main__":
    asyncio.run(chat())
