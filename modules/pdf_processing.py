from PyPDF2 import PdfReader


def get_pdf_text(pdf_docs) -> str:
    text = ""
    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text
