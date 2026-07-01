import streamlit as st
from src.pdf_parser import save_uploaded_file, extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score
from src.charts import create_skill_chart

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Analyzer")

st.markdown("""
Analyze your resume against a job description and receive an ATS compatibility score,
missing skills, and improvement suggestions.
""")

st.divider()

# -----------------------------
# User Input
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description",
    height=200,
    placeholder="Paste the complete job description here..."
)

analyze_button = st.button("Analyze Resume")

# -----------------------------
# Analyze Resume
# -----------------------------
if analyze_button:

    # Validate input
    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste the job description.")
        st.stop()

    # Save uploaded resume
    saved_path = save_uploaded_file(uploaded_file)

    # Extract resume text
    resume_text = extract_text_from_pdf(saved_path)

    # Extract resume skills
    skills = extract_skills(resume_text)

    # Calculate ATS score
    score, matched_skills, missing_skills = calculate_ats_score(
        resume_text,
        job_description
    )

    # -----------------------------
    # Dashboard
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:

        st.success("Resume uploaded successfully!")

        st.subheader("Resume Information")

        st.write(f"**File Name:** {uploaded_file.name}")

        file_size = uploaded_file.size / 1024

        st.write(f"**File Size:** {file_size:.2f} KB")

    with col2:

        st.subheader("ATS Compatibility")

        st.progress(score / 100)

        st.metric(
            label="ATS Score",
            value=f"{score:.1f}%"
        )

    st.divider()

    # -----------------------------
    # Resume Text
    # -----------------------------
    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

    st.divider()

    # -----------------------------
    # Skills Found
    # -----------------------------
    st.subheader("Skills Found")

    if skills:

        for skill in skills:
            st.success(skill)

    else:

        st.warning("No skills found.")

    st.divider()

    # -----------------------------
    # Matched & Missing Skills
    # -----------------------------
    left, right = st.columns(2)

    with left:

        st.subheader("Matched Skills")

        if matched_skills:

            for skill in matched_skills:
                st.success(skill)

        else:

            st.info("No matched skills.")

    with right:

        st.subheader(" Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.error(skill)

        else:

            st.success("No missing skills!")

    st.divider()

    # -----------------------------
    # Pie Chart
    # -----------------------------
    st.subheader("Skill Match Analysis")

    chart = create_skill_chart(
        matched_skills,
        missing_skills
    )

    st.plotly_chart(
        chart,
         width="stretch"
    )

    st.divider()

    # -----------------------------
    # Summary
    # -----------------------------
    st.subheader("Analysis Summary")

    st.write(f"**Resume Skills Found:** {len(skills)}")
    st.write(f"**Matched Skills:** {len(matched_skills)}")
    st.write(f"**Missing Skills:** {len(missing_skills)}")
    st.write(f"**Final ATS Score:** {score:.1f}%")