@Component
public class OrderForm extends FormLayout {
    private final Binder<CreateOrderRequest> binder = new Binder<>(CreateOrderRequest.class);
    public OrderForm() {
        TextField email = new TextField("Email");
        binder.forField(email).asRequired().bind(CreateOrderRequest::email, CreateOrderRequest::setEmail);
        add(email);
    }
}
