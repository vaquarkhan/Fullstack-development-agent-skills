---
name: spring-data-redis
description: Use when implementing caching, session storage, rate limiting, or any Redis integration. Covers cache-aside pattern, key naming, TTL strategy, and serialization config.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Spring Data Redis

## Use When

- Implementing Redis caching, TTL strategy, or cache-aside patterns
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
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
```

## Configuration

```java
@Configuration
@EnableCaching
public class RedisConfig {

    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer()); // JSON, not Java serialize
        template.setHashKeySerializer(new StringRedisSerializer());
        template.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());
        return template;
    }

    @Bean
    public RedisCacheManager cacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(10))
            .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))
            .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer()))
            .disableCachingNullValues();

        return RedisCacheManager.builder(factory)
            .cacheDefaults(config)
            .withCacheConfiguration("orders", config.entryTtl(Duration.ofMinutes(5)))
            .withCacheConfiguration("products", config.entryTtl(Duration.ofHours(1)))
            .build();
    }
}
```

## Key Naming Convention

```
{app}:{domain}:{id}          → orders:order:uuid-here
{app}:{domain}:list:{filter} → orders:order:list:status:PENDING
{app}:session:{userId}       → orders:session:uuid-here
{app}:ratelimit:{ip}         → orders:ratelimit:192.168.1.1
```

## @Cacheable — Declarative Caching

```java
@Service
@RequiredArgsConstructor
public class ProductService {

    @Cacheable(value = "products", key = "#id")
    public ProductResponse findById(UUID id) {
        return productRepository.findById(id)
            .map(ProductResponse::from)
            .orElseThrow(() -> new EntityNotFoundException("Product not found: " + id));
    }

    @CachePut(value = "products", key = "#result.id")  // update cache after write
    @Transactional
    public ProductResponse update(UUID id, UpdateProductRequest request) {
        Product product = productRepository.findById(id).orElseThrow();
        product.update(request);
        return ProductResponse.from(productRepository.save(product));
    }

    @CacheEvict(value = "products", key = "#id")  // invalidate on delete
    @Transactional
    public void delete(UUID id) {
        productRepository.deleteById(id);
    }

    @CacheEvict(value = "products", allEntries = true)  // clear all
    public void clearCache() {}
}
```

## Manual Cache-Aside Pattern

```java
@Service
@RequiredArgsConstructor
public class OrderCacheService {

    private final RedisTemplate<String, Object> redisTemplate;
    private final ObjectMapper objectMapper;
    private static final Duration TTL = Duration.ofMinutes(5);

    public Optional<OrderResponse> get(UUID orderId) {
        String key = "orders:order:" + orderId;
        Object cached = redisTemplate.opsForValue().get(key);
        if (cached == null) return Optional.empty();
        return Optional.of(objectMapper.convertValue(cached, OrderResponse.class));
    }

    public void put(OrderResponse order) {
        String key = "orders:order:" + order.id();
        redisTemplate.opsForValue().set(key, order, TTL);
    }

    public void evict(UUID orderId) {
        redisTemplate.delete("orders:order:" + orderId);
    }
}
```

## Rate Limiting with Redis

```java
@Component
@RequiredArgsConstructor
public class RateLimiter {

    private final RedisTemplate<String, String> redisTemplate;

    public boolean isAllowed(String identifier, int maxRequests, Duration window) {
        String key = "ratelimit:" + identifier;
        Long count = redisTemplate.opsForValue().increment(key);
        if (count == 1) {
            redisTemplate.expire(key, window);
        }
        return count <= maxRequests;
    }
}
```

## application.yml

```yaml
spring:
  data:
    redis:
      host: ${REDIS_HOST:localhost}
      port: ${REDIS_PORT:6379}
      password: ${REDIS_PASSWORD:}
      timeout: 2000ms
      lettuce:
        pool:
          max-active: 10
          max-idle: 5
          min-idle: 2
  cache:
    type: redis
```

## Cache Stampede

When a hot key expires, every concurrent request misses at once and they all hammer the DB to recompute
the same value (the "thundering herd"). For expensive, high-traffic loads, let one caller compute while
the rest wait:

```java
// sync = true — only one thread computes the value; others block on it
@Cacheable(value = "products", key = "#id", sync = true)
public ProductResponse findById(UUID id) { ... }
```

`sync = true` serializes recomputation per key within a single instance. For a fleet-wide guarantee,
add a short Redis lock (`SETNX` with a TTL) around the recompute. Pair with jittered TTLs so a batch of
keys written together doesn't all expire on the same second.

## Gotchas
- Agent uses Java serialization for values — always use JSON (`GenericJackson2JsonRedisSerializer`)
- Agent caches entities with JPA lazy fields — cache DTOs/response objects, not entities
- Agent uses no TTL — always set expiry, memory is not infinite
- Agent forgets `@EnableCaching` — `@Cacheable` silently does nothing without it
- Agent caches `null` values — use `.disableCachingNullValues()` to avoid storing misses
- Agent leaves hot keys unprotected — use `@Cacheable(sync = true)` to prevent stampede on expiry
- Agent gives every entry the same TTL — add jitter so keys don't expire in a synchronized wave

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
