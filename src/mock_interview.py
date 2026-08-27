import os

import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

genai.configure(api_key=api_key)


def generate_interview_question(
    resume_text,
    job_description,
    interview_type,
    previous_questions=None,
    previous_answer=None
):
    """
    Generate the next personalized interview question.
    """

    if previous_questions is None:
        previous_questions = []

    if previous_answer is None:
        previous_answer = ""

    previous_questions_text = "\n".join(
        f"- {question}" for question in previous_questions
    )

    prompt = f"""
You are an expert interviewer conducting a realistic job interview.

Candidate Resume:
{resume_text}

Job Description:
{job_description}

Interview Type:
{interview_type}

Questions already asked:
{previous_questions_text}

Candidate's previous answer:
{previous_answer}

Your task is to generate ONE next interview question.

Rules:
- Make the question relevant to the candidate's resume and the job.
- Do not repeat any previous question.
- Adapt the difficulty based on the candidate's previous answer.
- If the previous answer was weak, ask a simpler follow-up question.
- If the previous answer was strong, ask a deeper question.
- Keep the question natural and conversational.
- Return ONLY the question.
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text.strip()


def evaluate_interview_answer(
    question,
    answer,
    resume_text,
    job_description
):
    """
    Evaluate the candidate's answer.
    """

    prompt = f"""
You are an expert interview evaluator.

Candidate Resume:
{resume_text}

Job Description:
{job_description}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Provide:

1. Score out of 10
2. What was done well
3. What could be improved
4. A better example of how the answer could be structured

Be honest but constructive.

Keep the evaluation concise and useful.
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text.strip()