import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_feedback(resume_text, job_description):
    """
    Generate AI feedback for a resume using Gemini.
    """

    prompt = f"""
You are an expert ATS recruiter and professional resume reviewer.

Analyze the resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide your response using the following headings:

## Overall Evaluation

## Strengths

## Weaknesses

## Missing Skills

## Suggestions for Improvement

Keep the response professional, concise, and easy to understand.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"