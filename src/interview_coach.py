import os

import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

genai.configure(api_key=api_key)


def generate_interview_questions(resume_text, job_description, interview_type):
    prompt = f"""
You are an expert interviewer helping a candidate prepare for a job interview.

Analyze the candidate's resume and the job description below.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

INTERVIEW TYPE:
{interview_type}

Generate 5 personalized interview questions.

Requirements:
- Questions must be relevant to the candidate's resume.
- Questions must match the job description.
- Avoid generic questions.
- Include a mixture of technical and practical questions.
- Do not provide answers.
- Number the questions from 1 to 5.
"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text