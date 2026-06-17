---
name: hateoas
description: Use when adding hypermedia links to REST responses, building self-describing APIs, or implementing Spring HATEOAS. Use when you see EntityModel, CollectionModel, or RepresentationModel in the project.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Hateoas

## Use When

- Adding hypermedia links with Spring HATEOAS
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

## Dependency

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-hateoas</artifactId>
</dependency>
```

## When to Add Links

- `self` — always, on every resource response
- `collection` — link back to the list endpoint
- `related resources` — when a client commonly needs to navigate to them
- `actions` — links to state transitions (e.g., `cancel`, `ship`) when valid for current state

## Resource Model

```java
public class OrderModel extends RepresentationModel<OrderModel> {
    private final UUID id;
    private final String status;
    private final String customerEmail;
    private final Instant createdAt;

    // Static factory with links
    public static OrderModel from(Order order) {
        OrderModel model = new OrderModel(
            order.getId(), order.getStatus().name(),
            order.getCustomerEmail(), order.getCreatedAt()
        );

        // Self link — always
        model.add(linkTo(methodOn(OrderController.class).getById(order.getId())).withSelfRel());

        // Collection link
        model.add(linkTo(methodOn(OrderController.class).list(null)).withRel("orders"));

        // Conditional action links based on state
        if (order.getStatus() == OrderStatus.PENDING) {
            model.add(linkTo(methodOn(OrderController.class)
                .cancelOrder(order.getId())).withRel("cancel"));
        }
        if (order.getStatus() == OrderStatus.PROCESSING) {
            model.add(linkTo(methodOn(OrderController.class)
                .shipOrder(order.getId())).withRel("ship"));
        }

        return model;
    }
}
```

## Controller

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

    @GetMapping("/{id}")
    public ResponseEntity<OrderModel> getById(@PathVariable UUID id) {
        Order order = orderService.findById(id);
        return ResponseEntity.ok(OrderModel.from(order));
    }

    @GetMapping
    public ResponseEntity<CollectionModel<OrderModel>> list(Pageable pageable) {
        Page<Order> orders = orderService.findAll(pageable);

        List<OrderModel> models = orders.getContent().stream()
            .map(OrderModel::from)
            .toList();

        CollectionModel<OrderModel> collection = CollectionModel.of(models,
            linkTo(methodOn(OrderController.class).list(pageable)).withSelfRel()
        );

        // Pagination links
        if (orders.hasNext()) {
            collection.add(linkTo(methodOn(OrderController.class)
                .list(pageable.next())).withRel(IanaLinkRelations.NEXT));
        }
        if (orders.hasPrevious()) {
            collection.add(linkTo(methodOn(OrderController.class)
                .list(pageable.previousOrFirst())).withRel(IanaLinkRelations.PREV));
        }

        return ResponseEntity.ok(collection);
    }
}
```

## Response Shape

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "PENDING",
  "customerEmail": "user@example.com",
  "_links": {
    "self": { "href": "http://api.example.com/api/v1/orders/550e8400" },
    "orders": { "href": "http://api.example.com/api/v1/orders" },
    "cancel": { "href": "http://api.example.com/api/v1/orders/550e8400/cancel" }
  }
}
```

## RepresentationModelAssembler Pattern
- Spring's recommended way to build HATEOAS models from entities
- Implements `RepresentationModelAssembler<Entity, Model>` — reusable across controllers
- Inject the assembler into controllers instead of calling `Model.from()` directly

```java
@Component
public class OrderModelAssembler implements RepresentationModelAssembler<Order, EntityModel<OrderResponse>> {

    @Override
    public EntityModel<OrderResponse> toModel(Order order) {
        EntityModel<OrderResponse> model = EntityModel.of(OrderResponse.from(order),
            linkTo(methodOn(OrderController.class).getById(order.getId())).withSelfRel(),
            linkTo(methodOn(OrderController.class).list(null)).withRel("orders"));

        if (order.getStatus() == OrderStatus.PENDING) {
            model.add(linkTo(methodOn(OrderController.class)
                .cancelOrder(order.getId())).withRel("cancel"));
        }
        return model;
    }
}
```

## PagedModel for Paginated Collections
- Use `PagedResourcesAssembler` for automatic pagination links (first, prev, next, last)
- Inject `PagedResourcesAssembler<Order>` into controllers — Spring creates it automatically

```java
@GetMapping
public ResponseEntity<PagedModel<EntityModel<OrderResponse>>> list(
        Pageable pageable, PagedResourcesAssembler<Order> pagedAssembler) {
    Page<Order> orders = orderService.findAll(pageable);
    PagedModel<EntityModel<OrderResponse>> pagedModel =
        pagedAssembler.toModel(orders, orderModelAssembler);
    return ResponseEntity.ok(pagedModel);
}
```

## Gotchas
- Agent adds all links regardless of state — only add action links when the action is valid
- Agent hardcodes URLs in links — always use `linkTo(methodOn(...))` for type-safe links
- Agent returns plain DTO — wrap in `EntityModel.of(dto, links...)` or extend `RepresentationModel`
- Agent puts link logic in controller — extract to `RepresentationModelAssembler`
- Agent manually builds pagination links — use `PagedResourcesAssembler` instead
- Agent forgets `self` link — every resource must have a `self` link

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
