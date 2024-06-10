import streamlit as st
from dotenv import load_dotenv
from modules.pdf_processing import get_pdf_text
from modules.text_chunking import get_text_chunks
from modules.vector_store import get_vectorstore
from modules.conversation import get_conversational_chain, handle_user_question
from templates.html_template import css, bot_template, user_template


def main():
    load_dotenv()

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.set_page_config(page_title="Chat with handbooks", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    st.header("chat with handbooks :books:")
    user_question = st.text_input("Ask a question about the handbook:")

    if user_question:
        handle_user_question(user_question)

    with st.sidebar:
        st.subheader("handbook")
        pdf_docs = st.file_uploader(
            "Upload a handbook", accept_multiple_files=True)

        if st.button("Process"):
            with st.spinner("Cooking your documents"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversational_chain(
                    vector_store)


if __name__ == "__main__":
    main()
