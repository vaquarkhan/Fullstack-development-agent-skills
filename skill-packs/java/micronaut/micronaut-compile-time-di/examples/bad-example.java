// BAD — runtime field injection / manual new
public class OrderService {
    @Inject OrderRepository repository;
    public Order create(CreateOrderRequest r) {
        return new OrderRepository().save(...); // bypasses DI
    }
}
