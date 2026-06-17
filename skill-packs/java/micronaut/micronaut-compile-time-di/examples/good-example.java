// GOOD — compile-time wired singleton with constructor injection
@Singleton
public class OrderService {
    private final OrderRepository repository;

    public OrderService(OrderRepository repository) {
        this.repository = repository;
    }

    public Order create(CreateOrderRequest request) {
        return repository.save(Order.from(request));
    }
}
