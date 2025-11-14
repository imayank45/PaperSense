# src/embeddings.py

from langchain_openai import OpenAIEmbeddings

def get_embedding_model():
    """
    Returns the embedding model used for document embedding.
    Modify here if you want to change embeddings later.
    """
    return OpenAIEmbeddings(model="text-embedding-3-large")
