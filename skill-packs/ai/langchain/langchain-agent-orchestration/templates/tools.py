from langchain_core.tools import tool

@tool
def search_docs(query: str) -> str:
    """Search internal documentation."""
    return retriever.invoke(query)
