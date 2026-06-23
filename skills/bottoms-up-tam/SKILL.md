---
name: bottoms-up-tam
description: Builds a defensible bottoms-up Total Addressable Market model by counting real target units, filtering to the ICP, multiplying by ACV, and layering SAM/SOM. Use when sizing a market before a go/no-go or investment decision.
triggers: TAM analysis, market size, total addressable market, how big is the market, SAM SOM
allowed-tools: WebSearch, WebFetch, Bash
---

# Bottoms-Up TAM Analysis

## What This Skill Does

Produces a three-layer market size estimate (TAM → SAM → SOM) anchored in real unit counts rather than top-down industry revenue percentages. Bottoms-up TAM is more defensible because every number traces to a countable thing: firms, seats, or transactions.

## When to Use This vs. Top-Down

| Approach | Use When | Risk |
|----------|----------|------|
| **Bottoms-up** (this skill) | You know your ICP, price, and conversion assumptions | Numbers are only as good as your ICP filter |
| Top-down | You need a quick sanity check or macro framing | Easy to over-inflate with "1% of a $10B market" logic |

Always run both and triangulate. If they agree within 2×, you have a credible range.

---

## Process

### Step 1 — Define the ICP (Ideal Customer Profile)

Before counting anything, write down:
- **Segment:** Who exactly is the buyer? (industry, firm size, role, geography)
- **Qualifier:** What behavioral or structural filter determines they have the pain? (e.g., "does monthly close work for 10–50 clients")
- **Excluder:** Who looks similar but is NOT the buyer? (explicitly name them)

Precision here determines accuracy of everything downstream.

---

### Step 2 — Find the Universe Count

Find the total number of entities that match the segment definition (before qualifiers). Use the most authoritative source available, in order of preference:

| Source | What It Provides |
|--------|-----------------|
| US Census County Business Patterns (CBP) | Establishment counts by NAICS code, employee size band, geography |
| US Census Statistics of US Businesses (SUSB) | Firm counts by NAICS + firm size (employees/revenue) |
| BLS Occupational Employment Statistics (OES) | Worker counts by occupation (proxy for firm count when divided by avg firm size) |
| IBISWorld | Industry-level firm counts and market size (paywalled; use Google snippet) |
| Trade association membership numbers | Direct count of practitioners, often more precise than NAICS |
| Platform partner networks | e.g., QuickBooks ProAdvisor count as proxy for bookkeeping practices |

**Search templates:**
```
site:census.gov "NAICS [code]" county business patterns [year]
IBISWorld "[industry name]" "number of businesses" [year]
"[trade association name]" membership statistics [year]
```

---

### Step 3 — Apply ICP Filters

Sequentially filter the universe to the addressable segment. Document each filter step:

```
Universe:          [N] total [entity type] in [geography]
Filter 1 (size):   × [%] = [N] [why this % — data source]
Filter 2 (model):  × [%] = [N] [why this % — data source or reasoned estimate]
Filter 3 (other):  × [%] = [N] [why this % — data source or reasoned estimate]
ICP count:         [N] target units
```

For each filter, cite a data source or label it as a "reasoned estimate" and explain the reasoning. Never silently apply a filter.

---

### Step 4 — Calculate ACV (Annual Contract Value)

```
Price low:   $[X]/mo × 12 = $[X]/year
Price mid:   $[X]/mo × 12 = $[X]/year  ← use this as the base case
Price high:  $[X]/mo × 12 = $[X]/year
```

If pricing is not yet decided, use competitive pricing (from market analysis) as the reference.

---

### Step 5 — Compute TAM

```
TAM (strict ICP) = ICP count × ACV (mid)
TAM (broad)      = Universe after filter 1 only × ACV (mid)
```

Report both. Strict TAM is for internal planning; broad TAM is for investor/partner conversations.

---

### Step 6 — Compute SAM (Serviceable Addressable Market)

SAM filters TAM to units actually reachable through your planned go-to-market (GTM) channels.

**Inputs needed:**
- GTM channels (e.g., community, paid search, outbound, partnerships)
- Estimated reach of each channel into the ICP (% of ICP that participates in/is reachable by each channel)

```
SAM = TAM × [% of ICP reachable via your specific GTM channels]
```

Be honest about channel constraints. A community-led, self-serve GTM typically reaches 25–40% of an ICP. Enterprise sales with direct outbound can reach 60–80%.

---

### Step 7 — Compute SOM (Serviceable Obtainable Market)

SOM is your realistic capture over a defined time horizon, given team size, capital, and competitive dynamics.

```
Year 1 SOM = SAM × [penetration rate, Year 1]   → typically 0.5–2%
Year 2 SOM = SAM × [penetration rate, Year 2]   → typically 2–5%
Year 3 SOM = SAM × [penetration rate, Year 3]   → typically 5–10%
```

Express as both a customer count and ARR figure. Include the MRR milestone checkpoints that matter to the team.

---

### Step 8 — Identify Forcing Functions and Timing Spikes

Note any time-limited events that expand the near-term TAM or accelerate decision-making:

- Platform migrations (e.g., QuickBooks Desktop sunset)
- Regulatory deadlines
- Technology disruptions (e.g., AI replacing a prior workflow)
- Competitor discontinuations

Quantify each forcing function: how many target units does it affect, and over what window?

---

### Step 9 — Sanity Checks

Before finalizing, run these:

| Check | Method |
|-------|--------|
| Top-down cross-check | Find industry total revenue; divide by estimated ARPU; compare to your ICP count |
| Comparables check | Find a similar product in an adjacent market; their disclosed customer count ÷ their claimed TAM = implicit penetration rate to compare against your SOM |
| Revenue model check | Does SOM Year 3 produce a revenue figure consistent with the team size and business model? A 2-person self-serve team at $65/mo should not project $50M ARR in 3 years |

---

## Output Template

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOTTOMS-UP TAM — [Market Name]
Date: [YYYY-MM-DD]  |  Geography: [US / Global / other]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ICP DEFINITION
  Segment:    [who]
  Qualifier:  [behavioral/structural filter]
  Excluder:   [who looks similar but is out]

UNIT FUNNEL
  Universe:        [N] — [source]
  After filter 1:  [N] ([%]) — [filter name, source]
  After filter 2:  [N] ([%]) — [filter name, source]
  ICP count:       [N] target units

ACV
  Low / Mid / High: $[X] / $[X] / $[X] per year

TAM
  Strict ICP:  [N units] × $[ACV mid] = $[X]M
  Broad:       [N units] × $[ACV mid] = $[X]M

SAM
  GTM channels: [list]
  Reach %:      [%] of ICP
  SAM:          [N units] × $[ACV mid] = $[X]M

SOM
  Year 1: [N customers] × $[ACV mid] = $[X] ARR  ($[X]K MRR)
  Year 2: [N customers] × $[ACV mid] = $[X] ARR  ($[X]K MRR)
  Year 3: [N customers] × $[ACV mid] = $[X] ARR  ($[X]K MRR)

MRR MILESTONES
  $10K MRR:  [N customers] — [estimated timeline]
  $50K MRR:  [N customers] — [estimated timeline]
  $100K MRR: [N customers] — [estimated timeline]

FORCING FUNCTIONS
  [Event]: affects [N] units over [window]

SANITY CHECKS
  Top-down cross-check:  [result]
  Comparables check:     [result]
  Revenue model check:   [result]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Data Sources Quick Reference

| Source | URL | Best For |
|--------|-----|----------|
| US Census County Business Patterns | census.gov/programs-surveys/cbp.html | Establishment counts by NAICS + location |
| US Census SUSB | census.gov/programs-surveys/susb.html | Firm size distribution by NAICS |
| BLS OES | bls.gov/oes | Occupation headcounts |
| IBISWorld | ibisworld.com | Industry business counts (snippet via Google) |
| Statista | statista.com | Market stats (snippet via Google) |
| Trade association sites | varies | Direct member/practitioner counts |
| SBA size standards | sba.gov/document/support-table-size-standards | Official small business thresholds by NAICS |

---

## Common Mistakes

- **Skipping the excluder** — defining a segment without saying who is out leads to over-counting
- **Applying a single round-number filter** — "50% of the market" with no sourcing is a red flag; trace every filter to data or label it explicitly as a reasoned estimate
- **Confusing TAM with SAM** — TAM is theoretical; SAM is constrained by your GTM. Don't present SAM as TAM.
- **Ignoring ARR consistency** — if SOM Year 3 is $50M but you're a 2-person self-serve team at $65/month, the math requires 64,000 customers; that is not obtainable in 3 years
- **Not cross-checking top-down** — if IBISWorld says the industry is $1B and your TAM is $900M, you're claiming 90% share before you've launched
