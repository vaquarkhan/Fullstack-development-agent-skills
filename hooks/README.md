# Hooks

Optional pre-flight hooks for lifecycle guardrails.

- `session-start.sh` — load entry skill and starter pack context
- `spec-pre.sh` — enforce spec artifacts before build
- `validate-pre.sh` — enforce checklist evidence before ship
- `release-guard.sh` — block ship without rollback owner
