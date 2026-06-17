---
name: testing-pyramid
description: Use when writing tests of any kind — unit, slice, or integration. Covers test structure, naming conventions, Mockito patterns, @WebMvcTest, @DataJpaTest, and Testcontainers setup.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Testing Pyramid

## Use When

- Writing Spring Boot unit, slice, integration, or Testcontainers tests
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

## Structure

```
Unit Tests         — fast, no Spring context, mock dependencies    (70%)
Slice Tests        — partial Spring context (@WebMvcTest, @DataJpaTest) (20%)
Integration Tests  — full context + real DB via Testcontainers     (10%)
```

## Unit Tests — Services

```java
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {

    @Mock private OrderRepository orderRepository;
    @Mock private InventoryService inventoryService;

    @InjectMocks private OrderService orderService;

    @Test
    void createOrder_whenItemsAvailable_shouldSaveAndReturnOrder() {
        // Given
        var request = new CreateOrderRequest("user@example.com", List.of(new OrderItemRequest(UUID.randomUUID(), 2)));
        var savedOrder = Order.create("user@example.com");
        when(orderRepository.save(any(Order.class))).thenReturn(savedOrder);
        doNothing().when(inventoryService).reserve(any());

        // When
        Order result = orderService.createOrder(request);

        // Then
        assertThat(result).isNotNull();
        assertThat(result.getCustomerEmail()).isEqualTo("user@example.com");
        verify(inventoryService).reserve(request.items());
        verify(orderRepository).save(any(Order.class));
    }

    @Test
    void createOrder_whenInventoryUnavailable_shouldThrowException() {
        // Given
        var request = new CreateOrderRequest("user@example.com", List.of());
        doThrow(new InsufficientInventoryException("Out of stock"))
            .when(inventoryService).reserve(any());

        // When / Then
        assertThatThrownBy(() -> orderService.createOrder(request))
            .isInstanceOf(InsufficientInventoryException.class)
            .hasMessage("Out of stock");
    }
}
```

## Slice Tests — Controllers (@WebMvcTest)

```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {

    @Autowired MockMvc mockMvc;
    @Autowired ObjectMapper objectMapper;
    @MockitoBean OrderService orderService; // Spring Boot 3.4+: @MockBean is deprecated

    @Test
    @WithMockUser(roles = "USER")
    void createOrder_withValidRequest_shouldReturn201() throws Exception {
        // Given
        var request = new CreateOrderRequest("user@example.com", List.of());
        var order = Order.create("user@example.com");
        when(orderService.createOrder(any())).thenReturn(order);

        // When / Then
        mockMvc.perform(post("/api/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.success").value(true))
            .andExpect(jsonPath("$.data.customerEmail").value("user@example.com"));
    }

    @Test
    @WithMockUser
    void createOrder_withInvalidRequest_shouldReturn400() throws Exception {
        mockMvc.perform(post("/api/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{}")) // missing required fields
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.success").value(false))
            .andExpect(jsonPath("$.error.code").value("VALIDATION_FAILED"));
    }
}
```

## Slice Tests — Repositories (@DataJpaTest)

```java
@DataJpaTest
@AutoConfigureTestDatabase(replace = Replace.NONE) // use real DB (Testcontainers)
@Import(TestcontainersConfig.class)
class OrderRepositoryTest {

    @Autowired OrderRepository orderRepository;

    @Test
    void findByStatus_shouldReturnMatchingOrders() {
        // Given
        var order1 = orderRepository.save(Order.create("a@example.com"));
        var order2 = orderRepository.save(Order.create("b@example.com"));
        order2.ship(); // change status
        orderRepository.save(order2);

        // When
        List<Order> pending = orderRepository.findByStatus(OrderStatus.PENDING, Pageable.unpaged()).getContent();

        // Then
        assertThat(pending).hasSize(1);
        assertThat(pending.get(0).getCustomerEmail()).isEqualTo("a@example.com");
    }
}
```

## Integration Tests — Testcontainers

```java
// Shared config — reuse container across tests
@TestConfiguration(proxyBeanMethods = false)
public class TestcontainersConfig {

    @Bean
    @ServiceConnection
    PostgreSQLContainer<?> postgresContainer() {
        return new PostgreSQLContainer<>("postgres:16-alpine");
    }
}

// Full integration test
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@Import(TestcontainersConfig.class)
class OrderIntegrationTest {

    @Autowired TestRestTemplate restTemplate;
    @Autowired OrderRepository orderRepository;

    @Test
    void createAndRetrieveOrder_endToEnd() {
        // Create
        var createRequest = new CreateOrderRequest("user@example.com", List.of());
        var createResponse = restTemplate.postForEntity("/api/v1/orders", createRequest, ApiResponse.class);
        assertThat(createResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

        // Retrieve
        // ... assert persisted correctly
    }
}
```

## Naming Convention

```
// Method name: methodName_condition_expectedBehavior
createOrder_whenItemsAvailable_shouldSaveOrder()
findById_whenOrderNotFound_shouldThrowNotFoundException()
login_withInvalidCredentials_shouldReturn401()
```

## Testcontainers Dependencies

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-testcontainers</artifactId>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>postgresql</artifactId>
    <scope>test</scope>
</dependency>
```

## Gotchas
- Agent uses `@SpringBootTest` for everything — use slices for speed
- Agent uses `H2` in-memory DB for `@DataJpaTest` — use Testcontainers for accuracy
- Agent uses `@MockBean` — deprecated since Spring Boot 3.4; use `@MockitoBean` (and `@MockitoSpyBean` for spies)
- Agent uses `Mockito.mock()` instead of `@Mock` — use annotations with `@ExtendWith(MockitoExtension.class)`
- Agent forgets `@WithMockUser` on controller tests — security filter blocks all requests
- Agent uses `assertEquals` from JUnit — use AssertJ (`assertThat(...).isEqualTo(...)`)
- Agent names tests `test_createOrder()` — use `createOrder_condition_expected()` pattern

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

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
