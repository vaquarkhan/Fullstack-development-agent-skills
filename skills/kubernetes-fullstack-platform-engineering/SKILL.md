---
name: kubernetes-fullstack-platform-engineering
description: Operate fullstack workloads on Kubernetes with ingress, service mesh options, autoscaling, secrets, and GitOps delivery.
disable-model-invocation: true
---

# Kubernetes Fullstack Platform Engineering

## Use When

- Teams standardize on Kubernetes for UI and API workloads
- Need platform-level reliability and release controls

## Workflow

1. Define namespace, network, and identity boundaries
2. Configure ingress, TLS, and gateway policies
3. Set HPA/VPA and resource requests/limits
4. Implement GitOps or progressive delivery
5. Validate observability and incident runbooks

## Required Checks

- Readiness probes reflect dependency health
- Secrets are not baked into images
- Pod security standards enforced
- Rollback tested for deployment and config changes

## Decision Framework

- Separate platform concerns from application domain logic
- Use GitOps for auditable promotion across environments
- Limit blast radius with namespaces and network policies
- Define SLOs per critical user journey

## Common Rationalizations And Rebuttals

- "kubectl apply in prod is fine." -> Untracked drift and failed rollbacks follow.
- "One cluster for everything reduces cost." -> Noisy neighbor and security isolation suffer.
- "Liveness equals readiness." -> Traffic may route to unprepared pods.

## Evidence Pack

- GitOps promotion evidence
- Load test and autoscaling behavior report
- Ingress and TLS validation output
- Rollback drill record

## Exit Criteria

- Platform supports safe fullstack releases
- Teams can operate incidents with clear runbooks
