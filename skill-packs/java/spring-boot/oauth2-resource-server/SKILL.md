---
name: oauth2-resource-server
description: Use when configuring Spring Boot as an OAuth2 resource server, validating JWTs from an external auth provider (Keycloak, Auth0, Okta, Cognito), extracting claims, or implementing scope-based authorization.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Oauth2 Resource Server

## Use When

- Configuring OAuth2 resource server JWT validation and scope checks
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
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

## Security Configuration

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class ResourceServerConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(AbstractHttpConfigurer::disable)
            .sessionManagement(s -> s.sessionCreationPolicy(STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health").permitAll()
                .requestMatchers("/api/v1/admin/**").hasAuthority("SCOPE_admin")
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt.jwtAuthenticationConverter(jwtAuthConverter()))
            )
            .build();
    }

    @Bean
    public JwtAuthenticationConverter jwtAuthConverter() {
        var converter = new JwtGrantedAuthoritiesConverter();
        converter.setAuthoritiesClaimName("roles"); // Keycloak uses "roles"
        converter.setAuthorityPrefix("ROLE_");

        var authConverter = new JwtAuthenticationConverter();
        authConverter.setJwtGrantedAuthoritiesConverter(converter);
        return authConverter;
    }
}
```

## application.yml — Common Providers

```yaml
# Keycloak
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://keycloak.example.com/realms/my-realm
          jwk-set-uri: https://keycloak.example.com/realms/my-realm/protocol/openid-connect/certs

# Auth0
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://your-domain.auth0.com/
          audiences: https://your-api.example.com  # custom claim validation
```

## Custom Claim Extraction

```java
@Component
public class JwtClaimExtractor {

    public UUID getUserId(JwtAuthenticationToken token) {
        return UUID.fromString(token.getToken().getClaimAsString("sub"));
    }

    public String getEmail(JwtAuthenticationToken token) {
        return token.getToken().getClaimAsString("email");
    }

    public List<String> getRoles(JwtAuthenticationToken token) {
        // Keycloak nests roles under realm_access.roles
        Map<String, Object> realmAccess = token.getToken().getClaimAsMap("realm_access");
        if (realmAccess == null) return List.of();
        return (List<String>) realmAccess.getOrDefault("roles", List.of());
    }
}
```

## Controller — Accessing Current User

```java
@RestController
@RequiredArgsConstructor
public class OrderController {

    @GetMapping("/api/v1/orders/my")
    public ApiResponse<List<OrderResponse>> myOrders(
        @AuthenticationPrincipal Jwt jwt  // inject JWT directly
    ) {
        UUID userId = UUID.fromString(jwt.getSubject());
        return ApiResponse.ok(orderService.findByUser(userId));
    }

    // Or with JwtAuthenticationToken for full principal
    @GetMapping("/api/v1/profile")
    public ApiResponse<ProfileResponse> profile(JwtAuthenticationToken token) {
        return ApiResponse.ok(userService.findByEmail(
            token.getToken().getClaimAsString("email")
        ));
    }
}
```

## Method Security with Scopes

```java
@PreAuthorize("hasAuthority('SCOPE_orders:read')")
public List<Order> findAll() { ... }

@PreAuthorize("hasRole('ADMIN') or @orderSecurity.isOwner(#orderId, authentication)")
public Order findById(UUID orderId) { ... }

// Custom security bean
@Component("orderSecurity")
public class OrderSecurityService {
    public boolean isOwner(UUID orderId, Authentication auth) {
        Jwt jwt = (Jwt) auth.getPrincipal();
        UUID userId = UUID.fromString(jwt.getSubject());
        return orderRepository.existsByIdAndCustomerId(orderId, userId);
    }
}
```

## Gotchas
- Agent uses `hasRole("ADMIN")` for scope check — scopes use `hasAuthority("SCOPE_admin")`
- Agent forgets `issuer-uri` validation — always configure to prevent token forgery
- Agent maps roles wrong for Keycloak — roles are nested under `realm_access.roles`
- Agent uses `getPrincipal()` directly — cast to `Jwt` or use `@AuthenticationPrincipal Jwt`
- Agent adds `userDetailsService` bean — not needed for resource servers (stateless JWT)

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
