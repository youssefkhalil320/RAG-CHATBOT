import streamlit as st
from dotenv import load_dotenv
from modules.pdf_processing import get_pdf_text
from modules.text_chunking import get_text_chunks
from modules.vector_store import get_vectorstore


def main():
    load_dotenv()

    st.set_page_config(page_title="Chat with handbooks", page_icon=":books:")
    st.header("chat with handbooks :books:")
    st.text_input("Ask a question about the handbook:")

    with st.sidebar:
        st.subheader("handbook")
        pdf_docs = st.file_uploader(
            "Upload a handbook", accept_multiple_files=True)

        if st.button("Process"):
            with st.spinner("Cooking your documents"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vectorstore(text_chunks)


if __name__ == "__main__":
    main()
