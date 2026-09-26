from pgvector.psycopg2 import register_vector

def search_chunks(conn, query_embedding, top_k=5):
    register_vector(conn)
    cur = conn.cursor()
    
    cur.execute(
        """
        SELECT id, content, embeddings <=> %s AS distance
        FROM chunks_table
        ORDER BY distance
        LIMIT %s
        """,
        (query_embedding, top_k)
    )
    
    results = cur.fetchall()
    cur.close()
    return results