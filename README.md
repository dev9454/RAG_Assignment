Friendly Mental Health Chatbot
Overview
This project is a Retrieval-Augmented Generation (RAG)-based chatbot designed to provide empathetic and helpful responses rooted in trusted mental health resources. The chatbot offers emotional support by combining vector-based document retrieval with local language model generation, delivering informed and emotionally intelligent answers.

Problem Statement
The Challenge
Many people seeking emotional support may hesitate to consult professionals or find it overwhelming to sift through vast amounts of mental health literature.

Our Solution
This chatbot addresses these issues by providing accessible, reliable, and empathetic guidance based on verified mental health content. Unlike generic chatbots that solely rely on large language models (LLMs), this system uses RAG to ground responses in factual documents, reducing hallucinations and improving relevance.

Why Use Retrieval-Augmented Generation (RAG)?
RAG improves the quality and trustworthiness of chatbot responses by retrieving relevant text passages from verified resources before generating a reply. This process ensures that responses are:

Factually informed and accurate

Grounded in real-world data

Less prone to fabrications or hallucinations

By combining retrieval with generation, the chatbot produces helpful and contextually appropriate answers.

RAG Architecture Overview
Data for Retrieval
The chatbot uses a curated knowledge base stored in the file mental_health_resources.txt.

This file contains supportive advice, therapy techniques, and emotional wellness tips sourced from credible mental health resources.

Retrieval Component
Vector Store: ChromaDB, which efficiently indexes and searches document embeddings.

Embedding Model: all-MiniLM-L6-v2 from Hugging Face sentence-transformers, used to convert text documents into vector representations.

Document Splitting: LangChain’s RecursiveCharacterTextSplitter to break down large texts into manageable chunks for better retrieval.

Generation Component
Large Language Model (LLM): llama3 accessed via Ollama for local inference.

Framework: LangChain to orchestrate the retrieval and generation pipeline.

Prompting Strategy: A custom prompt template that incorporates conversation history and retrieved documents to generate concise, friendly, and relevant responses.

Tools and Frameworks
LangChain: For building and managing the RAG pipeline workflow.

ChromaDB: Acts as the vector database enabling fast similarity search over the knowledge base.

Ollama: Provides local, offline access to the LLaMA 3 model for response generation without external API dependencies.

Hugging Face Transformers: Used for embedding generation with the sentence-transformers library.

Matplotlib: Optional tool for visualizing response time analytics.

Model and Embeddings Details
Language Model: llama3 running locally via Ollama, enabling privacy and fast response times.

Embedding Model: all-MiniLM-L6-v2 from Sentence-Transformers, which balances performance and speed.

Cost and Accessibility: All components operate locally with no need for paid API keys, making the solution free-tier friendly and privacy-conscious.




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



