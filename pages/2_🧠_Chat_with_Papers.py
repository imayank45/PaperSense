import streamlit as st
from src.embeddings import get_embedding_model
from src.vector_db import load_embeddings
from src.retriever import build_retriever
from src.rag_chain import get_rag_chain
from src.notes import save_note

st.title("🧠 Chat with Research Papers")

query = st.text_input("Ask a question about your research papers")

if st.button("Ask") and query:

    embeddings = get_embedding_model()

    # Load the FAISS DB created in page 1
    db = load_embeddings(embeddings)

    retriever = build_retriever(db)
    rag_chain = get_rag_chain(retriever)

    answer = rag_chain.invoke(query)

    st.write(answer)

    save_note(query, answer)
