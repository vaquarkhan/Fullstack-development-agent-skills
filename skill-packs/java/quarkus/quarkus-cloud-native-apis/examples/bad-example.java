// BAD — entity returned directly, new service per request
@Path("/orders")
public class OrderResource {
    @POST
    public Order create(Order order) {
        return Order.persist(order); // leaks entity
    }
}
