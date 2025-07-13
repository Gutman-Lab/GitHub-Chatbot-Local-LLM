**GitHub Chatbot (Local LLM)**
A fully local chatbot that enables natural language querying of GitHub repositories. It indexes code and documentation from selected repos, then allows conversational queries using FAISS, LangChain, and Mistral (via Ollama) — all without requiring internet access.

Built with:

🧠 LangChain

📦 FAISS

🧬 HuggingFace Transformers

📄 Unstructured

🌐 Streamlit

🤖 Ollama for running Mistral locally

1. Prerequisites
Ensure the following are installed:
Python 3.10+
Git
pip (Python package manager)
virtualenv (recommended)
Ollama (for local LLM like mistral)

2. Project Setup
  git clone git@github.com:Gutman-Lab/GitHub-Chatbot-Local-LLM.git

  cd github-chatbot

4. Generate Embeddings

   python backend/vectorstore/store_embeddings.py

6. Run the Chatbot

   streamlit run frontend/streamlit_app.py

💬 Example Questions
Try asking natural language queries like:

What does the function parse_slide_metadata do?

Explain how job tracking is handled in job_tracker.php.

Which file contains the SLURM job duration analysis?

What is HistomicsUI used for?

Where is the Dockerfile located in the repository?

What is the purpose of the Digital Slide Archive?

How does HistomicsUI interact with the Girder backend?

What are the core components of HistomicsTK?

Which file contains the plugin definitions for HistomicsUI?

How are image annotations stored and retrieved?
