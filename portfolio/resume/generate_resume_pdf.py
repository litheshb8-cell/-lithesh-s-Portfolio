from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

out_path = Path(__file__).with_name("resume.pdf")


def build_resume():
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=30,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_style.fontName = "Helvetica-Bold"
    title_style.fontSize = 24
    title_style.textColor = colors.HexColor("#0f172a")
    title_style.spaceAfter = 12

    heading_style = styles["Heading2"]
    heading_style.fontName = "Helvetica-Bold"
    heading_style.fontSize = 14
    heading_style.textColor = colors.HexColor("#1d4ed8")
    heading_style.spaceBefore = 12
    heading_style.spaceAfter = 8

    body_style = styles["BodyText"]
    body_style.fontName = "Helvetica"
    body_style.fontSize = 10
    body_style.leading = 14
    body_style.textColor = colors.HexColor("#334155")

    story = []
    story.append(Paragraph("Lithesh B", title_style))
    story.append(Paragraph("Computer Science Engineering Student", styles["Heading1"]))
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "Email: litheshb8@gmail.com &nbsp;&nbsp; Phone: +91 99621 03057 &nbsp;&nbsp; Chennai, Tamil Nadu",
            body_style,
        )
    )

    story.append(Paragraph("Profile", heading_style))
    story.append(
        Paragraph(
            "Motivated and detail-oriented Computer Science Engineering student with a strong interest in web development, problem solving, and building practical software solutions. I enjoy turning ideas into responsive interfaces and learning new tools through hands-on experience.",
            body_style,
        )
    )

    story.append(Paragraph("Education", heading_style))
    story.append(Paragraph("<b>B.E. Computer Science Engineering</b>", body_style))
    story.append(Paragraph("Easwari Engineering College, Chennai", body_style))
    story.append(Paragraph("<b>Higher Secondary Education</b>", body_style))
    story.append(Paragraph("Sacred Heart Matric Hr. Sec. School, Chennai", body_style))

    story.append(Paragraph("Skills", heading_style))
    skills = [
        "C", "C++", "Python", "JavaScript", "HTML", "CSS", "Git", "VS Code"
    ]
    story.append(ListFlowable([ListItem(Paragraph(skill, body_style), bulletType="bullet") for skill in skills], bulletType="bullet", leftIndent=18))

    story.append(Paragraph("Projects", heading_style))
    project_items = [
        "Car Rental Website — Responsive booking platform built using HTML, CSS, and JavaScript.",
        "E-Commerce Platform — Shopping portal with product listing and user flow.",
        "Employee Engagement Study — Research-based project analyzing engagement factors.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(item, body_style), bulletType="bullet") for item in project_items], bulletType="bullet", leftIndent=18))

    story.append(Paragraph("Strengths", heading_style))
    strengths = [
        "Problem solving",
        "Responsive UI development",
        "Learning new technologies quickly",
        "Team collaboration",
    ]
    story.append(ListFlowable([ListItem(Paragraph(item, body_style), bulletType="bullet") for item in strengths], bulletType="bullet", leftIndent=18))

    story.append(Paragraph("Contact", heading_style))
    story.append(Paragraph("LinkedIn: linkedin.com/in/lithesh", body_style))
    story.append(Paragraph("GitHub: github.com/lithesh", body_style))

    doc.build(story)
    print(f"Created: {out_path}")


if __name__ == "__main__":
    build_resume()
