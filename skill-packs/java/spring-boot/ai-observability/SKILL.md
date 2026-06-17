---
name: ai-observability
description: Use when adding monitoring, metrics, logging, or tracing to Spring AI or LLM integration code. Covers token tracking, latency measurement, cost estimation, and prompt/response logging. Use when user mentions AI monitoring, token costs, or LLM observability.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Ai Observability

## Use When

- Monitoring token usage, latency, and prompt/response quality for Spring AI apps
- Spring Boot code generation or refactor where agent defaults would be wrong

## Workflow

1. Confirm the change matches this skill's domain triggers before coding.
2. Follow the domain guide conventions and gotchas below — not generic Spring Boot defaults.
3. Apply project-specific response envelopes, DTO boundaries, and dependency injection rules.
4. Validate with targeted tests (slice, integration, or contract as appropriate).
5. Capture evidence before merge: tests, migration notes, or observability proof.

## Required Checks

- Constructor injection used; no @Autowired field injection on new code
- Controllers return DTOs/envelopes — never raw JPA entities
- Business logic stays in @Service layer, not controllers or repositories
- Error handling uses project-standard envelope or RFC 9457 ProblemDetail

## Domain Guide

## Dependencies

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

## Spring AI Built-in Observability

Spring AI 1.0+ includes built-in Micrometer instrumentation:

```yaml
spring:
  ai:
    chat:
      observations:
        log-prompt: true       # GA renamed include-prompt → log-prompt. OFF in prod (PII).
        log-completion: true   # GA renamed include-completion → log-completion
management:
  metrics:
    tags:
      application: order-service
  endpoints:
    web:
      exposure:
        include: health,prometheus,metrics
```

Auto-generated metrics (OpenTelemetry GenAI semantic conventions):
- `gen_ai.client.operation` — model call latency, tagged with provider and model
- `gen_ai.client.token.usage` — token counts (input/output/total)
- `spring.ai.chat.client` — ChatClient-level operation timer/span

## Custom AI Metrics

```java
@Component
@RequiredArgsConstructor
public class AiMetrics {

    private final MeterRegistry meterRegistry;

    private final Timer.Builder promptTimer = Timer.builder("ai.prompt.latency")
        .description("LLM prompt latency");

    private final Counter.Builder tokenCounter = Counter.builder("ai.tokens.used")
        .description("Total tokens consumed");

    public <T> T track(String operation, String model, Supplier<T> call) {
        return Timer.builder("ai.prompt.latency")
            .tag("operation", operation)
            .tag("model", model)
            .register(meterRegistry)
            .recordCallable(() -> call.get());
    }

    public void recordTokens(String operation, String model, int inputTokens, int outputTokens) {
        Counter.builder("ai.tokens.used")
            .tag("operation", operation)
            .tag("model", model)
            .tag("type", "input")
            .register(meterRegistry)
            .increment(inputTokens);

        Counter.builder("ai.tokens.used")
            .tag("operation", operation)
            .tag("model", model)
            .tag("type", "output")
            .register(meterRegistry)
            .increment(outputTokens);
    }
}
```

## Prompt/Response Logging Advisor

GA replaced the whole advisor API: `CallAroundAdvisor` → `CallAdvisor`, `AdvisedRequest` →
`ChatClientRequest`, `AdvisedResponse` → `ChatClientResponse`, and `Usage.getGenerationTokens()` →
`getCompletionTokens()`. Agents reliably generate the old one — it does not compile on 1.0.

```java
@Component
public class AiAuditAdvisor implements CallAdvisor {

    private static final Logger log = LoggerFactory.getLogger(AiAuditAdvisor.class);

    @Override
    public ChatClientResponse adviseCall(ChatClientRequest request, CallAdvisorChain chain) {
        String requestId = UUID.randomUUID().toString();
        long start = System.currentTimeMillis();

        log.info("[AI-AUDIT] requestId={} promptLength={}",
            requestId, request.prompt().getUserMessage().getText().length());

        try {
            ChatClientResponse response = chain.nextCall(request);
            long latency = System.currentTimeMillis() - start;

            ChatResponse chatResponse = response.chatResponse();
            if (chatResponse != null && chatResponse.getMetadata() != null) {
                Usage usage = chatResponse.getMetadata().getUsage();
                log.info("[AI-AUDIT] requestId={} latencyMs={} inputTokens={} outputTokens={}",
                    requestId, latency,
                    usage.getPromptTokens(), usage.getCompletionTokens()); // GA: not getGenerationTokens()
            }
            return response;
        } catch (Exception e) {
            log.error("[AI-AUDIT] requestId={} FAILED after {}ms", requestId,
                System.currentTimeMillis() - start, e);
            throw e;
        }
    }

    @Override
    public String getName() { return "AiAuditAdvisor"; }

    @Override
    public int getOrder() { return Ordered.LOWEST_PRECEDENCE; }
}
```

## Cost Estimation

```java
@Service
public class AiCostEstimator {

    // Prices per million tokens — update when pricing changes
    private static final Map<String, double[]> PRICING = Map.of(
        "claude-sonnet-4-20250514", new double[]{3.0, 15.0},  // [input, output] per 1M tokens
        "claude-haiku-4-5-20251001", new double[]{0.8, 4.0},
        "gpt-4o", new double[]{5.0, 15.0},
        "gpt-4o-mini", new double[]{0.15, 0.6}
    );

    public double estimateCost(String model, int inputTokens, int outputTokens) {
        double[] prices = PRICING.getOrDefault(model, new double[]{5.0, 15.0});
        return (inputTokens * prices[0] + outputTokens * prices[1]) / 1_000_000;
    }
}
```

## Structured AI Audit Log (DB)

```java
@Entity
@Table(name = "ai_audit_log")
public class AiAuditLog {
    @Id @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String operation;
    private String model;
    private int inputTokens;
    private int outputTokens;
    private double estimatedCostUsd;
    private long latencyMs;
    private boolean success;
    private Instant createdAt;
}

// Async to avoid blocking main flow
@Async
public void saveAuditLog(AiAuditLog log) {
    auditLogRepository.save(log);
}
```

## application.yml — Full Observability

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,prometheus,metrics,info
  metrics:
    distribution:
      percentiles-histogram:
        ai.prompt.latency: true  # enables P50/P95/P99
  tracing:
    sampling:
      probability: 1.0  # 100% trace sampling in dev, reduce in prod

logging:
  level:
    org.springframework.ai: DEBUG  # enable in dev only
```

## Gotchas
- Agent implements `CallAroundAdvisor`/`AdvisedRequest` — removed in GA; use `CallAdvisor`/`ChatClientRequest`
- Agent calls `usage.getGenerationTokens()` — GA renamed it to `getCompletionTokens()`
- Agent logs full prompts in production — keep `log-prompt: false` for PII safety
- Agent skips async on audit saves — always `@Async` to avoid latency impact, and put the `@Async` method on a **separate bean**; calling it on `this` bypasses the proxy and runs synchronously
- Agent hardcodes token pricing — extract to config, prices change
- Agent misses failed calls in metrics — track errors separately with error tag

## Examples And Templates

See \examples/\ for side-by-side good vs bad patterns agents commonly get wrong.
See \	emplates/\ for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer Spring Boot 3.x and Spring AI 1.0 GA artifact coordinates — reject pre-GA dead names.
- Use constructor injection and immutable dependencies by default.
- Keep domain content in services; controllers are HTTP adapters only.
- Externalize prompts, API keys, and migration scripts — never hardcode secrets.

## Common Rationalizations And Rebuttals

- "@Autowired fields are fine for prototypes." -> Field injection hides dependencies and breaks testability; use constructor injection.
- "The agent knows Spring Boot." -> Agents default to outdated patterns; follow this skill's gotchas and GA coordinates.
- "We can skip Flyway for this column." -> Manual DDL drifts from environments; use versioned migrations.

## Evidence Pack

- Test output for changed endpoints, services, or migrations
- Diff showing DTO boundaries and no entity leakage in API layer
- Dependency or coordinate list confirming GA artifact names
- Observability or security checklist for auth/AI changes

## Exit Criteria

- Generated code matches project layering and naming conventions
- No pre-GA Spring AI or MCP artifact names in pom/build files
- Tests pass for happy path and at least one failure/edge case
