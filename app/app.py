import sys
sys.path.append("src")

import streamlit as st
from rag import ask


st.title("📚 Document Q&A")

question = st.text_input("Ask a question about your document:")

if question:
    answer = ask(question)

    st.subheader("Answer")
    st.write(answer)