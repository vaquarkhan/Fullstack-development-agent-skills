---
name: java-agent-core
description: Design and implement AI agent cores in Java/Spring Boot with tool registries, memory, orchestration, and safe execution boundaries. Use when building autonomous agents, multi-step workflows, or agent-as-a-service on the JVM.
disable-model-invocation: true
---

# Java Agent Core

## Use When

- Building autonomous or semi-autonomous agents on Spring Boot
- Orchestrating multi-step LLM workflows with tools, memory, and guardrails
- Exposing agent capabilities via REST, messaging, or MCP

## Workflow

1. Define agent goals, tool catalog, and memory scope (session vs user vs tenant).
2. Choose orchestration style: single ChatClient loop, state machine, or workflow engine.
3. Register tools with typed inputs/outputs; enforce idempotency on side-effecting tools.
4. Add guardrails: max iterations, token budget, timeout, human-in-the-loop checkpoints.
5. Instrument traces, token usage, and tool-call audit logs per request.
6. Validate with replay tests and adversarial prompt cases.

## Required Checks

- Tool handlers are idempotent or explicitly documented as non-idempotent
- Secrets and API keys loaded from environment/vault — never hardcoded
- Agent loop has max-iteration and timeout bounds
- Side-effecting tools require authorization and audit logging
- Memory scoped per user/session with explicit retention policy

## Decision Framework

- Prefer Spring AI ChatClient + advisors for LLM calls; MCP for external tool protocol.
- Keep tool implementations thin — delegate business logic to @Service layer.
- Use structured output (.entity()) for machine-parseable agent decisions.
- Separate planning from execution when financial, auth, or data-deletion tools are involved.

## Common Rationalizations And Rebuttals

- "One big prompt handles everything." -> Unbounded prompts drift; use tool registry and structured steps.
- "Agents can call repositories directly." -> Tools must go through services with auth and transaction boundaries.
- "Memory can be global." -> Cross-user memory leaks data; scope memory with conversationId per principal.

## Evidence Pack

- Agent architecture diagram: orchestrator, tools, memory, guardrails
- Tool catalog with input schema, auth requirements, and idempotency notes
- Token/latency metrics and sample trace for a multi-step run
- Adversarial test results (prompt injection, tool misuse attempts)

## Exit Criteria

- Agent completes defined workflows within iteration and token budgets
- Tool calls are auditable and authorization-checked
- Failure modes degrade safely without unbounded loops or silent errors
