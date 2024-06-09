import streamlit as st


def main():
    st.set_page_config(page_title="Chat with handbooks", page_icon=":books:")
    st.header("chat with handbooks :books:")
    st.text_input("Ask a question about the handbook:")

    with st.sidebar:
        st.subheader("handbook")
        st.file_uploader("Upload a handbook")
        st.button("Process")


if __name__ == "__main__":
    main()
