from markitdown import MarkItDown
from langchain_text_splitters import RecursiveCharacterTextSplitter




md=MarkItDown()

result=md.convert("/home/aggrey/doc_search/Crop_Recommendation_Presentation_Notes.docx")

maked_down=result.text_content

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)

chunks=text_splitter.split_text(maked_down)

print(chunks)