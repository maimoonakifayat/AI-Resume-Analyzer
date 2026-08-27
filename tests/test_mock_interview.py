from src.mock_interview import generate_interview_question


resume = """
Python developer with experience in Python, Machine Learning,
TensorFlow, OpenCV and Computer Vision.
"""

job_description = """
We are looking for an AI Engineer with experience in Python,
Machine Learning, TensorFlow and Computer Vision.
"""

question = generate_interview_question(
    resume,
    job_description,
    "Technical Interview"
)

print("\nMock Interview Question:\n")
print(question)