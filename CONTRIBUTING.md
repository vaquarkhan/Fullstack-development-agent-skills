# Contributing

Thank you for improving Fullstack Development Agent Skills.

## What to Contribute

- New or improved `SKILL.md` workflows with verification gates
- Presets, starter packs, references, tutorials, and examples
- Validation scripts and documentation fixes

## Skill Requirements

Follow `docs/skill-anatomy.md`. Every skill must include:

- YAML frontmatter (`name`, `description`)
- Use When, Workflow, Required Checks
- Decision Framework, Common Rationalizations And Rebuttals, Evidence Pack, Exit Criteria

## Validation

```bash
python scripts/validate-skills.py
python scripts/validate-assets.py
```

## Pull Request Checklist

- Skill folder name matches frontmatter `name`
- `skills-index.md` and `registry/assets.json` updated
- No secrets or environment-specific credentials in examples
