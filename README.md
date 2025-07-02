# pdf_qna
# 🤖 Chat with Your Notes – PDF Q&A Bot

Chat with your PDFs like they're your personal tutor.

This app allows you to upload any PDF (lecture notes, research papers, eBooks, manuals) and ask questions directly about its content. Powered by LangChain, HuggingFace Embeddings, and an LLM backend, it provides contextually relevant answers in natural language.

---

## 🚀 Features

- 📄 Upload any PDF and interact with its content
- 🧠 Uses `HuggingFaceEmbeddings` (all-MiniLM-L6-v2) for document vectorization
- 🔎 Retrieval-based question answering (RAG) via LangChain
- 💬 Answers powered by OpenAI GPT models
- 🌐 Streamlit frontend for easy interaction

---

## 🛠️ Tech Stack

| Component      | Tool/Library                          |
|----------------|---------------------------------------|
| PDF Extraction | PyMuPDF (`fitz`)                      |
| Embeddings     | HuggingFace `all-MiniLM-L6-v2`        |
| Vector Store   | ChromaDB                              |
| QA Pipeline    | LangChain                             |
| UI             | Streamlit                             |
| LLM            | OpenAI GPT-3.5                        |

---

## 🧑‍💻 How It Works

1. Upload a `.pdf` file through the Streamlit UI.
2. The app extracts and splits the text into manageable chunks.
3. Each chunk is converted into vector embeddings using HuggingFace.
4. When you ask a question, the app finds the most relevant chunks and uses a language model to answer.

