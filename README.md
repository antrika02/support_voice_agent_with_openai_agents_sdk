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

## Overview

Point this app at a documentation URL and it crawls, chunks, embeds and indexes the content into Qdrant. Users ask natural-language questions and receive grounded answers with confidence scores and source citations.

---

## Demo

<table>
<tr>
<td><img src="assets/Landing_pge.png"><br><sub>Landing Page</sub></td>
<td><img src="assets/Chat_response.png"><br><sub>AI Response</sub></td>
</tr>
<tr>
<td><img src="assets/Swagger_ui.png"><br><sub>Swagger UI</sub></td>
<td><img src="assets/ingestion_pipeline.png"><br><sub>Documentation Ingestion</sub></td>
</tr>
</table>

---

## Architecture

<p align="center">
<img src="assets/sys_architecture.png" width="850">
</p>

### Request Lifecycle

<p align="center">
<img src="assets/rqst_lifecycle.png" width="600">
</p>

### Ingestion Pipeline

<p align="center">
<img src="assets/ingestion_pipeline.png" width="600">
</p>

---

## Tech Stack

<p align="center">
<img src="assets/techno_stack.png" width="650">
</p>

---

## Project Structure

<p align="center">
<img src="assets/folder-structure.svg" width="700">
</p>

---

## Getting Started

```bash
git clone https://github.com/antrika02/ai-documentation-assistant.git
cd ai-documentation-assistant

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

---

## Roadmap

<p align="center">
<img src="assets/System_design.png" width="650">
</p>

- Voice interaction
- Streaming responses
- Conversational memory
- Hybrid retrieval
- Cloud deployment

---

## Author

**Antrika Kashyap**

GitHub: https://github.com/antrika02

LinkedIn: https://www.linkedin.com/in/antrika-kashyap-070502250/
