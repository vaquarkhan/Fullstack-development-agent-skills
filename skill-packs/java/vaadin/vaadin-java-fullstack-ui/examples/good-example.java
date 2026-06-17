// GOOD — @Route view with Binder and service injection
@Route("orders")
@PageTitle("Orders")
public class OrderListView extends VerticalLayout {
    private final OrderService orderService;
    private final Grid<OrderRow> grid = new Grid<>(OrderRow.class, false);

    public OrderListView(OrderService orderService) {
        this.orderService = orderService;
        grid.setItems(query -> orderService.stream(query).stream());
        add(grid);
    }
}
