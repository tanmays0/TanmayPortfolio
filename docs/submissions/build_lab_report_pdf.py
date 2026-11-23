#!/usr/bin/env python3
"""Build CPAD Assignments 1–10 lab report PDF with embedded screenshots."""

from __future__ import annotations

from pathlib import Path

from fpdf import FPDF
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SHOTS = ROOT / "docs" / "screenshots"
OUT = Path(__file__).resolve().parent / "Tanmay_Shinde_CPAD_Assignments_1-10_Lab_Report.pdf"

# Prefer DejaVu if present; otherwise Helvetica (ASCII-safe text).
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


class ReportPDF(FPDF):
    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_font("Body", "", 8)
        self.set_text_color(110, 110, 120)
        self.cell(0, 6, "Tanmay Shinde  |  CPAD Lab Report  |  Assignments 1-10", align="L")
        self.ln(8)

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Body", "", 8)
        self.set_text_color(140, 140, 150)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")


def add_title(pdf: ReportPDF, text: str) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "B", 18)
    pdf.set_text_color(20, 20, 28)
    pdf.multi_cell(0, 8, text)
    pdf.ln(2)


def add_h2(pdf: ReportPDF, text: str) -> None:
    pdf.ln(3)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "B", 13)
    pdf.set_text_color(61, 99, 232)
    pdf.multi_cell(0, 7, text)
    pdf.ln(1)


def add_h3(pdf: ReportPDF, text: str) -> None:
    pdf.ln(2)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "B", 11)
    pdf.set_text_color(30, 30, 40)
    pdf.multi_cell(0, 6, text)
    pdf.ln(1)


def add_body(pdf: ReportPDF, text: str) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(40, 40, 48)
    pdf.multi_cell(0, 5, text)
    pdf.ln(1)


def add_bullet(pdf: ReportPDF, text: str) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(40, 40, 48)
    pdf.multi_cell(0, 5, f"- {text}")


def add_table(pdf: ReportPDF, headers: list[str], rows: list[list[str]], col_w: list[float] | None = None) -> None:
    if col_w is None:
        usable = pdf.epw
        col_w = [usable / len(headers)] * len(headers)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "B", 9)
    pdf.set_fill_color(232, 236, 248)
    pdf.set_text_color(20, 20, 28)
    for i, h in enumerate(headers):
        pdf.cell(col_w[i], 7, h[:40], border=1, fill=True)
    pdf.ln()
    pdf.set_font("Body", "", 8)
    pdf.set_text_color(40, 40, 48)
    for row in rows:
        # Single-line cells for reliability
        if pdf.get_y() + 8 > pdf.page_break_trigger:
            pdf.add_page()
        pdf.set_x(pdf.l_margin)
        for i, cell in enumerate(row):
            text = cell if len(cell) < 55 else cell[:52] + "..."
            pdf.cell(col_w[i], 7, text, border=1)
        pdf.ln()
    pdf.ln(2)


def add_image(pdf: ReportPDF, path: Path, caption: str, max_h: float = 120) -> None:
    if not path.exists():
        add_body(pdf, f"[Missing screenshot: {path.name}]")
        return
    pdf.ln(2)
    page_w = pdf.epw
    with Image.open(path) as im:
        w, h = im.size
    # Phone screenshots are tall; constrain height
    disp_h = min(max_h, 140)
    disp_w = disp_h * (w / h)
    if disp_w > page_w * 0.55:
        disp_w = page_w * 0.55
        disp_h = disp_w * (h / w)
    if pdf.get_y() + disp_h + 14 > pdf.page_break_trigger:
        pdf.add_page()
    x = pdf.l_margin + (page_w - disp_w) / 2
    pdf.image(str(path), x=x, w=disp_w, h=disp_h)
    pdf.ln(disp_h + 2)
    pdf.set_font("Body", "", 8)
    pdf.set_text_color(100, 100, 110)
    pdf.multi_cell(0, 4, caption, align="C")
    pdf.ln(3)


def build() -> Path:
    pdf = ReportPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_font("Body", "", FONT_REG)
    pdf.add_font("Body", "B", FONT_BOLD)

    # Cover
    pdf.add_page()
    pdf.ln(30)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Body", "B", 22)
    pdf.set_text_color(20, 20, 28)
    pdf.cell(0, 10, "CPAD Laboratory Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Body", "B", 16)
    pdf.set_text_color(61, 99, 232)
    pdf.cell(0, 8, "Assignments 1-10", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)
    pdf.set_font("Body", "", 12)
    pdf.set_text_color(50, 50, 60)
    for line in [
        "Student: Tanmay Shinde",
        "B.Tech Information Technology | MIT ADT University, Pune",
        "Project: TanmayPortfolio (React Native Community CLI)",
        "Runtime: Android emulator via Metro + Android Studio",
        "GitHub: https://github.com/tanmays0/TanmayPortfolio",
    ]:
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 7, line, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(12)
    pdf.set_x(pdf.l_margin)
    add_body(
        pdf,
        "This report documents theory and implementation evidence for Laboratory Assignments 1 through 10. "
        "A single React Native portfolio application satisfies all tasks. Screenshots are captured from the running Android build.",
    )
    pdf.set_x(pdf.l_margin)
    add_body(
        pdf,
        "Note: Assignment 1 mentions Expo CLI. This project uses the React Native Community CLI, which also creates a React Native "
        "project, runs on an emulator, and provides a native android/ folder for Android Studio.",
    )

    # Status table
    pdf.add_page()
    add_title(pdf, "Status Overview")
    add_table(
        pdf,
        ["#", "Title", "COs", "Status"],
        [
            ["1", "RN setup + Hello World", "CO1, CO2", "Done"],
            ["2", "Native / Hybrid / RN comparison", "CO1", "Done"],
            ["3", "Components, Props, useState", "CO2, CO3", "Done"],
            ["4", "Folder structure + reusable components", "CO2, CO3", "Done"],
            ["5", "Student Profile core components", "CO3", "Done"],
            ["6", "Flexbox, TextInput, onPress, Alert", "CO3, CO4", "Done"],
            ["7", "Multi-screen Stack Navigation", "CO4", "Done"],
            ["8", "Local JSON + FlatList", "CO5", "Done"],
            ["9", "Student Portfolio Application", "CO3-CO5", "Done"],
            ["10", "Personal Portfolio Application", "CO1-CO5", "Done"],
        ],
        [12, 95, 35, 28],
    )

    # A1
    add_h2(pdf, "Assignment 1 - Setup and Hello World")
    add_h3(pdf, "Theory")
    add_body(
        pdf,
        "React Native builds mobile UIs with JavaScript/TypeScript and React. The Community CLI scaffolds Metro bundling, "
        "a JS entry registered with the native host, and android/ios native projects. A Hello World screen proves the "
        "toolchain: Metro, native install, and emulator.",
    )
    add_h3(pdf, "Tasks completed")
    add_bullet(pdf, "Created TanmayPortfolio with package.json declaring react-native 0.87.1")
    add_bullet(pdf, "Opened android/ in Android Studio; ran on Pixel emulator via npm run android")
    add_bullet(pdf, "First milestone: Hello World; same app now hosts the full portfolio")
    add_image(pdf, SHOTS / "assignment-1" / "01-home-hello-portfolio.png", "Figure A1. First running build on emulator")

    # A2
    pdf.add_page()
    add_h2(pdf, "Assignment 2 - Comparative Study")
    add_h3(pdf, "Theory")
    add_body(
        pdf,
        "Native apps use platform SDKs (Kotlin/Swift) for maximum performance and OS depth, at the cost of two codebases. "
        "Hybrid WebView apps wrap HTML/CSS/JS for fast reuse but often feel less native. React Native shares one React "
        "codebase that renders real native views via a bridge.",
    )
    add_table(
        pdf,
        ["Feature", "Native", "Hybrid", "React Native"],
        [
            ["Languages", "Kotlin/Swift", "HTML/CSS/JS", "TS + React"],
            ["UI", "Native widgets", "WebView", "Native via bridge"],
            ["Sharing", "Low", "High", "High"],
            ["Best for", "Games, banking", "Content apps", "Product UI, portfolios"],
        ],
        [35, 40, 40, 45],
    )
    add_body(
        pdf,
        "Why RN here: curriculum maps to components, Props, useState, core widgets, Flexbox, and navigation; Community CLI "
        "gives a Studio-friendly android/ workflow. Full write-up: docs/assignment-2-comparison-report.md",
    )

    # A3
    add_h2(pdf, "Assignment 3 - Components, Props, useState")
    add_h3(pdf, "Theory")
    add_body(
        pdf,
        "Functional components return UI. Props pass parent-to-child data. useState stores changing values and triggers re-render.",
    )
    add_bullet(pdf, "Reusable UI in src/components (ProjectCard, SkillChip, ThemeToggle, ContactForm)")
    add_bullet(pdf, "Props: ProjectsScreen maps catalog data into ProjectCard")
    add_bullet(pdf, "State: isDark theme in App.tsx; ContactForm validation; ProjectCard expand")
    add_image(pdf, SHOTS / "assignment-3" / "01-projects-props-cards.png", "Figure A3.1 Projects cards via Props")
    add_image(pdf, SHOTS / "assignment-3" / "03-dark-mode.png", "Figure A3.2 Dark mode via useState + Switch")
    add_image(pdf, SHOTS / "assignment-3" / "04-form-state-errors.png", "Figure A3.3 Form validation state")

    # A4
    pdf.add_page()
    add_h2(pdf, "Assignment 4 - Project Structure")
    add_body(
        pdf,
        "Maintainable RN apps separate screens, reusable components, data, theme, navigation, and types. App.tsx holds "
        "theme useState and wraps ThemeProvider + NavigationContainer. Full tree: docs/assignment-4-folder-structure.md",
    )
    add_bullet(pdf, "src/components - Props-driven UI")
    add_bullet(pdf, "src/screens - one screen per portfolio section")
    add_bullet(pdf, "src/data - profile, skills, projects.json")
    add_bullet(pdf, "src/navigation - Stack navigator")
    add_bullet(pdf, "State updates: theme Switch + contact validation errors")

    # A5
    add_h2(pdf, "Assignment 5 - Student Profile (Core Components)")
    add_body(
        pdf,
        "Core widgets: View, Text, Image, TextInput, Button, Switch, ScrollView, StyleSheet. Portfolio sections form a "
        "profile-style app (Home, About, Skills, Projects, Experience, Certs, Resume, Contact).",
    )
    add_table(
        pdf,
        ["Component", "Where used"],
        [
            ["View / Text", "Every screen"],
            ["Image", "Profile photo"],
            ["TextInput", "Contact form"],
            ["Button", "Contact submit"],
            ["Switch", "ThemeToggle"],
            ["ScrollView", "ScreenContainer"],
            ["StyleSheet", "All styled files"],
        ],
        [45, 125],
    )
    add_image(pdf, SHOTS / "assignment-5" / "01-home-profile.png", "Figure A5.1 Home / profile")
    add_image(pdf, SHOTS / "assignment-5" / "02-skills-scroll.png", "Figure A5.2 Skills")
    add_image(pdf, SHOTS / "assignment-5" / "03-experience.png", "Figure A5.3 Experience")
    add_image(pdf, SHOTS / "assignment-5" / "05-contact-form.png", "Figure A5.4 Contact (TextInput + Button)")
    add_image(pdf, SHOTS / "assignment-5" / "06-home-dark-switch.png", "Figure A5.5 Switch (dark mode)")

    # A6
    pdf.add_page()
    add_h2(pdf, "Assignment 6 - Flexbox, TextInput, onPress, Alert")
    add_body(
        pdf,
        "Flexbox lays out adaptive rows/columns. Controlled TextInputs bind value/onChangeText to useState. "
        "Button/Pressable onPress runs handlers; Alert shows feedback after valid submit.",
    )
    add_bullet(pdf, "Flexbox: Home CTA wrap, skill chips flexWrap, Experience rail")
    add_bullet(pdf, "ContactForm controlled inputs + Button onPress={handleSubmit}")
    add_bullet(pdf, "Empty submit shows errors; valid submit shows Alert")
    add_image(pdf, SHOTS / "assignment-6" / "02-skills-flexbox.png", "Figure A6.1 Skills Flexbox chips")
    add_image(pdf, SHOTS / "assignment-6" / "03-contact-textinput.png", "Figure A6.2 Contact TextInput")
    add_image(pdf, SHOTS / "assignment-6" / "04-contact-validation.png", "Figure A6.3 Validation onPress")
    add_image(pdf, SHOTS / "assignment-6" / "05-contact-success.png", "Figure A6.4 Success / Alert path")

    # A7
    pdf.add_page()
    add_h2(pdf, "Assignment 7 - Multi-Screen Stack Navigation")
    add_body(
        pdf,
        "Stack navigation pushes screens with navigation.navigate('Route'). AppNavigator uses createNativeStackNavigator "
        "with Home as initial route plus About, Skills, Projects, Contact, Experience, Certifications, Resume. "
        "Native header is hidden; brand mark and floating dock navigate between stack routes.",
    )
    add_bullet(pdf, "Home / About / Contact screens implemented")
    add_bullet(pdf, "Buttons and dock call navigation.navigate(...)")
    add_bullet(pdf, "File: src/navigation/AppNavigator.tsx")
    add_image(pdf, SHOTS / "assignment-3" / "03-dark-mode.png", "Figure A7.1 Home (stack root)")
    add_image(pdf, SHOTS / "assignment-5" / "04-more-menu.png", "Figure A7.2 About destination")
    add_image(pdf, SHOTS / "assignment-6" / "03-contact-textinput.png", "Figure A7.3 Contact destination")

    # A8
    add_h2(pdf, "Assignment 8 - Dynamic Data + FlatList")
    add_body(
        pdf,
        "Projects load from src/data/projects.json via fetchProjects() in projectCatalog.ts. ProjectsScreen renders a "
        "FlatList with efficient scrolling props. Loading and error UI keep the screen usable during refresh.",
    )
    add_image(pdf, SHOTS / "assignment-3" / "01-projects-props-cards.png", "Figure A8.1 Projects FlatList")
    add_image(pdf, SHOTS / "assignment-6" / "01-projects-layout.png", "Figure A8.2 Projects scroll surface")

    # A9
    pdf.add_page()
    add_h2(pdf, "Assignment 9 - Student Portfolio Application")
    add_body(
        pdf,
        "Combines profile UI, skills, projects FlatList, contact form, and Stack Navigation into one student portfolio.",
    )
    add_table(
        pdf,
        ["Requirement", "Evidence"],
        [
            ["Home name/photo/intro", "HomeScreen + profile.jpg"],
            ["About education/career", "AboutScreen"],
            ["Skills technical + soft", "SkillsScreen + Soft Skills category"],
            ["Projects FlatList", "ProjectsScreen + projects.json"],
            ["Contact form", "ContactForm TextInput + Button"],
            ["Stack Navigator", "AppNavigator"],
            ["StyleSheet + Flexbox", "All screens"],
        ],
        [55, 115],
    )
    add_image(pdf, SHOTS / "assignment-5" / "01-home-profile.png", "Figure A9.1 Home")
    add_image(pdf, SHOTS / "assignment-5" / "02-skills-scroll.png", "Figure A9.2 Skills")
    add_image(pdf, SHOTS / "assignment-5" / "05-contact-form.png", "Figure A9.3 Contact")

    # A10
    add_h2(pdf, "Assignment 10 - Personal Portfolio Application")
    add_body(
        pdf,
        "Capstone personal portfolio covering CO1-CO5: setup, comparison rationale, components/state, structure, "
        "core widgets, Flexbox/events, stack navigation, FlatList, and full portfolio UI. Same running app as Assignments 1-9.",
    )
    add_image(pdf, SHOTS / "assignment-3" / "03-dark-mode.png", "Figure A10.1 Personal portfolio Home")
    add_image(pdf, SHOTS / "assignment-5" / "03-experience.png", "Figure A10.2 Experience")
    add_image(pdf, SHOTS / "assignment-6" / "04-contact-validation.png", "Figure A10.3 Contact interaction")

    # Rubric + viva
    pdf.add_page()
    add_h2(pdf, "Rubric Alignment (Excellent)")
    add_table(
        pdf,
        ["Criteria", "Evidence"],
        [
            ["Functionality & Output", "All sections; theme; validation; links; stack; FlatList"],
            ["Code Structure", "Modular src/; TypeScript; consistent naming"],
            ["Concept Implementation", "Props, useState, core RN, Flexbox, onPress, Stack, FlatList"],
            ["Readability & Docs", "Comments, docs/, README, this report"],
        ],
        [50, 120],
    )
    add_h2(pdf, "Suggested Viva Walkthrough (4-5 minutes)")
    for i, step in enumerate(
        [
            "Home - name, photo, intro; stack CTAs / dock",
            "About - education + career direction",
            "Skills - technical + soft chips (Flexbox wrap)",
            "Projects - FlatList scroll, expand Details",
            "Contact - empty Submit errors; valid Submit Alert",
            "Toggle dark mode (useState + Switch)",
            "Mention projects.json + fetchProjects (Assignment 8)",
            "Optional: android/ in Android Studio + Logcat",
        ],
        1,
    ):
        add_bullet(pdf, f"{i}. {step}")

    add_h2(pdf, "References")
    add_bullet(pdf, "React Native Docs - https://reactnative.dev")
    add_bullet(pdf, "React Navigation - https://reactnavigation.org")
    add_bullet(pdf, "Android Developers - https://developer.android.com")
    add_bullet(pdf, "Repository - https://github.com/tanmays0/TanmayPortfolio")
    pdf.ln(6)
    add_body(pdf, "End of report - Tanmay Shinde - CPAD Laboratory Assignments 1-10")

    pdf.output(str(OUT))
    return OUT


if __name__ == "__main__":
    path = build()
    print(path)
