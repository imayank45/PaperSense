def build_retriever(vector_db):
    return vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )
