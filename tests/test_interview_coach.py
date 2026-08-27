from src.interview_coach import generate_interview_questions


resume = """
Python developer with experience in Python, Machine Learning,
TensorFlow, OpenCV and Computer Vision. Built AI projects using
Python and machine learning.
"""

job_description = """
We are looking for an AI Engineer with experience in Python,
Machine Learning, TensorFlow and Computer Vision.
"""

questions = generate_interview_questions(
    resume,
    job_description,
    "Technical Interview"
)

print("\nGenerated Interview Questions:\n")
print(questions)