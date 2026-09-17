# Daily Deep Thinking Skill

A portable AI thinking-coach Skill for short, evidence-aware daily reasoning sessions.

The core idea is simple: **start from a concrete role and a real decision, then work toward theory**. Instead of opening with an abstract question such as “How should monetary policy balance growth and inflation?”, the Skill prefers a situation the user can actually inhabit:

> You run a manufacturing company. Your borrowing rate has risen from 3% to 5.5%, demand is uncertain, and a new production line would take three years to pay back. Do you borrow to expand now, delay the investment, or choose a smaller plan? Why?

The discussion can then uncover interest-rate transmission, expectations, incentives, risk, policy, and relevant literature naturally.

## What it does

- Produces 3–5 distinct daily thinking questions.
- Prefers **role + realistic situation + constraints + decision** over abstract theory-first prompts.
- Uses current evidence when recent facts materially affect the question.
- Runs a short Socratic discussion with **one key question per turn**.
- Defaults to **2–4 high-value follow-up exchanges**, rather than an endless interrogation.
- Separates evidence, author views, other scholars' views, AI inference, and constructed examples.
- Stops once the user has a better causal model or decision framework, even if the issue remains unresolved.

## Good question design

A useful candidate usually has four parts:

1. **Identity** — Who are you in this situation?
2. **Reality** — What is actually happening?
3. **Constraint** — What makes the choice difficult?
4. **Decision** — What would you do, and what tradeoff are you accepting?

Real events can motivate the question, but the session should not collapse into a news summary. Books, theories, public policy, and academic concepts are introduced after they help explain the user's reasoning.

## Session flow

```text
current context + current evidence
            ↓
3–5 concrete candidate questions
            ↓
user chooses one
            ↓
user states an initial judgment/model
            ↓
2–4 rounds of focused questioning / teaching / counterargument / research
            ↓
compact synthesis + unresolved uncertainty + observation/test
```

## Files

- `SKILL.md` — the complete portable Skill contract.
- `README.md` — project overview and usage philosophy.
- `CHANGELOG.md` — version history.
- `LICENSE` — MIT License.

## Using the Skill

Install or load `SKILL.md` in a Skill-compatible agent environment, then invoke it for requests such as:

- “开始今天的每日深度思考。”
- “给我几个今天值得深入想的问题。”
- “继续昨天那个经济学问题。”
- “不要直接告诉我答案，带我一步一步推理。”

For scheduled use, a typical instruction is:

> Every morning, start a Daily Deep Thinking session. Give me 3–5 concrete candidate questions first and wait for me to choose before beginning the discussion.

## Design principles

This Skill intentionally avoids several common failure modes: abstract questions with no decision context, fake “counterintuitive” hooks, long lecture-first answers, multiple stacked questions in a single turn, treating an author's opinion as evidence, and continuing the dialogue after the useful reasoning work is already complete.

It is designed to improve the user's model, not to make decisions for the user.

## Version

Current version: **1.2.0**

## License

MIT
