---
name: transactional-patterns
description: Use when working with @Transactional, multi-step database operations, distributed transactions, or any code that needs atomicity guarantees. Covers propagation rules, isolation levels, read-only optimization, and common pitfalls.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Transactional Patterns

## Use When

- Configuring @Transactional propagation, sagas, or after-commit side effects
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

## Basic Rules

- `@Transactional` belongs on **service methods**, never controllers or repositories
- Default propagation is `REQUIRED` — joins existing transaction or creates one
- Always use on methods that write to the DB or coordinate multiple writes
- `@Transactional(readOnly = true)` on all read-only service methods — enables optimizations

```java
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true) // default for all methods in this service
public class OrderService {

    @Transactional // overrides readOnly for writes
    public Order createOrder(CreateOrderRequest request) {
        inventoryService.reserve(request.items()); // participates in same TX
        return orderRepository.save(Order.from(request));
    }

    public Optional<Order> findById(UUID id) {
        return orderRepository.findById(id); // readOnly = true inherited
    }
}
```

## Propagation

| Propagation | Behavior |
|-------------|----------|
| `REQUIRED` (default) | Join existing TX or create new |
| `REQUIRES_NEW` | Always create new TX, suspend existing |
| `SUPPORTS` | Join if exists, proceed without TX if not |
| `NOT_SUPPORTED` | Always run without TX |
| `MANDATORY` | Must have existing TX, throw if not |
| `NEVER` | Must NOT have TX, throw if one exists |

```java
// REQUIRES_NEW — for audit logging that must survive rollback
@Transactional(propagation = Propagation.REQUIRES_NEW)
public void logAuditEvent(AuditEvent event) {
    auditRepository.save(event); // commits independently of parent TX
}

// Order TX rolls back, audit log still saved
@Transactional
public void processOrder(Order order) {
    auditService.logAuditEvent(new AuditEvent("ORDER_START", order.getId()));
    try {
        // ... process, may throw
    } catch (Exception e) {
        auditService.logAuditEvent(new AuditEvent("ORDER_FAILED", order.getId()));
        throw e; // parent TX rolls back, audit TX already committed
    }
}
```

## Self-Invocation Pitfall

```java
// ❌ BROKEN — self-invocation bypasses Spring proxy, @Transactional ignored
@Service
public class OrderService {
    @Transactional
    public void processAll(List<UUID> ids) {
        ids.forEach(id -> this.processSingle(id)); // bypasses proxy!
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void processSingle(UUID id) { ... } // never creates new TX
}

// ✅ FIX — inject self or extract to separate bean
@Service
@RequiredArgsConstructor
public class OrderService {
    private final OrderProcessor orderProcessor; // separate bean

    @Transactional
    public void processAll(List<UUID> ids) {
        ids.forEach(id -> orderProcessor.processSingle(id)); // goes through proxy
    }
}
```

## Handling Exceptions

```java
// @Transactional rolls back on RuntimeException by default
// For checked exceptions, explicitly declare rollbackFor

@Transactional(rollbackFor = InsufficientInventoryException.class) // checked exception
public Order createOrder(CreateOrderRequest request) throws InsufficientInventoryException {
    ...
}

// noRollbackFor — for non-fatal exceptions you want to commit anyway
@Transactional(noRollbackFor = OptimisticLockException.class)
public void updateWithRetry(UUID id) { ... }
```

## Optimistic Locking

```java
@Entity
public class Order {
    @Version
    private Long version; // Hibernate handles conflicts automatically
}

// Handles concurrent updates
@Transactional
public Order updateStatus(UUID id, OrderStatus newStatus) {
    Order order = orderRepository.findById(id).orElseThrow();
    order.updateStatus(newStatus); // if another TX modified it, throws ObjectOptimisticLockingFailureException
    return orderRepository.save(order);
}
```

## Distributed Transactions (Saga Pattern)

For multi-service operations, use the Saga pattern instead of distributed TX:

```java
@Service
@RequiredArgsConstructor
public class OrderSaga {

    @Transactional
    public void execute(CreateOrderRequest request) {
        Order order = orderRepository.save(Order.create(request));
        try {
            inventoryClient.reserve(request.items());       // step 1
            paymentClient.charge(order.getId(), request.total()); // step 2
            order.confirm();
            orderRepository.save(order);
        } catch (PaymentException e) {
            inventoryClient.release(request.items()); // compensate step 1
            order.fail("Payment failed");
            orderRepository.save(order);
            throw e;
        }
    }
}
```

## Side Effects After Commit

Never fire an external side effect (email, Kafka publish, webhook, cache warm) inside the transaction —
if the TX rolls back, you've already sent it. Bind the side effect to the commit instead:

```java
// Publisher — inside the TX
@Transactional
public Order place(UUID id) {
    Order order = orderRepository.findById(id).orElseThrow();
    order.place();
    eventPublisher.publishEvent(new OrderPlaced(order.getId())); // not sent yet
    return orderRepository.save(order);
}

// Listener — runs ONLY if the TX commits successfully
@TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
public void onOrderPlaced(OrderPlaced event) {
    emailService.sendConfirmation(event.orderId()); // safe: data is durable
}
```

`AFTER_COMMIT` runs after the DB commits. Note: it runs **outside** the original transaction, so a
new `@Transactional(REQUIRES_NEW)` is needed if the listener itself writes to the DB. This is the
clean way to publish the domain events collected in the [[domain-driven-design]] aggregate.

## Gotchas
- Agent puts `@Transactional` on controllers — only on service layer
- Agent sends email / publishes events inside the TX — use `@TransactionalEventListener(AFTER_COMMIT)`
- Agent forgets `readOnly = true` on read methods — missed DB optimization
- Agent calls `@Transactional` methods on `this` — self-invocation bypasses proxy
- Agent expects checked exceptions to rollback — must add `rollbackFor`
- Agent uses `@Transactional` on `private` methods — Spring proxy can't intercept

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
