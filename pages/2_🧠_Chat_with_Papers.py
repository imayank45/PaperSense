import streamlit as st 
import os
from src.loader import load_papers
from src.splitter import chunk_docs
from src.embeddings import get_embedding_model
from src.vector_db import create_or_load_embeddings
from src.retriever import build_retriever
from src.rag_chain import get_rag_chain
from src.notes import save_note

st.title("🧠 Chat with Research Papers")


query = st.text_input("Ask a question about your research papers")

if st.button("Ask"):
    
    docs = load_papers("data/research_papers")
    chunks = chunk_docs(docs)
    embeddings = get_embedding_model()
    db = create_or_load_embeddings(chunks, embeddings)
    retriever = build_retriever(db) 
    
    rag_chain = get_rag_chain(retriever)
    answer = rag_chain.invoke(query)
    
    st.write(answer)
    
    save_note(query, answer)