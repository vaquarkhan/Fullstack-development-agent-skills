#!/usr/bin/env python3
"""Add examples/ and templates/ to skill packs missing them."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXAMPLES_SECTION = """
## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

"""

# skill_dir_relative -> (ext, good_example, bad_example, template_name, template_content)
PACKS: dict[str, tuple[str, str, str, str, str]] = {
    "skill-packs/java/spring-boot/spring-boot-enterprise-foundation": (
        "java",
        """// GOOD — constructor injection, layered entry, Actuator-ready service
@SpringBootApplication
public class OrderApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderApplication.class, args);
    }
}

@RestController
@RequestMapping("/api/v1/orders")
@RequiredArgsConstructor
class OrderController {
    private final OrderService orderService;

    @PostMapping
    ResponseEntity<OrderResponse> create(@Valid @RequestBody CreateOrderRequest request) {
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(OrderResponse.from(orderService.create(request)));
    }
}
""",
        """// BAD — field injection, business logic in controller, entity in response
@RestController
public class OrderController {
    @Autowired OrderRepository repo;

    @PostMapping("/orders")
    public Order create(@RequestBody Order order) {
        if (order.getItems().isEmpty()) throw new RuntimeException("empty");
        return repo.save(order);
    }
}
""",
        "Application.java",
        """@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
""",
    ),
    "skill-packs/java/spring-boot/java-agent-core": (
        "java",
        """// GOOD — bounded agent loop with tool registry and max iterations
@Service
@RequiredArgsConstructor
public class SupportAgentService {
    private final ChatClient chatClient;
    private static final int MAX_STEPS = 8;

    public AgentResult run(AgentRequest request) {
        for (int step = 0; step < MAX_STEPS; step++) {
            AgentStep result = chatClient.prompt()
                .user(request.prompt())
                .call()
                .entity(AgentStep.class);
            if (result.isTerminal()) {
                return AgentResult.done(result);
            }
        }
        throw new AgentBudgetExceededException(MAX_STEPS);
    }
}
""",
        """// BAD — unbounded loop, repository called directly from agent, no auth on tools
while (true) {
    var reply = chatClient.prompt().user(input).call().content();
    orderRepository.save(parse(reply)); // no tool boundary
}
""",
        "AgentToolRegistry.java",
        """@Component
public class OrderTools {
    private final OrderService orderService;

    @Tool(description = "Get order by UUID")
    public OrderResponse getOrder(@ToolParam(description = "Order UUID") String id) {
        return OrderResponse.from(orderService.findById(UUID.fromString(id)));
    }
}
""",
    ),
    "skill-packs/java/spring-boot/spring-cloud-gateway-routing": (
        "java",
        """// GOOD — explicit route with timeout and strip sensitive headers
@Bean
public RouteLocator routes(RouteLocatorBuilder builder) {
    return builder.routes()
        .route("orders-api", r -> r.path("/api/v1/orders/**")
            .filters(f -> f.stripPrefix(0)
                .removeRequestHeader("Cookie")
                .circuitBreaker(c -> c.setName("orders-cb")))
            .uri("lb://order-service"))
        .build();
}
""",
        """// BAD — catch-all proxy, no timeout, forwards cookies to upstream
.route(r -> r.path("/**").uri("http://backend:8080"))
""",
        "application-gateway.yml",
        """spring:
  cloud:
    gateway:
      routes:
        - id: orders
          uri: lb://order-service
          predicates:
            - Path=/api/v1/orders/**
          filters:
            - RemoveRequestHeader=Cookie
""",
    ),
    "skill-packs/java/spring-boot/spring-webflux-reactive": (
        "java",
        """// GOOD — non-blocking controller with timeout-aware WebClient
@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1/orders")
class OrderController {
    private final OrderService orderService;

    @GetMapping("/{id}")
    Mono<OrderResponse> get(@PathVariable UUID id) {
        return orderService.findById(id);
    }
}
""",
        """// BAD — block() on reactive thread / JDBC inside Mono
@GetMapping("/{id}")
Mono<Order> get(@PathVariable UUID id) {
    return Mono.fromCallable(() -> jdbcTemplate.queryForObject(...)); // blocks event loop
}
""",
        "WebClientConfig.java",
        """@Configuration
public class WebClientConfig {
    @Bean
    WebClient webClient(WebClient.Builder builder) {
        return builder
            .clientConnector(new ReactorClientHttpConnector(
                HttpClient.create().responseTimeout(Duration.ofSeconds(3))))
            .build();
    }
}
""",
    ),
    "skill-packs/java/spring-boot/testing-pyramid": (
        "java",
        """// GOOD — @WebMvcTest slice for controller only
@WebMvcTest(OrderController.class)
class OrderControllerTest {
    @Autowired MockMvc mockMvc;
    @MockitoBean OrderService orderService;

    @Test
    void create_returns201() throws Exception {
        when(orderService.create(any())).thenReturn(new Order(UUID.randomUUID()));
        mockMvc.perform(post("/api/v1/orders").contentType(APPLICATION_JSON)
                .content("{\"customerEmail\":\"a@b.com\"}"))
            .andExpect(status().isCreated());
    }
}
""",
        """// BAD — @SpringBootTest for every controller assertion (slow, brittle)
@SpringBootTest(webEnvironment = RANDOM_PORT)
class OrderControllerTest { /* loads entire context */ }
""",
        "OrderServiceTest.java",
        """@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
    @Mock OrderRepository repository;
    @InjectMocks OrderService service;

    @Test
    void create_persistsOrder() { /* unit test domain rules */ }
}
""",
    ),
    "skill-packs/java/quarkus/quarkus-cloud-native-apis": (
        "java",
        """// GOOD — JAX-RS resource with CDI injection and DTO response
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
""",
        """// BAD — entity returned directly, new service per request
@Path("/orders")
public class OrderResource {
    @POST
    public Order create(Order order) {
        return Order.persist(order); // leaks entity
    }
}
""",
        "application.properties",
        """quarkus.http.port=8080
quarkus.datasource.db-kind=postgresql
quarkus.hibernate-orm.database.generation=validate
quarkus.smallrye-health.root-path=/q/health
""",
    ),
    "skill-packs/java/quarkus/quarkus-kubernetes-native": (
        "yaml",
        """# GOOD — probes on Quarkus health endpoints, resource limits
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
        - name: app
          livenessProbe:
            httpGet: { path: /q/health/live, port: 8080 }
          readinessProbe:
            httpGet: { path: /q/health/ready, port: 8080 }
          resources:
            requests: { memory: "64Mi", cpu: "100m" }
            limits: { memory: "256Mi", cpu: "500m" }
""",
        """# BAD — no readiness, no limits, wrong health path
livenessProbe:
  httpGet: { path: /health, port: 8080 }
""",
        "kubernetes-deployment.yaml",
        """apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: order-service
          image: order-service:native
          ports: [{ containerPort: 8080 }]
          readinessProbe:
            httpGet: { path: /q/health/ready, port: 8080 }
""",
    ),
    "skill-packs/java/micronaut/micronaut-reactive-microservices": (
        "java",
        """// GOOD — reactive return type, injected singleton
@Controller("/api/v1/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderService orderService;

    @Get("/{id}")
    Mono<OrderResponse> get(UUID id) {
        return orderService.findById(id);
    }
}
""",
        """// BAD — blocking JDBC on Netty thread
@Get("/{id}")
Order get(UUID id) {
    return jdbcTemplate.queryForObject("...", Order.class); // blocks event loop
}
""",
        "application.yml",
        """micronaut:
  application:
    name: order-service
  server:
    port: 8080
""",
    ),
    "skill-packs/java/micronaut/micronaut-compile-time-di": (
        "java",
        """// GOOD — compile-time wired singleton with constructor injection
@Singleton
public class OrderService {
    private final OrderRepository repository;

    public OrderService(OrderRepository repository) {
        this.repository = repository;
    }

    public Order create(CreateOrderRequest request) {
        return repository.save(Order.from(request));
    }
}
""",
        """// BAD — runtime field injection / manual new
public class OrderService {
    @Inject OrderRepository repository;
    public Order create(CreateOrderRequest r) {
        return new OrderRepository().save(...); // bypasses DI
    }
}
""",
        "OrderRepository.java",
        """@Singleton
public class OrderRepository {
    private final DataSource dataSource;
    public OrderRepository(DataSource dataSource) { this.dataSource = dataSource; }
}
""",
    ),
    "skill-packs/java/jakarta-ee/jakarta-ee-enterprise-platform": (
        "java",
        """// GOOD — JAX-RS + CDI + DTO, jakarta.* imports
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
""",
        """// BAD — javax.* imports, entity in response
import javax.ws.rs.*; // wrong namespace on EE 10+
@POST
public Order create(Order order) { return orderService.save(order); }
""",
        "persistence.xml",
        """<persistence xmlns="https://jakarta.ee/xml/ns/persistence" version="3.0">
  <persistence-unit name="ordersPU" transaction-type="JTA">
    <jta-data-source>jdbc/orders</jta-data-source>
    <class>com.example.Order</class>
  </persistence-unit>
</persistence>
""",
    ),
    "skill-packs/java/hibernate/hibernate-orm-persistence": (
        "java",
        """// GOOD — lazy associations, version column, business-key equals
@Entity
@Table(name = "orders")
public class Order {
    @Id @GeneratedValue private UUID id;
    @Version private long version;
    @OneToMany(mappedBy = "order", fetch = FetchType.LAZY)
    private List<OrderLine> lines = new ArrayList<>();
}
""",
        """// BAD — EAGER collection, Lombok @Data on entity, no version
@Entity @Data
public class Order {
    @OneToMany(fetch = FetchType.EAGER)
    private List<OrderLine> lines;
}
""",
        "OrderRepository.java",
        """public interface OrderRepository extends JpaRepository<Order, UUID> {
    @EntityGraph(attributePaths = "lines")
    Optional<Order> findWithLinesById(UUID id);
}
""",
    ),
    "skill-packs/java/vaadin/vaadin-java-fullstack-ui": (
        "java",
        """// GOOD — @Route view with Binder and service injection
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
""",
        """// BAD — loads all rows in memory, business logic in UI
@Route("orders")
public class OrderListView extends VerticalLayout {
    public OrderListView(OrderRepository repo) {
        add(new Grid<>(Order.class).setItems(repo.findAll())); // OOM risk
    }
}
""",
        "OrderForm.java",
        """@Component
public class OrderForm extends FormLayout {
    private final Binder<CreateOrderRequest> binder = new Binder<>(CreateOrderRequest.class);
    public OrderForm() {
        TextField email = new TextField("Email");
        binder.forField(email).asRequired().bind(CreateOrderRequest::email, CreateOrderRequest::setEmail);
        add(email);
    }
}
""",
    ),
    "skill-packs/python/fastapi/fastapi-async-backend": (
        "py",
        """# GOOD — async route, Pydantic models, dependency injection
@router.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(
    body: CreateOrderRequest,
    service: OrderService = Depends(get_order_service),
) -> OrderResponse:
    return await service.create(body)
""",
        """# BAD — sync blocking DB in async def, no validation model
@router.post("/orders")
async def create_order(data: dict):
    return db.execute("INSERT INTO orders ...")  # blocks event loop
""",
        "schemas.py",
        """from pydantic import BaseModel, EmailStr

class CreateOrderRequest(BaseModel):
    customer_email: EmailStr

class OrderResponse(BaseModel):
    id: str
    customer_email: EmailStr
""",
    ),
    "skill-packs/python/django/django-enterprise-backend": (
        "py",
        """# GOOD — DRF viewset with serializer and select_related
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.select_related("customer").filter(tenant_id=self.request.tenant.id)
""",
        """# BAD — returns model directly, N+1 on list
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
""",
        "serializers.py",
        """from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer_email", "status"]
""",
    ),
    "skill-packs/go/gin/go-gin-rest-microservices": (
        "go",
        """// GOOD — thin handler, context passed, typed response
func (h *OrderHandler) Create(c *gin.Context) {
    var req CreateOrderRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(http.StatusBadRequest, problem(err))
        return
    }
    resp, err := h.service.Create(c.Request.Context(), req)
    if err != nil {
        c.JSON(http.StatusInternalServerError, problem(err))
        return
    }
    c.JSON(http.StatusCreated, resp)
}
""",
        """// BAD — global DB, no context, string errors
func Create(c *gin.Context) {
    db.Exec("INSERT INTO orders ...")
    c.JSON(200, "ok")
}
""",
        "handler.go",
        """type OrderHandler struct {
    service OrderService
}

func NewOrderHandler(service OrderService) *OrderHandler {
    return &OrderHandler{service: service}
}
""",
    ),
    "skill-packs/php/laravel/laravel-api-platform": (
        "php",
        """// GOOD — FormRequest validation + API Resource
class OrderController extends Controller {
    public function store(CreateOrderRequest $request, OrderService $service): OrderResource {
        return new OrderResource($service->create($request->validated()));
    }
}
""",
        """// BAD — raw request, returns Eloquent model
public function store(Request $request) {
    return Order::create($request->all());
}
""",
        "CreateOrderRequest.php",
        """class CreateOrderRequest extends FormRequest {
    public function rules(): array {
        return ['customer_email' => ['required', 'email']];
    }
}
""",
    ),
    "skill-packs/ruby/rails/rails-api-backend": (
        "rb",
        """# GOOD — strong params, policy, serializer/blueprint
class OrdersController < ApplicationController
  def create
    authorize Order
    order = OrderService.new(current_user).create(order_params)
    render json: OrderBlueprint.render(order), status: :created
  end

  private

  def order_params
    params.require(:order).permit(:customer_email)
  end
end
""",
        """# BAD — mass assignment, no policy
def create
  render json: Order.create(params[:order])
end
""",
        "order_blueprint.rb",
        """class OrderBlueprint < Blueprinter::Base
  identifier :id
  fields :customer_email, :status
end
""",
    ),
}


def patch_skill_md(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    if "## Examples And Templates" in text:
        return
    marker = "## Decision Framework"
    if marker in text:
        text = text.replace(marker, EXAMPLES_SECTION.strip() + "\n\n" + marker, 1)
    else:
        text = text.rstrip() + "\n" + EXAMPLES_SECTION
    skill_md.write_text(text, encoding="utf-8")


def main() -> None:
    for rel, (ext, good, bad, tmpl_name, tmpl_body) in PACKS.items():
        skill_dir = ROOT / rel
        if not skill_dir.exists():
            print(f"skip missing {rel}")
            continue

        examples = skill_dir / "examples"
        templates = skill_dir / "templates"
        examples.mkdir(exist_ok=True)
        templates.mkdir(exist_ok=True)

        good_name = f"good-example.{ext}" if ext != "yaml" else "good-deployment.yaml"
        bad_name = f"bad-example.{ext}" if ext != "yaml" else "bad-deployment.yaml"

        (examples / good_name).write_text(good.strip() + "\n", encoding="utf-8")
        (examples / bad_name).write_text(bad.strip() + "\n", encoding="utf-8")
        (templates / tmpl_name).write_text(tmpl_body.strip() + "\n", encoding="utf-8")

        patch_skill_md(skill_dir)
        print(f"examples added: {rel}")

    print(f"OK: updated {len(PACKS)} skill packs")


if __name__ == "__main__":
    main()
