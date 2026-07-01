import streamlit as st
from src.pdf_parser import save_uploaded_file, extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.markdown("""
Analyze your resume against a job description and receive an ATS compatibility score,
missing skills, and improvement suggestions.
""")

st.divider()

uploaded_file = st.file_uploader(
    " Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    " Paste the Job Description",
    height=200,
    placeholder="Paste the complete job description here..."
)

analyze_button = st.button(" Analyze Resume")

if analyze_button:

    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste the job description.")
        st.stop()

    saved_path = save_uploaded_file(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.write(f"**Saved to:** {saved_path}")

    st.write("### Resume Information")

    st.write(f"**File Name:** {uploaded_file.name}")

    file_size = uploaded_file.size / 1024

    st.write(f"**File Size:** {file_size:.2f} KB")

    resume_text = extract_text_from_pdf(saved_path)

    skills = extract_skills(resume_text)

    score, matched_skills, missing_skills = calculate_ats_score(
    resume_text,
    job_description
)

    st.write("## Resume Text")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=300
    )

    st.write("## Skills Found")

    if skills:

       for skill in skills:
         st.success(skill)

    else:

       st.warning("No skills found.")

    st.write("## ATS Compatibility Score")

    st.progress(score / 100)

    st.metric(
      "ATS Score",
       f"{score:.1f}%"
)   
 
    st.write("## Matched Skills")

    if matched_skills:

      for skill in matched_skills:
        st.success(skill)

    st.write("## Missing Skills")

    if missing_skills:

      for skill in missing_skills:
        st.error(skill)
    else:
      st.success("No missing skills!")    