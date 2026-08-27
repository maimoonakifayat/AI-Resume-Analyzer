import re


def extract_skills(text):
    """
    Extract technical skills from resume or job description text.
    """

    skills_database = [
        # Programming Languages
        "Python",
        "Java",
        "C++",
        "C",
        "C#",
        "JavaScript",
        "TypeScript",
        "Go",
        "Rust",
        "PHP",
        "Ruby",
        "Kotlin",
        "Swift",

        # AI / Machine Learning
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Natural Language Processing",
        "Computer Vision",
        "Generative AI",
        "Large Language Models",
        "LLM",
        "RAG",
        "Retrieval-Augmented Generation",
        "Prompt Engineering",
        "Reinforcement Learning",
        "Neural Networks",
        "Transformers",
        "Transfer Learning",

        # AI / ML Frameworks
        "TensorFlow",
        "PyTorch",
        "Keras",
        "Scikit-learn",
        "Hugging Face",
        "OpenCV",
        "LangChain",
        "LangGraph",

        # Data Science
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "SciPy",
        "Jupyter",
        "Jupyter Notebook",

        # Web Development
        "HTML",
        "CSS",
        "React",
        "Angular",
        "Vue.js",
        "Node.js",
        "Express.js",
        "Flask",
        "Django",
        "FastAPI",
        "Streamlit",

        # Databases
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "SQLite",
        "Redis",

        # Cloud / DevOps
        "AWS",
        "Microsoft Azure",
        "Azure",
        "Google Cloud",
        "GCP",
        "Docker",
        "Kubernetes",
        "Jenkins",
        "CI/CD",
        "GitHub Actions",
        "Terraform",

        # Tools / Version Control
        "Git",
        "GitHub",
        "GitLab",
        "Linux",
        "Bash",
        "PowerShell",

        # APIs / Other Technologies
        "REST API",
        "GraphQL",
        "WebSocket",
        "Firebase",
        "Postman"
    ]

    found_skills = []

    if not text:
        return found_skills

    lower_text = text.lower()

    for skill in skills_database:

        # Escape special characters such as +, #, ., etc.
        escaped_skill = re.escape(skill.lower())

        # Match the skill as a complete phrase/word.
        pattern = rf"(?<!\w){escaped_skill}(?!\w)"

        if re.search(pattern, lower_text):
            found_skills.append(skill)

    return found_skills