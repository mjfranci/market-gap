# Stage 02: Market Research

Research the target market using registered skills and web tools. Apply the KT Situational Appraisal framework to produce a structured market analysis.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | (conversation) | Target market and any scope constraints | Defines what to research |
| Registry | `../../skills-registry.md` | Full file | Agent picks relevant skills |
| Skills | `../../skills/[name]/SKILL.md` | Per skill as needed | Domain knowledge and research methods |
| Reference | `../../shared/kepner-tregoe-reference.md` | KT Situational Appraisal section | What/Why analysis framework |
| Reference | `../../shared/web-tools-setup.md` | Full file | Web search and scraping configuration |

## Process

1. Ask user for the target market and any scope constraints. Also ask: (a) whether they want you to read URLs stored in the shared resources, and (b) how many articles to read from each URL.
2. Load relevant skills from registry for identify trends, industry trend analysis, social media trends, forecast, customer segmentation, customer personas; load KT Situational Appraisal framework
3. If the user wants to read URLs from memory: read the memory file, fetch the specified number of articles from each URL, and synthesize findings — before doing any other research. Then continue with: market overview, size, growth, key players, identify trends, industry trend analysis, social media trends, forecast, customer segmentation, customer personas
4. Research Why did it happen: root causes, structural drivers, behavioral and technology shifts
5. Run audit checks; revise if any fail
6. Write `output/market-analysis.md`

## Audit

| Check | Pass Condition |
|-------|---------------|
| KT coverage | Both What is happening and Why did it happen sections are present and substantive |
| Evidence grounding | Every major claim cites a data point, source, or observable signal |
| Scope alignment | Analysis stays within the market the user specified |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Market analysis | `output/market-analysis.md` | Structured KT Situational Appraisal: What, Why, key players, trends, structural drivers |
