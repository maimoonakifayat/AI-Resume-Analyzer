import streamlit as st

from src.pdf_parser import save_uploaded_file, extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score
from src.charts import create_skill_chart
from src.resume_suggestions import generate_suggestions
from src.report_generator import generate_report
from src.ai_feedback import generate_ai_feedback


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
missing skills, and AI-powered improvement suggestions.
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

    # Extract text
    resume_text = extract_text_from_pdf(saved_path)

    # Extract skills
    skills = extract_skills(resume_text)

    # Calculate ATS score
    score, matched_skills, missing_skills = calculate_ats_score(
        resume_text,
        job_description
    )

    # Generate suggestions
    suggestions = generate_suggestions(
        score,
        missing_skills
    )

    # Generate AI feedback
    ai_feedback = generate_ai_feedback(
        resume_text,
        job_description
    )

    # Generate PDF report
    report_path = generate_report(
        uploaded_file.name,
        score,
        matched_skills,
        missing_skills,
        suggestions
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
        st.subheader("Missing Skills")

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
    # Analysis Summary
    # -----------------------------
    st.subheader("Analysis Summary")

    st.write(f"**Resume Skills Found:** {len(skills)}")
    st.write(f"**Matched Skills:** {len(matched_skills)}")
    st.write(f"**Missing Skills:** {len(missing_skills)}")
    st.write(f"**Final ATS Score:** {score:.1f}%")

    st.divider()

    # -----------------------------
    # Resume Suggestions
    # -----------------------------
    st.subheader("💡 Resume Improvement Suggestions")

    for suggestion in suggestions:
        if suggestion.startswith("   -"):
            st.markdown(suggestion)
        else:
            st.write(suggestion)

    st.divider()

    # -----------------------------
    # AI Feedback
    # -----------------------------
    st.subheader("🤖 AI Resume Review")

    st.markdown(ai_feedback)

    st.divider()

    # -----------------------------
    # Download Report
    # -----------------------------
    st.subheader("📄 Download Report")

    with open(report_path, "rb") as pdf_file:
        st.download_button(
            label="📥 Download Resume Analysis Report",
            data=pdf_file,
            file_name="Resume_Analysis_Report.pdf",
            mime="application/pdf"
        )