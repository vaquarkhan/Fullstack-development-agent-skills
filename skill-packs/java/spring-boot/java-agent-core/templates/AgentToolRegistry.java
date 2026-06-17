@Component
public class OrderTools {
    private final OrderService orderService;

    @Tool(description = "Get order by UUID")
    public OrderResponse getOrder(@ToolParam(description = "Order UUID") String id) {
        return OrderResponse.from(orderService.findById(UUID.fromString(id)));
    }
}
