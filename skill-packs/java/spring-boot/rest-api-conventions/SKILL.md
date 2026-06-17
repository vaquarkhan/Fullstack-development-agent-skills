---
name: rest-api-conventions
description: Use when generating REST controllers, response wrappers, DTOs, error handlers, or any HTTP-facing code. Defines response envelope, HTTP status mapping, pagination, and versioning.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Rest Api Conventions

## Use When

- Creating REST controllers, response envelopes, pagination, or error handlers
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

## Response Envelope

All endpoints return a consistent envelope:

```json
{
  "success": true,
  "data": { },
  "error": null,
  "timestamp": "2026-04-13T10:00:00Z"
}
```

Error response:
```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order with id 123 not found",
    "details": []
  },
  "timestamp": "2026-04-13T10:00:00Z"
}
```

## ApiResponse Wrapper

```java
@JsonInclude(JsonInclude.Include.NON_NULL)
public record ApiResponse<T>(
    boolean success,
    T data,
    ApiError error,
    Instant timestamp
) {
    public static <T> ApiResponse<T> ok(T data) {
        return new ApiResponse<>(true, data, null, Instant.now());
    }

    public static <T> ApiResponse<T> error(String code, String message) {
        return new ApiResponse<>(false, null, new ApiError(code, message, List.of()), Instant.now());
    }
}

public record ApiError(String code, String message, List<String> details) {}
```

## HTTP Status Mapping

| Scenario | Status |
|----------|--------|
| GET — found | 200 |
| POST — created resource | 201 |
| PUT/PATCH — updated | 200 |
| DELETE — deleted | 204 (no body) |
| Validation failure | 400 |
| Unauthenticated | 401 |
| Forbidden | 403 |
| Not found | 404 |
| Conflict (duplicate) | 409 |
| Unhandled server error | 500 |

## URL Conventions

- **Plural nouns** for resources: `/orders`, `/users`, `/products`
- **Kebab-case** for multi-word: `/order-items`, not `/orderItems`
- **Versioning in path**: `/api/v1/orders`
- **Nested resources** max 2 levels: `/orders/{id}/items` ✅, `/orders/{id}/items/{itemId}/notes` ❌ — flatten to `/order-item-notes/{id}`
- **IDs as UUIDs** in path, never auto-increment integers exposed in URL

```
GET    /api/v1/orders              → list (paginated)
POST   /api/v1/orders              → create
GET    /api/v1/orders/{id}         → get one
PUT    /api/v1/orders/{id}         → full update
PATCH  /api/v1/orders/{id}         → partial update
DELETE /api/v1/orders/{id}         → delete
GET    /api/v1/orders/{id}/items   → nested resource
```

## Pagination

```json
{
  "success": true,
  "data": {
    "content": [...],
    "page": 0,
    "size": 20,
    "totalElements": 150,
    "totalPages": 8,
    "last": false
  }
}
```

Query params: `?page=0&size=20&sort=createdAt,desc`

Use Spring Data `Pageable` in controllers:
```java
@GetMapping
public ApiResponse<Page<OrderResponse>> list(Pageable pageable) {
    return ApiResponse.ok(orderService.findAll(pageable).map(OrderResponse::from));
}
```

**Cap the page size.** A bare `Pageable` accepts `?size=100000` from any client — one request can
drag your whole table into memory. Spring's default cap is 2000, still too high for most APIs:

```yaml
spring:
  data:
    web:
      pageable:
        default-page-size: 20
        max-page-size: 100   # requests above this are silently clamped
```

## Global Exception Handler

```java
@RestControllerAdvice
@RequiredArgsConstructor
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ApiResponse<Void>> handleNotFound(EntityNotFoundException ex) {
        return ResponseEntity.status(404).body(ApiResponse.error("NOT_FOUND", ex.getMessage()));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiResponse<Void>> handleValidation(MethodArgumentNotValidException ex) {
        List<String> details = ex.getBindingResult().getFieldErrors().stream()
            .map(e -> e.getField() + ": " + e.getDefaultMessage()).toList();
        return ResponseEntity.status(400)
            .body(new ApiResponse<>(false, null, new ApiError("VALIDATION_FAILED", "Invalid input", details), Instant.now()));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Void>> handleGeneric(Exception ex) {
        return ResponseEntity.status(500).body(ApiResponse.error("INTERNAL_ERROR", "An unexpected error occurred"));
    }
}
```

## Gotchas
- Agent returns raw objects without envelope — always wrap in `ApiResponse.ok(...)`
- Agent uses `ResponseEntity<Map<String, Object>>` for errors — use `ApiResponse`
- Agent puts exception handlers in controllers — always use `@RestControllerAdvice`
- Agent uses `Long` IDs in URLs — use `UUID`
- Agent accepts unbounded `Pageable` — set `spring.data.web.pageable.max-page-size` or one request can pull the whole table
- Agent returns `Page<Entity>` serialized directly — exposes Hibernate internals; map to DTOs first

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
