import streamlit as st
from src.notes import load_notes

st.title("🗒️ Research Notes")

notes = load_notes()

for n in notes:
    st.write("### Question")
    st.write(n["question"])
    st.write("### Answer")
    st.write(n["answer"])
    st.write("---")
