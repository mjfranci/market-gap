# Stage 05: QC Stress Test

Stress test the validated opportunity brief by spawning five independent sub-agents that examine the full context for blindspots.

The QC skill must be registered in `skills-registry.md` before this stage begins. If it is not present, stop and direct the user to Stage 01 to add it.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../04-collaboration-validation/output/validated-opportunity-brief.md` | Full file | Primary artifact to stress test |
| Prior context | `../03-problem-identification/output/problem-brief.md` | Full file | Original problem framing for comparison |
| Prior context | `../02-market-research/output/market-analysis.md` | Full file | Source market data for sub-agent grounding |
| QC skill | `../../skills/[qc-skill-name]/SKILL.md` | Full file | Examination framework and sub-agent brief |

## Process

1. Verify the QC skill is present in `skills/` and registered in `skills-registry.md`; if missing, stop and prompt user to add it via Stage 01
2. Load QC skill to extract the examination framework and sub-agent brief
3. Spawn 5 sub-agents, each given the full context (market analysis, problem brief, validated opportunity brief) and the QC skill framework
4. Each sub-agent independently surfaces blindspots and produces recommendations
5. Collect all sub-agent outputs; aggregate into `output/stress-test-report.md`

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Stress test report | `output/stress-test-report.md` | Aggregated blindspot analysis and recommendations from all five sub-agents |

## Post-Completion Steps

After writing `output/stress-test-report.md`, run the following steps in order:

### Step 1 — Archive offer

Ask the user:

> "Would you like to save an aggregate research report for this session? It will combine the market analysis, problem brief, validated opportunity brief, and stress test report into a single file in the `archive/` folder."

If **yes**:
1. Derive a filename from the market/topic (e.g. `archive/<topic-slug>-research-YYYY-MM-DD.md`) using today's date
2. Run the `combine_markdown_workspace` method in `skills/archive.py` using the derived filename
3. Confirm the filename path to the user

If **no**: skip to Step 2.

### Step 2 — Workspace reset offer

Ask the user:

> "Would you like to clear the workspace for a new session? This will erase the content of all stage 02–05 output files (the files will remain, just emptied)."

If **yes**:
1. Overwrite each of the following files with empty content (do not delete the files):
   - `stages/02-market-research/output/market-analysis.md`
   - `stages/03-problem-identification/output/problem-brief.md`
   - `stages/04-collaboration-validation/output/validated-opportunity-brief.md`
   - `stages/05-qc-stress-test/output/stress-test-report.md`
2. Confirm the workspace is cleared and ready for a new session

If **no**: leave all output files untouched and close out the stage.
