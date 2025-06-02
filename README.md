
---

````md
# 🧠 Friendly Mental Health Chatbot

A Retrieval-Augmented Generation (RAG)-based chatbot that provides empathetic and helpful responses grounded in reliable mental health resources. Ideal for offering emotional support, this assistant uses vector-based retrieval and local LLM generation for informed, emotionally intelligent responses.

---

🧩 Problem Statement

Many individuals seek emotional support but hesitate to approach professionals or find it difficult to search through mental health literature. This chatbot addresses that by enabling **accessible, reliable, and emotionally aware guidance**, grounded in real mental health resources.

Unlike generic LLM-based bots, this system uses **Retrieval-Augmented Generation (RAG)** to provide **fact-based responses**, reducing hallucinations and increasing relevance.

---

🧠 Why RAG?

RAG improves trustworthiness by retrieving relevant text passages from verified content (e.g., therapy guides or support articles) and **feeding them to the LLM** before generation. This ensures responses are **informed and grounded**, not hallucinated.

---

🏗️ RAG Architecture Overview

🔹 Data Used for Retrieval
- A curated file: `mental_health_resources.txt`  
  Contains supportive advice, therapy techniques, and emotional wellness tips.

🔹 Retrieval Component
- **Vector Store**: ChromaDB  
- **Embedding Model**: `all-MiniLM-L6-v2` via Hugging Face  
- **Document Splitter**: LangChain `RecursiveCharacterTextSplitter`  

🔹 Generation Component
- **LLM**: `llama3` via Ollama  
- **Framework**: LangChain  
- **Prompting Strategy**: Custom RAG prompt with retrieved context

---

 🛠️ Tools and Frameworks

- **LangChain** – RAG pipeline management  
- **ChromaDB** – Vector store for retrieval  
- **Ollama** – Runs LLaMA 3 locally for fast, offline generation  
- **Hugging Face Transformers** – Embeddings with `sentence-transformers`  
- **Matplotlib** – Optional analysis of response time  

---

 🧪 LLM Details

- **LLM Used**: `llama3` via [Ollama](https://ollama.com) (local inference)
- **Embedding Model**: `all-MiniLM-L6-v2` from Sentence-Transformers
- **Free-Tier Friendly**: All tools run locally; no paid APIs required

---

 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/chatbot.git
cd chatbot
````

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



