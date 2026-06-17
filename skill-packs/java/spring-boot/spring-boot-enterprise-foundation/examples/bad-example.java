// BAD — field injection, business logic in controller, entity in response
@RestController
public class OrderController {
    @Autowired OrderRepository repo;

    @PostMapping("/orders")
    public Order create(@RequestBody Order order) {
        if (order.getItems().isEmpty()) throw new RuntimeException("empty");
        return repo.save(order);
    }
}
