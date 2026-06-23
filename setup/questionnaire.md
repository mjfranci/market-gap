# Onboarding Questionnaire: Market Research and Problem Discovery

Read this file when the user types `setup`. Follow the instructions below exactly.

---

## System-Level Placeholders

This workspace has no system-level placeholder variables. There is nothing to hydrate via string substitution.

**Why:** This workspace is configured entirely through user-provided skills (dynamic, registered at runtime) and per-run inputs (target market, collected conversationally by Stage 02). There are no identity, brand, design, or preference values that stay constant across all runs.

**Web tools** are deliberately excluded from onboarding. They require tool-specific credentials and configuration steps that vary per tool and cannot be resolved through a flat questionnaire. Direct the user to `shared/web-tools-setup.md` to configure them separately after skills are registered.

---

## Setup Flow

When the user types `setup`, do the following in order:

1. Confirm to the user that there are no placeholder variables to hydrate
2. Go to `stages/01-skills-onboarding/CONTEXT.md` and run skills onboarding
3. After skills are registered, remind the user to configure web tools in `shared/web-tools-setup.md`
4. Remind the user that the QC skill required by Stage 05 can be added at any time by returning to Stage 01

Setup is complete when the skills registry contains at least one registered skill.

---

## Per-Run Variables

These are NOT part of setup. They are collected conversationally at the start of each relevant stage.

| Variable | Collected By | How |
|----------|-------------|-----|
| Target market and scope constraints | Stage 02, step 1 | Agent asks the user at stage start |

---

## After Setup

Tell the user: "Setup complete. When you are ready to begin, go to `stages/02-market-research/CONTEXT.md` and tell the agent which market you want to explore."
