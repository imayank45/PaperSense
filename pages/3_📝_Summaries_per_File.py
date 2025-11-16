import streamlit as st
from src.loader import load_papers
from src.summaries import summarize_paper

st.title("📝 Summaries Per File")

docs = load_papers("data/research_papers")

# Group pages by title
papers = {}
for d in docs:
    title = d.metadata.get("paper_title")
    papers.setdefault(title, []).append(d)

# Create summarize buttons
for title, pages in papers.items():
    if st.button(f"Summarize: {title}"):
        s = summarize_paper(pages, title)
        st.write(f"### {title}")
        st.write(s)
