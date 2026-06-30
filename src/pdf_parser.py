import os
import pdfplumber

def save_uploaded_file(uploaded_file):
    """
    Save the uploaded PDF into the uploads folder.
    """

    upload_folder = "uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.
    """

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            text += page.extract_text() or ""

    return text