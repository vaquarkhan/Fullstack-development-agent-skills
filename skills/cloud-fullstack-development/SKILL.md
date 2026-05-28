---
name: cloud-fullstack-development
description: Deliver cloud-ready fullstack systems across frontend and microservices with environment strategy, security, observability, and CI/CD controls. Use when users ask for AWS, Azure, or GCP fullstack architecture and deployment planning.
disable-model-invocation: true
---

# Cloud Fullstack Development

## Workflow

1. Define frontend, API, and data architecture for the target cloud.
2. Define environment boundaries (dev, staging, prod).
3. Implement identity, secrets, and network security controls.
4. Add observability and release automation.
5. Validate cost, reliability, and disaster recovery readiness.

## Required Checks

- Infrastructure-as-code plan exists
- Least-privilege access model is documented
- Service and UI telemetry are correlated
- Rollback and incident response paths are tested

## Decision Framework

- Start with clear scope and ownership boundaries.
- Prefer incremental, testable slices over broad rewrites.
- Define compatibility and rollback expectations before release.
- Require evidence for reliability and operability outcomes.

## Common Rationalizations And Rebuttals

- "We can fill gaps after merge." -> Critical gaps are harder and riskier to fix in production.
- "This change is too small for process." -> Small changes still need clear validation criteria.
- "Docs can wait." -> Missing context increases future delivery and incident cost.

## Evidence Pack

- Scope and acceptance criteria with owner
- Test or validation evidence for changed behavior
- Compatibility and rollback notes
- Operational visibility requirements for production impact

## Exit Criteria

- Workflow decisions are documented and implementation-ready
- Validation evidence exists for quality, reliability, and compatibility
- Operational readiness and rollback expectations are explicit

