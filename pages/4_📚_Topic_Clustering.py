import streamlit as st
from src.loader import load_papers
from src.clustering import cluster_embeddings

st.title("📚 Topic Clustering")

docs = load_papers("data/research_papers")

papers = {}
for d in docs:
    title = d.metadata.get("paper_title")
    papers.setdefault(title, []).append(d)

num_papers = len(papers)

st.write(f"📄 Total Papers Loaded: **{num_papers}**")

k = st.slider("Number of Clusters", 1, max(1, num_papers), 2)

if st.button("Generate Clusters"):
    clusters = cluster_embeddings(papers, num_clusters=k)

    for cid, paper_list in clusters.items():
        st.subheader(f"Cluster {cid + 1}")
        for p in paper_list:
            st.write(f"- {p}")
