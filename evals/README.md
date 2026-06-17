# Skill Routing Evaluations

Lightweight benchmarks to verify agents pick the right skills and lifecycle commands for common fullstack scenarios.

## How To Run

```bash
python scripts/run-skill-routing-benchmark.py
```

Or manually:

1. Load `skills/using-fullstack-agent-skills/SKILL.md`.
2. For each scenario in `evals/skill-routing-benchmark.md`, ask the agent which skill(s) and command(s) it would use.
3. Score against expected routes; target **≥ 90%** match on critical paths.

## Scenarios Covered

- MVP greenfield delivery
- OAuth provider integration
- Zero-downtime database migration
- Serverless AWS delivery
- GDPR erasure request
- Production incident triage
- Spring Boot / Java stack implementation (skill pack routing)

## Evidence

Record agent responses and scoring in your team's QA tracker or PR checklist when changing skill names, pack paths, or command routes.
