from sklearn.cluster import KMeans
import numpy as np


def cluster_embeddings(vectors, docs, k=3):
    
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(vectors)
    
    grouped = {}
    for label, doc in zip(labels, docs):
        grouped.setdefault(label, []).append(doc)
        
    return grouped