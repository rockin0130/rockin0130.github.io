#!/usr/bin/env python3
"""Generate Ian_Lee_Portfolio.pdf (A4) from website-aligned content."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# Paths
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
IMAGES = ROOT / "images"
PDF_PATH = OUTPUT_DIR / "Ian_Lee_Portfolio.pdf"

# A4 with comfortable margins (Apple-like whitespace)
PAGE_W, PAGE_H = A4
MARGIN_X = 22 * mm
MARGIN_Y = 20 * mm

# Brand-ish colors
BLACK = colors.HexColor("#111111")
GRAY = colors.HexColor("#6b7280")
BLUE = colors.HexColor("#0066cc")
RULE = colors.HexColor("#d2d2d7")


def styles():
    base = getSampleStyleSheet()
    return {
        "cover_name": ParagraphStyle(
            "CoverName",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=32,
            leading=38,
            textColor=BLACK,
            alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "cover_tag": ParagraphStyle(
            "CoverTag",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=14,
            leading=20,
            textColor=BLACK,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "cover_sub": ParagraphStyle(
            "CoverSub",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=16,
            textColor=GRAY,
            alignment=TA_CENTER,
            spaceAfter=28,
        ),
        "cover_contact": ParagraphStyle(
            "CoverContact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=15,
            textColor=BLACK,
            alignment=TA_CENTER,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=BLACK,
            spaceBefore=0,
            spaceAfter=10,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            textColor=BLACK,
            spaceBefore=14,
            spaceAfter=6,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            textColor=GRAY,
            spaceAfter=8,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            textColor=BLACK,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        ),
        "tech": ParagraphStyle(
            "Tech",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=13,
            textColor=GRAY,
            spaceBefore=4,
            spaceAfter=12,
        ),
        "footer_note": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            textColor=GRAY,
            alignment=TA_CENTER,
        ),
    }


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def p(text: str, style) -> Paragraph:
    return Paragraph(esc(text), style)


def add_image(flow, filename: str, max_w_mm: float = 166):
    path = IMAGES / filename
    if not path.exists():
        flow.append(
            p(f"[Image not found: {filename} — add file to images/]", styles()["tech"])
        )
        return
    img = Image(str(path))
    w_max = max_w_mm * mm
    iw, ih = img.imageWidth, img.imageHeight
    scale = w_max / float(iw)
    img.drawWidth = w_max
    img.drawHeight = ih * scale
    flow.append(Spacer(1, 8))
    flow.append(img)
    flow.append(Spacer(1, 10))


def build_story():
    S = styles()
    story = []

    # ----- Page 1: Cover -----
    story.append(Spacer(1, 55 * mm))
    story.append(p("Ian Lee", S["cover_name"]))
    story.append(p("Make it work. Then make it better.", S["cover_tag"]))
    story.append(p("Building AI systems that actually ship.", S["cover_sub"]))
    story.append(Spacer(1, 20 * mm))
    story.append(
        p(
            "seokinlee0130@gmail.com<br/>"
            "linkedin.com/in/seokin-lee",
            S["cover_contact"],
        )
    )
    story.append(PageBreak())

    # ----- Page 2: About -----
    story.append(p("About", S["h1"]))
    story.append(
        p(
            "Product-minded engineer working across AI, data, and full-stack delivery. "
            "I focus on systems that ship: clear requirements, reliable pipelines, and "
            "interfaces people can trust. Based on the portfolio at rockin0130.github.io.",
            S["body"],
        )
    )
    story.append(p("Focus areas", S["h2"]))
    story.append(
        p(
            "• <b>AI &amp; ML</b> — intent understanding, embeddings, cloud AI APIs, "
            "explainable outputs.<br/>"
            "• <b>Data</b> — integration, cleansing, SQL analytics, dashboards (Tableau).<br/>"
            "• <b>Product engineering</b> — React web apps, mobile (Capacitor), "
            "calendar integrations, browser extensions.",
            S["body"],
        )
    )
    story.append(p("Tech stack highlights", S["h2"]))
    story.append(
        p(
            "Python, VBA, SQL, Tableau · React, Capacitor · Google Cloud AI · "
            "Google Calendar / Apple Calendar APIs · Embedding-based models · "
            "Browser extension development",
            S["body"],
        )
    )
    story.append(PageBreak())

    # ----- Project 1 (pages 3–4) -----
    story.append(p("Data-Driven Global Marketing Integration", S["h1"]))
    story.append(p("Hyundai Motor Group | Data Assistant", S["role"]))
    story.append(
        p("<b>Technologies:</b> Python, VBA, SQL, Tableau", S["tech"])
    )
    add_image(story, "hyundai.png")

    story.append(p("Overview", S["h2"]))
    story.append(
        p(
            "Innocean, a subsidiary of Hyundai Motor Group, leads global marketing for "
            "Hyundai Motor Company and its premium brand, Genesis.",
            S["body"],
        )
    )
    story.append(
        p(
            "Within the Global Strategy Planning team, Genesis faced challenges in "
            "consolidating marketing performance, as each international branch "
            "independently executed and reported campaigns. This lack of standardization "
            "limited visibility into global operations and hindered data-driven "
            "decision-making at headquarters.",
            S["body"],
        )
    )
    story.append(p("What I Did", S["h2"]))
    story.append(
        p(
            "I integrated and cleansed fragmented global marketing data using Python "
            "and VBA, transforming it into a unified, query-ready dataset of 1,000+ records.",
            S["body"],
        )
    )
    story.append(
        p(
            "Building on this foundation, I developed a global marketing tracker using "
            "SQL and Tableau, incorporating trend analysis and interactive dashboards "
            "(Gantt charts and tree maps) to standardize campaign reporting.",
            S["body"],
        )
    )
    story.append(
        p(
            "This system centralized marketing data across 10+ international branches, "
            "enabling consistent cross-regional comparison and operational visibility "
            "for the first time.",
            S["body"],
        )
    )
    story.append(p("Impact", S["h2"]))
    story.append(
        p(
            "The tracker enabled headquarters to benchmark past campaigns and plan "
            "future marketing initiatives in emerging markets such as Indonesia and "
            "India, contributing to a projected 12% increase in Genesis brand revenue.",
            S["body"],
        )
    )
    story.append(
        p(
            "Additionally, improved visibility into campaign timelines allowed HQ to "
            "identify inefficiencies in European marketing processes, leading to "
            "optimizations that contributed to a 15% increase in regional sales.",
            S["body"],
        )
    )
    story.append(PageBreak())

    # ----- Project 2 (pages 5–6) -----
    story.append(p("AI Scheduling Assistant", S["h1"]))
    story.append(p("WideCity | Lead Product Engineer", S["role"]))
    story.append(
        p(
            "<b>Technologies:</b> React, Capacitor, Google Calendar &amp; Apple Calendar "
            "APIs, Google Cloud AI",
            S["tech"],
        )
    )
    add_image(story, "calendar.png")

    story.append(p("Overview", S["h2"]))
    story.append(
        p(
            "Currently developing a startup product under the advisory of Edward Kim "
            "(CTO at Gusto), in collaboration with cross-functional team members across "
            "finance and law.",
            S["body"],
        )
    )
    story.append(
        p(
            "The product reimagines the traditional personal calendar into a shared, "
            "relationship-centric platform, enabling users to coordinate schedules with "
            "partners, friends, and family.",
            S["body"],
        )
    )
    story.append(
        p(
            "By integrating AI, the system allows flexible and personalized scheduling "
            "based on user preferences, context, and intent.",
            S["body"],
        )
    )
    story.append(p("What I Built", S["h2"]))
    story.append(
        p(
            "I generated the initial web application using Lovable AI, then refined and "
            "extended the system using React by resolving bugs and improving core "
            "functionality.",
            S["body"],
        )
    )
    story.append(
        p(
            "I converted the application into a cross-platform iOS app using Capacitor "
            "and implemented integrations with Google Calendar and Apple Calendar, "
            "enabling seamless synchronization of user schedules.",
            S["body"],
        )
    )
    story.append(
        p(
            "I also improved Apple Calendar-related UI/UX issues to ensure consistency "
            "across platforms.",
            S["body"],
        )
    )
    story.append(
        p(
            "On the AI side, I evaluated multiple approaches and integrated Google "
            "Cloud AI APIs. I designed the core logic enabling the system to interpret "
            "user intent and dynamically adapt scheduling decisions, creating a more "
            "personalized and interactive experience.",
            S["body"],
        )
    )
    story.append(p("Impact (Pre-Launch)", S["h2"]))
    story.append(
        p(
            "The product is currently in its final pre-launch stage, with a soft launch "
            "scheduled this month.",
            S["body"],
        )
    )
    story.append(
        p(
            "It is designed to reduce manual coordination overhead and improve "
            "scheduling efficiency through AI-driven decision support. By enabling "
            "multi-user coordination and personalized AI interactions, the system aims to "
            "streamline how users plan and manage their time across personal and social "
            "contexts.",
            S["body"],
        )
    )
    story.append(PageBreak())

    # ----- Project 3 (pages 7–8) -----
    story.append(p("Fashion Extension", S["h1"]))
    story.append(
        p(
            "Marshall Artificial Intelligence Association | Lead AI Engineer",
            S["role"],
        )
    )
    story.append(
        p(
            "<b>Technologies:</b> Embedding models, browser extension, end-to-end AI "
            "pipeline",
            S["tech"],
        )
    )
    add_image(story, "fashion.png")

    story.append(p("Overview", S["h2"]))
    story.append(
        p(
            "This project was developed as part of the Marshall Artificial Intelligence "
            "Association (MAIA) to address a common problem among users who lack "
            "confidence in their fashion decisions.",
            S["body"],
        )
    )
    story.append(
        p(
            "We built a browser extension that evaluates clothing items directly on "
            "e-commerce websites, providing a compatibility score and explanation based "
            "on a user's personal style profile.",
            S["body"],
        )
    )
    story.append(
        p(
            "The goal was to deliver real-time, personalized decision support embedded "
            "directly into the online shopping experience.",
            S["body"],
        )
    )
    story.append(p("What I Built", S["h2"]))
    story.append(
        p(
            "As Lead AI Engineer, I designed the core AI system and defined how it "
            "integrates with the overall product pipeline.",
            S["body"],
        )
    )
    story.append(
        p(
            "I evaluated multiple approaches including rule-based methods, image "
            "classification, and embedding-based models, and selected an "
            "embedding-based style similarity model as the most scalable solution for "
            "the MVP.",
            S["body"],
        )
    )
    story.append(
        p(
            "I designed the end-to-end AI pipeline, where the extension extracts product "
            "data such as images and metadata and combines it with user profile inputs. "
            "The system converts these inputs into embeddings and computes a "
            "compatibility score based on similarity.",
            S["body"],
        )
    )
    story.append(
        p(
            "I also defined key AI capabilities including visual attribute analysis, "
            "user preference modeling, compatibility scoring, and explanation generation, "
            "ensuring outputs were both interpretable and actionable.",
            S["body"],
        )
    )
    story.append(p("Impact", S["h2"]))
    story.append(
        p(
            "The MVP was successfully launched, and early testing demonstrated strong "
            "alignment between AI-generated scores and user preferences.",
            S["body"],
        )
    )
    story.append(
        p(
            "In a user survey, over 80% of participants (40 out of 50) reported that the "
            "recommendations closely matched their personal taste, validating the "
            "effectiveness of the system.",
            S["body"],
        )
    )
    story.append(
        p(
            "The project has been selected for a demo presentation to industry "
            "leaders, including the CEO of LinkedIn and the CFO of Google, highlighting "
            "both its technical depth and practical relevance.",
            S["body"],
        )
    )
    story.append(PageBreak())

    # ----- Page 9: Contact -----
    story.append(Spacer(1, 30 * mm))
    story.append(p("Contact &amp; Links", S["h1"]))
    story.append(Spacer(1, 8))
    rows = [
        ["Email", "seokinlee0130@gmail.com"],
        ["LinkedIn", "linkedin.com/in/seokin-lee"],
        ["GitHub", "github.com/rockin0130"],
        ["Portfolio", "rockin0130.github.io"],
    ]
    t = Table([[esc(a), esc(b)] for a, b in rows], colWidths=[32 * mm, 120 * mm])
    t.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("TEXTCOLOR", (0, 0), (0, -1), GRAY),
                ("TEXTCOLOR", (1, 0), (1, -1), BLACK),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, -1), (-1, -1), 0.5, RULE),
            ]
        )
    )
    story.append(t)
    story.append(Spacer(1, 24))
    story.append(
        p(
            "Generated from portfolio content · A4 · Ian Lee",
            S["footer_note"],
        )
    )

    return story


def on_page(canv, doc):
    canv.saveState()
    canv.setStrokeColor(RULE)
    canv.setLineWidth(0.5)
    # Footer rule
    y = MARGIN_Y * 0.5
    canv.line(MARGIN_X, y, PAGE_W - MARGIN_X, y)
    canv.setFont("Helvetica", 8)
    canv.setFillColor(GRAY)
    canv.drawRightString(
        PAGE_W - MARGIN_X,
        y - 12,
        f"Page {doc.page}",
    )
    canv.restoreState()


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    S = styles()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_Y,
        bottomMargin=MARGIN_Y + 8,
        title="Ian Lee — Portfolio",
        author="Ian Lee",
    )
    doc.build(build_story(), onFirstPage=on_page, onLaterPages=on_page)
    print(f"Wrote {PDF_PATH}")


if __name__ == "__main__":
    main()
