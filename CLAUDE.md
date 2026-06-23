# Market Research and Problem Discovery

This workspace guides an entrepreneur through researching a target market, identifying an unsolved problem, validating the business opportunity, and stress-testing the conclusion.

## Folder Map

```
market-research-problem-discovery/
├── CLAUDE.md                           (you are here)
├── CONTEXT.md                          (task routing)
├── skills-registry.md                  (index of all registered skills)
├── skills/                             (one subfolder per registered skill)
├── shared/
│   ├── kepner-tregoe-reference.md      (KT framework guide for agents)
│   └── web-tools-setup.md              (web search and scraping configuration)
├── setup/
│   └── questionnaire.md               (onboarding -- run once)
└── stages/
    ├── 01-skills-onboarding/           (register skills)
    ├── 02-market-research/             (research the target market)
    ├── 03-problem-identification/      (identify the unsolved problem)
    ├── 04-collaboration-validation/    (validate the business opportunity)
    └── 05-qc-stress-test/              (stress test with 5 sub-agents)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run onboarding -- register skills and configure the workspace |
| `status` | Show pipeline completion for all five stages |

## Routing

| Task | Go To |
|------|-------|
| Register or add skills | `stages/01-skills-onboarding/CONTEXT.md` |
| Research a target market | `stages/02-market-research/CONTEXT.md` |
| Identify an unsolved problem | `stages/03-problem-identification/CONTEXT.md` |
| Validate the business opportunity | `stages/04-collaboration-validation/CONTEXT.md` |
| Stress test the conclusion | `stages/05-qc-stress-test/CONTEXT.md` |

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| Register skills | `stages/01-skills-onboarding/CONTEXT.md` | All other stages |
| Research market | `stages/02-market-research/CONTEXT.md`, `shared/kepner-tregoe-reference.md` (Situational Appraisal section), `skills-registry.md` | Stages 03-05 |
| Identify problem | `stages/03-problem-identification/CONTEXT.md`, `stages/02-market-research/output/market-analysis.md`, `shared/kepner-tregoe-reference.md` (Decision Analysis and Potential Problem Analysis sections), `skills-registry.md` | Stages 04-05 |
| Validate opportunity | `stages/04-collaboration-validation/CONTEXT.md`, `stages/03-problem-identification/output/problem-brief.md`, `skills-registry.md` | Stages 02-03, stage 05 |
| Stress test | `stages/05-qc-stress-test/CONTEXT.md`, `stages/04-collaboration-validation/output/validated-opportunity-brief.md`, `stages/03-problem-identification/output/problem-brief.md`, `stages/02-market-research/output/market-analysis.md`, QC skill SKILL.md | All other skills |
