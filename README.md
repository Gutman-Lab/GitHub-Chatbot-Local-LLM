# 🤖 GitHub Chatbot with Local LLM

An interactive chatbot for querying GitHub code repositories using local LLMs. 

---

## Project Structure

github-chatbot/
├── backend/
│ ├── api.py # FastAPI backend server
│ ├── chat/
│ │ ├── history_utils.py # Chat history handling
│ │ └── rag_chat.py # RAG (LLM + vector) core logic
│ ├── ingest/
│ │ ├── store_embeddings.py # Embedding and vector DB generator
│ │ └── github_scraper.py # Scrapes code from GitHub repo URL
├── data/ # Put your code repos here
├── vectorstore/ # Stores embeddings / vector index
├── frontend/
│ └── streamlit_app.py # Streamlit frontend chatbot UI
├── requirements.txt # Python dependencies

---

## Prerequisites

- Python **3.9+**
- `pip` (latest)
- Optional for local LLMs:
  - [Ollama](https://ollama.com) installed and running for local model support (e.g., `mistral`, `codellama`)
- System Requirements:
  - Minimum **16GB RAM**
  - Recommended GPU **≥48GB VRAM** for large models (use quantized models otherwise)

---

## Installation

### 1. Clone the repository

git clone https://github.com/Gutman-Lab/GitHub-Chatbot-Local-LLM.git
cd GitHub-Chatbot-Local-LLM

2. Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows

3. Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

Ingest Code Repository Embeddings
Option A: Manual Repository
Clone or place your code repositories into the data/ folder.

Generate embeddings:

python backend/ingest/store_embeddings.py data/
Option B: Scrape from GitHub
Use github_scraper.py to automatically download a GitHub repository to data/:

python backend/ingest/github_scraper.py https://github.com/username/repo-name
Then generate embeddings:

python backend/ingest/store_embeddings.py data/

Running Locally

1. Start Backend (FastAPI API)
uvicorn backend.api:app --reload
Access API at: http://localhost:8000/

2. Start Frontend (Streamlit Chatbot UI)
streamlit run frontend/streamlit_app.py

Opens chatbot at: http://localhost:8501/

## Features
- Code-aware search over entire GitHub repos
- RAG (Retrieval-Augmented Generation) with local LLMs
- Chat history and memory
- Support for multiple models via Ollama (mistral, llama3, codellama, etc.)
- Ingest repos manually or from GitHub link
- Local vectorstore support with FAISS