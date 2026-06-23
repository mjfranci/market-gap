# Stage 03: Problem Identification

Distill the market analysis into a concrete unsolved problem and opportunity brief. Apply the KT Decision Analysis and Potential Problem Analysis frameworks.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../02-market-research/output/market-analysis.md` | Full file | Market context to analyze for problems |
| Registry | `../../skills-registry.md` | Full file | Agent picks relevant skills |
| Skills | `../../skills/[name]/SKILL.md` | Per skill as needed | Domain knowledge and analytical frameworks |
| Reference | `../../shared/kepner-tregoe-reference.md` | KT Decision Analysis and Potential Problem Analysis sections | What to do / What could go wrong frameworks |
| Reference | `../../shared/web-tools-setup.md` | Full file | Web search and scraping for gap validation |

## Process

1. Read the market analysis from Stage 02 output
2. Load relevant skills from registry; load KT Decision Analysis and Potential Problem Analysis frameworks
3. Analyze What should we do: identify whitespace, underserved segments, and opportunity surface
4. Analyze What could go wrong: risk landscape, timing threats, structural barriers, assumption risks
5. Identify the single most compelling unsolved problem to capitalize upon
6. **[Checkpoint]** -- Present the selected problem and opportunity framing to the user
7. Run audit checks; revise if any fail
8. Write `output/problem-brief.md`

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 5 | Selected problem stated as a job-to-be-done, with opportunity surface and top risks | Whether this is the right problem, or redirect to a different candidate |

## Audit

| Check | Pass Condition |
|-------|---------------|
| KT coverage | Both What should we do and What could go wrong sections are present and substantive |
| Single problem focus | One primary unsolved problem is named, not a list of candidates |
| Opportunity framing | Problem is stated as a job-to-be-done with a named customer segment and barrier |
| Risk completeness | At least three distinct risks are identified with specific mechanisms |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Problem brief | `output/problem-brief.md` | Structured doc: opportunity surface, primary unsolved problem, risk landscape |
