---
name: terraform-fullstack-infrastructure-as-code
description: Manage fullstack cloud infrastructure with Terraform modules, environment promotion, drift detection, and safe rollout practices.
disable-model-invocation: true
---

# Terraform Fullstack Infrastructure As Code

## Use When

- Infrastructure managed across AWS, Azure, or GCP
- Teams need repeatable environment provisioning

## Workflow

1. Model environments with clear variable contracts
2. Use modules for network, compute, data, and observability
3. Enforce plan/apply gates in CI/CD
4. Define state backend locking and access controls
5. Document destroy and rollback implications

## Required Checks

- Terraform plans reviewed before apply
- Secrets not stored in state plaintext
- Drift detection scheduled or enforced
- Blast radius limited per module boundary

## Decision Framework

- Keep modules small and composable
- Pin provider versions for reproducibility
- Separate state per environment or domain
- Run policy checks (OPA/Sentinel/Checkov) in pipeline

## Common Rationalizations And Rebuttals

- "ClickOps is faster." -> Drift and audit gaps accumulate.
- "One giant module is easier." -> Changes become risky and slow.
- "Apply without plan review." -> Production incidents become likely.

## Evidence Pack

- Plan output attached to change request
- Policy check pass evidence
- Rollback or destroy-safe notes for data resources
- Post-apply smoke test results

## Exit Criteria

- Infrastructure changes are auditable and reversible
- Environments stay consistent across teams
