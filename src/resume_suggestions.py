def generate_suggestions(score, missing_skills):

    suggestions = []

    if score < 50:
        suggestions.append(
            "Your resume needs significant improvements to match the job description."
        )

    elif score < 75:
        suggestions.append(
            "Your resume is a decent match but could be improved."
        )

    else:
        suggestions.append(
            "Your resume is a strong match for this position."
        )

    if missing_skills:

        suggestions.append(
            "Consider adding experience with these missing skills:"
        )

        for skill in missing_skills:
            suggestions.append(f"   - {skill}")

    suggestions.append(
        "Use action verbs such as Developed, Built, Designed, Implemented."
    )

    suggestions.append(
        "Include measurable achievements whenever possible."
    )

    suggestions.append(
        "Tailor your professional summary for each application."
    )

    return suggestions