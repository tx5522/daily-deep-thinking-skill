# Changelog

All notable changes to this project are documented here.

## [1.2.0] - 2026-09-17

### Changed

- Reworked candidate-question design around **identity/role + realistic situation + constraints + decision problem**.
- Made concrete real-world judgment the preferred entry point; abstract theory, books, and policy now emerge later when they help explain the user's reasoning.
- Added an explicit filter against questions that are merely factual, rhetorical, or abstract without a meaningful tradeoff.
- Reinforced the **one key question per turn** rule.
- Kept sessions intentionally short: normally 2–4 high-value follow-up exchanges, followed by synthesis and closure.
- Clarified that real events are useful entry points rather than a reason to turn the session into a news digest.
- Added a neutral-agency rule for political and electoral topics: provide sourced information and let the user make the political judgment.

## [1.1.0] - 2026-09-17

### Changed

- Improved daily candidate prompts to begin from concrete identities and decision contexts rather than abstract policy or theory.
- Added stronger evidence-lane separation between author quotations, author views, real-world evidence, other scholars' views, AI inference, and constructed examples.
- Refined the short-session stopping rule so the coach closes once the user's model has materially improved.

## [1.0.0] - 2026-09-16

### Added

- Initial Daily Thinking Coach workflow.
- 3–5 daily candidate questions with optional current-event grounding.
- Socratic questioning, brief teaching, counterargument, collaborative reasoning, and current-fact research.
- Compact end-of-session synthesis and light thinking-profile guidance.
