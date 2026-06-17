# Skill Anatomy For This Repository

How skills in this repository should be written — useful, compact, and original.

## Design Principles

- Workflow over theory: instructions must drive execution steps
- Verification before merge: every skill must define evidence
- Progressive disclosure: keep `SKILL.md` focused and link deep detail files
- Fullstack alignment: include both UI and backend considerations when relevant
- Stack depth in packs: cross-stack patterns live in `skills/`; framework playbooks in `skill-packs/`

## Where Skills Live

| Location | Count | Scope |
| --- | --- | --- |
| `skills/<name>/SKILL.md` | 72 | Cross-stack workflows |
| `skill-packs/<lang>/<framework>/<name>/SKILL.md` | 45 | Stack-specific implementation |

Skill packs should include:

- `examples/` — good vs bad code patterns
- `templates/` — starter files for agents to copy

## Required Structure

Every skill must contain:

1. YAML frontmatter (`name`, `description`)
2. `#` title matching the skill intent
3. `## Use When`
4. `## Workflow`
5. `## Required Checks`
6. `## Decision Framework`
7. `## Common Rationalizations And Rebuttals`
8. `## Evidence Pack`
9. `## Exit Criteria`

Skill packs should also include:

10. `## Examples And Templates` — links to `examples/` and `templates/`

Use this skeleton:

```markdown
---
name: my-skill-name
description: Explain what the skill does and when to use it.
disable-model-invocation: true
---

# My Skill Name

## Use When
- Trigger condition 1

## Workflow
1. Step one

## Required Checks
- Check one

## Decision Framework
- Option A vs B

## Common Rationalizations And Rebuttals
- "We can skip tests" → rebuttal

## Evidence Pack
- Artifact one

## Exit Criteria
- Outcome one

## Examples And Templates
- `examples/good/` and `examples/bad/` (skill packs only)
```

## Naming And Scope Rules

- `name` uses lowercase hyphen-separated format
- Directory name and frontmatter `name` must match
- Keep one skill focused on one workflow outcome
- Move deep references to `references/` when the body gets long

## Originality Rules

- Do not clone section names word-for-word from external packs
- Use repo-specific examples (fullstack UI + backend lifecycle)
- Include at least one project-specific check per skill
- Keep language practical and implementation-oriented
- Imported packs (e.g. Spring Boot) must include `## Examples And Templates`

## Quality Gate For New Skills

- Description includes both capability and trigger (≤ 1024 chars)
- Workflow is concrete and ordered
- Checks are testable in CI or review
- Exit criteria are measurable and not subjective
- Body length meets validator minimums (`scripts/validate-skills.py`)
- No duplicate headings within a skill

## Validation

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
python scripts/validate-assets.py
```

After adding or renaming skills:

```bash
python scripts/sync-skills-index.py
python scripts/sync-registry.py
```
