// GOOD — non-blocking controller with timeout-aware WebClient
@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1/orders")
class OrderController {
    private final OrderService orderService;

    @GetMapping("/{id}")
    Mono<OrderResponse> get(@PathVariable UUID id) {
        return orderService.findById(id);
    }
}
