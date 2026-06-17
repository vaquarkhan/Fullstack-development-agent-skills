// BAD — block() on reactive thread / JDBC inside Mono
@GetMapping("/{id}")
Mono<Order> get(@PathVariable UUID id) {
    return Mono.fromCallable(() -> jdbcTemplate.queryForObject(...)); // blocks event loop
}
