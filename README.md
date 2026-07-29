# 🤖 AI Documentation Assistant

**A Retrieval-Augmented Generation (RAG) app that turns any documentation site into a chatbot with cited, source-grounded answers.**

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black">
<img src="https://img.shields.io/badge/TypeScript-5-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
<img src="https://img.shields.io/badge/Qdrant-Vector%20DB-DC244C?style=for-the-badge">
<img src="https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4?style=for-the-badge&logo=google">
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</p>

<p align="center">
<a href="#demo">Demo</a> •
<a href="#architecture">Architecture</a> •
<a href="#tech-stack">Tech Stack</a> •
<a href="#getting-started">Getting Started</a> •
<a href="#api-reference">API</a> •
<a href="#roadmap">Roadmap</a>
</p>

---

## Overview

Point this app at a documentation URL (e.g. `docs.stripe.com`) and it crawls, chunks, and indexes the content into a vector database. Users then ask natural-language questions and get answers **grounded in that documentation** — not the LLM's general knowledge — along with a confidence score and clickable source citations.

This matters because plain LLM chat hallucinates and keyword search on large docs sites returns too much noise. Combining semantic retrieval with generation fixes both problems.

**What it demonstrates:** a complete, production-style RAG system — ingestion pipeline, vector search, prompt engineering, a FastAPI backend, a React frontend, Docker packaging, and an evaluation framework — built end-to-end as a single project.

---

## Key Features

| | |
|---|---|
| 🔍 **Semantic retrieval** | FastEmbed embeddings + Qdrant cosine similarity search |
| 🧠 **Grounded generation** | Gemini 2.5 Flash answers strictly from retrieved context |
| 📚 **Source attribution** | Every answer links back to the originating documentation |
| 📊 **Confidence scoring** | Surfaces how reliable each answer is |
| 🌐 **One-URL ingestion** | Firecrawl crawls & indexes a full docs site automatically |
| 💬 **Chat UI** | Responsive React + TypeScript interface |
| 🐳 **Dockerized** | One command to build and run the full backend |
| 🧪 **Tested & evaluated** | Pytest suite + a RAG quality evaluation framework |

---

## Demo

<table>
<tr>
<td width="50%"><img src="assets/landing-page.png"><p align="center"><sub>Chat interface with suggested prompts</sub></p></td>
<td width="50%"><img src="assets/chat-response.png"><p align="center"><sub>Answer with confidence score & sources</sub></p></td>
</tr>
<tr>
<td width="50%"><img src="assets/swagger-api.png"><p align="center"><sub>Interactive Swagger API docs</sub></p></td>
<td width="50%"><img src="assets/ingestion-api.png"><p align="center"><sub>Indexing a docs site from a URL</sub></p></td>
</tr>
</table>

---

## Architecture

The system follows a classic RAG flow: retrieve relevant context *before* generating, instead of asking the LLM to answer from memory alone.

<p align="center">
<img src="assets/system-architecture.png" width="850">
</p>

**Request lifecycle** — user question → embedding → vector search → prompt construction → generation → cited answer:

<p align="center">
<img src="assets/request-lifecycle.png" width="500">
</p>

**Ingestion pipeline** — how a documentation URL becomes searchable vectors:

<p align="center">
<img src="assets/ingestion-pipeline.png" width="480">
</p>

<details>
<summary><b>Component breakdown</b></summary>

| Layer | Responsibility |
|---|---|
| **React Frontend** | Chat UI, renders confidence scores & source citations |
| **FastAPI Backend** | Request validation, orchestration, prompt construction, response formatting |
| **FastEmbed** | Converts the user query into a dense semantic vector |
| **Qdrant** | Vector similarity search over indexed documentation chunks |
| **Prompt Builder** | Combines the question + retrieved chunks + system instructions |
| **Gemini 2.5 Flash** | Generates the final answer strictly from supplied context |

</details>

---

## Tech Stack

<p align="center">
<img src="assets/tech-stack.png" width="600">
</p>

| Layer | Technologies |
|---|---|
| **Frontend** | React, TypeScript, Tailwind CSS, Axios |
| **Backend** | FastAPI, Pydantic, Docker |
| **AI / Data** | Gemini 2.5 Flash, FastEmbed, Firecrawl, Qdrant |

<details>
<summary><b>Why these choices?</b></summary>

| Choice | Reason |
|---|---|
| **RAG over plain LLM chat** | Grounds answers in real docs → fewer hallucinations, traceable sources |
| **FastAPI** | Async support, automatic OpenAPI docs, type-safe validation |
| **Qdrant** | Fast, production-ready vector search with metadata filtering |
| **FastEmbed** | Lightweight embeddings — low memory footprint for local/Docker use |
| **Gemini 2.5 Flash** | Fast inference with strong instruction-following for context-bound answers |
| **Firecrawl** | Automates crawling, link discovery, and clean Markdown extraction |

</details>

---

## Project Structure

```
ai-documentation-assistant/
├── app/
│   ├── api/            # Route handlers
│   ├── ingestion/      # Crawling, chunking, embedding
│   ├── retrieval/      # Vector search
│   ├── services/       # Prompt building, LLM calls
│   ├── models.py
│   └── main.py
├── frontend/
│   ├── components/
│   ├── hooks/
│   ├── pages/
│   └── api/
├── evaluation/         # RAG quality evaluation framework
├── tests/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Getting Started

### Prerequisites

Python 3.12+, Node.js 20+, Docker, Git

### 1. Clone & configure

```bash
git clone https://github.com/<your-github-username>/ai-documentation-assistant.git
cd ai-documentation-assistant
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
FIRECRAWL_API_KEY=your_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
COLLECTION_NAME=documentation
UPSERT_BATCH_SIZE=50
```

### 2. Run the backend

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend → `http://localhost:8000`  •  Swagger docs → `http://localhost:8000/docs`

### 3. Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend → `http://localhost:5173`

### Or, run everything with Docker

```bash
docker compose up --build
```

---

## API Reference

| Endpoint | Description |
|---|---|
| `POST /ingest` | Crawl and index a documentation URL |
| `POST /chat` | Ask a question, get an answer + confidence + sources |
| `GET /health` | Health check |
| `GET /metrics` | Request count, latency, documents indexed |

**Example — `POST /chat`**

```json
// Request
{ "question": "What is Stripe?" }
```

```json
// Response
{
  "answer": "Stripe is a financial infrastructure platform that enables businesses to accept online payments...",
  "confidence": 0.77,
  "sources": [
    { "title": "Common use cases | Stripe Documentation",
      "url": "https://docs.stripe.com/get-started/use-cases" }
  ]
}
```

---

## Testing & Evaluation

```bash
pytest              # run test suite
python evaluation/runner.py   # RAG quality evaluation (retrieval, correctness, confidence)
```

Evaluation reports are written to `evaluation/results.json`.

---

## Roadmap

This repo is **v1** — a working RAG chatbot. Planned next:

<p align="center">
<img src="assets/system-design-roadmap.png" width="600">
</p>

- 🎤 **Voice interaction** — speech-to-text (Whisper/Deepgram) and text-to-speech (ElevenLabs/Azure)
- 🎧 **Streaming responses** — token + voice streaming for lower latency
- 💬 **Conversational memory** — multi-turn, context-aware follow-ups
- 🔍 **Hybrid search** — semantic + BM25 keyword search
- 🎯 **Reranking** — cross-encoder reranking before prompt construction
- 🔐 **Auth** — user accounts and API authentication
- ☁️ **Cloud deployment** — AWS / GCP / Azure / Kubernetes

---

## License

MIT — free to use, modify, and build on for learning or personal projects.

---

## Author

**Antrika Kashyap** — Computer Science Undergraduate, AI & Backend Developer

[GitHub](https://github.com/antrika02) • [LinkedIn](https://www.linkedin.com/in/antrika-kashyap-070502250/)

<p align="center"><sub>⭐ If this project was useful or interesting, consider starring the repo.</sub></p>
