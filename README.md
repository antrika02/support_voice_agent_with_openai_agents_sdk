# 🎙️ Customer Support Voice Agent
### Enterprise AI Documentation Assistant with Retrieval-Augmented Generation (RAG)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Status](https://img.shields.io/badge/Status-Under%20Active%20Development-success)

---

# 📖 Overview

Customer Support Voice Agent is a production-oriented AI assistant built completely from scratch using a Retrieval-Augmented Generation (RAG) architecture.

Unlike many RAG projects that rely heavily on orchestration frameworks such as LangChain or LlamaIndex, this project focuses on implementing every major component manually to understand how modern enterprise AI systems are designed.

The application crawls documentation websites, builds a semantic knowledge base using vector embeddings, retrieves the most relevant documentation chunks, generates context-aware responses using Google's Gemini LLM, and exposes the complete workflow through a production-ready FastAPI backend.

The long-term objective is to evolve this project into a real-time conversational Voice AI Agent capable of interacting naturally with users through speech while maintaining enterprise-grade software engineering practices.

---

# 🎯 Project Goals

This project aims to build a complete AI-powered customer support platform capable of:

- Crawling documentation websites automatically
- Building semantic knowledge bases
- Performing intelligent vector search
- Retrieval-Augmented Generation (RAG)
- Multi-turn conversational memory
- Confidence scoring
- Source attribution
- Dynamic documentation ingestion
- REST API services
- Production logging
- Middleware architecture
- Dependency Injection
- Global exception handling
- Docker containerization
- Real-time voice conversations (Upcoming)
- Cloud deployment (Upcoming)

---

# ✨ Current Features

## Knowledge Base

- Automatic documentation discovery
- Documentation crawling using Firecrawl
- Markdown extraction
- Intelligent document chunking
- Metadata preservation
- Sliding window chunking

---

## Retrieval

- FastEmbed embeddings
- Qdrant vector database
- Semantic similarity search
- Top-K retrieval
- Retrieval score filtering
- Configurable similarity thresholds

---

## RAG Pipeline

- Prompt engineering
- Conversation memory
- Gemini LLM integration
- Context-aware responses
- Confidence calculation
- Source attribution

---

## Backend

- FastAPI REST API
- Request validation
- Response models
- Dependency Injection
- Lifespan events
- Middleware
- Structured logging
- Global exception handling
- Docker support

---

## Evaluation

- Custom evaluation datasets
- Automated evaluation pipeline
- Confidence reporting
- JSON reports
- Regression testing

---

# 🏗 High-Level System Architecture

```text
                     Documentation Website
                              │
                              ▼
                   Documentation Discovery
                              │
                              ▼
                   Firecrawl Documentation
                              │
                              ▼
                     Raw Documentation
                              │
                              ▼
                      Document Chunker
                              │
                              ▼
                      Semantic Chunks
                              │
                              ▼
                   FastEmbed Embeddings
                              │
                              ▼
                    Qdrant Vector Database
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
     User Question                      Conversation Memory
          │                                       │
          └───────────────┬───────────────────────┘
                          ▼
                  Retrieval Engine
                          │
                          ▼
                 Prompt Builder
                          │
                          ▼
                     Gemini LLM
                          │
                          ▼
                  Final AI Response
                          │
                          ▼
                    FastAPI Response

                  (Voice Layer Coming Soon)
```

---

# 🧠 Retrieval-Augmented Generation Pipeline

The assistant follows a complete RAG workflow.

```text
User Question

      │

      ▼

Generate Embedding

      │

      ▼

Semantic Search

      │

      ▼

Retrieve Top-K Chunks

      │

      ▼

Confidence Calculation

      │

      ▼

Prompt Engineering

      │

      ▼

Gemini LLM

      │

      ▼

Answer + Sources
```

Unlike a traditional chatbot, responses are grounded in retrieved documentation instead of relying solely on the language model's internal knowledge.

---

# 🧩 Core Components

## 1. Documentation Discovery

Automatically discovers documentation pages starting from a root URL.

Responsibilities:

- URL discovery
- Sitemap traversal
- Documentation indexing

---

## 2. Documentation Crawler

Uses Firecrawl to extract structured documentation.

Responsibilities:

- Markdown extraction
- Metadata preservation
- Clean document generation

---

## 3. Document Chunker

Large documents are split into overlapping semantic chunks.

Benefits:

- Better retrieval accuracy
- Improved context preservation
- Reduced hallucinations

---

## 4. Embedding Generator

Uses FastEmbed to convert text into dense vector representations.

Responsibilities:

- Query embeddings
- Chunk embeddings
- Batch embedding generation

---

## 5. Vector Store

Uses Qdrant as the semantic database.

Responsibilities:

- Collection creation
- Batched uploads
- Vector search
- Metadata storage
- Collection management

---

## 6. Retriever

Responsible for semantic search.

Pipeline:

Question

↓

Embedding

↓

Vector Search

↓

Top K Results

↓

Score Filtering

↓

Relevant Context

---

## 7. Prompt Builder

Builds production-quality prompts.

Prompt includes:

- Conversation history
- Retrieved documentation
- Current question
- System instructions

---

## 8. Conversation Memory

Maintains conversational context across multiple interactions.

Capabilities:

- Previous user messages
- Previous assistant messages
- Configurable history size

---

## 9. RAG Engine

Acts as the orchestration layer.

Workflow:

Question

↓

Retriever

↓

Confidence

↓

Prompt Builder

↓

Gemini

↓

Response

---

## 10. Evaluation Framework

Provides automated evaluation of RAG performance.

Supports:

- Ground truth comparisons
- Confidence analysis
- JSON reports
- Regression testing

---

# ⚙️ Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Backend | FastAPI |
| LLM | Google Gemini |
| Embeddings | FastEmbed |
| Vector Database | Qdrant |
| Crawling | Firecrawl |
| Validation | Pydantic |
| API Docs | Swagger / OpenAPI |
| Logging | Python Logging |
| Containerization | Docker |
| Testing | Pytest / Custom Test Suite |

---

# 📂 Project Structure

```text
customer-support-voice-agent/

├── app/
│
├── api/
│   ├── routes.py
│   ├── schemas.py
│   ├── dependencies.py
│   └── metrics.py
│
├── rag/
│   ├── rag_engine.py
│   ├── prompt_builder.py
│   └── confidence.py
│
├── retrieval/
│   ├── retriever.py
│   ├── embeddings.py
│   └── vector_store.py
│
├── ingestion/
│   ├── discovery.py
│   ├── crawler.py
│   └── manager.py
│
├── llm/
│   ├── factory.py
│   ├── gemini.py
│   └── base.py
│
├── memory/
│
├── middleware/
│
├── logging/
│
├── exceptions/
│
├── evaluation/
│
├── tests/
│
├── data/
│
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.py
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/customer-support-voice-agent.git

cd customer-support-voice-agent
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=

FIRECRAWL_API_KEY=

QDRANT_URL=

QDRANT_API_KEY=
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

The API will be available at

```
http://localhost:8000
```

Swagger documentation

```
http://localhost:8000/docs
```

---

# 🌐 REST API

## Chat

```
POST /chat
```

Example

```json
{
  "question": "How does Python support object-oriented programming?"
}
```

---

## Dynamic Documentation Ingestion

```
POST /ingest
```

Example

```json
{
  "url": "https://docs.stripe.com"
}
```

---

## Health

```
GET /health
```

---

## Metrics

```
GET /metrics
```

# 📊 Evaluation Framework

One of the primary goals of this project is to build an AI system whose performance can be measured rather than assumed.

The project includes a custom evaluation pipeline capable of testing the RAG system against predefined datasets.

## Evaluation Workflow

```text
Evaluation Dataset
        │
        ▼
User Question
        │
        ▼
RAG Pipeline
        │
        ▼
Generated Answer
        │
        ▼
Compare With Ground Truth
        │
        ▼
Generate Evaluation Report
```

### Current Evaluation Metrics

- Ground Truth Comparison
- Retrieved Context Inspection
- Confidence Score
- Source Validation
- JSON Report Generation

Example:

```bash
python -m tests.test_evaluation
```

Generated report:

```
evaluation/results.json
```

---

# 📈 Confidence Scoring

The retrieval engine computes a confidence score for every response using retrieval similarity scores.

Current strategy:

```
Confidence =
0.7 × Highest Retrieval Score
+
0.3 × Average Retrieval Score
```

This score provides an estimate of how relevant the retrieved documentation is for answering the user's question.

Future improvements include:

- Cross-Encoder confidence
- Answer faithfulness
- Hallucination detection
- Calibration curves

---

# 🧾 Structured Logging

Every major subsystem uses structured logging instead of print statements.

Logging includes:

- Application startup
- Shutdown
- API requests
- Retrieval events
- Prompt generation
- Knowledge ingestion
- Qdrant operations
- Error tracking

Example log:

```
INFO | app.rag.rag_engine | Prompt length: 1315 characters

INFO | app.retrieval.vector_store | Connected to Qdrant

INFO | app.ingestion.manager | Knowledge base successfully indexed.
```

Benefits:

- Easier debugging
- Production observability
- Cleaner monitoring
- Better developer experience

---

# 🛡 Global Exception Handling

The project implements centralized exception handling to provide consistent API responses.

Instead of exposing internal stack traces, the API returns standardized error responses.

Example:

```json
{
    "detail": "Internal server error."
}
```

Benefits:

- Improved security
- Cleaner client experience
- Consistent API behavior

---

# ⚡ Middleware

The application uses custom middleware to intercept requests before they reach the API endpoints.

Current middleware includes:

### Request Logging

Logs:

- HTTP Method
- Endpoint
- Client IP
- Processing information

---

### Request Timing

Measures request latency for performance monitoring.

Future enhancements:

- Request IDs
- Correlation IDs
- Prometheus metrics
- OpenTelemetry tracing

---

# 🔄 Dependency Injection

FastAPI's dependency injection system is used throughout the project.

Benefits include:

- Loose coupling
- Improved testing
- Better maintainability
- Cleaner architecture

Example:

```python
rag: RAGEngine = Depends(get_rag_engine)
```

Rather than instantiating services inside API routes, dependencies are provided automatically by FastAPI.

---

# 🚀 Application Lifespan Management

The application initializes shared resources during startup.

Resources initialized include:

- Gemini client
- FastEmbed model
- Vector Store
- RAG Engine
- Knowledge Base Manager

Benefits:

- Faster requests
- Reduced initialization overhead
- Cleaner startup sequence

---

# 📚 Dynamic Documentation Ingestion

Unlike many RAG systems that require rebuilding the application to ingest new data, this project supports runtime knowledge ingestion.

Workflow:

```text
POST /ingest

        │

        ▼

Documentation URL

        │

        ▼

Discovery

        │

        ▼

Firecrawl

        │

        ▼

Chunking

        │

        ▼

Embeddings

        │

        ▼

Qdrant

        │

        ▼

Knowledge Base Updated
```

This enables the assistant to continuously learn from new documentation without modifying the source code.

---

# 🧪 Testing

The repository includes tests for major components.

Current coverage includes:

- Documentation crawler
- Chunker
- Embedding generator
- Retrieval pipeline
- Evaluation pipeline
- Knowledge ingestion
- RAG engine

Run all tests:

```bash
python -m tests.test_chunker

python -m tests.test_embeddings

python -m tests.test_rag

python -m tests.test_ingestion

python -m tests.test_evaluation
```

---

# 🛠 Engineering Decisions

This project intentionally avoids high-level orchestration frameworks.

Instead of relying on LangChain or LlamaIndex for the core pipeline, the following components are implemented manually:

- Retrieval
- Prompt Construction
- Confidence Scoring
- Conversation Memory
- Knowledge Ingestion
- Vector Storage
- RAG Orchestration

The objective is to understand the underlying architecture rather than abstracting it away.

---

# 📅 Development Milestones

## ✅ Phase 1 — Project Foundation

- Modular project architecture
- Configuration management
- Environment variables

---

## ✅ Phase 2 — Documentation Discovery

- URL discovery
- Documentation indexing

---

## ✅ Phase 3 — Documentation Crawling

- Firecrawl integration
- Markdown extraction
- Structured document generation

---

## ✅ Phase 4 — Document Chunking

- Sliding window chunking
- Metadata preservation
- Configurable chunk sizes

---

## ✅ Phase 5 — Embedding Generation

- FastEmbed integration
- Batch embedding generation

---

## ✅ Phase 6 — Vector Database

- Qdrant integration
- Collection management
- Batched uploads
- Semantic search

---

## ✅ Phase 7 — Retrieval Layer

- Query embeddings
- Top-K retrieval
- Similarity filtering

---

## ✅ Phase 8 — Prompt Engineering

- Context-aware prompt generation
- Conversation history integration

---

## ✅ Phase 9 — Gemini Integration

- LLM abstraction layer
- Gemini implementation
- Factory pattern

---

## ✅ Phase 10 — Conversation Memory

- Multi-turn conversations
- Configurable history window

---

## ✅ Phase 11 — RAG Engine

Complete orchestration layer.

Responsible for:

- Retrieval
- Prompt building
- LLM invocation
- Source generation
- Confidence scoring

---

## ✅ Phase 12 — Evaluation Framework

- Evaluation datasets
- Automated reporting
- JSON results

---

## ✅ Phase 13 — Dynamic Knowledge Ingestion

- Runtime documentation indexing
- FastAPI endpoint

---

## ✅ Phase 14 — Production Backend

- FastAPI
- REST APIs
- Dependency Injection
- Lifespan
- Middleware
- Logging
- Exception handling

---

## ✅ Phase 15 — Dockerization

- Dockerfile
- Docker Compose
- Containerized execution

---

# 🚧 Current Progress

| Module | Status |
|----------|---------|
| Documentation Discovery | ✅ Complete |
| Firecrawl Integration | ✅ Complete |
| Chunking | ✅ Complete |
| Embeddings | ✅ Complete |
| Qdrant Integration | ✅ Complete |
| Semantic Retrieval | ✅ Complete |
| Prompt Engineering | ✅ Complete |
| Gemini Integration | ✅ Complete |
| Conversation Memory | ✅ Complete |
| Confidence Scoring | ✅ Complete |
| Evaluation Framework | ✅ Complete |
| Dynamic Knowledge Ingestion | ✅ Complete |
| FastAPI REST API | ✅ Complete |
| Dependency Injection | ✅ Complete |
| Lifespan Events | ✅ Complete |
| Middleware | ✅ Complete |
| Logging | ✅ Complete |
| Exception Handling | ✅ Complete |
| Docker | ✅ Complete |
| React Frontend | 🚧 In Progress |
| Speech-to-Text | 🚧 Planned |
| Text-to-Speech | 🚧 Planned |
| Real-Time Streaming | 🚧 Planned |
| CI/CD | 🚧 Planned |
| Cloud Deployment | 🚧 Planned |

---

# 🔮 Future Roadmap

The next development phase focuses on transforming the backend into a complete conversational AI platform.

## 🎤 Voice AI

- OpenAI Whisper
- Real-time transcription
- Streaming audio

---

## 🔊 Text-to-Speech

- ElevenLabs
- OpenAI TTS
- Azure Speech

---

## 🌐 Frontend

- React
- TypeScript
- Tailwind CSS
- Streaming chat interface
- Voice recording
- Conversation history

---

## ☁️ Cloud Deployment

- Docker Compose
- GitHub Actions
- Render / Railway
- Azure Container Apps
- AWS ECS

---

## 📊 Observability

- Prometheus
- Grafana
- OpenTelemetry
- Request tracing
- Latency dashboards

---

## 🧠 Advanced RAG

- Hybrid Search
- BM25
- Reciprocal Rank Fusion (RRF)
- Cross-Encoder Reranking
- Metadata Filtering
- Streaming Responses

---

# 💼 Resume Highlights

This project demonstrates practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- LLM Integration
- Prompt Engineering
- FastAPI
- Docker
- Dependency Injection
- Middleware
- Structured Logging
- REST API Development
- Software Architecture
- Evaluation Frameworks
- Production-Oriented Backend Design

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "feat: add new feature"
```

4. Push the branch

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Antrika Kashyap**

Computer Science Undergraduate | AI & Backend Engineering Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub!

---

