# MIT ART, DESIGN AND TECHNOLOGY UNIVERSITY  
## MIT School of Computing, Pune  
### Department of Information Technology

**Course:** Cross Platform App Development (CPAD)  
**ASSIGNMENT REPORT — Assignments 1 to 10**  
**React Native Developer Portfolio (TanmayPortfolio)**

| Field | Detail |
| --- | --- |
| Student Name | Tanmay Shinde |
| Enrollment Number | ADT23SOCB1617 |
| Roll No. / Division | 12 / LY-SMAD |
| Program | B.Tech Information Technology |
| Year | Final Year (LY) |
| Course Faculty | Prof. Rohini Bhosale |
| Academic Year | 2026–27 |
| Repository | https://github.com/tanmays0/TanmayPortfolio |

---

## Declaration

I, Tanmay Shinde, a student of B.Tech Information Technology (Enrollment No. ADT23SOCB1617, Roll No. 12, Division LY-SMAD), declare that this report and the accompanying project, **TanmayPortfolio**, are my own work, completed for Assignments **1 to 10** of the Cross Platform App Development (CPAD) course. The application was built with React Native (Community CLI) and executed on the Pixel Android emulator. All screenshots in this report were captured from that running application.

**Student Name:** Tanmay Shinde  
**Enrollment Number:** ADT23SOCB1617  
**Signature:** ______________________

---

## Table of Contents

1. Introduction and Project Overview  
2. Assignment 1: Setup and Hello World  
3. Assignment 2: Native vs Hybrid vs React Native  
4. Assignment 3: Components, Props and useState  
5. Assignment 4: Folder Structure and State  
6. Assignment 5: Student Profile App with Core Components  
7. Assignment 6: Flexbox, TextInput and onPress  
8. Assignment 7: Multi-Screen Stack Navigation  
9. Assignment 8: Dynamic Data Rendering with FlatList  
10. Assignment 9: Student Portfolio Application  
11. Assignment 10: Personal Portfolio Application  
12. Rubric Alignment  
13. Conclusion  

---

# 1. Introduction and Project Overview

This report documents the work completed for Assignments **1 to 10** of the Cross Platform App Development (CPAD) course. Instead of building ten unrelated exercises, each assignment is implemented as part of **one** application: a React Native developer portfolio named **TanmayPortfolio**.

The app contains Home, About, Skills, Projects, Experience, Certifications, Resume and Contact screens. It is used throughout this report to demonstrate every concept in the laboratory brief.

### 1.1 Technology used

| Item | Detail |
| --- | --- |
| Framework | React Native 0.87 with TypeScript |
| Project creation | React Native Community CLI (real `android/` Gradle project, not Expo Go) |
| Run target | Pixel Android emulator |
| Tooling | Community CLI, Metro bundler and Android Studio |
| Navigation | React Navigation — native Stack Navigator |

**Note on Expo vs Community CLI:** The Assignment 1 brief mentions Expo CLI. This project uses the **Community CLI**, which also creates a React Native project and runs on an emulator, and additionally provides a native `android/` folder that opens in Android Studio—matching the lab demo workflow.

### 1.2 Assignment mapping

| Assignment | Topic | Where it is shown in the project |
| --- | --- | --- |
| 1 | Setup + Hello World | Community CLI project, `android/` folder, first emulator run |
| 2 | Comparison report | Native vs Hybrid vs React Native, and why RN was chosen |
| 3 | Components, Props, useState | `src/components`, ProjectCard props, theme and form state |
| 4 | Folder structure + state | Documented `src/` tree, Switch and validation updates |
| 5 | Profile app + core components | View, Text, Image, TextInput, Button, Switch, ScrollView |
| 6 | Flexbox, TextInput, onPress | Skill wrap, contact inputs, Submit handler, Alert |
| 7 | Stack Navigation | `AppNavigator`, Home / About / Contact and other routes |
| 8 | JSON + FlatList | `projects.json`, `ProjectsScreen` FlatList |
| 9 | Student Portfolio | Full multi-screen portfolio product |
| 10 | Personal Portfolio | Capstone covering CO1–CO5 in one app |

---

# 2. Assignment 1: Setup and Hello World

**COs:** CO1, CO2

### 2.1 Aim

To show that the project is a real React Native Community CLI application that installs and runs on the Android emulator.

### 2.2 Theory

React Native is a framework for building mobile user interfaces with JavaScript or TypeScript and the React component model. A Community CLI project includes:

1. A JavaScript entry file (`index.js`) registered with the native host through `AppRegistry`.  
2. **Metro**, the bundler that packages JavaScript and supports Fast Refresh during development.  
3. Native project folders (`android/` and `ios/`) that build platform APKs / apps.

The first academic milestone is a **Hello World** screen: a minimal UI that proves Metro, the native shell, and the emulator can install and display the app. Later screens replace Hello World without changing the project creation path.

### 2.3 Steps performed

- Create the project with Community CLI. The project root is `TanmayPortfolio` and `package.json` lists `react-native` 0.87.1.  
- Open `android/` in Android Studio. The Gradle project is opened in Android Studio, rather than using Expo Go.  
- Run on the emulator with `npm run android`, or with Run in Android Studio.  
- The same CLI app that first displayed Hello World now hosts the complete portfolio.

### 2.4 Explanation

The Community CLI was used so that the project contains a real `android/` folder. Metro bundles the JavaScript, and Android Studio installs the APK on the emulator. The first milestone was Hello World; the same application now hosts the full portfolio.

### 2.5 Output

![Figure 1: Portfolio Home screen running on the emulator](../screenshots/assignment-1/01-home-hello-portfolio.png)

---

# 3. Assignment 2: Native vs Hybrid vs React Native

**COs:** CO1

### 3.1 Aim

To compare three ways of building a mobile app for the same product goal, and to justify the choice made for this project. React Native sits in the middle: shared JavaScript with real native views.

### 3.2 Theory

**Native development** uses platform SDKs and languages (Kotlin/Java on Android; Swift on iOS). Each platform is a separate codebase with full access to device APIs. Performance and OS integration are strongest, but cost and maintenance rise when the same product must ship on two platforms.

**Hybrid (WebView-based) development** wraps a web application (HTML, CSS, JavaScript) inside a native WebView shell. Teams reuse web skills quickly. The UI is largely rendered by a browser engine, so complex gestures and native look-and-feel can be weaker than true native widgets.

**React Native** is a cross-platform framework where UI is written in JavaScript/TypeScript with React. React Native bridges to **real native views** (`View`, `Text`, and so on) on Android and iOS—not a full-page WebView. One shared codebase can target both platforms while still teaching React concepts required by this course.

### 3.3 Comparison

| Aspect | Native | Hybrid (WebView) | React Native |
| --- | --- | --- | --- |
| Approach | Kotlin / Swift + platform SDKs | HTML / CSS / JS in a WebView | TypeScript + React to native views |
| Strength | Best performance and OS APIs | Fastest reuse of a website | One UI codebase, Metro Fast Refresh |
| Trade-off | Two codebases to maintain | Weaker gestures and native feel | Needs some Gradle / native tooling |
| Best suited to | Banking, games, camera-heavy apps | News, brochure, simple forms | This portfolio, product UIs, SaaS |

### 3.4 Why React Native for this project

1. **Curriculum fit.** Functional components, Props, `useState`, core React Native widgets and Flexbox are the language of the assignment list.  
2. **Studio workflow.** Community CLI ships the `android/` folder. It opens in Android Studio, runs on the emulator and shows Logcat.  
3. **One codebase.** A full student profile (Home to Contact) is built without separate Kotlin and Swift apps.  
4. **Industry signal.** React Native is widely used for cross-platform product UI.

### 3.5 Conclusion of comparison

Native wins on raw performance, Hybrid wins on web reuse, and React Native is the best fit for this course and this project.

*Detailed write-up also available in `docs/assignment-2-comparison-report.md`.*

---

# 4. Assignment 3: Components, Props and useState

**COs:** CO2, CO3

### 4.1 Aim

To build reusable components driven by Props, and to create a dynamic interface from state rather than from rewriting the UI. Data lives in `src/data`, and components stay simple and reusable.

### 4.2 Theory

A **functional component** is a JavaScript function that returns React Native elements. Components are the unit of reuse in the UI.

**Props** (properties) are inputs passed from a parent to a child. The child should treat props as read-only. Passing `title`, `description` and `tags` into `ProjectCard` is an example: the same card component renders many projects with different data.

**State** holds values that change over time. The React Hook **`useState`** returns the current value and a setter. Calling the setter schedules a re-render so the UI updates. Examples in this project:

- `isDark` in `App.tsx` drives light/dark theme for the whole tree.  
- Contact form fields and error messages live in `useState` inside `ContactForm`.  
- Expanded/collapsed details live in `useState` inside `ProjectCard`.

### 4.3 Reusable components

| Component | Purpose |
| --- | --- |
| ProjectCard | Receives title, description and tags via Props |
| SkillChip | Takes a label and an accent; used in Skills and inside cards |
| ThemeToggle | A controlled Switch with no hard-coded theme |
| ContactForm | A stateful form composed of ContactInput |

### 4.4 Data flow on the Projects screen

`ProjectsScreen` reads project data from `src/data` and maps each item to a `ProjectCard`, passing title and tags as Props. The Details control is a `Pressable`, and the expanded state lives inside the card using `useState`.

### 4.5 Output

![Figure 2: Projects screen built from ProjectCard components](../screenshots/assignment-3/01-projects-props-cards.png)

![Figure 3: Theme — isDark with the dark-mode Switch](../screenshots/assignment-3/03-dark-mode.png)

![Figure 4: Form — ContactForm errors driven by useState](../screenshots/assignment-3/04-form-state-errors.png)

---

# 5. Assignment 4: Folder Structure and State

**COs:** CO2, CO3

### 5.1 Aim

To organise the project with a documented `src/` tree in which every folder matches a concept from the course, and to show state updating the interface through the Switch and validation.

### 5.2 Theory

A well-structured React Native project separates concerns:

- **Screens** map to routes or pages the user navigates between.  
- **Components** are reusable UI pieces configured with Props.  
- **Data** modules hold static content so components stay dumb and reusable.  
- **Theme** holds colours, typography and theme context.  
- **Navigation** wires screens into a navigator.  
- **Types** document TypeScript interfaces for safety.

`App.tsx` is the root. It owns theme `useState`, wraps `ThemeProvider` and `NavigationContainer`, and mounts the stack navigator. State-based updates (theme toggle, form validation) prove the UI reacts to state without rewriting component trees by hand.

### 5.3 Documented folder structure

| Folder / File | Responsibility |
| --- | --- |
| `android/` | Native Gradle project, opened in Android Studio |
| `App.tsx` | Root `useState(isDark)`, ThemeProvider and Navigation |
| `src/components/` | Reusable UI: ProjectCard, SkillChip, ThemeToggle and others |
| `src/screens/` | One screen per portfolio section |
| `src/data/` | Static content, which keeps components prop-driven |
| `src/theme/` | Colours, tokens and ThemeContext |
| `src/navigation/` | Stack navigator for all screens |
| `docs/` | Reports and screenshots for submission |

### 5.4 State in the application

- **Theme state.** `isDark` lives in `App.tsx` and the Switch updates the whole theme when toggled.  
- **Validation state.** The contact form updates its error state on submission, which changes borders and messages on screen.

*Full tree: `docs/assignment-4-folder-structure.md`.*

---

# 6. Assignment 5: Student Profile App with Core Components

**COs:** CO3

### 6.1 Aim

To build a student profile style application that uses the eight core React Native components. The portfolio sections form the profile app: Home, About, Skills, Projects, Experience, Certifications, Resume and Contact.

### 6.2 Theory

React Native provides a small set of **core components** that map to native UI:

| Component | Role in theory | Role in this app |
| --- | --- | --- |
| `View` | Layout container (like a `div`) | Almost every layout |
| `Text` | All visible text | Titles, bio and errors |
| `Image` | Bitmap / photo display | Profile photo (`profile.jpg`) |
| `TextInput` | Text entry field | Contact form fields |
| `Button` | Platform button control | Contact submit |
| `Switch` | Boolean toggle | ThemeToggle |
| `ScrollView` | Scrollable container | ScreenContainer |
| `StyleSheet` | Style definitions | Every styled file |

Styling is applied with `StyleSheet.create`, which groups style objects and keeps render code readable. Layout among Views uses Flexbox (covered further in Assignment 6).

### 6.3 Profile screens

Each section of the portfolio is a profile screen. Skills uses `SkillChip` inside a `ScrollView`, Experience shows AdMax and CodSoft on a timeline rail, About uses profile-style cards, and Contact uses `TextInput` and `Button`.

### 6.4 Output

![Figure 5: Skills — SkillChip + ScrollView](../screenshots/assignment-5/02-skills-scroll.png)

![Figure 6: Experience — AdMax and CodSoft rail](../screenshots/assignment-5/03-experience.png)

![Figure 7: About — profile-style cards](../screenshots/assignment-5/04-more-menu.png)

![Figure 8: Contact — TextInput + Button](../screenshots/assignment-5/05-contact-form.png)

![Figure 9: Switch — dark mode](../screenshots/assignment-5/06-home-dark-switch.png)

---

# 7. Assignment 6: Flexbox, TextInput and onPress

**COs:** CO3, CO4

### 7.1 Aim

To design responsive layouts with Flexbox, accept user input through controlled TextInputs, handle `onPress` events, and display Alert messages based on user actions.

### 7.2 Theory — Flexbox

Flexbox is the primary layout system in React Native. Important properties include:

- `flexDirection` — `'row'` or `'column'` (default is column on RN)  
- `flexWrap` — allow items to wrap to the next line  
- `justifyContent` — alignment along the main axis  
- `alignItems` — alignment along the cross axis  
- `flex` — how much space a child should grow to fill  

In this project, Explore CTAs and skill chips use wrapping rows so content reflows on smaller widths. Experience uses a horizontal row: timeline rail on the left, card content on the right.

### 7.3 Theory — TextInput and events

A **controlled** TextInput always displays a value from state (`value={name}`) and updates that state in `onChangeText`. This keeps the UI and data in sync and makes validation straightforward.

**`onPress`** is the press handler for `Button` and `Pressable`. Pressing Submit runs `handleSubmit`, which validates fields. Empty submit updates error state (red borders and messages). Valid submit shows an **`Alert`** confirmation—the academic feedback required by the brief.

`Pressable` is the modern replacement for older `TouchableOpacity`-style APIs; it still demonstrates touchable event handling with `onPress`, `onPressIn` and `onPressOut`.

### 7.4 Flexbox layouts in the app

| Layout | Implementation |
| --- | --- |
| Home CTA wrap | Explore buttons use `flexWrap` so CTAs reflow |
| SkillCategory chips | SkillChip row with `flexWrap` |
| Experience row + rail | Horizontal row: rail left, card right |
| Project card actions | Details and GitHub in a Flexbox row |

### 7.5 Output

![Figure 10: Skills screen — chips wrapping](../screenshots/assignment-6/02-skills-flexbox.png)

![Figure 11: Empty form — TextInput fields](../screenshots/assignment-6/03-contact-textinput.png)

![Figure 12: Submit pressed — onPress errors](../screenshots/assignment-6/04-contact-validation.png)

![Figure 13: Valid path — Alert / success](../screenshots/assignment-6/05-contact-success.png)

---

# 8. Assignment 7: Multi-Screen Stack Navigation

**COs:** CO4

### 8.1 Aim

To create Home, About and Contact screens, implement Stack Navigation, and navigate between screens using buttons.

### 8.2 Theory

**Navigation** lets an app show one screen at a time while keeping a history of previous screens.

A **stack navigator** models screens as a stack of cards:

- The **initial route** (Home) is the first card.  
- Calling `navigation.navigate('About')` **pushes** About onto the stack (or focuses it if already present).  
- Returning to a previous screen **pops** or navigates to that route name.  
- Transitions (for example slide from the right) communicate that a new screen was pushed.

**React Navigation** provides `createNativeStackNavigator`, which uses native platform navigation containers for smooth transitions. Each screen is registered with `<Stack.Screen name="…" component={…} />`.

Button presses are the usual trigger: a `Pressable` or `Button` calls `navigation.navigate('Contact')`. This links **touchable events** (Assignment 6) with **multi-screen structure** (Assignment 7).

### 8.3 Implementation in TanmayPortfolio

| Requirement | Evidence |
| --- | --- |
| Home, About, Contact screens | `HomeScreen`, `AboutScreen`, `ContactScreen` |
| Stack Navigation | `src/navigation/AppNavigator.tsx` — `createNativeStackNavigator` |
| Navigate with buttons | Home CTAs, floating dock and menu call `navigation.navigate(…)` |

Additional stack screens: Skills, Projects, Experience, Certifications, Resume. The native header is hidden (`headerShown: false`); the brand mark and floating dock act as navigation controls. Animation is `slide_from_right`.

### 8.4 Explanation

From Home, tapping **View work**, **About**, or **Talk (Contact)** pushes the corresponding stack screen. Tapping the brand mark navigates back to Home. The user experiences multi-screen navigation without leaving the single React Native process.

### 8.5 Output

![Figure 14: Home — stack root](../screenshots/assignment-3/03-dark-mode.png)

![Figure 15: About destination](../screenshots/assignment-5/04-more-menu.png)

![Figure 16: Contact destination](../screenshots/assignment-6/03-contact-textinput.png)

---

# 9. Assignment 8: Dynamic Data Rendering with FlatList

**COs:** CO5

### 9.1 Aim

To fetch data from a local JSON file (or public API), display it with `FlatList`, and allow efficient scrolling.

### 9.2 Theory

Static arrays hard-coded inside a screen become hard to maintain. Storing projects in a **local JSON file** separates content from presentation. A loader function (`fetchProjects`) can read that JSON asynchronously—simulating the same pattern used for network APIs.

**`FlatList`** is React Native’s efficient list component. Unlike mapping every item inside a `ScrollView` (which mounts all children at once), FlatList **virtualises** the list: only rows near the viewport are rendered. Important props include:

- `data` — the array of items  
- `renderItem` — how each item becomes a component  
- `keyExtractor` — stable unique keys  
- `initialNumToRender`, `windowSize`, `removeClippedSubviews` — tune memory and scroll performance  

Loading and error states improve UX while data is fetched or if loading fails.

### 9.3 Implementation

| Requirement | Evidence |
| --- | --- |
| Local JSON | `src/data/projects.json` loaded by `fetchProjects()` in `projectCatalog.ts` |
| FlatList | `ProjectsScreen.tsx` |
| Efficient scrolling | FlatList tuning props on the projects list |

### 9.4 Explanation

Opening Projects triggers a refresh of the catalog. While loading, an activity indicator may appear. The list then scrolls smoothly; expanding a card still uses Props and local `useState` from Assignment 3.

### 9.5 Output

![Figure 17: Projects FlatList](../screenshots/assignment-3/01-projects-props-cards.png)

![Figure 18: Projects layout / scroll](../screenshots/assignment-6/01-projects-layout.png)

---

# 10. Assignment 9: Student Portfolio Application

**COs:** CO3, CO4, CO5

### 10.1 Aim / Objective

To develop a responsive and interactive **Student Portfolio Application** using React Native that presents identity, education, skills, projects and contact information with stack navigation and Flexbox / StyleSheet layout.

### 10.2 Theory

A student portfolio app is a **product composition** of earlier labs:

- **Identity screens** use core components (`Image`, `Text`, `View`) for name, photo and introduction.  
- **About** presents education and career objectives as structured content cards.  
- **Skills** communicate technical and soft abilities; chips with Flexbox wrap keep the layout responsive.  
- **Projects** use FlatList over JSON data so the list scales.  
- **Contact** uses controlled TextInputs and Button `onPress` for interaction.  
- **Stack Navigation** connects every screen into one flow.

Responsive UI means layouts adapt with Flexbox and StyleSheet rather than fixed absolute positions that break on different emulator sizes.

### 10.3 Requirements checklist

| Requirement | Evidence in TanmayPortfolio |
| --- | --- |
| Home — name, photo, intro | `HomeScreen` + `profile.jpg` |
| About — education + career objectives | `AboutScreen` |
| Skills — technical + soft | `SkillsScreen` + Soft Skills in `skills.ts` |
| Projects — FlatList | `ProjectsScreen` + `projects.json` |
| Contact — TextInput + Button | `ContactForm` |
| Stack Navigator | `AppNavigator` |
| StyleSheet + Flexbox | All screens |

### 10.4 Output

![Figure 19: Home — student identity](../screenshots/assignment-5/01-home-profile.png)

![Figure 20: Skills — technical and soft](../screenshots/assignment-5/02-skills-scroll.png)

![Figure 21: Projects — FlatList](../screenshots/assignment-3/01-projects-props-cards.png)

![Figure 22: Contact — form](../screenshots/assignment-5/05-contact-form.png)

---

# 11. Assignment 10: Personal Portfolio Application

**COs:** CO1, CO2, CO3, CO4, CO5

### 11.1 Aim / Objective

To develop a responsive and interactive **Personal Portfolio Application** using React Native. Assignment 10 is the capstone: the same product surface as Assignment 9, with explicit coverage of every course outcome from setup through dynamic lists.

### 11.2 Theory

A personal portfolio on mobile must balance **content**, **structure** and **interaction**:

1. **Content** — who the student is, what they know, what they built, how to reach them.  
2. **Structure** — modular folders, reusable components, typed data, and a navigator that keeps screens organised.  
3. **Interaction** — theme switching, form validation, press handlers, and list scrolling that feel native.

React Native is appropriate because one TypeScript codebase demonstrates both React concepts (Props, state, components) and mobile concepts (native views, Flexbox, navigation, FlatList) without maintaining separate native apps.

### 11.3 Capstone mapping to earlier assignments

| Earlier concept | Visible in the personal portfolio |
| --- | --- |
| A1 Setup + emulator | App runs on Pixel via Community CLI |
| A2 Why RN | Documented comparison and project choice |
| A3–A4 Props, state, structure | Cards, theme, form, `src/` layout |
| A5 Core components | View, Text, Image, TextInput, Button, Switch, ScrollView |
| A6 Flexbox + onPress + Alert | Layouts and Contact submit |
| A7 Stack Navigation | Multi-screen navigator |
| A8 JSON + FlatList | Projects list |
| A9 Portfolio UI | Home through Contact (+ Experience, Certs, Resume) |

### 11.4 Output

![Figure 23: Personal portfolio Home](../screenshots/assignment-3/03-dark-mode.png)

![Figure 24: Experience section](../screenshots/assignment-5/03-experience.png)

![Figure 25: Contact interaction](../screenshots/assignment-6/04-contact-validation.png)

---

# 12. Rubric Alignment

| Criterion | Evidence in the project |
| --- | --- |
| Functionality and Output | All sections run. Theme Switch works. Form validation works. External links open. App installs on emulator. Stack navigation and FlatList work. |
| Code Structure and Syntax | Modular `src/` layout, TypeScript, consistent component names, not a single-file app. |
| Concept Implementation | Props, useState, eight core components, Flexbox, TextInput, onPress, Stack Navigation and FlatList are all visible. |
| Readability and Documentation | File comments, `docs/` reports, README and screenshot folders for assignments. |

---

# 13. Conclusion

Assignments **1 to 10** were completed as a single React Native application built with the Community CLI and run on the Android emulator. The project covers:

- setup and Hello World,  
- a comparison of Native, Hybrid and React Native,  
- reusable components with Props and state with `useState`,  
- a documented folder structure,  
- the core React Native components,  
- Flexbox layouts and controlled inputs with `onPress` / Alert,  
- multi-screen Stack Navigation,  
- dynamic JSON data with FlatList,  
- and a complete student / personal portfolio product.

Two ideas summarise the design: **data lives in `src/data` while components stay reusable through Props**, and **`isDark` in `App.tsx` updates the whole theme when the Switch is toggled**. Stack navigation and FlatList complete the multi-screen, data-driven portfolio required for Assignments 7–10.

**Submitted by:** Tanmay Shinde  
**Enrollment Number:** ADT23SOCB1617  

---

## References

- React Native Documentation — https://reactnative.dev  
- React Navigation — https://reactnavigation.org  
- Android Developers — https://developer.android.com  
- Project repository — https://github.com/tanmays0/TanmayPortfolio  
