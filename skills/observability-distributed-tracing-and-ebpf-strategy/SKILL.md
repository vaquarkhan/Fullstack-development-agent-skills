---
name: observability-distributed-tracing-and-ebpf-strategy
description: Build deep observability with traces, metrics, logs, and eBPF-assisted network visibility. Use when diagnosing latency storms, call-path failures, or opaque service interactions.
disable-model-invocation: true
---

# Observability Distributed Tracing And eBPF Strategy

## Use When

- Root cause analysis is slow in distributed systems
- Service mesh or network-layer behavior is hard to debug

## Workflow

1. Define trace propagation and correlation requirements.
2. Instrument critical paths with spans and semantic attributes.
3. Add RED/USE metrics and high-cardinality-safe labels.
4. Use eBPF-based telemetry for network and syscall visibility where supported.
5. Build SLO-linked dashboards and alerting runbooks.

## Required Checks

- Trace context survives all async and sync hops
- Alert noise is controlled with actionable thresholds
- Telemetry costs and retention policies are defined

## Decision Framework

- Propagate W3C trace context through every sync hop, async queue, and browser-initiated request.
- Instrument RED metrics per service and USE metrics per resource; cap label cardinality before production.
- Adopt eBPF for kernel/network visibility only where root cause spans logs and metrics cannot explain latency.
- Tie alerts to SLO burn rates and user journeys, not raw infrastructure thresholds.

## Common Rationalizations And Rebuttals

- "Logs are enough for debugging." -> Cross-service failures need span correlation; logs alone multiply MTTR.
- "Trace everything at max detail." -> Unsampled full fidelity blows cost and storage; sample with tail-based retention for errors.
- "eBPF replaces application instrumentation." -> eBPF sees network/kernel; business spans still need app-level attributes.

## Evidence Pack

- Trace propagation test across UI, API gateway, and downstream services
- Dashboard links for SLO-aligned RED/USE panels with on-call runbook mapping
- Sampling and retention policy with cost estimate
- eBPF deployment scope note (if used): what visibility gap it closes

## Exit Criteria

- Teams can isolate failure domains within minutes
- Observability supports both incident response and capacity planning
