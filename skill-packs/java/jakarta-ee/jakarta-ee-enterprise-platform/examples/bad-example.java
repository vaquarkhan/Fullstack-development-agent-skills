// BAD — javax.* imports, entity in response
import javax.ws.rs.*; // wrong namespace on EE 10+
@POST
public Order create(Order order) { return orderService.save(order); }
