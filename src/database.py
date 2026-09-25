import psycopg2
import os
from pgvector.psycopg import register_vector

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="document_search",
        user="postgres",
        password=os.environ.get("ag")
    )
    return conn

def insert_chunk(conn,content,embedding):
    register_vector(conn)
    cur=conn.cursor()

    cur.execute("INSERT INTO chunks (content,embedding) VALUES (%s,%s)",(content,embedding))

    conn.commit()
    cur.close()
        