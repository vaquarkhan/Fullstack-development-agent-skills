// GOOD — repository pattern, typed API client, error mapping
class OrderRepository {
  const OrderRepository(this._client);
  final ApiClient _client;

  Future<Order> createOrder(CreateOrderRequest request) async {
    final response = await _client.post('/orders', body: request.toJson());
    if (response.statusCode == 201) {
      return Order.fromJson(response.data);
    }
    throw ApiException.fromResponse(response);
  }
}
