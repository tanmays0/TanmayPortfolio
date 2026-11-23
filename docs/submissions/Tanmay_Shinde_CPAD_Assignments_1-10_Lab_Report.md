# CPAD Laboratory Report — Assignments 1–10

**Student:** Tanmay Shinde  
**Programme:** B.Tech (Information Technology) · MIT ADT University, Pune  
**Subject:** Cross-Platform Application Development (CPAD)  
**Project:** TanmayPortfolio — React Native Developer Portfolio  
**Repository:** https://github.com/tanmays0/TanmayPortfolio  
**Runtime:** Android emulator (Pixel) via React Native Community CLI + Android Studio  

---

## Declaration

This report documents how a single React Native portfolio application satisfies Laboratory Assignments **1 through 10**. Theory for each assignment is followed by implementation evidence and screenshots from the running app.

**Note on tooling:** The Assignment 1 brief mentions Expo CLI. This project was created with the **React Native Community CLI**, which also creates a React Native project, runs on an emulator, and additionally provides a native `android/` folder openable in Android Studio. All functional requirements of Assignment 1 are met.

---

## Status overview

| Assignment | Title | COs | Status |
| --- | --- | --- | --- |
| 1 | RN setup + Hello World on emulator | CO1, CO2 | Done |
| 2 | Native vs Hybrid vs React Native comparison | CO1 | Done |
| 3 | Functional components, Props, `useState` | CO2, CO3 | Done |
| 4 | Project structure + reusable components + state | CO2, CO3 | Done |
| 5 | Student Profile — core RN components | CO3 | Done |
| 6 | Flexbox, TextInput, Button `onPress`, Alert | CO3, CO4 | Done |
| 7 | Multi-screen Stack Navigation | CO4 | Done |
| 8 | Local JSON + FlatList | CO5 | Done |
| 9 | Student Portfolio Application | CO3, CO4, CO5 | Done |
| 10 | Personal Portfolio Application | CO1–CO5 | Done |

---

# Assignment 1 — Setup and Hello World

**COs:** CO1, CO2

## Theory

React Native lets you build mobile UIs with JavaScript/TypeScript and React. The Community CLI scaffolds a project with:

- A JavaScript entry (`index.js`) registered with the native host
- Metro bundler for JS packaging and Fast Refresh
- Native folders `android/` and `ios/` for platform builds

A first milestone is a “Hello World” screen that proves Metro, the native shell, and the emulator can install and run the app.

## Tasks completed

| Task | How it was done |
| --- | --- |
| Create RN project | `TanmayPortfolio` root; `package.json` declares `react-native` `0.87.1` |
| Run on emulator | `npm run android` / Android Studio Run on Pixel emulator |
| Basic first app | Early Hello World stage; app now hosts the full portfolio |

## Evidence / screenshots

![Assignment 1 — first running build](../screenshots/assignment-1/01-home-hello-portfolio.png)

**Demo tip:** Mention CLI init → Metro → first successful emulator install. Open `android/` in Android Studio and show Logcat if asked.

---

# Assignment 2 — Comparative Study (Native, Hybrid, React Native)

**COs:** CO1

## Theory

### Native

Apps written with platform SDKs (Kotlin/Java + Android SDK; Swift + UIKit/SwiftUI). Best performance and deepest OS access; separate codebases per platform.

### Hybrid (WebView)

A web app (HTML/CSS/JS) wrapped in a native WebView shell. High code reuse for content apps; often weaker gestures and “web-like” feel.

### React Native

One React/TypeScript codebase that renders **real native views** (`View`, `Text`, …) via a bridge — not a full-page WebView. Strong fit for shared UI products and academic React curricula.

## Feature comparison

| Feature | Native | Hybrid | React Native |
| --- | --- | --- | --- |
| Languages | Kotlin / Swift | HTML / CSS / JS | JS / TypeScript + React |
| UI rendering | Native widgets | WebView | Native widgets via bridge |
| Performance | Excellent | Often weaker | Near-native for most apps |
| Code sharing | Low | High | High |
| Tooling | Studio / Xcode | Web + shell | Metro + Studio / Xcode |

## Advantages / limitations / use cases

- **Native** — best for banking, games, deep hardware; costly dual codebases  
- **Hybrid** — fastest web reuse; weaker native feel  
- **React Native** — portfolios, SaaS clients, cross-platform product UI; occasional native modules needed  

## Why React Native for this project

Curriculum maps to components, Props, `useState`, core widgets, Flexbox, and navigation. Community CLI gives a real `android/` Studio workflow. One codebase covers the full student portfolio.

**Detailed write-up:** [`../assignment-2-comparison-report.md`](../assignment-2-comparison-report.md)

---

# Assignment 3 — Functional Components, Props, and State

**COs:** CO2, CO3

## Theory

- **Functional components** are JavaScript functions that return UI.  
- **Props** pass data from parent → child (read-only for the child).  
- **`useState`** stores values that change over time; updating state re-renders the component.

## Implementation

| Requirement | Evidence |
| --- | --- |
| Reusable components | `src/components/` — `ProjectCard`, `SkillChip`, `ThemeToggle`, `ContactForm`, … |
| Props | `ProjectsScreen` → `<ProjectCard title={…} />` from `src/data/projectCatalog.ts` |
| Dynamic UI | Theme `isDark` in `App.tsx`; form errors in `ContactForm`; expand in `ProjectCard` |

## Screenshots

![Projects — cards via Props](../screenshots/assignment-3/01-projects-props-cards.png)

![Theme toggle / useState](../screenshots/assignment-3/02-home-theme-toggle-bottom.png)

![Dark mode](../screenshots/assignment-3/03-dark-mode.png)

![Form state errors](../screenshots/assignment-3/04-form-state-errors.png)

**Viva lines:**  
1. “Data lives in `src/data`; components stay reusable via Props.”  
2. “`isDark` updates the whole theme when the Switch toggles.”

---

# Assignment 4 — Project Structure and Reusable Components

**COs:** CO2, CO3

## Theory

A maintainable React Native app separates:

- **Screens** — one route / page  
- **Components** — reusable UI pieces  
- **Data** — static content / JSON  
- **Theme / navigation / types** — cross-cutting concerns  

State-based updates (theme, form validation) prove the UI reacts to `useState` without rewriting components.

## Folder structure (summary)

```
TanmayPortfolio/
├── android/              # Native Android (Android Studio)
├── assets/images/        # profile.jpg, project covers
├── docs/                 # Reports & screenshots
├── src/
│   ├── components/       # Props-driven UI
│   ├── screens/          # Portfolio sections
│   ├── data/             # profile, skills, projects.json, …
│   ├── theme/            # colors, ThemeContext
│   ├── navigation/       # Stack navigator
│   └── types/
├── App.tsx               # useState theme + NavigationContainer
└── package.json
```

**Full document:** [`../assignment-4-folder-structure.md`](../assignment-4-folder-structure.md)

State demos: dark-mode Switch; Contact validation errors (see Assignment 3 screenshots).

---

# Assignment 5 — Student Profile Application (Core Components)

**COs:** CO3

## Theory

React Native core building blocks:

| Component | Role |
| --- | --- |
| `View` | Layout container |
| `Text` | Labels, titles, body |
| `Image` | Profile / media |
| `TextInput` | User input |
| `Button` | Primary actions |
| `Switch` | Boolean toggle |
| `ScrollView` | Scrollable pages |
| `StyleSheet` | Styles object |

## Where used in TanmayPortfolio

| Component | Location |
| --- | --- |
| `View` / `Text` | Every screen |
| `Image` | Profile photo (`assets/images/profile.jpg`) |
| `TextInput` | `ContactInput` / Contact form |
| `Button` | Contact submit |
| `Switch` | `ThemeToggle` |
| `ScrollView` | `ScreenContainer` |
| `StyleSheet` | All styled components |

Portfolio sections act as a student-profile app: Home, About, Skills, Projects, Experience, Certifications, Resume, Contact.

## Screenshots

![Home / profile](../screenshots/assignment-5/01-home-profile.png)

![Skills scroll](../screenshots/assignment-5/02-skills-scroll.png)

![Experience](../screenshots/assignment-5/03-experience.png)

![More / About menu](../screenshots/assignment-5/04-more-menu.png)

![Contact form](../screenshots/assignment-5/05-contact-form.png)

![Dark mode Switch](../screenshots/assignment-5/06-home-dark-switch.png)

---

# Assignment 6 — Flexbox, TextInput, onPress, Alert

**COs:** CO3, CO4

## Theory

- **Flexbox** (`flexDirection`, `flexWrap`, `justifyContent`, `alignItems`) lays out rows/columns that adapt to screen width.  
- **Controlled TextInput** binds `value` + `onChangeText` to `useState`.  
- **`onPress`** on `Button` / `Pressable` runs handlers (validate, navigate, open links).  
- **`Alert`** shows feedback after actions.

## Implementation

| Requirement | Evidence |
| --- | --- |
| Flexbox | Home CTA wrap; skill chips `flexWrap`; Experience row + rail |
| TextInput | Controlled fields in `ContactForm` |
| `onPress` | `<Button onPress={handleSubmit} />`; Pressable CTAs / dock |
| Alert | Valid contact submit shows confirmation Alert |

## Screenshots

![Projects layout](../screenshots/assignment-6/01-projects-layout.png)

![Skills Flexbox chips](../screenshots/assignment-6/02-skills-flexbox.png)

![Contact TextInput](../screenshots/assignment-6/03-contact-textinput.png)

![Validation on empty submit](../screenshots/assignment-6/04-contact-validation.png)

![Contact success path](../screenshots/assignment-6/05-contact-success.png)

---

# Assignment 7 — Multi-Screen Stack Navigation

**COs:** CO4

## Theory

**Stack Navigation** keeps screens in a stack. `navigate('About')` pushes About; returning pops or navigates to another named route. React Navigation’s native stack (`createNativeStackNavigator`) integrates with platform transitions.

## Implementation

| Requirement | Evidence |
| --- | --- |
| Home, About, Contact | `HomeScreen`, `AboutScreen`, `ContactScreen` |
| Stack Navigator | `src/navigation/AppNavigator.tsx` |
| Navigate with buttons | Home / dock / menu call `navigation.navigate(…)` |

Screens on the stack: Home (initial), About, Skills, Projects, Contact, Experience, Certifications, Resume.

Native header is hidden (`headerShown: false`); branding + floating dock provide navigation. Transitions use `animation: 'slide_from_right'`.

## Screenshots (navigation surfaces)

![Home — entry to stack](../screenshots/assignment-3/03-dark-mode.png)

![About / More destination](../screenshots/assignment-5/04-more-menu.png)

![Contact destination](../screenshots/assignment-6/03-contact-textinput.png)

**Demo:** From Home tap **About** / **Talk (Contact)** / **View work** and show the screen change; tap brand mark to return Home.

---

# Assignment 8 — Dynamic Data + FlatList

**COs:** CO5

## Theory

- **Local JSON** stores list data without a server.  
- **`FlatList`** virtualizes long lists (only visible rows mount), with props such as `initialNumToRender`, `windowSize`, and `removeClippedSubviews`.  
- Loading / error UI keeps the screen usable while data loads.

## Implementation

| Requirement | Evidence |
| --- | --- |
| Local JSON | `src/data/projects.json` via `fetchProjects()` in `projectCatalog.ts` |
| FlatList | `ProjectsScreen.tsx` |
| Efficient scroll | FlatList tuning props on the projects list |

## Screenshots

![Projects FlatList](../screenshots/assignment-3/01-projects-props-cards.png)

![Projects layout](../screenshots/assignment-6/01-projects-layout.png)

**Demo:** Open Projects — brief loading if refreshing — then scroll the list and expand a card.

---

# Assignment 9 — Student Portfolio Application

**COs:** CO3, CO4, CO5

## Theory / objective

A student portfolio is a multi-screen app that presents identity, education, skills, projects, and contact — with navigation and responsive layout. It combines Assignments 5–8 into one coherent product.

## Requirements checklist

| Requirement | Where in app |
| --- | --- |
| Home — name, photo, intro | `HomeScreen` + profile image |
| About — education + career objectives | `AboutScreen` |
| Skills — technical + soft | `SkillsScreen` + `SKILL_CATEGORIES` (includes Soft Skills) |
| Projects — FlatList | `ProjectsScreen` + `projects.json` |
| Contact — TextInput + Button | `ContactForm` |
| Stack Navigator | `AppNavigator` |
| StyleSheet + Flexbox | All screens |

## Screenshots

![Home](../screenshots/assignment-5/01-home-profile.png)

![About](../screenshots/assignment-5/04-more-menu.png)

![Skills](../screenshots/assignment-5/02-skills-scroll.png)

![Projects](../screenshots/assignment-3/01-projects-props-cards.png)

![Contact](../screenshots/assignment-5/05-contact-form.png)

---

# Assignment 10 — Personal Portfolio Application

**COs:** CO1, CO2, CO3, CO4, CO5

## Theory / objective

Assignment 10 is the capstone personal portfolio: the same product surface as Assignment 9, with full coverage of earlier concepts (setup, comparison rationale, components/state, structure, core widgets, Flexbox/events, stack nav, FlatList).

## Capstone mapping

| Concept from earlier labs | Visible in portfolio |
| --- | --- |
| RN project + emulator (A1) | App runs on Pixel via Community CLI |
| Why RN (A2) | Documented comparison report |
| Props + `useState` (A3–A4) | Cards, theme, form validation |
| Core components (A5) | View/Text/Image/TextInput/Button/Switch/ScrollView |
| Flexbox + onPress + Alert (A6) | Layouts + Contact submit |
| Stack Navigation (A7) | Multi-screen navigator |
| JSON + FlatList (A8) | Projects list |
| Full portfolio UI (A9–A10) | Home → Contact (+ Experience, Certs, Resume) |

## Screenshots (capstone set)

![Home dark](../screenshots/assignment-3/03-dark-mode.png)

![Skills Flexbox](../screenshots/assignment-6/02-skills-flexbox.png)

![Experience](../screenshots/assignment-5/03-experience.png)

![Contact validation](../screenshots/assignment-6/04-contact-validation.png)

![Contact success](../screenshots/assignment-6/05-contact-success.png)

---

## Rubric alignment (Excellent)

| Criteria | How this project scores |
| --- | --- |
| Functionality & Output | All sections run; theme; validation; links; stack nav; FlatList |
| Code Structure & Syntax | Modular `src/`; TypeScript; consistent naming |
| Concept Implementation | Props, useState, core components, Flexbox, Pressable/Button, Stack, FlatList |
| Readability & Documentation | Comments, `docs/`, README, this report |

---

## Suggested viva walkthrough (4–5 minutes)

1. Home — name, photo, intro; stack CTAs / dock  
2. About — education + career direction  
3. Skills — technical + soft skill chips (Flexbox wrap)  
4. Projects — FlatList scroll, expand Details  
5. Contact — empty Submit → errors; valid Submit → Alert  
6. Toggle dark mode (`useState` + Switch)  
7. Mention `projects.json` + `fetchProjects` (Assignment 8)  
8. Optionally open `android/` in Android Studio + Logcat (Assignment 1)

---

## References

- React Native Docs — https://reactnative.dev  
- React Navigation — https://reactnavigation.org  
- Android Developers — https://developer.android.com  
- Project repository — https://github.com/tanmays0/TanmayPortfolio  

---

*End of report — Tanmay Shinde · CPAD Laboratory Assignments 1–10*
