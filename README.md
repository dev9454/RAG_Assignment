# Friendly Mental Health Chatbot

A Retrieval-Augmented Generation (RAG)-based chatbot that offers emotionally supportive and informed responses grounded in curated mental health content. The assistant combines document retrieval with a local language model (LLM) to ensure that responses are both empathetic and fact-based.

---

## Problem Statement

### The Challenge

Many individuals seek mental health support but hesitate to speak to professionals or struggle to navigate online resources. Most generic AI assistants generate responses based on patterns in data rather than real-world information, making them unreliable for sensitive emotional guidance.

### The Solution

This chatbot provides accessible, emotionally intelligent responses backed by verified mental health material. It uses Retrieval-Augmented Generation (RAG) to extract helpful information from a trusted knowledge base before generating a response, ensuring that the answers are more relevant, grounded, and context-aware.

---

## Why Use Retrieval-Augmented Generation (RAG)?

RAG improves the reliability and precision of chatbot responses by retrieving relevant data from curated resources before the model generates output. This approach:

- Reduces hallucination
- Ensures responses are backed by factual content
- Increases user trust
- Produces more domain-relevant guidance

---

## RAG Architecture Overview

### Data Source for Retrieval

- A single curated file: `mental_health_resources.txt`  
- Contains therapy advice, mental health techniques, and well-being tips

### Retrieval Component

- **Vector Store:** ChromaDB  
- **Embedding Model:** all-MiniLM-L6-v2 (from Hugging Face)  
- **Chunking Method:** LangChain’s `RecursiveCharacterTextSplitter`

### Generation Component

- **LLM:** LLaMA 3 (run locally via Ollama)  
- **Framework:** LangChain  
- **Prompt Strategy:** Injects chat history and retrieved documents into a custom template to guide the model

---

## Tools and Frameworks Used

- **LangChain** – RAG orchestration and prompt chaining  
- **ChromaDB** – Lightweight vector store for document retrieval  
- **Hugging Face Sentence-Transformers** – Embeddings using `all-MiniLM-L6-v2`  
- **Ollama** – Local execution of the LLaMA 3 model  
- **Matplotlib** – For response time visualization  
- **Asyncio & Python** – For fast interaction loop

---

## LLM and Embedding Model Details

- **LLM Used:** LLaMA 3 via Ollama  
- **Embedding Model:** all-MiniLM-L6-v2  
- **Deployment:** Fully local, privacy-focused, no API keys or cloud calls  
- **Free Tier:** All tools run offline and free of cost

---

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/chatbot.git
cd chatbot
``

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama

Ensure you have [Ollama](https://ollama.com) installed and the `llama3` model downloaded:

```bash
ollama run llama3
```

### 5. Add Your Resource File

Place the `mental_health_resources.txt` file in the project directory.

---

## 💬 Run the Chatbot

```bash
python chatbot.py
```

* Type your message to receive a short, friendly response.
* Type `exit` or `quit` to end the chat and view performance plot.

---

## 📊 Visualize Response Time

After exiting, a Matplotlib plot will show LLM response time per user interaction.

---
⚠️ Note on Deployment
This project uses Ollama to run llama3 locally, which means:

Cloud deployment is currently not possible due to the local nature of the LLM.

However, the chatbot has been successfully deployed and tested locally, and relevant screenshots of the local deployment are included in the repository.

For cloud compatibility, replacing Ollama with a cloud-hosted LLM API (like OpenAI or HuggingFace endpoints) is recommended.

## 📁 Project Structure

```
chatbot/
│
├── chatbot.py                  # Main chatbot script
├── mental_health_resources.txt # Your knowledge base
├── requirements.txt            # Dependency list
└── README.md                   # This file
```

---

## 📦 Dependencies (`requirements.txt`)

```txt
langchain
langchain-community
langchain-core
langchain-ollama
langchain-huggingface
huggingface_hub
sentence-transformers
chromadb
matplotlib
asyncio
```


## 🙏 Acknowledgements

* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.com/)
* [Hugging Face](https://huggingface.co/)
* [ChromaDB](https://www.trychroma.com/)

---

## 💙 Disclaimer

This chatbot is a demo and **not a substitute for professional mental health support**.
Please consult a licensed mental health professional when needed.

```



