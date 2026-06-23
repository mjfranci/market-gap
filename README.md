# Market Gap — Market Research & Problem Discovery

## What this is

This repository is a lightweight framework, collection of skills, and working workspace for market research and problem discovery. It provides structured stages, prompts, and helper skills to guide entrepreneurs, product teams, and researchers through researching a target market, identifying unsolved problems, validating opportunities, and stress-testing conclusions.

Key parts of the repo:
- `CLAUDE.md` — advice and examples for using Claude with this workspace.
- `CONTEXT.md` — high-level context for the project.
- `stages/` — step-by-step stages and templates for research and validation.
- `skills/` — reusable skill modules and scripts used to support research tasks.

## Who this is for

- Entrepreneurs and founders doing problem discovery and market validation.
- Product managers and researchers running lightweight discovery sprints.
- Consultants and analysts who want a reproducible process and prompts for LLMs.

## How to start using this with Claude

1. Open this repository in your editor or upload it to Claude (or provide the relevant files). The most useful entry points are [CLAUDE.md](CLAUDE.md) and [CONTEXT.md](CONTEXT.md).
2. Ask Claude to summarize the repository and suggest next steps. Example prompt to paste into Claude:

```
You are an expert market-research assistant. Summarize the purpose of this repository, list the most relevant files and folders, and propose a 3-step plan to run a first discovery sprint using this workspace.
Files to inspect: CLAUDE.md, CONTEXT.md, stages/02-market-research/CONTEXT.md, stages/03-problem-identification/CONTEXT.md
Return: brief summary, top 5 files to start with, and an actionable 3-step checklist.
```

3. Use Claude to expand or run specific stages. For example, tell Claude: "Run the `02-market-research` stage and generate a one-page market analysis using the templates in `stages/02-market-research/output/`." Provide the stage folder or paste the stage `CONTEXT.md` content if needed.

4. Iterate: use Claude to draft research questions, synthesize notes, and produce candidate problem briefs. The `stages/03-problem-identification/` content includes templates for turning findings into testable opportunity briefs.

## Quick Start (local)

1. Open the repo in VS Code:

```
code .
```

2. Inspect the stage you want to run, for example:

```
less stages/02-market-research/CONTEXT.md
```

3. Copy relevant context into Claude (or reference the files), then ask Claude to produce the outputs defined in the stage.

## Helpful pointers

- If you plan to use Claude via API or a workspace integration, upload the small set of files the assistant should read (the relevant `CONTEXT.md` and `CLAUDE.md`) rather than the entire repo.
- Use the `skills/` scripts only when you need repeatable automation; many tasks can be done interactively with Claude and the templates in `stages/`.

---

If you'd like, I can also:
- add a short script to gather and package the most important files for Claude input, or
- create a one-page starter checklist for the `02-market-research` stage.
