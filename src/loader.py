from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_papers(folder_path = "data/research_papers"):
    
    loader = DirectoryLoader(
        path = folder_path,
        glob = "*.pdf",
        loader_cls = PyPDFLoader
    )
    
    papers = loader.load()
    
    return papers