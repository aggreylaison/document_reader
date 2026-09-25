import psycopg2
import os
from pgvector.psycopg2 import register_vector

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="document_search",
        user="postgres",
        password=os.environ.get("DB_PASSWORD")
    )
    return conn

def insert_chunk(conn,content,embeddings):
    register_vector(conn)
    cur=conn.cursor()

    cur.execute("INSERT INTO chunks_table (content,embeddings) VALUES (%s,%s)",(content,embeddings))

    conn.commit()
    cur.close()
        