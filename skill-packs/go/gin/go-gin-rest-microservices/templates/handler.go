type OrderHandler struct {
    service OrderService
}

func NewOrderHandler(service OrderService) *OrderHandler {
    return &OrderHandler{service: service}
}
