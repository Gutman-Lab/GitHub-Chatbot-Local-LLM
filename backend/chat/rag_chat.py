from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings


def chat_with_repo(query: str) -> str:
    # Load embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Load FAISS vector store
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Set up retriever
    retriever = db.as_retriever()

    # Load the Ollama model (e.g., mistral)
    llm = OllamaLLM(model="mistral")

    # Set up RetrievalQA
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)

    # Return only the result (no query or dict)
    return qa.invoke(query)["result"]
