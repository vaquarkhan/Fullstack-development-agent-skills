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

## Exit Criteria

- Teams can isolate failure domains within minutes
- Observability supports both incident response and capacity planning
