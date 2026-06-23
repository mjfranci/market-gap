# Stage 04: Collaboration and Validation

Determine whether the identified problem is worth solving as a business venture through structured back-and-forth dialogue with the user.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../03-problem-identification/output/problem-brief.md` | Full file | The opportunity to validate |
| Registry | `../../skills-registry.md` | Full file | Agent checks for collaboration or validation framework skills |
| Skills | `../../skills/[name]/SKILL.md` | Per skill as needed | May define collaboration structure or business assessment frameworks |
| User | (conversation) | Ongoing dialogue | Human validation and steering |

## Process

1. Read the problem brief from Stage 03 output
2. Check registry for any skill defining a collaboration or validation framework; load if present
3. Interrogate the opportunity with the user across five dimensions: business model viability, founder fit, competitive moat, market timing, and resource requirements
4. Continue dialogue until a go/no-go position is reached with supporting reasoning
5. Run audit checks; revise if any fail
6. Write `output/validated-opportunity-brief.md`

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | Initial questions covering all five dimensions | Whether to answer, redirect, or add dimensions |
| 4 | Draft go/no-go position with reasoning | Whether the reasoning accurately reflects the dialogue |

## Audit

| Check | Pass Condition |
|-------|---------------|
| All dimensions covered | Business model, founder fit, moat, timing, and resources each have a stated position |
| Go/no-go stated | Brief contains a clear go or no-go conclusion, not a hedge |
| Reasoning grounded | Each position links to a specific point from the market analysis or dialogue |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Validated opportunity brief | `output/validated-opportunity-brief.md` | Revised problem brief with go/no-go, validation reasoning, and dimension-by-dimension assessment |
