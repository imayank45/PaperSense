import streamlit as st

st.set_page_config(page_title="PaperSense", layout="wide")

st.sidebar.title("📚 PaperSense Navigation")
st.sidebar.write("Local Research Assistant")

st.sidebar.page_link("pages/1_📄_Upload_and_Index_Papers.py", label="Upload & Index Papers")
st.sidebar.page_link("pages/2_🧠_Chat_with_Papers.py", label="Chat with Papers")
st.sidebar.page_link("pages/3_📝_Summaries_per_File.py", label="Paper Summaries")
st.sidebar.page_link("pages/4_📚_Topic_Clustering.py", label="Topic Clusters")
st.sidebar.page_link("pages/5_🗒️_Research_Notes.py", label="Research Notes")

st.title("📘 PaperSense — Local AI Research Assistant")
st.write("Select a page from the sidebar to begin.")
 