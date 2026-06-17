// GOOD — minimal API with typed handler, Results pattern, auth
app.MapPost("/api/v1/orders", async (
    CreateOrderRequest request,
    IOrderService service,
    CancellationToken ct) =>
{
    var order = await service.CreateAsync(request, ct);
    return Results.Created($"/api/v1/orders/{order.Id}", order);
})
.RequireAuthorization()
.WithName("CreateOrder");
