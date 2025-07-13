🔍 GitHub Chatbot (Local LLM)
A fully local chatbot that enables natural language querying of GitHub repositories. It indexes code and documentation from selected repos, then allows conversational queries using FAISS, LangChain, and Mistral (via Ollama) — all without requiring internet access.

Built with:

🧠 LangChain

📦 FAISS

🧬 HuggingFace Transformers

📄 Unstructured

🌐 Streamlit

🤖 Ollama for running Mistral locally

⚙️ 1. Prerequisites
Install the following on your system before starting:

Python 3.10+

Git

pip

virtualenv (recommended)

Ollama (to run mistral or other local LLMs)

Then pull the Mistral model:

bash
Copy
Edit
ollama pull mistral
📦 2. Project Setup (From Scratch)
bash
Copy
Edit
# Clone the repo
git clone git@github.com:Gutman-Lab/GitHub-Chatbot-Local-LLM.git

# Navigate into project directory
cd GitHub-Chatbot-Local-LLM
🧪 3. Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # or 'venv\Scripts\activate' on Windows
📥 4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

# Additional packages (if not included)
pip install -U langchain-community
pip install unstructured tiktoken chardet
📁 5. Project Structure
bash
Copy
Edit
GitHub-Chatbot-Local-LLM/
├── backend/
│   ├── ingest/
│   │   └── github_scraper.py         # Downloads GitHub repos
│   ├── vectorstore/
│   │   └── store_embeddings.py       # Embeds files with LLM encoder
│   └── chat/
│       └── rag_chat.py               # RAG pipeline using FAISS + Mistral
├── frontend/
│   └── streamlit_app.py              # Chat interface using Streamlit
├── data/                             # Downloaded repositories go here
├── .env                              # Environment config
├── requirements.txt
└── README.md
🔄 6. Clone GitHub Repositories to Query
Run the scraper script to download public GitHub repositories into the data/ folder:

bash
Copy
Edit
python backend/ingest/github_scraper.py
📝 You may edit the script to customize the repository URLs you want to scrape.

🧠 7. Generate Embeddings
After downloading the repos, generate vector embeddings:

bash
Copy
Edit
python backend/vectorstore/store_embeddings.py
This will embed the documents using a HuggingFace model and store them in a FAISS index.

💬 8. Launch the Chatbot Interface
Start the Streamlit-based UI:

bash
Copy
Edit
streamlit run frontend/streamlit_app.py
Open your browser at: http://localhost:8501

🧪 9. Example Questions to Try
You can ask natural language queries like:

“What does the function parse_slide_metadata do?”

“Explain how job tracking is handled in job_tracker.php.”

“Which file contains the SLURM job duration analysis?”

“What is HistomicsUI used for?”

“Where is the Dockerfile located in the repository?”

“What is the purpose of the Digital Slide Archive?”

“How does HistomicsUI interact with the Girder backend?”

“What are the core components of HistomicsTK?”

“Which file contains plugin definitions for HistomicsUI?”

“How are image annotations stored and retrieved?”

✅ Final Checklist
 ✅ Python + pip installed

 ✅ Ollama with Mistral pulled

 ✅ Repo cloned

 ✅ Virtualenv activated

 ✅ All dependencies installed

 ✅ GitHub repos scraped

 ✅ Embeddings generated

 ✅ Streamlit app running

