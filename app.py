import streamlit as st

# Configure the page
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Main Heading
st.title("📄 AI Resume Analyzer")

st.write("""
Welcome to the AI Resume Analyzer!

This application will:
-  Read your resume
-  Compare it with a job description
-  Calculate a match score
-  Suggest improvements
""")

st.success("Project setup completed successfully! ")