// BAD — blocking JDBC on Netty thread
@Get("/{id}")
Order get(UUID id) {
    return jdbcTemplate.queryForObject("...", Order.class); // blocks event loop
}
