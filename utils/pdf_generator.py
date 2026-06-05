from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER


def create_pdf(filename, content):

    pdf = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=30,
        textColor=colors.HexColor("#2563EB"),
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#6B7280"),
        alignment=TA_CENTER
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading1"],
        textColor=colors.white,
        backColor=colors.HexColor("#2563EB"),
        spaceBefore=10,
        spaceAfter=10,
        leftIndent=10
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        leading=18
    )

    story = []

    # =====================
    # COVER PAGE
    # =====================

    story.append(Spacer(1, 180))

    story.append(
        Paragraph(
            "AI SOFTWARE TEAM SIMULATOR",
            title_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Professional Software Design Report",
            subtitle_style
        )
    )

    story.append(Spacer(1, 40))

    story.append(
        Paragraph(
            "Generated using Multi-Agent AI System",
            subtitle_style
        )
    )

    story.append(PageBreak())

    # =====================
    # SECTION HEADINGS
    # =====================

    headings = [
        "PRODUCT MANAGER",
        "ARCHITECT",
        "DATABASE",
        "BACKEND",
        "QA",
        "DEVOPS",
        "RISK",
        "COST",
        "DOCUMENTATION"
    ]

    # =====================
    # CONTENT
    # =====================

    for line in content.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line in headings:

            story.append(
                Paragraph(
                    line,
                    heading_style
                )
            )

            story.append(
                Spacer(1, 10)
            )

        else:

            story.append(
                Paragraph(
                    line,
                    body_style
                )
            )

            story.append(
                Spacer(1, 5)
            )

    pdf.build(story)