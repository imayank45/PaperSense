from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

def format_docs(docs):
    formatted = []
    for d in docs:
        title = d.metadata.get('paper_title', d.metadata.get('title', 'Unknown Title'))
        page = d.metadata.get('page', '')

        formatted.append(
            f"Paper: {title} (page {page})\nContent: {d.page_content}"
        )
        
    return "\n\n".join(formatted)



def get_rag_chain(retriever):
    
    prompt_template = """
You are a research synthesis assistant.

Use ONLY the information in the context to answer the question.
Speak naturally (like ChatGPT), not robotically.
Whenever you use information from a paper, mention the paper title as citation:
Example: (from "Agentic_AI_Survey")

---
CONTEXT:
{context}

QUESTION:
{question}

---
Final Answer:
    """
    
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=['context','question']
    )
    
    llm = ChatOpenAI(
        model='gpt-4o-mini',
        temperature=0.2
    )
    
    parser = StrOutputParser()
    
    parallel = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })
    
    return parallel | prompt | llm | parser