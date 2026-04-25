from pypdf import PdfReader
from PyPDF2 import PdfReader

def process_pdf(file_path):
    reader = PdfReader(file_path)

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text

    # Split into chunks
    chunk_size = 500
    chunks = []

    for i in range(0, len(full_text), chunk_size):
        chunks.append(
            full_text[i:i+chunk_size]
        )

    return chunks
def extract_text_from_pdf(pdf_path):
    reader=PdfReader(pdf_path)
    text=""

    for page in reader.pages:
        text += page.extract_text()

    return text


def chunk_text(text,chunk_size=500,overlap=50):
    chunks=[]

    for i in range(
       0,
       len(text),
       chunk_size-overlap
    ):
       chunks.append(
         text[i:i+chunk_size]
       )

    return chunks
