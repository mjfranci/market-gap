# Stage 01: Skills Onboarding

Register skills for the workspace to use. Return here any time to add more skills, including the QC skill required by Stage 05.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | (conversation) | Skill sources: file path, git repo URL, local folder, or description | What to register |

## Process

1. Ask the user which skills they want to register; accept any combination of source types
2. For each skill, handle the source type:
   - File path: copy files into `skills/[skill-name]/`
   - Git repo URL: clone into `skills/[skill-name]/`
   - Local folder: confirm contents, copy into `skills/[skill-name]/`
   - Conversation: collaboratively build skill files in `skills/[skill-name]/`
3. For each registered skill, append an entry to `skills-registry.md` with: name, trigger keyword, purpose, and source type
4. Present the completed registry to the user for confirmation
5. Remind the user: the QC skill required by Stage 05 can be added here at any time before Stage 05 runs

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Registered skills | `skills/` (workspace root) | One subfolder per skill |
| Skills registry | `skills-registry.md` (workspace root) | Table: name, trigger, purpose, source type |
| Onboarding log | `output/onboarding-log.md` | List of registered skills with registration date |
