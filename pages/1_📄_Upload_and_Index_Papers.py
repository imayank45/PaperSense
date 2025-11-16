import streamlit as st
import os
from src.loader import load_papers
from src.splitter import chunk_docs
from src.embeddings import get_embedding_model
from src.vector_db import rebuild_embeddings
from dotenv import load_dotenv

load_dotenv()

st.title("📄 Upload & Index Papers")

uploaded = st.file_uploader("Upload PDFs", accept_multiple_files=True)

# Save uploaded PDFs
if uploaded:
    for file in uploaded:
        with open(f"data/research_papers/{file.name}", "wb") as f:
            f.write(file.read())

    st.success("Files uploaded successfully!")

# Rebuild vector DB
if st.button("Build Vector Index"):

    docs = load_papers("data/research_papers")
    chunks = chunk_docs(docs)

    embeddings = get_embedding_model()

    rebuild_embeddings(chunks, embeddings)

    st.success("Vector Database Rebuilt Successfully!")
