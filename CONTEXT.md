# Market Research and Problem Discovery

## Task Routing

| Task | Stage |
|------|-------|
| Register or add skills | `stages/01-skills-onboarding/CONTEXT.md` |
| Research a target market | `stages/02-market-research/CONTEXT.md` |
| Identify an unsolved problem | `stages/03-problem-identification/CONTEXT.md` |
| Validate the business opportunity | `stages/04-collaboration-validation/CONTEXT.md` |
| Stress test the conclusion | `stages/05-qc-stress-test/CONTEXT.md` |

## Shared Resources

| Resource | Location | Used By |
|----------|----------|---------|
| Skills registry | `skills-registry.md` | All stages |
| All skills | `skills/` | All stages (each stage picks relevant skills) |
| KT framework | `shared/kepner-tregoe-reference.md` | Stages 02, 03 |
| Web tools setup | `shared/web-tools-setup.md` | Stages 02, 03 |
| Research sources | `shared/research-sources.md` | Stage 02 |

---

## Persistent Context

### User Profile

Background: mechanical engineering, software engineering, and biomedical engineering — plus working knowledge of AI and specialized in active prosthetics/orthotics. Small team.

Industry: healthcare and biomedical engineering (where the user works — not necessarily the research target). Do not assume this is the target market; ask fresh each session.

- Solutions involving hardware/device design, embedded software, medical device development, and AI integration are all in play
- Avoid recommendations requiring large teams, deep sales organizations, or regulatory-heavy clinical trials without flagging the constraint
- Favor tooling, software, or instrumentation plays that a small technical team can build and ship
- AI-augmented medical/biomedical tools are a strong fit given the skill stack

### Behavioral Rules

- **Archive folder:** Never read, reference, or load any files from `archive/` unless the user explicitly asks. Skip archive paths when exploring the workspace; ask before loading archive content.
- **Research sources:** At the start of each Stage 02 session, load `shared/research-sources.md` and ask the user whether they want to draw from the listed consulting firm sources (McKinsey, BCG, Bain, Deloitte, PwC, KPMG, EY, Accenture, Roland Berger, Capgemini). Never silently use or skip them.

### Current Project State

**SESSION CLOSED (2026-06-23):** Four concepts tested and archived; workspace stage outputs (02–05) are currently EMPTY (archived). Session summary at `archive/session-summary-2026-06-23.md`. **Selected direction:** a fully open-source, experimentally-grounded benchmark for protein-ligand prediction uncertainty ("does the model know when it's wrong?"), with an agentic plan→simulate→surrogate→critique loop as a reference implementation; first artifact = an OOD-calibration benchmark over public affinity data (BindingDB/ChEMBL/PDBbind) — no wet lab needed for v1. To resume, pull `agentic-protein-ligand-opensource-research-2026-06-23.md` from archive.

**Aggregate archives:** `archive/benchtop-lab-automation-ngs-research-2026-06-23.md` (NGS physical-lab run), `archive/protein-ligand-binding-automation-research-2026-06-23.md` (protein-ligand physical-lab run), and `archive/agentic-in-silico-protein-ligand-research-2026-06-23.md` (agentic loop, commercial framing). The active outputs now hold the FOURTH concept: a FULLY OPEN-SOURCE agentic protein-ligand workflow (monetization completely de-valued).

**ACTIVE CONCEPT (2026-06-23, 4th iteration — OPEN SOURCE):** Same agentic plan→simulate→surrogate→critique loop, but as a COMPLETELY OPEN-SOURCE project with monetization entirely out of scope; success = scientific validity, adoption, community, maintainer sustainability, impact for underserved academic/small labs. Council verdict: **GO — strongest framing of the entire session, executed as an experimentally-grounded BENCHMARK/STANDARD first, not a framework.** KEY SYNTHESIS: removing monetization dissolved the commercial risks (out-capitalizing AWS/Schrödinger, moat, commoditization) AND surfaced the resolution to the scientific crux that killed all 3 prior framings — the external experimental ground truth ALREADY EXISTS in public databases (BindingDB/ChEMBL/PDBbind); a rigorous OOD-calibration benchmark over real measured affinities (target/scaffold/time splits) needs NO wet lab for v1. Plan: (a) ship a tiny experimentally-grounded OOD-calibration benchmark first (metrics ECE/NLL + selective-prediction; 3-4 baselines incl. Boltz-2 confidence; headline = "open models are badly calibrated OOD"); (b) agentic loop = optional reference implementation; (c) earn referee legitimacy via COALITION (RDKit UGM/Polaris/OpenBioSim), don't self-compete on your own leaderboard; (d) apply to Open Source for Science Fund / OS4LS AFTER first traction (baseline + ≥1 external submission); (e) cheap OPEN wet rig = Phase-2 community crowdsourced-truth flywheel (team's hardware edge → public good). Top risks: referee legitimacy (earned not declared), social cold-start (a leaderboard with only your entries is a tombstone), maintainer burnout (OSS crisis: 60% unpaid/44% burnout), and the core calibration claim being partly unsolved research (but publishing the negative result is itself valuable). THE ONE THING FIRST: ship the experimentally-grounded OOD-calibration benchmark this quarter — it's the kill-test, the public good, the credibility play, and the grant application in one artifact.

--- superseded agentic commercial run (archived) ---

**Target market (active):** Affordable benchtop lab automation for small & academic labs — global market, no geographic scope constraint set. (Pivoted 2026-06-23: user reset the brainstorm and explicitly moved off prosthetics/orthotics.)

**Stage 02 status:** Complete (2026-06-23). Market analysis written to `stages/02-market-research/output/market-analysis.md`. KT Situational Appraisal covering market size/growth, key players (Hamilton, Tecan, Beckman, SPT Labtech, Opentrons, Trilobio, open-source/DIY), business models, segments, personas, trends (SLAS 2026), and structural drivers (funding mismatch, lab-workforce crisis, reproducibility crisis, commoditized AI/motion). Core thesis: a "barbell" market with an underserved affordable/low-end benchtop tier; strong solver-fit (hardware + embedded + software + AI, no human-FDA path).

**Stage 03 status:** Complete (2026-06-23). Problem brief written to `stages/03-problem-identification/output/problem-brief.md`. Locked problem (JTBD): small academic + seed/Series-A biotech labs that already own affordable benchtop automation (Opentrons-class, ~$10k) cannot reliably automate and continuously adapt their own frequently-changing protocols without scripting/automation expertise, so they underutilize or abandon the hardware. Selected opportunity = the AI-assisted "authoring + adaptive execution" layer (NOT another lab OS). Top risks: AI-native co-option by incumbents, reliability/trust chasm (wasted reagents → reversion to manual), hardware-fragmentation tax, academic willingness-to-pay ceiling, and the "build another lab OS" trap. Stage 04 validation targets: size the abandonment cohort + who pays (academia vs biotech); define the reliability bar for trust.

**ACTIVE CONCEPT (2026-06-23, 3rd iteration):** An **agentic in-silico workflow for protein-ligand research** — a software loop of plan→simulate→surrogate→critique, with lab/equipment integration DEFERRED until the loop is validated. Stages 03–05 outputs now reflect THIS concept (Stage 02 market analysis retained as the eventual Phase-2 integration market). Council verdict: **GO, but Phase 1 reframed from "validate the loop" to a FALSIFICATION kill-test** — a closed loop with no external oracle proves only self-consistency, not correctness (4 of 5 advisors converged), and the critique/uncertainty differentiator is structurally unmeasurable without ground truth. Corrections: (a) run the kill-test first (~1 month, no wet-lab): does predicted uncertainty inflate appropriately on held-out chemotypes AND generalize across protein families? If not, the concept dies cheaply; (b) bring the smallest external truth oracle FORWARD — self-consistency is not validation; since the team builds hardware, a cheap truth/wet rig is the near-term MOAT, not a deferred afterthought (premise inversion); (c) make calibration-that-generalizes the product (not orchestration, not raw prediction); (d) honest altitude: not a standalone business vs AWS/Google/Schrödinger/Recursion, but the best founder-fit concept tested. Beware mistaking memorization for calibration (public labels share surrogate training distribution). Best founder-fit of the session (pure software/AI in Phase 1; the "some access / partial wet-lab depth" gaps stop mattering).

--- superseded protein-ligand physical-lab run (archived) ---

**Stage 04 status:** Complete (2026-06-23, rerun). Vertical RE-RUN from NGS library prep → **protein-ligand binding research** per user request. Validated opportunity brief at `stages/04-collaboration-validation/output/validated-opportunity-brief.md`. Verdict: **GO (conditional)**, scoped to protein-ligand binding-assay prep & screening (dose-response serial dilutions for Kd, fragment/compound handling, plate setup feeding SPR/ITC/MST/DSF/anisotropy readers). Rationale vs NGS: better fits the "changing-protocol" thesis (binding assays are bespoke, not kit-standardized) and reliability is worth more (precious protein, tiny error budget). Founder direction: revenue de-weighted. Dialogue answers carried: access="some", depth="partial/would partner", resources=full-time ~12-mo. GO conditions: (1) design partner(s) with real protein + a measurement instrument; (2) protein-biophysics domain co-founder/advisor (more critical here); (3) retire the reliability bar first; (4) scope discipline.

**Stage 05 status:** Complete (2026-06-23, rerun). Stress-test report (llm-council, 5 advisors + chairman) at `stages/05-qc-stress-test/output/stress-test-report.md`. Verdict: **GO survives, but sharper downgrade than NGS — a ≤90-day feasibility probe, higher execution risk + higher upside.** Mandatory reframe: (a) product = a TRUSTWORTHY-RESULT / REPRODUCIBILITY-QC layer, not "prep automation" (prep is the cheap step; value is belief in the Kd, gated by protein quality + interpretation); (b) moat = a LOW-COST OPTICAL SENSING module that detects protein AGGREGATION/turbidity + verifies transfers — the chairman's blindspot: aggregation is optically detectable and the team builds hardware, so the Contrarian's "blind hardware" fatal flaw and the moat are the SAME component; (c) the binding-affinity corpus is the long-term asset (clean experimental affinities the AI drug-discovery world can't buy). Critical path = the measurement loop the team does NOT own. THE ONE THING FIRST: before buying a robot or coding, secure ONE partner giving BOTH purified protein AND measurement-instrument time (start with DSF) and close the round-trip once: automated dilution series → measured → does Kd match hand-pipetting within error? If no partner-with-instrument in ~60 days → no-go. Pipeline (Stages 02–05) complete for the active target (protein-ligand vertical).

**Prior pipeline (superseded):** An earlier session pursued Prosthetics & orthotics through Stages 02–04 (Verdict: GO). That thesis is stale after the 2026-06-23 pivot and should not be reused unless the user reverts the target.

