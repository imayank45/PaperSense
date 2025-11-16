# src/vector_db.py
from langchain_community.vectorstores import FAISS
import os
import shutil

def rebuild_embeddings(chunks, embeddings, save_path="data/vector_store"):
    """Always rebuild FAISS index from scratch."""
    if os.path.exists(save_path):
        shutil.rmtree(save_path)

    os.makedirs(save_path, exist_ok=True)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(save_path)
    return db


def load_embeddings(embeddings, save_path="data/vector_store"):
    """Load FAISS index for chat page."""
    index_file = os.path.join(save_path, "index.faiss")
    pkl_file   = os.path.join(save_path, "index.pkl")

    if not (os.path.exists(index_file) and os.path.exists(pkl_file)):
        raise ValueError("❌ Vector DB not built yet. Go to 'Upload & Index' page first.")

    db = FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return db
