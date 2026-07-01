from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    score,
    matched_skills,
    missing_skills,
    suggestions
):

    pdf_name = "Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(pdf_name)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"])
    )

    story.append(
        Paragraph(f"<b>Resume:</b> {filename}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>ATS Score:</b> {score:.1f}%", styles["Normal"])
    )

    story.append(
        Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"])
    )

    for skill in matched_skills:
        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"])
    )

    for skill in missing_skills:
        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/><b>Suggestions</b>", styles["Heading2"])
    )

    for suggestion in suggestions:
        story.append(
            Paragraph(suggestion, styles["Normal"])
        )

    doc.build(story)

    return pdf_name