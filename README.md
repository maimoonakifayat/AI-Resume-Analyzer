# AI Resume Analyzer & Interview Coach

An AI-powered resume analysis and interview preparation system built with Python and Streamlit. The application analyzes a resume against a job description, calculates an ATS compatibility score, identifies missing skills, provides AI-powered feedback, and conducts interactive mock interviews.

---

## Features

### Resume Analysis

- Upload a resume in PDF format
- Extract resume text automatically
- Detect technical skills
- Compare resume skills with job requirements

### ATS Compatibility Analysis

- Calculate an ATS compatibility score
- Identify matched skills
- Identify missing skills
- Visualize skill matching with an interactive chart

### Resume Improvement

- Generate personalized resume improvement suggestions
- Provide AI-powered resume feedback using Google Gemini
- Generate a downloadable PDF analysis report

### AI Interview Coach

- Generate personalized interview questions
- Questions are based on the candidate's resume and job description
- Support different interview types:
  - Technical Interview
  - HR Interview
  - Project Interview
  - Job-Specific Interview

### Interactive Mock Interview

- Start a simulated interview
- Answer AI-generated questions
- Receive AI evaluation of your answers
- Get follow-up questions based on previous answers
- Complete a 5-question interview session

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- pdfplumber
- Plotly
- python-dotenv
- Git & GitHub

---

## Project Structure

```text
AI-Resume-Analyzer/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|
|-- src/
|   |-- __init__.py
|   |-- pdf_parser.py
|   |-- skill_extractor.py
|   |-- ats_score.py
|   |-- charts.py
|   |-- resume_suggestions.py
|   |-- ai_feedback.py
|   |-- interview_coach.py
|   |-- mock_interview.py
|   `-- report_generator.py
|
|-- tests/
|   |-- test_interview_coach.py
|   `-- test_mock_interview.py
|
|-- data/
`-- uploads/