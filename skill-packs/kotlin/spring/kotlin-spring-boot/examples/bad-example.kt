// BAD — platform types, nullable abuse, blocking call in suspend
@RestController
class OrderController {
    @PostMapping("/orders")
    suspend fun create(@RequestBody body: Map<String, Any?>): Any? {
        return jdbcTemplate.queryForMap("SELECT * FROM orders LIMIT 1")
    }
}
