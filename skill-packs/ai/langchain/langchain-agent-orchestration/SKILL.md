---
name: langchain-agent-orchestration
description: Build LangChain/LangGraph agents with tool registries, memory checkpointers, structured outputs, and production guardrails. Use for Python backend AI orchestration beyond generic LLM integration skills.
disable-model-invocation: true
---

# LangChain Agent Orchestration

## Use When

- Implementing multi-step AI agents in Python with LangChain or LangGraph
- Wiring tools, memory, human-in-the-loop, and eval hooks
- Pairing with `skills/ai-llm-integration-in-fullstack-apps` for Python depth

## Workflow

1. Define tools with explicit schemas and docstrings — one capability per tool.
2. Choose graph (LangGraph) for branching; ReAct for simpler loops.
3. Set recursion_limit, timeouts, and max tokens on LLM calls.
4. Persist state with checkpointer (Redis/Postgres) for resumable sessions.
5. Log prompts, tool calls, and latencies with PII redaction.
6. Evaluate with golden datasets before prompt/tool changes ship.

## Required Checks

- No arbitrary code execution tools in production without sandbox
- Tool inputs validated; outputs truncated before re-prompting
- Human approval step for destructive or billing actions
- Fallback response when LLM or tool chain fails

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- LangGraph when flows have branches, retries, or human gates.
- Structured output (Pydantic) for machine-consumed responses.
- RAG retriever behind dedicated search tool — not raw DB in prompt.
- Separate dev/staging LLM keys and rate limits per tenant.

## Common Rationalizations And Rebuttals

- "More tools make agents smarter." -> Tool sprawl confuses routing; curate minimal set.
- "Unlimited recursion fixes hard tasks." -> Causes cost loops; cap steps and budget.
- "Prompt logging is enough observability." -> Trace tool latency and failure rates too.

## Evidence Pack

- Eval run scores on golden questions
- Trace with tool spans and redacted prompts
- Recursion/timeout test proving loop termination
- Human-in-the-loop audit for sensitive actions

## Exit Criteria

- Agent terminates within configured limits
- Tools are schema-safe and authorization-checked
- Observability and eval gates pass before production enablement
