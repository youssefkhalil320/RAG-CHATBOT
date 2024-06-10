from langchain.text_splitter import CharacterTextSplitter


def get_text_chunks(raw_text: str):
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separator="\n",
        length_function=len,
    )

    chunks = text_splitter.split_text(raw_text)

    return chunks
