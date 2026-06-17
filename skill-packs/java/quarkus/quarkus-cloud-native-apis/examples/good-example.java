// GOOD — JAX-RS resource with CDI injection and DTO response
@Path("/api/v1/orders")
@ApplicationScoped
public class OrderResource {
    @Inject OrderService orderService;

    @POST
    @Consumes(APPLICATION_JSON)
    @Produces(APPLICATION_JSON)
    public Response create(@Valid CreateOrderRequest request) {
        OrderResponse body = orderService.create(request);
        return Response.status(CREATED).entity(body).build();
    }
}
