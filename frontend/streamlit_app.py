import sys
import os
import streamlit as st

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.chat.rag_chat import chat_with_repo

# --- Page config ---
st.set_page_config(page_title="GitHub Chatbot", layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        padding-top: 2rem;
    }
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #262730;
        text-align: center;
        margin-bottom: 1rem;
    }
    .query-box input {
        border: 2px solid #4a90e2;
        border-radius: 8px;
        padding: 12px;
        font-size: 1rem;
    }
    .response-box {
        background-color: #ffffff;
        border-left: 6px solid #4a90e2;
        padding: 20px;
        margin-top: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="title"> GitHub Chatbot (Local LLM)</div>', unsafe_allow_html=True)

# --- Input ---
query = st.text_input("Ask a question about your GitHub repositories:", key="query")

# --- Process Query ---
if query:
    with st.spinner("Thinking..."):
        response = chat_with_repo(query)

    # --- Display Answer ---
    st.markdown(f'<div class="response-box"><strong>Answer:</strong><br>{response}</div>', unsafe_allow_html=True)
