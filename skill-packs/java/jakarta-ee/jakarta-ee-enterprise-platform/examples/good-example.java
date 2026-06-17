// GOOD — JAX-RS + CDI + DTO, jakarta.* imports
@Path("/api/v1/orders")
@RequestScoped
public class OrderResource {
    @Inject OrderService orderService;

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response create(@Valid CreateOrderRequest request) {
        OrderResponse body = orderService.create(request);
        return Response.status(Response.Status.CREATED).entity(body).build();
    }
}
