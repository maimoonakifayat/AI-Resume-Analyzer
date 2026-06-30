import streamlit as st
from src.pdf_parser import save_uploaded_file, extract_text_from_pdf
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume in PDF format to begin the analysis."
)

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf"]
)

if uploaded_file is not None:

    saved_path = save_uploaded_file(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.write(f"**Saved to:** {saved_path}")

    st.write("### Resume Information")

    st.write(f"**File Name:** {uploaded_file.name}")

    file_size = uploaded_file.size / 1024

    st.write(f"**File Size:** {file_size:.2f} KB")

    resume_text = extract_text_from_pdf(saved_path)

    st.write("## Resume Text")

    st.text_area(
    "Extracted Text",
    resume_text,
    height=300
)