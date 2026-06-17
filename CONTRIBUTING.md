# Contributing

Thank you for improving Fullstack Development Agent Skills.

## What to Contribute

- New or improved `SKILL.md` workflows with verification gates
- Skill packs under `skill-packs/` (stack-specific playbooks with examples)
- Presets, starter packs, references, tutorials, and architecture blueprints
- Validation scripts and documentation fixes

## Skill Requirements

Follow `docs/skill-anatomy.md`. Every skill must include:

- YAML frontmatter (`name`, `description`)
- Use When, Workflow, Required Checks
- Decision Framework, Common Rationalizations And Rebuttals, Evidence Pack, Exit Criteria
- Skill packs: `## Examples And Templates` plus `examples/` and `templates/` folders

## Adding Core vs Pack Skills

| Type | Location | When |
| --- | --- | --- |
| Core | `skills/<name>/` | Cross-stack workflow (auth, ship, observability) |
| Pack | `skill-packs/<lang>/<framework>/<name>/` | Framework-specific implementation |

## Validation

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
python scripts/validate-assets.py
python scripts/validate-version-sync.py
python scripts/validate-reference-provenance.py
python scripts/run-skill-routing-benchmark.py
```

## Pull Request Checklist

- Skill folder name matches frontmatter `name`
- `skills-index.md` and `registry/assets.json` updated (`sync-skills-index.py`, `sync-registry.py`)
- Skill packs include examples and templates where applicable
- No secrets or environment-specific credentials in examples
- Routing benchmark passes if skill names or lifecycle paths changed
