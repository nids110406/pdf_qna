# Requirements:
# pip install streamlit langchain chromadb openai python-dotenv sentence-transformers pymupdf
#OPENAI API KEY: xxxxxx


import streamlit as st
import os
import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="Chat with Your Notes", layout="centered")
st.title("📝 Chat with Your Notes (PDF Q&A Bot)")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# PDF extraction
def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Main app logic
if uploaded_file:
    with st.spinner("📖 Reading and processing your PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = splitter.split_text(raw_text)

        # ✅ Use HuggingFace embeddings instead of OpenAI
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = Chroma.from_texts(texts, embedding=embeddings, persist_directory="db")
        vectordb.persist()

        # Use OpenAI model only for answering (you can replace this too)
        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
            retriever=vectordb.as_retriever(search_kwargs={"k": 3})
        )
    st.success("✅ PDF processed! You can now ask questions.")

    user_query = st.text_input("❓ Ask a question from your PDF:")

    if user_query:
        with st.spinner("🤔 Thinking..."):
            result = qa.run(user_query)
            st.write("💡 **Answer:**")
            st.write(result)
