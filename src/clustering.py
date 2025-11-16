from sklearn.cluster import KMeans
import numpy as np
from src.embeddings import get_embedding_model

def cluster_embeddings(papers_by_title, num_clusters=3):

    titles = []
    paper_texts = []

    # Combine document pages per paper
    for title, pages in papers_by_title.items():
        full_text = "\n".join(p.page_content for p in pages)
        titles.append(title)
        paper_texts.append(full_text)

    # If too few papers -> reduce k
    total_papers = len(titles)
    if total_papers < num_clusters:
        num_clusters = total_papers  # Auto-adjust
    if num_clusters == 0:
        return {}  # no papers

    embeddings = get_embedding_model()
    vectors = embeddings.embed_documents(paper_texts)
    vectors = np.array(vectors)

    # KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(vectors)

    clusters = {}
    for label, title in zip(labels, titles):
        clusters.setdefault(label, []).append(title)

    return clusters
