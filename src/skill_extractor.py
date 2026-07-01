def extract_skills(text):
    """
    Extract common technical skills from resume text.
    """

    skills_database = [
        "Python",
        "Java",
        "C++",
        "C",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "TensorFlow",
        "PyTorch",
        "OpenCV",
        "Git",
        "GitHub",
        "Docker",
        "Linux",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Flask",
        "Django",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Scikit-learn"
    ]

    found_skills = []

    lower_text = text.lower()

    for skill in skills_database:

        if skill.lower() in lower_text:

            found_skills.append(skill)

    return found_skills