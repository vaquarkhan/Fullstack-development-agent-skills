# Skill Anatomy For This Repository

This guide defines how skills in this repository should be written so they stay useful, compact, and clearly original to this project.

## Design Principles

- Workflow over theory: instructions must drive execution steps
- Verification before merge: every skill must define evidence
- Progressive disclosure: keep `SKILL.md` focused and link deep detail files
- Fullstack alignment: include both UI and backend considerations when relevant

## Required Structure

Every skill must contain:

1. YAML frontmatter
2. `#` title matching the skill intent
3. `## Use When`
4. `## Workflow`
5. `## Required Checks`
6. `## Exit Criteria`

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
- Trigger condition 2

## Workflow
1. Step one
2. Step two

## Required Checks
- Check one
- Check two

## Exit Criteria
- Outcome one
- Outcome two
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

## Quality Gate For New Skills

- Description includes both capability and trigger
- Workflow is concrete and ordered
- Checks are testable in CI or review
- Exit criteria are measurable and not subjective
