import streamlit as st

from src.pdf_parser import save_uploaded_file, extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score
from src.charts import create_skill_chart
from src.resume_suggestions import generate_suggestions
from src.report_generator import generate_report
from src.ai_feedback import generate_ai_feedback
from src.interview_coach import generate_interview_questions
from src.mock_interview import (
    generate_interview_question,
    evaluate_interview_answer
)


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

st.markdown(
    """
    Analyze your resume against a job description and receive an ATS compatibility
    score, missing skills, improvement suggestions, AI-powered feedback, and
    personalized interview preparation.
    """
)

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
# Initialize Session State
# -----------------------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "report_path" not in st.session_state:
    st.session_state.report_path = ""

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if "previous_questions" not in st.session_state:
    st.session_state.previous_questions = []

if "previous_answers" not in st.session_state:
    st.session_state.previous_answers = []

if "interview_evaluations" not in st.session_state:
    st.session_state.interview_evaluations = []


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

    # Extract text from resume
    resume_text = extract_text_from_pdf(saved_path)

    if not resume_text.strip():
        st.error("Could not extract text from the uploaded PDF.")
        st.stop()

    # Save important information in session state
    st.session_state.resume_text = resume_text
    st.session_state.job_description = job_description

    # Extract skills
    skills = extract_skills(resume_text)

    # Calculate ATS score
    score, matched_skills, missing_skills = calculate_ats_score(
        resume_text,
        job_description
    )

    # Generate improvement suggestions
    suggestions = generate_suggestions(
        score,
        missing_skills
    )

    # Generate PDF report
    report_path = generate_report(
        uploaded_file.name,
        score,
        matched_skills,
        missing_skills,
        suggestions
    )

    st.session_state.report_path = report_path
    st.session_state.analysis_done = True

    # Reset previous interview
    st.session_state.interview_started = False
    st.session_state.current_question = ""
    st.session_state.previous_questions = []
    st.session_state.previous_answers = []
    st.session_state.interview_evaluations = []

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
        value=resume_text,
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
    # Matched and Missing Skills
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
    # Skill Match Chart
    # -----------------------------
    st.subheader("Skill Match Analysis")

    chart = create_skill_chart(
        matched_skills,
        missing_skills
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Analysis Summary
    # -----------------------------
    st.subheader("Analysis Summary")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:
        st.metric("Resume Skills", len(skills))

    with summary_col2:
        st.metric("Matched Skills", len(matched_skills))

    with summary_col3:
        st.metric("Missing Skills", len(missing_skills))

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

    with st.spinner("Analyzing your resume with Gemini..."):

        ai_feedback = generate_ai_feedback(
            resume_text,
            job_description
        )

    if ai_feedback.startswith("❌"):
        st.error(ai_feedback)
    else:
        st.markdown(ai_feedback)


# ============================================================
# AI INTERVIEW COACH
# ============================================================

if st.session_state.analysis_done:

    st.divider()

    st.subheader("🎤 AI Interview Coach")

    st.write(
        "Practice for your interview with questions personalized "
        "to your resume and the selected job."
    )

    interview_type = st.selectbox(
        "Choose Interview Type",
        [
            "Technical Interview",
            "HR Interview",
            "Project Interview",
            "Job-Specific Interview"
        ],
        key="interview_type"
    )

    # -----------------------------
    # Start Mock Interview
    # -----------------------------
    if not st.session_state.interview_started:

        if st.button("🎤 Start Mock Interview"):

            with st.spinner(
                "Preparing your personalized interview..."
            ):

                first_question = generate_interview_question(
                    st.session_state.resume_text,
                    st.session_state.job_description,
                    interview_type
                )

            st.session_state.current_question = first_question
            st.session_state.previous_questions = []
            st.session_state.previous_answers = []
            st.session_state.interview_evaluations = []
            st.session_state.interview_started = True

            st.rerun()

    # -----------------------------
    # Interview In Progress
    # -----------------------------
    if st.session_state.interview_started:

        st.success("Mock interview started!")

        question_number = (
            len(st.session_state.previous_questions) + 1
        )

        st.subheader(
            f"Question {question_number} of 5"
        )

        st.info(
            st.session_state.current_question
        )

        answer = st.text_area(
            "Your Answer",
            height=180,
            key=f"answer_{question_number}",
            placeholder="Type your answer here..."
        )

        submit_answer = st.button(
            "Submit Answer",
            key=f"submit_{question_number}"
        )

        if submit_answer:

            if not answer.strip():

                st.warning(
                    "Please write an answer before submitting."
                )

            else:

                with st.spinner(
                    "Evaluating your answer..."
                ):

                    evaluation = evaluate_interview_answer(
                        st.session_state.current_question,
                        answer,
                        st.session_state.resume_text,
                        st.session_state.job_description
                    )

                st.session_state.previous_questions.append(
                    st.session_state.current_question
                )

                st.session_state.previous_answers.append(
                    answer
                )

                st.session_state.interview_evaluations.append(
                    evaluation
                )

                st.subheader("📊 AI Evaluation")

                st.markdown(evaluation)

                # -----------------------------
                # Next Question
                # -----------------------------
                if len(st.session_state.previous_questions) < 5:

                    with st.spinner(
                        "Preparing your next question..."
                    ):

                        next_question = generate_interview_question(
                            st.session_state.resume_text,
                            st.session_state.job_description,
                            interview_type,
                            st.session_state.previous_questions,
                            answer
                        )

                    st.session_state.current_question = next_question

                    st.rerun()

                else:

                    st.success(
                        "🎉 Mock interview completed!"
                    )

                    st.subheader(
                        "📋 Interview Summary"
                    )

                    st.write(
                        f"You completed "
                        f"{len(st.session_state.previous_questions)} "
                        f"interview questions."
                    )

                    if st.button(
                        "🔄 Start New Interview"
                    ):

                        st.session_state.interview_started = False
                        st.session_state.current_question = ""
                        st.session_state.previous_questions = []
                        st.session_state.previous_answers = []
                        st.session_state.interview_evaluations = []

                        st.rerun()


# ============================================================
# DOWNLOAD REPORT
# ============================================================

if st.session_state.analysis_done:

    st.divider()

    st.subheader("📄 Download Report")

    report_path = st.session_state.report_path

    if report_path and st.session_state.analysis_done:

        with open(report_path, "rb") as pdf_file:

            pdf_data = pdf_file.read()

        st.download_button(
            label="📥 Download Resume Analysis Report",
            data=pdf_data,
            file_name="Resume_Analysis_Report.pdf",
            mime="application/pdf"
        )