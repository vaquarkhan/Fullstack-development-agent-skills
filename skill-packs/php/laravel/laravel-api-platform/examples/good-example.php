// GOOD — FormRequest validation + API Resource
class OrderController extends Controller {
    public function store(CreateOrderRequest $request, OrderService $service): OrderResource {
        return new OrderResource($service->create($request->validated()));
    }
}
