import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from backend.chat.history_utils import save_chat
from backend.logging_config import logger

QA_PROMPT = PromptTemplate.from_template("""
You are a helpful assistant trained to explain GitHub codebases. Format your response in Markdown with bullet points, code blocks, and helpful tips.

Context:
{context}

Question:
{question}

Answer (Markdown):
""")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def chat_with_repo(query: str, model: str = "mistral:latest") -> str:
    logger.info(f"User query: {query}")

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en",
        model_kwargs={"device": "cpu"}
    )
    db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = OllamaLLM(model=model, temperature=0.2)

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": QA_PROMPT},
        return_source_documents=False
    )

    memory_vars = memory.load_memory_variables({})
    inputs = {"question": query, "chat_history": memory_vars.get("chat_history", [])}
    result = qa_chain.invoke(inputs)["answer"]
    logger.info(f"LLM response: {result[:100]}...")
    save_chat(query, result, model=model)
    return result
