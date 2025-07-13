# GitHub-Chatbot-Local-LLM

GitHub-Chatbot-Local-LLM (Local LLM)
A fully local chatbot that allows you to query your GitHub repositories using natural language. Built with LangChain, FAISS, HuggingFace, and Streamlit, this project indexes source code and documentation from GitHub repos and enables ChatGPT-style querying powered by Mistral via Ollama.

**1. Prerequisites**
Ensure the following are installed:
Python 3.10+
Git
pip (Python package manager)
virtualenv (recommended)
Ollama (for local LLM like mistral)

**2. Project Setup**
git clone git@github.com:Gutman-Lab/GitHub-Chatbot-Local-LLM.git
cd github-chatbot

**3. Create a Virtual Environment**
python3 -m venv venv
source venv/bin/activate

**4. Install Required Packages**
pip install -r requirements.txt
Additional required packages:
pip install -U langchain-community
pip install unstructured tiktoken chardet
5. Project Structure

github-chatbot/
├── backend/
│   ├── ingest/
│   │   └── github_scraper.py          # GitHub repo downloader
│   ├── vectorstore/
│   │   └── store_embeddings.py        # Embedding generator
│   ├── chat/
│   │   └── rag_chat.py                # RAG logic using FAISS + LLM
├── frontend/
│   └── streamlit_app.py               # Web interface
├── data/                              # Downloaded GitHub repo contents
├── .env
└── README.md
└── requirements.txt

Clone GitHub Repositories
python backend/ingest/github_scraper.py
This will download the repos into data 

**6. Generate Embeddings**
python backend/vectorstore/store_embeddings.py

**7. Run the Chatbot**
streamlit run frontend/streamlit_app.py

**8. Test It Out**
Open your browser at: http://localhost:port


**Example questions:**

What does the function parse_slide_metadata do?
Explain how job tracking is handled in job_tracker.php.
Which file contains the SLURM job duration analysis?
What is HistomicsUI used for?
Where is the Dockerfile located in the repository?
What is the purpose of the Digital Slide Archive?
How does HistomicsUI interact with the Girder backend?
What are the core components of HistomicsTK?
Which file contains the plugin definitions for HistomicsUI?
How are image annotations stored and retrieved? write steps from scrach)
