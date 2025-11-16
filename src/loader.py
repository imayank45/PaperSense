from langchain_community.document_loaders import PyPDFLoader
import os

def load_papers(dir_path):
    docs = []

    for file in os.listdir(dir_path):
        if file.endswith(".pdf"):
            path = os.path.join(dir_path, file)
            loader = PyPDFLoader(path)
            pages = loader.load()

            # Inject metadata: paper title = filename
            for p in pages:
                p.metadata["paper_title"] = file

            docs.extend(pages)

    return docs
