// BAD — loads all rows in memory, business logic in UI
@Route("orders")
public class OrderListView extends VerticalLayout {
    public OrderListView(OrderRepository repo) {
        add(new Grid<>(Order.class).setItems(repo.findAll())); // OOM risk
    }
}
