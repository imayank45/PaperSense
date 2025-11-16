from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def summarize_paper(pages, title):

    text = "\n".join([p.page_content for p in pages])

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    prompt = f"""
    Summarize the following research paper in exactly 3 lines.

    **Paper Title:** {title}

    ----------------------
    {text}
    ----------------------
    """

    return llm.invoke(prompt).content
