import streamlit as st
from src.loader import load_papers
from src.summaries import summarize_paper

st.title("📝 Summaries Per File")

docs = load_papers("data/research_papers")
papers = {}

for d in docs:
    # Safely get title from metadata
    title = d.metadata.get("paper_title") or d.metadata.get("title") or "Unknown Paper"

    papers.setdefault(title, []).append(d)
    
for title, pages in papers.items():
    if st.button(f"Summarize: {title}"):
        s = summarize_paper(pages, title)
        st.write(f"### {title}")
        st.write(s)
