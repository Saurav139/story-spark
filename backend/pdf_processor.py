import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """Extract text from a single PDF file."""
    text = ""
    pdf = fitz.open(stream=pdf_file, filetype="pdf")
    for page_num in range(pdf.page_count):
        page = pdf[page_num]
        text += page.get_text()
    pdf.close()
    return text

def chunk_text(text, chunk_size=10):
    """Split text into chunks of approximately `chunk_size` words."""
    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks
