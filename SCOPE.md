# Serpent Trials

## 1. Overview

**Project Name:** Serpent Trials

**Purpose:** Create a progressive, trial-based Python course for 13-year-old beginners where learners build a playable Snake game step-by-step.

The course will:

* Be hosted as a public GitHub repository
* Use GitHub Pages (`/docs`) for navigation and content delivery
* Be structured as a series of trials (Trial 0, Trial 1, ...)
* Modify the same codebase progressively
* End with two independent playable projects:

  * Terminal ASCII Snake
  * Turtle Graphical Snake

---

## 2. Core Philosophy

### Pedagogical Principles

* Engagement first
* Visible results every trial
* Progressive code evolution
* Fun > perfection
* Minimal tool friction
* Real project ownership (students fork repository)

### Audience

* Age: ~13 years old
* Assumes:

  * Basic computer literacy
  * Basic folder understanding
  * Basic terminal awareness

* Designed for:

  * Guided learning
  * Independent learners
  * Open-source public consumption

---

## 3. Language Policy

| Component           | Language          |
|---------------------|-------------------|
| SCOPE               | English           |
| Code                | English           |
| Code comments       | English           |
| Course content      | Spanish (primary) |
| Future translations | Optional          |

Tone of course content:

* Informal Spanish (tú)
* Clear
* Motivating
* Not academic  

---

## 4. Technical Constraints

### Operating System

* Primary: Windows
* Must avoid OS-heavy instructions
* Use Visual Studio Code as primary editor
* Avoid PowerShell / Git Bash complexity
* Keep Git interaction minimal and VS Code friendly

Future OS-specific notes may be added later.

---

### Python Strategy

* Use system-installed Python
* No virtual environments
* No dependency management complexity
* Keep focus on programming, not tooling

---

### Git Strategy

Learners must:

* Fork repository
* Clone their fork
* Commit progress
* Push changes

Git depth:

* Slightly structured
* No complex branching model required
* Progressive development on main branch acceptable

---

## 5. Repository Architecture

```
serpent-trials/
│
├── docs/                      # GitHub Pages content (Spanish course)
│
├── trials/                    # Trial instructions (Spanish markdown)
│   ├── trial-00-setup/
│   ├── trial-01-variables/
│   ├── trial-02-conditions/
│   └── ...
│
├── projects/
│   ├── snake-terminal/
│   │   └── main.py
│   │
│   └── snake-turtle/
│       └── main.py
│
├── scaffolding/
│   ├── terminal-base.py
│   └── turtle-base.py
│
├── PRD.md
└── README.md
```

### Rules

* Trials modify the same project progressively.
* `snake-terminal` is built first.
* `snake-turtle` starts after terminal version is complete.
* Final versions must run independently.

#### Critical Invariant: Main File Path Never Changes

For each project, the learner will progressively edit the SAME main entry file in-place:

- Terminal project entrypoint: `projects/snake-terminal/main.py`
- Turtle project entrypoint: `projects/snake-turtle/main.py`

Trials MUST NOT rename, move, duplicate, or replace these entry files as a progression mechanism.
All trial instructions must assume the entrypoint paths above remain constant for the entire course.

If a trial needs to introduce new files, it may ONLY add helper modules (e.g., `grid.py`, `render.py`) inside the same project folder, while keeping `main.py` as the stable entrypoint.

---

## 6. Trial Structure Standard

Each trial must follow this structure:

### 🎯 Objective

Clear measurable goal.

### 🧠 Concept Explanation

Explain Python concept (Spanish).

### 🧩 Snake Connection

How this concept moves us closer to the final game.

### 🛠️ Requirement

Concrete task to implement.

### ✅ Expected Result

What should appear on screen.

### 🚀 Optional Challenge

Stretch goal for advanced learners.

---

## 7. Trial Roadmap

---

## TRIAL 0 – Setup & Ownership

**Goal:**
Students fork, clone, open in VS Code, and run first Python file.

**Outcome:**
They see:

```
Welcome to Serpent Trials
```

This trial establishes:

* GitHub account
* Forking
* Cloning
* Running Python file

---

# PHASE 1 – Terminal Snake (ASCII)

Final Goal:
Playable ASCII snake with:

* Smooth movement
* Food
* Score
* Game over
* Restart logic

---

## TRIAL 1 – Variables & Printing

* Define grid size
* Print static board

---

## TRIAL 2 – Lists & Coordinates

* Represent snake as list of coordinates
* Print snake position

---

## TRIAL 3 – Functions

* Extract rendering into function
* Extract snake creation

---

## TRIAL 4 – Manual Movement (Step-Based)

Player presses:
W / A / S / D
Snake moves one step.

No loop automation yet.

This introduces:

* Input handling
* Position updates

---

## TRIAL 5 – Continuous Movement

Introduce:

* Game loop (`while`)
* Clear screen and redraw
* Store last direction

Snake moves automatically in last chosen direction.

This creates the first "real game feel."

---

## TRIAL 6 – Food System

* Random food position
* Collision detection (snake eats food)
* Snake grows

---

## TRIAL 7 – Collision Detection

* Wall collision
* Self collision
* Game Over message

---

## TRIAL 8 – Score & Restart Logic

* Score counter
* Restart option without exiting program

Terminal version complete.

---

# PHASE 2 – Turtle Graphics

Now we rebuild using Turtle.

---

## TRIAL 9 – Turtle Setup

* Open window
* Draw square
* Move square

---

## TRIAL 10 – Snake Body in Turtle

* Represent snake graphically
* Move head
* Follow segments

---

## TRIAL 11 – Food & Collision (Graphical)

* Reimplement logic visually

---

## TRIAL 12 – Polish

* Score display
* Game over screen
* Restart logic

Graphical version complete.

---

## 8. Movement Design Decision

Movement progression:

1. Step-based manual movement (no loop)
2. Introduce game loop
3. Clear + redraw approach
4. Store last direction pressed
5. Automatic motion

We will:

* Avoid complex OS-specific input
* Keep implementation simple
* Use redraw-per-frame approach

---

## 9. Scaffolding Strategy

Each trial includes:

* A partially completed file
* TODO markers like:

```python
# TODO: Update snake position based on direction
```

Scaffolding must:

* Prevent blank-file paralysis
* Avoid over-abstracting early
* Grow complexity gradually

---

## 10. GitHub Pages

* `/docs` folder
* Markdown-based
* Navigation index
* Trial links
* Clean minimal theme

No game rendering in browser.

---

## 11. Non-Goals

* No virtual environments
* No packaging
* No advanced architecture patterns
* No automated testing
* No multiplayer
* No advanced performance optimizations
* No external dependencies (except turtle)

---

## 12. Future Extensions (Not in Initial Scope)

* Pygame version
* Difficulty levels
* Speed increase
* Sound effects
* Achievement badges
* Leaderboard
* Multi-language support
* Linux/Mac setup notes

---

## 13. Success Criteria

The course succeeds if:

* A 13-year-old can complete it independently.
* Every trial produces visible progress.
* The final snake is playable.
* Students feel ownership of their forked repo.
* They understand core Python fundamentals:

  * Variables
  * Lists
  * Conditions
  * Loops
  * Functions
  * Basic state management