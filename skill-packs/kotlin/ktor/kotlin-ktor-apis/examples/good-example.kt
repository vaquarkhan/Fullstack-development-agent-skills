// GOOD — Ktor route with validation, service call, status mapping
post("/api/v1/orders") {
    val request = call.receive<CreateOrderRequest>()
    val order = orderService.create(request)
    call.respond(HttpStatusCode.Created, order.toResponse())
}
