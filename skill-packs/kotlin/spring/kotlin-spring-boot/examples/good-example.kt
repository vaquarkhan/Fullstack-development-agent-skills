// GOOD — Kotlin data class DTO, coroutine controller, null-safe service
@RestController
@RequestMapping("/api/v1/orders")
class OrderController(private val service: OrderService) {
    @PostMapping
    suspend fun create(@Valid @RequestBody request: CreateOrderRequest): ResponseEntity<OrderResponse> {
        val order = service.create(request)
        return ResponseEntity.status(HttpStatus.CREATED).body(order.toResponse())
    }
}
