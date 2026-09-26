from ollama import chat
from search import search_chunks
from embedding import get_embedding
from database import connect_db

def ask(question):

    question_embedding=get_embedding(question)

    conn=connect_db()

    result=search_chunks(conn,question_embedding,top_k=3)
    conn.close()

    context="/n/n".join(
        content for _,content,_ in result
    )

    prompt=f""" use the following context to answer the question
    context:{context}
    Question:{question}"""

    response=chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role":"user",
                "content":prompt

            }
        ]
    )

    return response.message.content