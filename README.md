# 🎙️ Customer Support Voice Agent (Built From Scratch)

An AI-powered Customer Support Voice Agent built from scratch using a Retrieval-Augmented Generation (RAG) architecture.

This project is being developed step-by-step to understand every component of a production-grade RAG system instead of relying on high-level frameworks. The system crawls documentation websites, processes and chunks the content, generates semantic embeddings, stores them in a vector database, retrieves relevant context for user queries, and finally generates intelligent text and voice responses.

---

# 🚀 Project Goal

The objective of this project is to build a production-ready Voice AI Assistant capable of:

- Crawling documentation websites
- Building a semantic knowledge base
- Performing intelligent document retrieval
- Answering user questions accurately
- Generating natural voice responses
- Providing source attribution
- Deploying as a complete web application

---


# 🏗️ System Architecture

Current architecture:

```
Documentation Website
        │
        ▼
 Firecrawl Crawler
        │
        ▼
   Raw Documents
        │
        ▼
 Document Chunker
        │
        ▼
 Document Chunks
        │
        ▼
 FastEmbed Embeddings
        │
        ▼
  (Next)
 Qdrant Vector Database
        │
        ▼
 Semantic Retrieval
        │
        ▼
 Language Model
        │
        ▼
 Text Response
        │
        ▼
 Voice Generation
```

---

# 🧠 Learning Objectives

This repository focuses on understanding the internals of a RAG system rather than simply assembling libraries.

Topics covered include:

- Documentation Crawling
- Text Processing
- Document Chunking
- Sliding Window Chunking
- Embeddings
- Semantic Search
- Vector Databases
- Retrieval-Augmented Generation
- Prompt Engineering
- Voice AI
- Production Deployment

---

# 📂 Project Structure

```
customer-support-voice-agent/
│
├── app/
│   ├── __init__.py
│   ├── crawler.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── llm.py
│   ├── voice.py
│   ├── prompts.py
│   ├── models.py
│   ├── ui.py
│   └── utils.py
│
├── tests/
│   ├── test_config.py
│   ├── test_crawler.py
│   ├── test_chunker.py
│   └── test_embeddings.py
│
├── data/
│
├── logs/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# 🧩 Core Components

## 1. Documentation Crawler

Responsible for:

- Crawling documentation websites
- Extracting clean Markdown
- Creating structured Document objects

Technology:

- Firecrawl API

---

## 2. Document Chunker

Responsible for:

- Splitting large documents into manageable chunks
- Supporting overlapping chunks
- Preserving document metadata

Concepts:

- Sliding Window
- Chunk Size
- Overlap

---

## 3. Embedding Generator

Responsible for:

- Converting document chunks into vector embeddings
- Preparing vectors for semantic search

Technology:

- FastEmbed

---

## 4. Vector Store *(Coming Next)*

Responsible for:

- Storing embeddings
- Fast similarity search
- Metadata storage

Technology:

- Qdrant

---

## 5. Retrieval Engine *(Upcoming)*

Responsible for:

- Finding the most relevant chunks
- Building context for the LLM

---

## 6. Language Model *(Upcoming)*

Responsible for:

- Understanding user questions
- Generating accurate answers
- Using retrieved documentation as context

---

## 7. Voice Generation *(Upcoming)*

Responsible for:

- Converting generated answers into natural speech

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Firecrawl | Documentation Crawling |
| FastEmbed | Embeddings |
| HuggingFace | Language Models |
| Qdrant | Vector Database |
| Streamlit | User Interface |
| edge-tts | Text-to-Speech |
| Git | Version Control |

---

# 🔄 Current Workflow

```
Documentation URL

        │

        ▼

Firecrawl

        │

        ▼

Document

        │

        ▼

Chunker

        │

        ▼

Chunks

        │

        ▼

Embedding Generator

        │

        ▼

Vectors
```

---

# 🧪 Running the Project

Clone the repository

```bash
git clone <repository-url>
cd customer-support-voice-agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
FIRECRAWL_API_KEY=

HUGGINGFACE_API_KEY=

QDRANT_URL=

QDRANT_API_KEY=
```

Run tests

```bash
python -m tests.test_crawler
python -m tests.test_chunker
python -m tests.test_embeddings
```

Run the application

```bash
streamlit run app.py
```

---

# 📚 Key Concepts Learned

- API Integration
- Environment Variables
- Python Packages
- Data Classes
- Modular Project Design
- Sliding Window Chunking
- Semantic Embeddings
- Vector Representations
- Software Architecture

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---
