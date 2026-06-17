---
name: spring-webflux-reactive
description: Build reactive Spring WebFlux APIs with non-blocking I/O, backpressure-aware streams, and Project Reactor. Use for high-concurrency Java services without virtual-thread blocking models.
disable-model-invocation: true
---

# Spring WebFlux Reactive

## Use When

- Building non-blocking REST or SSE APIs with Spring WebFlux
- High fan-out I/O with external HTTP, DB, or messaging clients
- Streaming responses (SSE, Flux) to clients

## Workflow

1. Define @RestController methods returning Mono/Flux.
2. Use WebClient for outbound calls with explicit timeouts.
3. Choose reactive drivers (R2DBC, reactive Mongo) or offload blocking work.
4. Handle errors with onErrorMap and consistent ProblemDetail responses.
5. Load-test with concurrent clients to validate backpressure behavior.

## Required Checks

- No blocking JDBC or Thread.sleep on reactor threads
- WebClient configured with connect/read/write timeouts
- Error signals mapped to RFC 9457 or project error envelope
- SSE/stream endpoints document client disconnect handling

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer WebFlux when I/O-bound concurrency dominates; use MVC + virtual threads when team prefers imperative style.
- Blockhound or reactor debugging in CI for accidental blocking detection.
- Use bounded elastic scheduler for unavoidable blocking sections.
- Keep reactive chains readable — extract operators into named methods.

## Common Rationalizations And Rebuttals

- "Reactive is always faster." -> Reactive adds complexity; use only when concurrency gains justify it.
- "block() is fine once." -> block() on reactive thread stalls event loop; use publishOn/subscribeOn.
- "Same service layer as MVC." -> Shared blocking services need scheduler isolation in WebFlux.

## Evidence Pack

- Blockhound or thread audit showing no blocking on event loop
- WebClient timeout configuration and failure test output
- Load test summary for target concurrency
- Sample SSE/stream client disconnect behavior

## Exit Criteria

- Reactive endpoints scale under I/O load without event-loop stalls
- Error and timeout behavior matches API contract
- Team can maintain reactor chains with documented patterns
