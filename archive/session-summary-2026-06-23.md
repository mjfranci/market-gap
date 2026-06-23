# Session Summary — Market-Gap Discovery, 2026-06-23

**Workspace:** Market Research & Problem Discovery (Stages 02–05)
**Date:** 2026-06-23
**Founder profile:** Small technical team — mechanical + software + biomedical engineering + applied AI; hardware/embedded capability; originally specialized in active prosthetics/orthotics.
**Session shape:** A single Stage-02 run that opened into a brainstorm, then **four full concept iterations** through the Stage 02→05 pipeline, each archived. This document summarizes the arc, the decisions, the recurring crux, and the conclusion.

---

## 1. How the Session Unfolded (decision trail)

| Step | User steer | Result |
|------|-----------|--------|
| Start | "Run stage 02" → "no target, help me brainstorm" | Brainstormed candidate markets from consulting/industry signals. |
| Pivot 1 | "Don't focus on prosthetics" | Widened to non-P&O markets; chose **affordable benchtop lab automation for small/academic labs**. |
| Pipeline run A | (continue) | Stage 02 market analysis → Stage 03 problem (hardware abandonment / can't automate changing protocols) → Stage 04 GO, vertical = **NGS library prep** → Stage 05 council. |
| Pivot 2 | "Rerun, vertical = protein-ligand research" | Re-ran Stages 04–05 → vertical = **protein-ligand binding-assay prep**. |
| Pivot 3 | "Test an agentic workflow for protein-ligand research; lab integration comes after the loop is validated" | Re-framed to a **software-first agentic loop** (plan→simulate→surrogate→critique); re-ran Stages 03–05. |
| Pivot 4 | "Rerun with monetization completely de-valued — a completely open-source solution" | Re-ran Stages 04–05 under a **pure open-source lens**. |

Throughout, revenue was progressively de-weighted (nice-to-have → irrelevant), culminating in the open-source framing.

---

## 2. The Four Concepts Tested

| # | Concept | Stage 04 verdict | Stage 05 council outcome | Fatal/central issue |
|---|---------|------------------|--------------------------|---------------------|
| 1 | **NGS library-prep automation** on cheap benchtop hardware | Conditional GO | GO → ≤90-day probe | Cheap hardware is *blind* (no sensing); NGS too standardized for the "changing-protocol" thesis; founder wet-lab gap. |
| 2 | **Protein-ligand binding-assay prep** automation | Conditional GO | GO → ≤90-day probe; sharper | Reliability amplified (precious protein, tiny error budget, aggregation); the **measurement loop you don't own** is the critical path; "prep is the cheap step." |
| 3 | **Agentic in-silico loop** (commercial), hardware deferred | Conditional GO (de-risking) | GO → reframe to a **falsification kill-test** | A closed loop with no external truth proves **self-consistency, not correctness** (4/5 advisors converged); hyper-capitalized incumbents; deferring lab defers the moat. |
| 4 | **Agentic in-silico loop — FULLY OPEN-SOURCE** | **GO — strongest of the session** | GO, **benchmark-first** | Commercial risks dissolved; remaining: referee legitimacy, social cold-start, maintainer sustainability, partly-unsolved research. |

---

## 3. The Recurring Crux — and How Open-Source Resolved It

A single scientific problem shadowed every concept:

> **A system that grades its own outputs without external ground truth demonstrates internal consistency, not correctness.**

- In the **hardware** concepts (1, 2) it appeared as: cheap robots are *blind* to the failures that invalidate results (mis-transfer, protein aggregation), and you can't validate prep quality without an expensive measurement loop you don't own.
- In the **commercial agentic loop** (3) it appeared as: "validate the loop without wet-lab" only proves the components agree with each other; physics simulation is "just another model" that degrades out-of-distribution exactly where novel discovery lives.
- In the **open-source** framing (4) it **resolved**: the external experimental ground truth *already exists* in public databases (**BindingDB, ChEMBL, PDBbind**). A rigorous **OOD-calibration benchmark over real measured affinities** (target/scaffold/time splits) is a legitimate external test that needs **no wet lab for v1**. Removing the commercial pressure to own proprietary data is precisely what made the public-data path the obvious answer.

This is the session's central insight: **the open-source lens didn't just dodge the business risks — it dissolved the scientific blocker that defeated the other three concepts.**

---

## 4. The Conclusion (recommended direction)

**Build a completely open-source, experimentally-grounded benchmark/standard for protein-ligand prediction uncertainty — "does the model know when it's wrong?" — with an agentic plan→simulate→surrogate→critique loop as an optional reference implementation.**

Why it fits this founder:
- **Best founder-fit of the session:** Phase 1 is pure software/AI (the team's core); the "some lab access / partial wet-lab depth" gaps stop mattering.
- **Timing is rare:** open surrogates (Boltz-2 ≈ FEP, ~1000× faster) made capable loops buildable by small teams, *and* dedicated science-OSS funding arrived in 2026 (Open Source for Science Fund — Renaissance Philanthropy, $20M from Biohub + Wellcome; OS4LS; OpenBioSim).
- **The hardware edge becomes a public good:** a cheap *open* wet rig is the Phase-2 crowdsourced-truth flywheel no closed incumbent can replicate.

### The one thing to do first
Ship a tiny, rigorous, **experimentally-grounded OOD-calibration benchmark** this quarter: real measured affinities (BindingDB/ChEMBL/PDBbind), target/scaffold splits, metrics locked (ECE/NLL + selective-prediction accuracy-vs-coverage), and 3–4 baselines you run yourself (Boltz-2 confidence, an ensemble, a similarity-distance baseline). If the headline is *"open models are badly calibrated out-of-distribution,"* that result **is** the scientific contribution, the credibility, the community hook, and the grant application — all from one artifact.

### Watch-outs (from the council)
- **Score against experimental labels, not simulation** — the make-or-break design choice (else it's the old self-consistency trap in a costume).
- **Earn referee legitimacy via coalition** (RDKit UGM / Polaris / OpenBioSim); don't be both player and referee.
- **Cold-start is the real work** — seed by porting others' published models; secure ≥1 external submission within ~60 days.
- **Apply for science-OSS funding after first traction**, not before.
- **Maintainer sustainability** (OSS burnout crisis: 60% unpaid, 44% burnout) must be a day-one design constraint: permissive license, multi-maintainer governance.

---

## 5. Archive Index (this session)

| Concept | Archived report |
|---------|-----------------|
| NGS library-prep automation | `archive/benchtop-lab-automation-ngs-research-2026-06-23.md` |
| Protein-ligand binding-assay prep | `archive/protein-ligand-binding-automation-research-2026-06-23.md` |
| Agentic in-silico loop (commercial) | `archive/agentic-in-silico-protein-ligand-research-2026-06-23.md` |
| Agentic loop (open-source) — **selected direction** | `archive/agentic-protein-ligand-opensource-research-2026-06-23.md` |
| **This summary** | `archive/session-summary-2026-06-23.md` |

Each concept archive contains its full Stage 02 market analysis, Stage 03 problem brief, Stage 04 validated-opportunity brief, and Stage 05 stress-test report.

---

## 6. Notes for a Future Session
- **Market analysis (Stage 02)** stayed constant across all four concepts: *affordable benchtop lab automation for small & academic labs*. It remains the eventual Phase-2 integration market for the open-source direction (the open wet rig).
- The workspace stage outputs are currently **empty** (archived). A future session can start fresh, or resume the open-source direction by pulling `agentic-protein-ligand-opensource-research-2026-06-23.md` from the archive.
- The methodology that worked: iterate the **solution concept** through Stages 04–05 (validation + council) while holding the market/problem framing, archiving each pass. The 5-advisor council reliably surfaced the load-bearing flaw within one round.
