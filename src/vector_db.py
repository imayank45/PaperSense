# src/vector_db.py
from langchain_community.vectorstores import FAISS
import os

def create_or_load_embeddings(chunks, embeddings, save_path="data/vector_store"):
    index_file = os.path.join(save_path, "index.faiss")
    pkl_file   = os.path.join(save_path, "index.pkl")

    if os.path.exists(index_file) and os.path.exists(pkl_file):
        try:
            db = FAISS.load_local(
                save_path,
                embeddings,
                allow_dangerous_deserialization=True
            )

            # dimension check
            test_vec = embeddings.embed_query("dimension_check")
            if len(test_vec) != db.index.d:
                print("⚠️ Dimension mismatch! Rebuilding FAISS index...")
                raise ValueError("dimension mismatch")

            return db
        except:
            pass  # fall through to rebuild

    os.makedirs(save_path, exist_ok=True)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(save_path)
    return db
