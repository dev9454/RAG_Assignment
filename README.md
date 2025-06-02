Friendly Mental Health Chatbot
A Retrieval-Augmented Generation (RAG)-based chatbot designed to provide empathetic and helpful responses grounded in reliable mental health resources. This assistant offers emotional support by combining vector-based retrieval of relevant documents with local LLM generation to produce informed, emotionally intelligent answers.

Problem Statement
Many individuals seek emotional support but hesitate to approach professionals or find it difficult to navigate extensive mental health literature. This chatbot aims to make emotional guidance accessible, reliable, and empathetic by grounding responses in trusted mental health resources.

Unlike generic large language model-based chatbots, this system leverages Retrieval-Augmented Generation (RAG) to generate fact-based, contextually relevant responses. This approach reduces hallucinations and increases the reliability of the chatbot’s advice.

Why Use RAG?
RAG enhances the trustworthiness of generated responses by first retrieving relevant passages from verified content, such as therapy guides and support articles. These retrieved documents are then provided as context to the LLM, which ensures that the chatbot’s replies are factually informed and grounded rather than fabricated or hallucinated.

RAG Architecture Overview
Data Used for Retrieval

A curated knowledge base stored in the file mental_health_resources.txt, containing supportive advice, therapy techniques, and emotional wellness tips.

Retrieval Component

Vector Store: ChromaDB

Embedding Model: all-MiniLM-L6-v2 from Hugging Face sentence-transformers

Document Splitting: LangChain’s RecursiveCharacterTextSplitter

Generation Component

Large Language Model: llama3 accessed via Ollama for local inference

Framework: LangChain managing the RAG pipeline

Prompting Strategy: Custom prompt template combining conversation history and retrieved documents

Tools and Frameworks
LangChain for orchestrating the RAG pipeline

ChromaDB as the vector database to enable efficient similarity search

Ollama to run LLaMA 3 locally for fast, offline language generation

Hugging Face Transformers for embedding generation using sentence-transformers

Matplotlib for optional visualization and analysis of chatbot response times

LLM and Embeddings Details
Primary LLM: llama3 running locally via Ollama

Embedding Model: all-MiniLM-L6-v2 from Sentence-Transformers

Fully free-tier compatible as all components run locally without requiring paid API keys



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



