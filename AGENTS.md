    # Serpent Trials – Agent Governance Rules

    ---

    ## 1. Authority Model

    The agent:

    * Owns course content generation (Spanish)
    * Owns project scaffolding and code skeletons
    * Owns trial-by-trial progression design
    * May create the initial repository structure (if not already created)

    The agent may NOT:

    * Modify `SCOPE.md`
    * Modify `AGENTS.md`
    * Change repository architecture after it is established
    * Perform structural refactors without explicit authorization

    If a structural change is needed, the agent must propose it separately and wait for approval.

    ---

    ## 2. Stability Principle

    This course is public and may be used by students progressively.

    Therefore:

    * No drastic changes after initial stabilization.
    * No rewriting earlier trials once published.
    * Only additive improvements are allowed unless explicitly requested.

    Backwards compatibility of earlier trials is mandatory.

    ---

    ## 3. Pedagogical Scope

    ### Objective

    Teach Python fundamentals through building a Snake game.

    This is NOT:

    * Professional engineering training
    * A software architecture course
    * A performance optimization course

    Keep everything simple.

    ---

    ## 4. Code Governance Rules

    ### Allowed

    * Variables
    * Lists
    * Basic dictionaries (if needed)
    * Conditionals (`if`)
    * Loops (`while`, `for`)
    * Functions
    * Basic imports from standard library
    * Basic OOP (only when pedagogically justified)

    ### Allowed as Optional Bonus Only

    * List comprehensions
    * Minor refactors
    * Cleaner patterns as “exploration”

    ### Forbidden

    * Async
    * Threading
    * External dependencies (except `turtle`)
    * Design patterns
    * Advanced abstractions
    * Metaprogramming
    * Complex class hierarchies
    * Dependency injection
    * Performance tuning

    This is beginner-level Python.

    ---

    ## 5. Trial Design Contract

    Each trial MUST:

    * Modify the same progressive codebase
    * Produce visible change in output
    * Be achievable in 30–60 minutes
    * Introduce minimal new concepts
    * End with a runnable project

    Each trial MUST follow this structure:

    1. Objective
    2. Concept explanation (Spanish)
    3. Snake connection
    4. Concrete requirement
    5. Expected visible result
    6. Optional challenge

    No trial may exist purely for theory.

    Every trial must visually evolve the game.

    ---

    ## 6. Trial Sizing Policy

    Trials are defined by outcome, not concept count.

    Design method:

    1. Define what the game looks like at end of trial.
    2. Identify minimal concepts required.
    3. Introduce only those concepts.

    If a trial becomes too heavy:

    * Split into two trials.

    Small wins > Large jumps.

    ---

    ## 7. Code Scaffolding Rules

    Every trial must include runnable code.

    From Trial 0 onward:

    * The project must execute.
    * Even if it only prints a placeholder.

    Use clear TODO markers:

    ```python
    # TODO: Implement snake movement logic
    ```

    Never present blank files.

    Prevent beginner paralysis.

    ---

    ## 8. Visual Consistency Rules

    The terminal snake must:

    * Use consistent symbols
    * Use a consistent coordinate system
    * Use a consistent grid size
    * Maintain same visual identity across trials

    Do not change representation mid-course.

    No aesthetic redesign mid-series.

    ---

    ## 9. Movement Design Policy

    Movement progression must follow this sequence:

    1. Manual step-based movement
    2. Introduce loop
    3. Clear and redraw grid
    4. Store last direction
    5. Continuous automatic motion

    No OS-specific complexity.

    Keep implementation simple and redraw-based.

    ---

    ## 10. Repository Structure Integrity

    The agent MUST NOT:

    * Rename root folders
    * Add new top-level directories
    * Move projects between folders
    * Restructure documentation

    If the repo structure exists, it is fixed.

    ---

    ## 11. Refactoring Policy

    Refactoring is allowed only:

    * After introducing a relevant concept
    * When it improves clarity for beginners
    * Without breaking prior trial instructions

    No structural rewrites.

    No architectural redesign.

    Only incremental clarity improvements.

    ---

    ## 12. Solution Policy

    Solutions must:

    * Be separated from main exercise content
    * Be accessible but not immediately visible
    * Be placed in a predictable location (e.g., `solutions/` or separate file)

    Students should attempt first.
    Reference solutions should exist.

    ---

    ## 13. Tone & Narrative Rules

    All course content must:

    * Address learner as “tú”
    * Use informal Spanish
    * Avoid academic tone
    * Avoid excessive emojis
    * Be motivating but not exaggerated
    * Avoid sounding like a textbook

    Style: mentor, not professor.

    ---

    ## 14. Engagement Rule

    Every trial must:

    * Evolve the game
    * Provide visible improvement
    * Reinforce progression
    * Build toward final product

    If a trial does not improve the snake, it must not exist.

    ---

    ## 15. Expansion Guardrails

    The agent must NOT:

    * Add features not defined in PRD
    * Introduce gamification systems
    * Add badges or achievements
    * Add speed scaling unless defined
    * Add multiplayer
    * Add sound
    * Add Pygame unless explicitly added to scope

    Scope discipline is mandatory.

    ---

    ## 16. Versioning Policy

    * Progress through commits only.
    * No branching model required.
    * No release tagging required.
    * No semantic versioning needed.

    Simplicity over ceremony.

    ---

    ## 17. Long-Term Stability Principle

    Once students are actively using the course:

    * Only additive content is allowed.
    * No destructive rewrites.
    * No altering early trial assumptions.

    Stability is more important than elegance.

    ---

    ## 18. Agent Behavior Rule

    When uncertain:

    * Prefer simplicity.
    * Prefer clarity.
    * Prefer visual feedback.
    * Prefer smaller trials.
    * Prefer fewer concepts per trial.

    If complexity increases cognitive load, reduce it.