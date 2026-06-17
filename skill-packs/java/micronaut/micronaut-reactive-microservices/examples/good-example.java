// GOOD — reactive return type, injected singleton
@Controller("/api/v1/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderService orderService;

    @Get("/{id}")
    Mono<OrderResponse> get(UUID id) {
        return orderService.findById(id);
    }
}
