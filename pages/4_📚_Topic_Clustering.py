import streamlit as st
from src.loader import load_papers
from src.splitter import chunk_docs
from src.embeddings import get_embedding_model
from src.clustering import cluster_embeddings

st.title("📚 Topic Clustering")

docs = load_papers("data/research_papers")
chunks = chunk_docs(docs)
emb = get_embedding_model()

vectors = emb.embed_documents([c.page_content for c in chunks])
clusters = cluster_embeddings(vectors, chunks, k=3)

for cluster, items in clusters.items():
    st.subheader(f"Cluster {cluster + 1}")
    for doc in items:
        st.write(f"- {doc.metadata.get('paper_title', 'Unknown Title')}")
