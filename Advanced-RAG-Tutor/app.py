import streamlit as st
from dotenv import load_dotenv
import os

# LangChain (NEW imports)
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from groq import Groq

# Load env
load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# UI
st.set_page_config(page_title="AI Tutor RAG", layout="wide")
st.title("🧠 Advanced AI Tutor (RAG + Multi PDF)")

# Difficulty
level = st.selectbox(
    "Select Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

# Upload PDFs
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

# Store DB
if "db" not in st.session_state:
    st.session_state.db = None

# Process PDFs
if uploaded_files:
    with st.spinner("Processing PDFs... 📄"):
        documents = []

        for file in uploaded_files:
            with open(file.name, "wb") as f:
                f.write(file.read())

            loader = PyPDFLoader(file.name)
            documents.extend(loader.load())

        # Split
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=100
        )
        chunks = splitter.split_documents(documents)

        # Fast embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        # Vector DB
        db = FAISS.from_documents(chunks, embeddings)
        st.session_state.db = db

    st.success("✅ PDFs processed successfully!")

# Question input
query = st.text_input("Ask your question:")

# Ask button
if st.button("Ask"):
    if not st.session_state.db:
        st.warning("⚠️ Please upload PDF first")
    elif not query:
        st.warning("⚠️ Please enter a question")
    else:
        with st.spinner("Thinking... 🤔"):

            # Retrieve
            docs = st.session_state.db.similarity_search(query, k=3)

            context = "\n\n".join([doc.page_content for doc in docs])

            # Prompt
            prompt = f"""
You are an AI Tutor.

Difficulty Level: {level}

Use ONLY the context below to answer.

Context:
{context}

Question:
{query}

Answer in this format:
1. Definition
2. Key idea
3. Example
"""

            # LLM call
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            answer = response.choices[0].message.content

        # Show answer
        st.subheader("📘 Answer:")
        st.write(answer)

        # Sources
        st.subheader("📄 Sources:")
        for i, doc in enumerate(docs):
            page = doc.metadata.get("page", "N/A")
            st.write(f"Source {i+1}: Page {page}")