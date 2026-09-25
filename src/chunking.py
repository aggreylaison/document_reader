from markitdown import MarkItDown
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embedding import get_embedding
from database import connect_db, insert_chunk



md=MarkItDown()

result=md.convert("/home/aggrey/doc_search/Crop_Recommendation_Presentation_Notes.docx")

maked_down=result.text_content

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)

chunks=text_splitter.split_text(maked_down)

conn=connect_db()
embedded_chunks=[]

for chunk in chunks:
    embedded = get_embedding(chunk)
    embedded_chunks.append(embedded)
    insert_chunk(conn, chunk, embedded)

conn.close()