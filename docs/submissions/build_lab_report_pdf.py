#!/usr/bin/env python3
"""Build CPAD Assignments 1-10 lab report PDF — theory-first, matching the 1-6 report style."""

from __future__ import annotations

from pathlib import Path

from fpdf import FPDF
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SHOTS = ROOT / "docs" / "screenshots"
OUT = Path(__file__).resolve().parent / "Tanmay_Shinde_CPAD_Assignments_1-10_Lab_Report.pdf"

FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


class ReportPDF(FPDF):
    def header(self) -> None:
        if self.page_no() <= 2:
            return
        self.set_font("Body", "", 8)
        self.set_text_color(110, 110, 120)
        self.set_x(self.l_margin)
        self.cell(0, 5, "Tanmay Shinde  |  CPAD Assignments 1-10", align="L")
        self.ln(7)

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Body", "", 8)
        self.set_text_color(140, 140, 150)
        self.cell(0, 8, f"Tanmay Shinde  |  CPAD Assignments 1-10  |  Page {self.page_no()}", align="C")


def sx(pdf: ReportPDF) -> None:
    pdf.set_x(pdf.l_margin)


def h1(pdf: ReportPDF, text: str) -> None:
    sx(pdf)
    pdf.set_font("Body", "B", 14)
    pdf.set_text_color(20, 20, 28)
    pdf.multi_cell(0, 7, text)
    pdf.ln(2)


def h2(pdf: ReportPDF, text: str) -> None:
    pdf.ln(2)
    sx(pdf)
    pdf.set_font("Body", "B", 11)
    pdf.set_text_color(30, 30, 40)
    pdf.multi_cell(0, 6, text)
    pdf.ln(1)


def body(pdf: ReportPDF, text: str) -> None:
    sx(pdf)
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(35, 35, 42)
    pdf.multi_cell(0, 5, text)
    pdf.ln(1.5)


def bullet(pdf: ReportPDF, text: str) -> None:
    sx(pdf)
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(35, 35, 42)
    pdf.multi_cell(0, 5, f"- {text}")


def table(pdf: ReportPDF, headers: list[str], rows: list[list[str]], widths: list[float]) -> None:
    sx(pdf)
    pdf.set_font("Body", "B", 8)
    pdf.set_fill_color(230, 234, 245)
    pdf.set_text_color(20, 20, 28)
    for i, h in enumerate(headers):
        pdf.cell(widths[i], 6.5, h, border=1, fill=True)
    pdf.ln()
    pdf.set_font("Body", "", 8)
    pdf.set_text_color(40, 40, 48)
    for row in rows:
        # compute row height from wrapped lines
        lines_per = []
        for i, cell in enumerate(row):
            n = pdf.multi_cell(widths[i], 4.2, cell, dry_run=True, output="LINES")
            lines_per.append(max(1, len(n)))
        row_h = 4.2 * max(lines_per) + 2
        if pdf.get_y() + row_h > pdf.page_break_trigger:
            pdf.add_page()
            sx(pdf)
        x0, y0 = pdf.l_margin, pdf.get_y()
        for i, cell in enumerate(row):
            pdf.set_xy(x0 + sum(widths[:i]), y0)
            # draw border box then text
            pdf.rect(x0 + sum(widths[:i]), y0, widths[i], row_h)
            pdf.set_xy(x0 + sum(widths[:i]) + 1, y0 + 1)
            pdf.multi_cell(widths[i] - 2, 4.2, cell)
        pdf.set_y(y0 + row_h)
    pdf.ln(3)


def fig(pdf: ReportPDF, path: Path, caption: str, max_h: float = 105) -> None:
    if not path.exists():
        body(pdf, f"[Missing screenshot: {path.name}]")
        return
    with Image.open(path) as im:
        w, h = im.size
    page_w = pdf.epw
    disp_h = min(max_h, 115)
    disp_w = disp_h * (w / h)
    if disp_w > page_w * 0.5:
        disp_w = page_w * 0.5
        disp_h = disp_w * (h / w)
    # two-up friendly: allow side by side if space; else center single
    if pdf.get_y() + disp_h + 16 > pdf.page_break_trigger:
        pdf.add_page()
    x = pdf.l_margin + (page_w - disp_w) / 2
    pdf.image(str(path), x=x, w=disp_w, h=disp_h)
    pdf.set_y(pdf.get_y() + disp_h + 1)
    sx(pdf)
    pdf.set_font("Body", "", 8)
    pdf.set_text_color(90, 90, 100)
    pdf.multi_cell(0, 4, caption, align="C")
    pdf.ln(3)


def fig_pair(pdf: ReportPDF, p1: Path, c1: str, p2: Path, c2: str, max_h: float = 95) -> None:
    """Place two phone screenshots side by side."""
    page_w = pdf.epw
    gap = 6
    col = (page_w - gap) / 2

    def size_for(path: Path) -> tuple[float, float]:
        with Image.open(path) as im:
            w, h = im.size
        disp_h = max_h
        disp_w = disp_h * (w / h)
        if disp_w > col:
            disp_w = col
            disp_h = disp_w * (h / w)
        return disp_w, disp_h

    if not p1.exists() or not p2.exists():
        if p1.exists():
            fig(pdf, p1, c1, max_h)
        if p2.exists():
            fig(pdf, p2, c2, max_h)
        return

    w1, h1 = size_for(p1)
    w2, h2 = size_for(p2)
    h = max(h1, h2)
    if pdf.get_y() + h + 18 > pdf.page_break_trigger:
        pdf.add_page()
    y = pdf.get_y()
    x1 = pdf.l_margin + (col - w1) / 2
    x2 = pdf.l_margin + col + gap + (col - w2) / 2
    pdf.image(str(p1), x=x1, y=y, w=w1, h=h1)
    pdf.image(str(p2), x=x2, y=y, w=w2, h=h2)
    pdf.set_y(y + h + 1)
    pdf.set_font("Body", "", 7.5)
    pdf.set_text_color(90, 90, 100)
    sx(pdf)
    pdf.cell(col, 4, c1, align="C")
    pdf.cell(gap, 4, "")
    pdf.cell(col, 4, c2, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)


def build() -> Path:
    pdf = ReportPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_font("Body", "", FONT_REG)
    pdf.add_font("Body", "B", FONT_BOLD)

    # ===== COVER =====
    pdf.add_page()
    pdf.ln(18)
    sx(pdf)
    pdf.set_font("Body", "B", 12)
    pdf.set_text_color(20, 20, 28)
    for line in [
        "MIT ART, DESIGN AND TECHNOLOGY UNIVERSITY",
        "MIT School of Computing, Pune",
        "Department of Information Technology",
    ]:
        pdf.cell(0, 6, line, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)
    pdf.set_font("Body", "", 11)
    pdf.cell(0, 6, "Course: Cross Platform App Development (CPAD)", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_font("Body", "B", 16)
    pdf.set_text_color(61, 99, 232)
    pdf.cell(0, 8, "ASSIGNMENT REPORT", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Body", "B", 13)
    pdf.set_text_color(20, 20, 28)
    pdf.cell(0, 7, "Assignments 1 to 10", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Body", "", 11)
    pdf.cell(0, 6, "React Native Developer Portfolio (TanmayPortfolio)", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(12)
    table(
        pdf,
        ["Field", "Detail"],
        [
            ["Student Name", "Tanmay Shinde"],
            ["Enrollment Number", "ADT23SOCB1617"],
            ["Roll No. / Division", "12 / LY-SMAD"],
            ["Program", "B.Tech Information Technology"],
            ["Year", "Final Year (LY)"],
            ["Course Faculty", "Prof. Rohini Bhosale"],
            ["Academic Year", "2026-27"],
            ["Repository", "github.com/tanmays0/TanmayPortfolio"],
        ],
        [55, 115],
    )

    # ===== DECLARATION =====
    pdf.add_page()
    h1(pdf, "Declaration")
    body(
        pdf,
        "I, Tanmay Shinde, a student of B.Tech Information Technology (Enrollment No. ADT23SOCB1617, "
        "Roll No. 12, Division LY-SMAD), declare that this report and the accompanying project, TanmayPortfolio, "
        "are my own work, completed for Assignments 1 to 10 of the Cross Platform App Development (CPAD) course. "
        "The application was built with React Native (Community CLI) and executed on the Pixel Android emulator. "
        "All screenshots in this report were captured from that running application.",
    )
    pdf.ln(6)
    body(pdf, "Student Name: Tanmay Shinde")
    body(pdf, "Enrollment Number: ADT23SOCB1617")
    body(pdf, "Signature: ______________________")

    # ===== TOC =====
    pdf.add_page()
    h1(pdf, "Table of Contents")
    toc = [
        "1. Introduction and Project Overview",
        "2. Assignment 1: Setup and Hello World",
        "3. Assignment 2: Native vs Hybrid vs React Native",
        "4. Assignment 3: Components, Props and useState",
        "5. Assignment 4: Folder Structure and State",
        "6. Assignment 5: Student Profile App with Core Components",
        "7. Assignment 6: Flexbox, TextInput and onPress",
        "8. Assignment 7: Multi-Screen Stack Navigation",
        "9. Assignment 8: Dynamic Data Rendering with FlatList",
        "10. Assignment 9: Student Portfolio Application",
        "11. Assignment 10: Personal Portfolio Application",
        "12. Rubric Alignment",
        "13. Conclusion",
    ]
    for item in toc:
        bullet(pdf, item)

    # ===== 1 INTRO =====
    pdf.add_page()
    h1(pdf, "1. Introduction and Project Overview")
    body(
        pdf,
        "This report documents the work completed for Assignments 1 to 10 of the Cross Platform App Development "
        "(CPAD) course. Instead of building ten unrelated exercises, each assignment is implemented as part of one "
        "application: a React Native developer portfolio named TanmayPortfolio. The app contains Home, About, Skills, "
        "Projects, Experience, Certifications, Resume and Contact screens, and is used throughout this report to "
        "demonstrate every concept in the laboratory brief.",
    )
    h2(pdf, "1.1 Technology used")
    table(
        pdf,
        ["Item", "Detail"],
        [
            ["Framework", "React Native 0.87 with TypeScript"],
            ["Project creation", "React Native Community CLI (real android/ Gradle project, not Expo Go)"],
            ["Run target", "Pixel Android emulator"],
            ["Tooling", "Community CLI, Metro bundler and Android Studio"],
            ["Navigation", "React Navigation native Stack Navigator"],
        ],
        [40, 130],
    )
    body(
        pdf,
        "Note: Assignment 1 mentions Expo CLI. This project uses the Community CLI, which also creates a React Native "
        "project and runs on an emulator, and additionally provides a native android/ folder that opens in Android Studio.",
    )
    h2(pdf, "1.2 Assignment mapping")
    table(
        pdf,
        ["#", "Topic", "Where shown in the project"],
        [
            ["1", "Setup + Hello World", "Community CLI project, android/, first emulator run"],
            ["2", "Comparison report", "Native vs Hybrid vs RN; why RN was chosen"],
            ["3", "Components, Props, useState", "src/components, ProjectCard props, theme and form state"],
            ["4", "Folder structure + state", "Documented src/ tree, Switch and validation"],
            ["5", "Profile + core components", "View, Text, Image, TextInput, Button, Switch, ScrollView"],
            ["6", "Flexbox, TextInput, onPress", "Skill wrap, contact inputs, Submit, Alert"],
            ["7", "Stack Navigation", "AppNavigator; Home / About / Contact and more"],
            ["8", "JSON + FlatList", "projects.json; ProjectsScreen FlatList"],
            ["9", "Student Portfolio", "Full multi-screen portfolio product"],
            ["10", "Personal Portfolio", "Capstone covering CO1-CO5 in one app"],
        ],
        [12, 48, 110],
    )

    # ===== A1 =====
    pdf.add_page()
    h1(pdf, "2. Assignment 1: Setup and Hello World")
    body(pdf, "COs: CO1, CO2")
    h2(pdf, "2.1 Aim")
    body(
        pdf,
        "To show that the project is a real React Native Community CLI application that installs and runs on the Android emulator.",
    )
    h2(pdf, "2.2 Theory")
    body(
        pdf,
        "React Native is a framework for building mobile user interfaces with JavaScript or TypeScript and the React "
        "component model. A Community CLI project includes: (1) a JavaScript entry file (index.js) registered with the "
        "native host through AppRegistry; (2) Metro, the bundler that packages JavaScript and supports Fast Refresh; "
        "and (3) native project folders (android/ and ios/) that build platform APKs. The first academic milestone is a "
        "Hello World screen: a minimal UI that proves Metro, the native shell, and the emulator can install and display "
        "the app. Later screens replace Hello World without changing the project creation path.",
    )
    h2(pdf, "2.3 Steps performed")
    bullet(pdf, "Create the project with Community CLI. Root TanmayPortfolio; package.json lists react-native 0.87.1.")
    bullet(pdf, "Open android/ in Android Studio rather than using Expo Go.")
    bullet(pdf, "Run on the emulator with npm run android or Studio Run.")
    bullet(pdf, "The same CLI app that first displayed Hello World now hosts the complete portfolio.")
    h2(pdf, "2.4 Explanation")
    body(
        pdf,
        "The Community CLI was used so that the project contains a real android/ folder. Metro bundles the JavaScript, "
        "and Android Studio installs the APK on the emulator. The first milestone was Hello World; the same application "
        "now hosts the full portfolio.",
    )
    h2(pdf, "2.5 Output")
    fig(pdf, SHOTS / "assignment-1" / "01-home-hello-portfolio.png", "Figure 1: Portfolio Home screen running on the emulator")

    # ===== A2 =====
    pdf.add_page()
    h1(pdf, "3. Assignment 2: Native vs Hybrid vs React Native")
    body(pdf, "COs: CO1")
    h2(pdf, "3.1 Aim")
    body(
        pdf,
        "To compare three ways of building a mobile app for the same product goal, and to justify the choice made for "
        "this project. React Native sits in the middle: shared JavaScript with real native views.",
    )
    h2(pdf, "3.2 Theory")
    body(
        pdf,
        "Native development uses platform SDKs and languages (Kotlin/Java on Android; Swift on iOS). Each platform is a "
        "separate codebase with full access to device APIs. Performance and OS integration are strongest, but cost and "
        "maintenance rise when the same product must ship on two platforms.",
    )
    body(
        pdf,
        "Hybrid (WebView-based) development wraps a web application (HTML, CSS, JavaScript) inside a native WebView shell. "
        "Teams reuse web skills quickly. The UI is largely rendered by a browser engine, so complex gestures and native "
        "look-and-feel can be weaker than true native widgets.",
    )
    body(
        pdf,
        "React Native is a cross-platform framework where UI is written in JavaScript/TypeScript with React. React Native "
        "bridges to real native views (View, Text, and so on) on Android and iOS - not a full-page WebView. One shared "
        "codebase can target both platforms while still teaching React concepts required by this course.",
    )
    h2(pdf, "3.3 Comparison")
    table(
        pdf,
        ["Aspect", "Native", "Hybrid (WebView)", "React Native"],
        [
            ["Approach", "Kotlin/Swift + SDKs", "HTML/CSS/JS in WebView", "TypeScript + React to native views"],
            ["Strength", "Best performance & OS APIs", "Fastest website reuse", "One UI codebase, Metro Fast Refresh"],
            ["Trade-off", "Two codebases", "Weaker native feel", "Some Gradle / native tooling"],
            ["Best suited", "Banking, games, camera", "News, brochure apps", "Portfolio, product UIs, SaaS"],
        ],
        [28, 45, 48, 49],
    )
    h2(pdf, "3.4 Why React Native for this project")
    bullet(pdf, "Curriculum fit: functional components, Props, useState, core widgets and Flexbox match the assignment list.")
    bullet(pdf, "Studio workflow: Community CLI ships android/; opens in Android Studio; runs on emulator; shows Logcat.")
    bullet(pdf, "One codebase: full student profile without separate Kotlin and Swift apps.")
    bullet(pdf, "Industry signal: React Native is widely used for cross-platform product UI.")
    h2(pdf, "3.5 Conclusion of comparison")
    body(
        pdf,
        "Native wins on raw performance, Hybrid wins on web reuse, and React Native is the best fit for this course and this project.",
    )

    # ===== A3 =====
    pdf.add_page()
    h1(pdf, "4. Assignment 3: Components, Props and useState")
    body(pdf, "COs: CO2, CO3")
    h2(pdf, "4.1 Aim")
    body(
        pdf,
        "To build reusable components driven by Props, and to create a dynamic interface from state rather than from "
        "rewriting the UI. Data lives in src/data, and components stay simple and reusable.",
    )
    h2(pdf, "4.2 Theory")
    body(
        pdf,
        "A functional component is a JavaScript function that returns React Native elements. Components are the unit of "
        "reuse in the UI. Props (properties) are inputs passed from a parent to a child. The child should treat props as "
        "read-only. Passing title, description and tags into ProjectCard is an example: the same card component renders "
        "many projects with different data.",
    )
    body(
        pdf,
        "State holds values that change over time. The React Hook useState returns the current value and a setter. Calling "
        "the setter schedules a re-render so the UI updates. In this project: isDark in App.tsx drives light/dark theme; "
        "ContactForm keeps field values and errors in useState; ProjectCard keeps expanded/collapsed details in useState.",
    )
    h2(pdf, "4.3 Reusable components")
    table(
        pdf,
        ["Component", "Purpose"],
        [
            ["ProjectCard", "Receives title, description and tags via Props"],
            ["SkillChip", "Takes a label and accent; used in Skills and inside cards"],
            ["ThemeToggle", "Controlled Switch with no hard-coded theme"],
            ["ContactForm", "Stateful form composed of ContactInput"],
        ],
        [40, 130],
    )
    h2(pdf, "4.4 Data flow on the Projects screen")
    body(
        pdf,
        "ProjectsScreen reads project data from src/data and maps each item to a ProjectCard, passing title and tags as "
        "Props. The Details control is a Pressable, and the expanded state lives inside the card using useState.",
    )
    h2(pdf, "4.5 Output")
    fig(pdf, SHOTS / "assignment-3" / "01-projects-props-cards.png", "Figure 2: Projects screen built from ProjectCard components")
    fig_pair(
        pdf,
        SHOTS / "assignment-3" / "03-dark-mode.png",
        "Figure 3: Theme - isDark with Switch",
        SHOTS / "assignment-3" / "04-form-state-errors.png",
        "Figure 4: Form errors driven by useState",
    )

    # ===== A4 =====
    pdf.add_page()
    h1(pdf, "5. Assignment 4: Folder Structure and State")
    body(pdf, "COs: CO2, CO3")
    h2(pdf, "5.1 Aim")
    body(
        pdf,
        "To organise the project with a documented src/ tree in which every folder matches a concept from the course, "
        "and to show state updating the interface through the Switch and validation.",
    )
    h2(pdf, "5.2 Theory")
    body(
        pdf,
        "A well-structured React Native project separates concerns. Screens map to routes. Components are reusable UI "
        "pieces configured with Props. Data modules hold static content so components stay dumb and reusable. Theme holds "
        "colours and ThemeContext. Navigation wires screens into a navigator. Types document TypeScript interfaces. "
        "App.tsx is the root: it owns theme useState, wraps ThemeProvider and NavigationContainer, and mounts the stack. "
        "State-based updates prove the UI reacts to state without rewriting component trees by hand.",
    )
    h2(pdf, "5.3 Documented folder structure")
    table(
        pdf,
        ["Folder / File", "Responsibility"],
        [
            ["android/", "Native Gradle project, opened in Android Studio"],
            ["App.tsx", "Root useState(isDark), ThemeProvider and Navigation"],
            ["src/components/", "Reusable UI: ProjectCard, SkillChip, ThemeToggle, ..."],
            ["src/screens/", "One screen per portfolio section"],
            ["src/data/", "Static content; keeps components prop-driven"],
            ["src/theme/", "Colours, tokens and ThemeContext"],
            ["src/navigation/", "Stack navigator for all screens"],
            ["docs/", "Reports and screenshots for submission"],
        ],
        [40, 130],
    )
    h2(pdf, "5.4 State in the application")
    bullet(pdf, "Theme state: isDark lives in App.tsx; the Switch updates the whole theme when toggled.")
    bullet(pdf, "Validation state: the contact form updates error state on submission, changing borders and messages.")

    # ===== A5 =====
    pdf.add_page()
    h1(pdf, "6. Assignment 5: Student Profile App with Core Components")
    body(pdf, "COs: CO3")
    h2(pdf, "6.1 Aim")
    body(
        pdf,
        "To build a student profile style application that uses the eight core React Native components. The portfolio "
        "sections form the profile app: Home, About, Skills, Projects, Experience, Certifications, Resume and Contact.",
    )
    h2(pdf, "6.2 Theory")
    body(
        pdf,
        "React Native provides a small set of core components that map to native UI. View is a layout container. Text "
        "renders all visible text. Image displays photos. TextInput accepts typing. Button triggers actions. Switch "
        "toggles a boolean. ScrollView makes content scrollable. StyleSheet groups style objects for readable render code. "
        "Layout among Views uses Flexbox (Assignment 6).",
    )
    h2(pdf, "6.3 Core components used")
    table(
        pdf,
        ["Component", "Where it is used"],
        [
            ["View", "Almost every layout"],
            ["Text", "Titles, bio and errors"],
            ["Image", "ProfileCard and profile.jpg"],
            ["TextInput", "ContactInput fields"],
            ["Button", "ContactForm submit"],
            ["Switch", "ThemeToggle"],
            ["ScrollView", "ScreenContainer"],
            ["StyleSheet", "Every styled file"],
        ],
        [40, 130],
    )
    h2(pdf, "6.4 Profile screens")
    body(
        pdf,
        "Each section of the portfolio is a profile screen. Skills uses SkillChip inside a ScrollView. Experience shows "
        "AdMax and CodSoft on a timeline rail. About uses profile-style cards. Contact uses TextInput and Button.",
    )
    h2(pdf, "6.5 Output")
    fig_pair(
        pdf,
        SHOTS / "assignment-5" / "02-skills-scroll.png",
        "Figure 5: Skills - SkillChip + ScrollView",
        SHOTS / "assignment-5" / "03-experience.png",
        "Figure 6: Experience - AdMax and CodSoft rail",
    )
    fig_pair(
        pdf,
        SHOTS / "assignment-5" / "04-more-menu.png",
        "Figure 7: About - profile-style cards",
        SHOTS / "assignment-5" / "05-contact-form.png",
        "Figure 8: Contact - TextInput + Button",
    )
    fig(pdf, SHOTS / "assignment-5" / "06-home-dark-switch.png", "Figure 9: Switch - dark mode")

    # ===== A6 =====
    pdf.add_page()
    h1(pdf, "7. Assignment 6: Flexbox, TextInput and onPress")
    body(pdf, "COs: CO3, CO4")
    h2(pdf, "7.1 Aim")
    body(
        pdf,
        "To design responsive layouts with Flexbox, accept user input through controlled TextInputs, handle onPress "
        "events, and display Alert messages based on user actions.",
    )
    h2(pdf, "7.2 Theory - Flexbox")
    body(
        pdf,
        "Flexbox is the primary layout system in React Native. Important properties include flexDirection (row or column; "
        "default is column on RN), flexWrap (allow items to wrap), justifyContent (main-axis alignment), alignItems "
        "(cross-axis alignment), and flex (how much a child should grow). In this project, Explore CTAs and skill chips "
        "use wrapping rows so content reflows on smaller widths. Experience uses a horizontal row: timeline rail on the "
        "left, card content on the right.",
    )
    h2(pdf, "7.3 Theory - TextInput and events")
    body(
        pdf,
        "A controlled TextInput always displays a value from state (value={name}) and updates that state in onChangeText. "
        "This keeps the UI and data in sync and makes validation straightforward. onPress is the press handler for Button "
        "and Pressable. Pressing Submit runs handleSubmit, which validates fields. Empty submit updates error state "
        "(red borders and messages). Valid submit shows an Alert confirmation - the academic feedback required by the brief. "
        "Pressable is the modern replacement for older TouchableOpacity-style APIs; it still demonstrates touchable event "
        "handling with onPress, onPressIn and onPressOut.",
    )
    h2(pdf, "7.4 Flexbox layouts in the app")
    table(
        pdf,
        ["Layout", "Implementation"],
        [
            ["Home CTA wrap", "Explore buttons use flexWrap so CTAs reflow"],
            ["SkillCategory chips", "SkillChip row with flexWrap"],
            ["Experience row + rail", "Horizontal row: rail left, card right"],
            ["Project card actions", "Details and GitHub in a Flexbox row"],
        ],
        [50, 120],
    )
    h2(pdf, "7.5 Output")
    fig(pdf, SHOTS / "assignment-6" / "02-skills-flexbox.png", "Figure 10: Skills screen - chips wrapping")
    fig_pair(
        pdf,
        SHOTS / "assignment-6" / "03-contact-textinput.png",
        "Figure 11: Empty form - TextInput fields",
        SHOTS / "assignment-6" / "04-contact-validation.png",
        "Figure 12: Submit pressed - onPress errors",
    )

    # ===== A7 =====
    pdf.add_page()
    h1(pdf, "8. Assignment 7: Multi-Screen Stack Navigation")
    body(pdf, "COs: CO4")
    h2(pdf, "8.1 Aim")
    body(
        pdf,
        "To create Home, About and Contact screens, implement Stack Navigation, and navigate between screens using buttons.",
    )
    h2(pdf, "8.2 Theory")
    body(
        pdf,
        "Navigation lets an app show one screen at a time while keeping a history of previous screens. A stack navigator "
        "models screens as a stack of cards. The initial route (Home) is the first card. Calling navigation.navigate('About') "
        "pushes About onto the stack (or focuses it if already present). Returning to a previous screen pops or navigates "
        "to that route name. Transitions (for example slide from the right) communicate that a new screen was pushed.",
    )
    body(
        pdf,
        "React Navigation provides createNativeStackNavigator, which uses native platform navigation containers for smooth "
        "transitions. Each screen is registered with Stack.Screen. Button presses are the usual trigger: a Pressable or "
        "Button calls navigation.navigate('Contact'). This links touchable events (Assignment 6) with multi-screen "
        "structure (Assignment 7).",
    )
    h2(pdf, "8.3 Implementation")
    table(
        pdf,
        ["Requirement", "Evidence"],
        [
            ["Home, About, Contact", "HomeScreen, AboutScreen, ContactScreen"],
            ["Stack Navigation", "src/navigation/AppNavigator.tsx - createNativeStackNavigator"],
            ["Navigate with buttons", "Home CTAs, floating dock and menu call navigation.navigate(...)"],
        ],
        [50, 120],
    )
    body(
        pdf,
        "Additional stack screens: Skills, Projects, Experience, Certifications, Resume. The native header is hidden "
        "(headerShown: false); the brand mark and floating dock act as navigation controls. Animation is slide_from_right.",
    )
    h2(pdf, "8.4 Explanation")
    body(
        pdf,
        "From Home, tapping View work, About, or Talk (Contact) pushes the corresponding stack screen. Tapping the brand "
        "mark navigates back to Home. The user experiences multi-screen navigation without leaving the single React Native process.",
    )
    h2(pdf, "8.5 Output")
    fig(pdf, SHOTS / "assignment-3" / "03-dark-mode.png", "Figure 13: Home - stack root")
    fig_pair(
        pdf,
        SHOTS / "assignment-5" / "04-more-menu.png",
        "Figure 14: About destination",
        SHOTS / "assignment-6" / "03-contact-textinput.png",
        "Figure 15: Contact destination",
    )

    # ===== A8 =====
    pdf.add_page()
    h1(pdf, "9. Assignment 8: Dynamic Data Rendering with FlatList")
    body(pdf, "COs: CO5")
    h2(pdf, "9.1 Aim")
    body(
        pdf,
        "To fetch data from a local JSON file (or public API), display it with FlatList, and allow efficient scrolling.",
    )
    h2(pdf, "9.2 Theory")
    body(
        pdf,
        "Static arrays hard-coded inside a screen become hard to maintain. Storing projects in a local JSON file separates "
        "content from presentation. A loader function (fetchProjects) can read that JSON asynchronously - simulating the "
        "same pattern used for network APIs.",
    )
    body(
        pdf,
        "FlatList is React Native's efficient list component. Unlike mapping every item inside a ScrollView (which mounts "
        "all children at once), FlatList virtualises the list: only rows near the viewport are rendered. Important props "
        "include data (the array), renderItem (how each item becomes a component), keyExtractor (stable unique keys), and "
        "tuning props such as initialNumToRender, windowSize and removeClippedSubviews. Loading and error states improve "
        "UX while data is fetched or if loading fails.",
    )
    h2(pdf, "9.3 Implementation")
    table(
        pdf,
        ["Requirement", "Evidence"],
        [
            ["Local JSON", "src/data/projects.json via fetchProjects() in projectCatalog.ts"],
            ["FlatList", "ProjectsScreen.tsx"],
            ["Efficient scrolling", "FlatList tuning props on the projects list"],
        ],
        [45, 125],
    )
    h2(pdf, "9.4 Explanation")
    body(
        pdf,
        "Opening Projects triggers a refresh of the catalog. While loading, an activity indicator may appear. The list "
        "then scrolls smoothly; expanding a card still uses Props and local useState from Assignment 3.",
    )
    h2(pdf, "9.5 Output")
    fig_pair(
        pdf,
        SHOTS / "assignment-3" / "01-projects-props-cards.png",
        "Figure 16: Projects FlatList",
        SHOTS / "assignment-6" / "01-projects-layout.png",
        "Figure 17: Projects layout / scroll",
    )

    # ===== A9 =====
    pdf.add_page()
    h1(pdf, "10. Assignment 9: Student Portfolio Application")
    body(pdf, "COs: CO3, CO4, CO5")
    h2(pdf, "10.1 Aim / Objective")
    body(
        pdf,
        "To develop a responsive and interactive Student Portfolio Application using React Native that presents identity, "
        "education, skills, projects and contact information with stack navigation and Flexbox / StyleSheet layout.",
    )
    h2(pdf, "10.2 Theory")
    body(
        pdf,
        "A student portfolio app is a product composition of earlier labs. Identity screens use core components (Image, "
        "Text, View) for name, photo and introduction. About presents education and career objectives as structured "
        "content cards. Skills communicate technical and soft abilities; chips with Flexbox wrap keep the layout "
        "responsive. Projects use FlatList over JSON data so the list scales. Contact uses controlled TextInputs and "
        "Button onPress for interaction. Stack Navigation connects every screen into one flow. Responsive UI means "
        "layouts adapt with Flexbox and StyleSheet rather than fixed absolute positions that break on different emulator sizes.",
    )
    h2(pdf, "10.3 Requirements checklist")
    table(
        pdf,
        ["Requirement", "Evidence in TanmayPortfolio"],
        [
            ["Home - name, photo, intro", "HomeScreen + profile.jpg"],
            ["About - education + career", "AboutScreen"],
            ["Skills - technical + soft", "SkillsScreen + Soft Skills in skills.ts"],
            ["Projects - FlatList", "ProjectsScreen + projects.json"],
            ["Contact - TextInput + Button", "ContactForm"],
            ["Stack Navigator", "AppNavigator"],
            ["StyleSheet + Flexbox", "All screens"],
        ],
        [55, 115],
    )
    h2(pdf, "10.4 Output")
    fig_pair(
        pdf,
        SHOTS / "assignment-5" / "01-home-profile.png",
        "Figure 18: Home - student identity",
        SHOTS / "assignment-5" / "02-skills-scroll.png",
        "Figure 19: Skills - technical and soft",
    )
    fig_pair(
        pdf,
        SHOTS / "assignment-3" / "01-projects-props-cards.png",
        "Figure 20: Projects - FlatList",
        SHOTS / "assignment-5" / "05-contact-form.png",
        "Figure 21: Contact - form",
    )

    # ===== A10 =====
    pdf.add_page()
    h1(pdf, "11. Assignment 10: Personal Portfolio Application")
    body(pdf, "COs: CO1, CO2, CO3, CO4, CO5")
    h2(pdf, "11.1 Aim / Objective")
    body(
        pdf,
        "To develop a responsive and interactive Personal Portfolio Application using React Native. Assignment 10 is the "
        "capstone: the same product surface as Assignment 9, with explicit coverage of every course outcome from setup "
        "through dynamic lists.",
    )
    h2(pdf, "11.2 Theory")
    body(
        pdf,
        "A personal portfolio on mobile must balance content, structure and interaction. Content answers who the student "
        "is, what they know, what they built, and how to reach them. Structure uses modular folders, reusable components, "
        "typed data, and a navigator that keeps screens organised. Interaction includes theme switching, form validation, "
        "press handlers, and list scrolling that feel native. React Native is appropriate because one TypeScript codebase "
        "demonstrates both React concepts (Props, state, components) and mobile concepts (native views, Flexbox, "
        "navigation, FlatList) without maintaining separate native apps.",
    )
    h2(pdf, "11.3 Capstone mapping to earlier assignments")
    table(
        pdf,
        ["Earlier concept", "Visible in the personal portfolio"],
        [
            ["A1 Setup + emulator", "App runs on Pixel via Community CLI"],
            ["A2 Why RN", "Documented comparison and project choice"],
            ["A3-A4 Props, state, structure", "Cards, theme, form, src/ layout"],
            ["A5 Core components", "View, Text, Image, TextInput, Button, Switch, ScrollView"],
            ["A6 Flexbox + onPress + Alert", "Layouts and Contact submit"],
            ["A7 Stack Navigation", "Multi-screen navigator"],
            ["A8 JSON + FlatList", "Projects list"],
            ["A9 Portfolio UI", "Home through Contact (+ Experience, Certs, Resume)"],
        ],
        [55, 115],
    )
    h2(pdf, "11.4 Output")
    fig(pdf, SHOTS / "assignment-3" / "03-dark-mode.png", "Figure 22: Personal portfolio Home")
    fig_pair(
        pdf,
        SHOTS / "assignment-5" / "03-experience.png",
        "Figure 23: Experience section",
        SHOTS / "assignment-6" / "04-contact-validation.png",
        "Figure 24: Contact interaction",
    )

    # ===== RUBRIC =====
    pdf.add_page()
    h1(pdf, "12. Rubric Alignment")
    body(pdf, "The table below states where each evaluation criterion is demonstrated in the project.")
    table(
        pdf,
        ["Criterion", "Evidence in the project"],
        [
            [
                "Functionality and Output",
                "All sections run. Theme Switch works. Form validation works. External links open. App installs on emulator. Stack navigation and FlatList work.",
            ],
            [
                "Code Structure and Syntax",
                "Modular src/ layout, TypeScript, consistent component names, and no single-file app.",
            ],
            [
                "Concept Implementation",
                "Props, useState, eight core components, Flexbox, TextInput, onPress, Stack Navigation and FlatList are all visible.",
            ],
            [
                "Readability and Documentation",
                "File comments, docs/ reports, README and screenshot folders for assignments.",
            ],
        ],
        [45, 125],
    )

    # ===== CONCLUSION =====
    h1(pdf, "13. Conclusion")
    body(
        pdf,
        "Assignments 1 to 10 were completed as a single React Native application built with the Community CLI and run on "
        "the Android emulator. The project covers setup and Hello World; a comparison of Native, Hybrid and React Native; "
        "reusable components with Props and state with useState; a documented folder structure; the core React Native "
        "components; Flexbox layouts and controlled inputs with onPress / Alert; multi-screen Stack Navigation; dynamic "
        "JSON data with FlatList; and a complete student / personal portfolio product.",
    )
    body(
        pdf,
        "Two ideas summarise the design: data lives in src/data while components stay reusable through Props, and isDark "
        "in App.tsx updates the whole theme when the Switch is toggled. Stack navigation and FlatList complete the "
        "multi-screen, data-driven portfolio required for Assignments 7-10.",
    )
    pdf.ln(4)
    body(pdf, "Submitted by: Tanmay Shinde")
    body(pdf, "Enrollment Number: ADT23SOCB1617")
    pdf.ln(4)
    h2(pdf, "References")
    bullet(pdf, "React Native Documentation - https://reactnative.dev")
    bullet(pdf, "React Navigation - https://reactnavigation.org")
    bullet(pdf, "Android Developers - https://developer.android.com")
    bullet(pdf, "Project repository - https://github.com/tanmays0/TanmayPortfolio")

    pdf.output(str(OUT))
    return OUT


if __name__ == "__main__":
    print(build())
