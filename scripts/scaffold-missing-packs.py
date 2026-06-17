#!/usr/bin/env python3
"""Scaffold planned skill packs from docs/fullstack-skills-catalog.md roadmap."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# rel_skill_dir -> (ext, good, bad, template_name, template_body, skill_md)
PACKS: dict[str, tuple[str, str, str, str, str, str]] = {
    "skill-packs/typescript/nestjs/nestjs-enterprise-backend": (
        "ts",
        """// GOOD — module boundaries, DTO validation, service injection
@Controller('orders')
export class OrdersController {
  constructor(private readonly orders: OrdersService) {}

  @Post()
  @HttpCode(201)
  create(@Body() dto: CreateOrderDto): Promise<OrderResponseDto> {
    return this.orders.create(dto);
  }
}
""",
        """// BAD — fat controller, any type, no validation pipe
@Controller('orders')
export class OrdersController {
  @Post()
  create(@Body() body: any) {
    return prisma.order.create({ data: body });
  }
}
""",
        "create-order.dto.ts",
        """import { IsEmail, IsNotEmpty } from 'class-validator';

export class CreateOrderDto {
  @IsEmail()
  customerEmail!: string;

  @IsNotEmpty()
  sku!: string;
}
""",
        """---
name: nestjs-enterprise-backend
description: Build enterprise NestJS APIs with modular architecture, class-validator DTOs, TypeORM/Prisma persistence, guards, interceptors, and OpenAPI. Use for deep TypeScript backend microservice implementation beyond cross-stack patterns.
disable-model-invocation: true
---

# NestJS Enterprise Backend

## Use When

- Implementing production NestJS APIs with modular domain boundaries
- Wiring auth guards, validation pipes, interceptors, and OpenAPI in NestJS
- Teams need NestJS-specific patterns beyond `skills/nodejs-nestjs-backend-microservices`

## Workflow

1. Organize feature modules (controller, service, repository/DTO) per domain.
2. Define DTOs with class-validator; enable global ValidationPipe with whitelist.
3. Add guards for JWT/API keys; policies via custom decorators or CASL.
4. Configure TypeORM/Prisma with migrations and transaction boundaries in services.
5. Document OpenAPI via @ApiTags and generate client SDKs for frontend consumers.
6. Test with @nestjs/testing unit tests and supertest e2e with test DB.

## Required Checks

- ValidationPipe forbids unknown properties (whitelist + forbidNonWhitelisted)
- Services own transactions; controllers stay thin
- ConfigModule loads secrets from env — no secrets in source
- E2E tests cover auth failure and validation error envelopes

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer feature modules over god AppModule imports.
- Use CQRS (@nestjs/cqrs) only when read/write models genuinely diverge.
- Cache with explicit TTL and invalidation keys — not ad-hoc Map in service.
- Bull/BullMQ for durable jobs; @Cron only for lightweight schedulers.

## Common Rationalizations And Rebuttals

- "DTOs are optional with TypeScript." -> Runtime validation catches bad clients; use DTOs at boundary.
- "Prisma in controller is faster." -> Leaks persistence; breaks testing and module boundaries.
- "Global exception filter later." -> Inconsistent error shapes break API consumers early.

## Evidence Pack

- OpenAPI diff for changed endpoints
- E2E test output for auth and validation matrix
- Module dependency graph (no circular imports)
- Migration script with rollback note

## Exit Criteria

- Modules are bounded; controllers delegate to services
- Validation, auth, and error envelopes are consistent
- Tests cover happy path and boundary failures
""",
    ),
    "skill-packs/dotnet/aspnetcore/aspnetcore-minimal-apis": (
        "cs",
        """// GOOD — minimal API with typed handler, Results pattern, auth
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
""",
        """// BAD — anonymous object, no auth, sync blocking
app.MapPost("/orders", (HttpContext ctx) =>
{
    var body = ctx.Request.ReadFromJsonAsync<object>().Result;
    return new { ok = true, data = body };
});
""",
        "Program.cs",
        """var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddAuthentication().AddJwtBearer();
builder.Services.AddAuthorization();
builder.Services.AddScoped<IOrderService, OrderService>();

var app = builder.Build();
app.UseAuthentication();
app.UseAuthorization();
// Map endpoints here
app.Run();
""",
        """---
name: aspnetcore-minimal-apis
description: Build ASP.NET Core minimal APIs with endpoint filters, JWT auth, OpenAPI, and clean handler delegation. Use for lightweight .NET microservices and BFF endpoints without MVC ceremony.
disable-model-invocation: true
---

# ASP.NET Core Minimal APIs

## Use When

- Building .NET 8+ minimal API services or BFF layers
- Teams want thin Program.cs with endpoint groups and filters
- Cross-stack skill `dotnet-aspnet-core-microservices` needs .NET-specific implementation depth

## Workflow

1. Register services in DI (DbContext, handlers, auth).
2. Group endpoints with MapGroup and route prefixes (/api/v1).
3. Use typed request records and IResult/Results for responses.
4. Add endpoint filters for validation, logging, and problem details.
5. Configure JWT bearer or Entra ID; apply RequireAuthorization per route.
6. Test with WebApplicationFactory and integration tests.

## Required Checks

- CancellationToken forwarded to all async I/O
- ProblemDetails for errors — consistent with RFC 9457
- OpenAPI documents auth schemes and error responses
- No .Result or .Wait() on async calls in request path

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer minimal APIs for small services; MVC/controllers when view-heavy or complex model binding.
- Use IMediator (MediatR) when handlers grow — keep MapPost one-liners as entry only.
- Health checks at /health; readiness includes DB ping.
- Use IOptions<T> for config — not static ConfigurationManager reads in handlers.

## Common Rationalizations And Rebuttals

- "Minimal APIs are only for demos." -> Production-ready with filters, auth, and testing patterns.
- "One file is fine." -> Split endpoint groups by domain as service grows.
- "Exception middleware is enough." -> Validate at boundary; return typed validation problems.

## Evidence Pack

- OpenAPI snapshot with security schemes
- Integration test output for authorized vs anonymous calls
- Endpoint filter unit test for validation failures
- Health/readiness probe configuration

## Exit Criteria

- Endpoints are typed, authorized, and documented
- Async and cancellation used throughout request path
- Error responses match API contract
""",
    ),
    "skill-packs/dotnet/efcore/ef-core-persistence": (
        "cs",
        """// GOOD — async repository, AsNoTracking for reads, explicit includes
public async Task<OrderDto?> GetByIdAsync(Guid id, CancellationToken ct)
{
    return await _db.Orders
        .AsNoTracking()
        .Where(o => o.Id == id)
        .Select(o => new OrderDto(o.Id, o.Status))
        .FirstOrDefaultAsync(ct);
}
""",
        """// BAD — tracking leak, sync ToList, loads entire graph
public Order Get(Guid id) =>
    _db.Orders.Include(o => o.Items).Include(o => o.Customer).First(o => o.Id == id);
""",
        "OrderConfiguration.cs",
        """public class OrderConfiguration : IEntityTypeConfiguration<Order>
{
    public void Configure(EntityTypeBuilder<Order> builder)
    {
        builder.HasKey(o => o.Id);
        builder.Property(o => o.Status).HasMaxLength(32).IsRequired();
        builder.HasIndex(o => o.TenantId);
    }
}
""",
        """---
name: ef-core-persistence
description: Model relational domains with EF Core 8, fluent configurations, migrations, interceptors, and performant queries. Use for .NET persistence layers with zero-downtime migration discipline.
disable-model-invocation: true
---

# EF Core Persistence

## Use When

- Implementing EF Core data access in ASP.NET Core services
- Designing entities, configurations, migrations, and query performance
- Pairing with `aspnetcore-minimal-apis` or `skills/dotnet-aspnet-core-microservices`

## Workflow

1. Define entities and IEntityTypeConfiguration classes per aggregate.
2. Register DbContext with pooled factory; configure connection resiliency.
3. Use migrations with review for locking — prefer expand/contract for large tables.
4. Implement repositories or specifications; project to DTOs in queries.
5. Add interceptors for auditing, soft delete, or multi-tenant filters.
6. Test with Testcontainers SQL Server/Postgres or in-memory only for unit scope.

## Required Checks

- No N+1 — use Select projections or explicit Include with purpose
- AsNoTracking on read-only queries
- Concurrency tokens on contested aggregates
- Migrations tested against production-like row counts when tables are large

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer configurations over data annotations for team consistency.
- Owned types for value objects; avoid primitive obsession on entities.
- Raw SQL only for reporting or bulk ops — document and parameterize.
- Split read models (Dapper/raw SQL) when EF projections are insufficient.

## Common Rationalizations And Rebuttals

- "Lazy loading is convenient." -> Causes N+1 in APIs; use explicit loading or projections.
- "One DbContext for everything." -> Bounded contexts may need separate contexts.
- "Migrate in app startup always." -> Run migrations in CI/CD job with rollback plan.

## Evidence Pack

- Migration script with expand/contract notes
- Query plan or EF logging proof for critical list endpoints
- Concurrency conflict test output
- Interceptor audit sample (created/updated by)

## Exit Criteria

- Queries are tracked appropriately; hot paths avoid N+1
- Migrations are safe for production table sizes
- Multi-tenant or soft-delete rules enforced at persistence layer
""",
    ),
    "skill-packs/rust/axum/rust-axum-microservices": (
        "rs",
        """// GOOD — axum handler with State, typed Json, error mapping
async fn create_order(
    State(state): State<AppState>,
    Json(payload): Json<CreateOrderRequest>,
) -> Result<(StatusCode, Json<OrderResponse>), AppError> {
    let order = state.orders.create(payload).await?;
    Ok((StatusCode::CREATED, Json(order.into())))
}
""",
        """// BAD — unwrap panics, no error type, blocking call
async fn create_order(Json(p): Json<serde_json::Value>) -> String {
    let conn = db::connect().unwrap();
    conn.execute("INSERT ...").unwrap();
    "ok".into()
}
""",
        "main.rs",
        """#[tokio::main]
async fn main() {
    let state = AppState::new().await.expect("init state");
    let app = Router::new()
        .route("/health", get(health))
        .route("/api/v1/orders", post(create_order))
        .with_state(state);
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
""",
        """---
name: rust-axum-microservices
description: Build Rust HTTP microservices with Axum, Tower middleware, SQLx/SeaORM, structured errors, and Tokio async runtime. Use for high-performance Rust APIs and edge services.
disable-model-invocation: true
---

# Rust Axum Microservices

## Use When

- Building Rust backend APIs with Axum and Tokio
- Teams need memory-safe, high-throughput services with explicit error handling
- Replacing or complementing Go/Node edge services with Rust

## Workflow

1. Structure crates: domain, application, infrastructure, api binary.
2. Define AppState with Arc-wrapped pools and services; inject via State extractor.
3. Map errors to IntoResponse with consistent problem JSON.
4. Add Tower layers: trace, timeout, compression, auth.
5. Use SQLx compile-time queries or SeaORM with migrations.
6. Test handlers with axum::test and integration tests with testcontainers.

## Required Checks

- No unwrap/expect in request handlers
- Timeouts on outbound HTTP and DB pool acquire
- SQL parameterized — sqlx macros or bind parameters only
- Graceful shutdown on SIGTERM via with_graceful_shutdown

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer thiserror/anyhow boundary pattern — domain errors vs internal errors.
- Keep handlers thin; business logic in async service functions.
- Use tracing spans with request IDs propagated from middleware.
- Actix-web only when team already standardized — Axum + Tower is default here.

## Common Rationalizations And Rebuttals

- "unwrap is fine for prototypes." -> Panics become 500 storms under load; use Result.
- "Clone Arc everywhere is free." -> Profile hot paths; prefer references in service layer.
- "Blocking std::fs in async fn." -> Use tokio::fs or spawn_blocking.

## Evidence Pack

- Handler tests with mock services
- Trace sample with request_id through DB call
- Load test summary for target RPS
- Graceful shutdown behavior under in-flight requests

## Exit Criteria

- Handlers return typed errors mapped to HTTP problem responses
- Observability and timeouts configured on all I/O boundaries
- Service passes clippy and fmt in CI
""",
    ),
    "skill-packs/kotlin/ktor/kotlin-ktor-apis": (
        "kt",
        """// GOOD — Ktor route with validation, service call, status mapping
post("/api/v1/orders") {
    val request = call.receive<CreateOrderRequest>()
    val order = orderService.create(request)
    call.respond(HttpStatusCode.Created, order.toResponse())
}
""",
        """// BAD — raw map, no validation, runBlocking JDBC
post("/orders") {
    val body = call.receive<Map<String, Any>>()
    runBlocking { jdbc.update("INSERT ...") }
    call.respond(mapOf("ok" to true))
}
""",
        "Application.kt",
        """fun Application.module() {
    install(ContentNegotiation) { json() }
    install(Authentication) { jwt { /* configure */ } }
    install(StatusPages) { exception<ValidationException> { call, cause -> /* 400 */ } }
    routing {
        route("/api/v1") { orderRoutes() }
    }
}
""",
        """---
name: kotlin-ktor-apis
description: Build Kotlin backend APIs with Ktor, kotlinx.serialization, coroutines, and Koin/DI. Use for lightweight JVM services without Spring Boot ceremony.
disable-model-invocation: true
---

# Kotlin Ktor APIs

## Use When

- Building Kotlin HTTP APIs with Ktor instead of Spring Boot
- Coroutine-first services with kotlinx.serialization JSON
- Teams want minimal framework surface on the JVM

## Workflow

1. Configure Application.module with plugins: ContentNegotiation, Authentication, StatusPages.
2. Define @Serializable request/response models with validation.
3. Organize routes in extension functions per domain.
4. Inject services via Koin or manual composition root.
5. Use Exposed/Flyway or R2DBC drivers for persistence.
6. Test with testApplication and mocked services.

## Required Checks

- No runBlocking in request pipeline — use suspend handlers
- Serialization ignores unknown keys policy documented
- Auth plugin validates issuer/audience for JWT
- StatusPages map domain exceptions to consistent error JSON

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer Ktor for API-only Kotlin services; Spring when ecosystem integration dominates.
- Use CIO engine for prototyping; Netty for production concurrency.
- HttpClient with timeouts for outbound calls.
- Structured logging via kotlin-logging + logback JSON encoder.

## Common Rationalizations And Rebuttals

- "Ktor is only for prototypes." -> Production patterns exist for auth, testing, and metrics.
- "Blocking JDBC in suspend is fine." -> Blocks dispatcher; use R2DBC or dedicated pool.
- "Map responses are flexible." -> Breaks contract; use typed @Serializable models.

## Evidence Pack

- testApplication route tests including 401/422 cases
- kotlinx.serialization schema diff for API changes
- Coroutine dispatcher audit (no blocking on Default)
- JWT validation test vectors

## Exit Criteria

- Routes are suspend-based with typed models
- Errors and auth behavior match API contract
- Tests cover validation and authorization paths
""",
    ),
    "skill-packs/kotlin/spring/kotlin-spring-boot": (
        "kt",
        """// GOOD — Kotlin data class DTO, coroutine controller, null-safe service
@RestController
@RequestMapping("/api/v1/orders")
class OrderController(private val service: OrderService) {
    @PostMapping
    suspend fun create(@Valid @RequestBody request: CreateOrderRequest): ResponseEntity<OrderResponse> {
        val order = service.create(request)
        return ResponseEntity.status(HttpStatus.CREATED).body(order.toResponse())
    }
}
""",
        """// BAD — platform types, nullable abuse, blocking call in suspend
@RestController
class OrderController {
    @PostMapping("/orders")
    suspend fun create(@RequestBody body: Map<String, Any?>): Any? {
        return jdbcTemplate.queryForMap("SELECT * FROM orders LIMIT 1")
    }
}
""",
        "CreateOrderRequest.kt",
        """data class CreateOrderRequest(
    @field:Email val customerEmail: String,
    @field:NotBlank val sku: String,
)
""",
        """---
name: kotlin-spring-boot
description: Build Spring Boot services in idiomatic Kotlin with coroutines, data classes, extension functions, and Spring AI integration. Use when JVM teams prefer Kotlin over Java for Spring microservices.
disable-model-invocation: true
---

# Kotlin Spring Boot

## Use When

- Building Spring Boot microservices in Kotlin (not Java)
- Using suspend controllers, coroutines with WebFlux or MVC + coroutines
- Pairing with `skill-packs/java/spring-boot/` skills for Spring ecosystem depth

## Workflow

1. Use Kotlin data classes for DTOs with jakarta.validation annotations.
2. Prefer constructor injection and `val` immutability in services.
3. Enable coroutines for I/O-bound service methods where supported.
4. Configure Jackson Kotlin module or kotlinx.serialization consistently.
5. Reuse Spring Boot patterns: Actuator, ProblemDetail, Testcontainers.
6. Test with @WebMvcTest and coroutine test utilities (runTest).

## Required Checks

- No platform types (String!) in public API models
- Null-safety enforced at boundaries — avoid Map<String, Any?>
- Spring Security Kotlin DSL or Java config — document chosen style
- Detekt/ktlint in CI for consistent style

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Share patterns with Java Spring Boot pack — differ only in Kotlin idioms.
- Use extension functions for mapping, not inheritance-heavy hierarchies.
- Flow API for streaming when paired with WebFlux or SSE endpoints.
- Spring AI ChatClient works identically — prefer Kotlin data classes for prompts.

## Common Rationalizations And Rebuttals

- "Java patterns pasted to Kotlin are fine." -> Use data classes, sealed errors, and coroutines idiomatically.
- "!! operator saves time." -> Model nullability explicitly at API boundary.
- "Skip Detekt." -> Kotlin style drift makes reviews harder at scale.

## Evidence Pack

- Detekt/ktlint CI output
- Coroutine controller integration test results
- DTO schema diff for API changes
- Comparison note linking to relevant Java Spring Boot skill

## Exit Criteria

- Kotlin idioms used throughout service and API layers
- Spring Boot operational baselines (health, metrics, security) met
- Tests cover suspend endpoints and validation failures
""",
    ),
    "skill-packs/flutter/flutter-fullstack-mobile": (
        "dart",
        """// GOOD — repository pattern, typed API client, error mapping
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
""",
        """// BAD — http call in widget, no error handling, dynamic JSON
ElevatedButton(
  onPressed: () async {
    final r = await http.post(Uri.parse('$base/orders'), body: jsonEncode(fields));
    setState(() => order = jsonDecode(r.body));
  },
  child: Text('Submit'),
)
""",
        "api_client.dart",
        """class ApiClient {
  ApiClient({required this.baseUrl, required this.tokenProvider});
  final String baseUrl;
  final Future<String?> Function() tokenProvider;

  Future<ApiResponse> get(String path) async { /* dio/http with auth header */ }
}
""",
        """---
name: flutter-fullstack-mobile
description: Build Flutter mobile clients with clean architecture, Riverpod/Bloc state, typed REST/GraphQL clients, offline sync, and secure token storage. Use for fullstack mobile delivery paired with backend APIs.
disable-model-invocation: true
---

# Flutter Fullstack Mobile

## Use When

- Building Flutter apps consuming REST or GraphQL backends
- Implementing auth, offline-first sync, or real-time features on mobile
- Pairing with `skills/react-native-fullstack-integration` patterns for Flutter stacks

## Workflow

1. Layer app: presentation (widgets), domain (entities/use cases), data (repositories).
2. Choose Riverpod or Bloc for state; keep widgets dumb.
3. Implement ApiClient with interceptors for auth refresh and correlation IDs.
4. Use secure_storage for tokens; never SharedPreferences for secrets.
5. Handle offline with local DB (Drift/Isar) and sync queue patterns.
6. Test repositories with mock clients; widget tests for critical flows.

## Required Checks

- No API keys or secrets in source — use flavors and CI injection
- Token refresh handled centrally — not per-screen ad hoc
- List views paginated — no unbounded fetch in build()
- Accessibility semantics on interactive widgets (Semantics)

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer repository abstraction over calling http in widgets.
- GraphQL when schema is stable and mobile needs flexible queries; REST for simpler CRUD.
- go_router for navigation with deep link handling.
- Feature flags via remote config for risky mobile releases.

## Common Rationalizations And Rebuttals

- "setState in screen is fastest." -> Untestable; use state management and repositories.
- "Store JWT in SharedPreferences." -> Insecure on rooted devices; use secure_storage.
- "Load all data on startup." -> Slow cold start; paginate and lazy-load.

## Evidence Pack

- Widget/repository test output
- Offline sync conflict resolution notes
- Auth refresh sequence diagram
- App size and startup time baseline

## Exit Criteria

- UI decoupled from HTTP; errors mapped to user-visible states
- Auth and secrets handled securely
- Critical flows covered by automated tests
""",
    ),
    "skill-packs/data/mongodb/mongodb-document-modeling": (
        "js",
        """// GOOD — bounded document, indexed query, projection
db.orders.createIndex({ tenantId: 1, createdAt: -1 });
const orders = await db.collection('orders')
  .find({ tenantId, status: 'open' })
  .project({ _id: 1, status: 1, totalCents: 1 })
  .sort({ createdAt: -1 })
  .limit(50)
  .toArray();
""",
        """// BAD — unbounded array growth, no index, full document scan
await db.collection('orders').updateOne(
  { _id: id },
  { $push: { events: { type: 'note', text: hugeLog } } } // unbounded array
);
const all = await db.collection('orders').find({}).toArray();
""",
        "order-schema.json",
        """{
  "bsonType": "object",
  "required": ["tenantId", "status", "createdAt"],
  "properties": {
    "tenantId": { "bsonType": "string" },
    "status": { "enum": ["open", "paid", "cancelled"] },
    "totalCents": { "bsonType": "int" }
  }
}
""",
        """---
name: mongodb-document-modeling
description: Design MongoDB document schemas, indexes, aggregation pipelines, and multi-tenant patterns with operational safety. Use for document-store backends in fullstack applications.
disable-model-invocation: true
---

# MongoDB Document Modeling

## Use When

- Modeling domains in MongoDB (Atlas or self-hosted)
- Designing embed vs reference, indexes, and aggregation for app queries
- Pairing with Node, Java, Python, or Go services using MongoDB drivers

## Workflow

1. Map access patterns first — one document shape per dominant query pattern.
2. Choose embed vs reference; cap array growth; use bucketing for high-volume subdocs.
3. Define JSON Schema validation and compound indexes for hot queries.
4. Implement transactions only when cross-document invariants require them.
5. Plan sharding keys early if tenant scale warrants it.
6. Monitor slow queries and index hit rates in Atlas or profiler.

## Required Checks

- Every production query uses supporting index (explain plan reviewed)
- Tenant isolation enforced in query filter — not only application logic
- Unbounded arrays avoided or capped with archival strategy
- Write concern and read concern documented per use case

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Embed when data is read together and bounded; reference when shared or unbounded.
- Prefer aggregation pipeline for analytics; avoid $lookup storms without indexes.
- Change streams for CDC to search/cache — not polling entire collections.
- Use transactions sparingly; design atomic single-document updates when possible.

## Common Rationalizations And Rebuttals

- "Mongo is schema-less." -> Undocumented schema causes production drift; use validation.
- "Indexes slow writes." -> Missing indexes slow reads more; right-size indexes per query.
- "ObjectId everywhere." -> Use UUID strings for client-facing IDs when integrating APIs.

## Evidence Pack

- explain() output for top 5 queries
- Index list with rationale
- Schema validation rules
- Tenant isolation test cases

## Exit Criteria

- Hot queries are indexed and tenant-scoped
- Document shapes match access patterns without unbounded growth
- Operational monitoring for slow ops is configured
""",
    ),
    "skill-packs/data/elasticsearch/elasticsearch-search-patterns": (
        "json",
        """// GOOD — explicit mappings, bulk index, search with filters + pagination
PUT orders-v1
{
  "mappings": {
    "properties": {
      "tenantId": { "type": "keyword" },
      "status": { "type": "keyword" },
      "createdAt": { "type": "date" },
      "customerEmail": { "type": "text", "fields": { "raw": { "type": "keyword" } } }
    }
  }
}
""",
        """// BAD — dynamic mapping surprises, wildcard query on text field, no tenant filter
GET orders/_search
{
  "query": { "query_string": { "query": "*"+ userInput +"*" } }
}
""",
        "search-request.json",
        """{
  "from": 0,
  "size": 20,
  "query": {
    "bool": {
      "filter": [{ "term": { "tenantId": "{{tenantId}}" } }],
      "must": [{ "match": { "customerEmail": "{{q}}" } }]
    }
  },
  "sort": [{ "createdAt": "desc" }]
}
""",
        """---
name: elasticsearch-search-patterns
description: Implement Elasticsearch/OpenSearch indexing, mappings, analyzers, and secure search APIs with sync from primary databases. Use for full-text search, faceted browse, and observability log search in fullstack apps.
disable-model-invocation: true
---

# Elasticsearch Search Patterns

## Use When

- Adding full-text or faceted search to a fullstack product
- Syncing Postgres/Mongo data to Elasticsearch via CDC or outbox
- Building admin search UIs with filters, sorting, and pagination

## Workflow

1. Define index mappings explicitly — avoid dynamic mapping in production.
2. Choose analyzers per field (keyword vs text, subfields for sort/raw).
3. Implement bulk indexing with backoff; version indexes for reindex (alias swap).
4. Query with bool filters for tenant isolation; never trust client-side filters alone.
5. Expose search API with max result window and query complexity limits.
6. Monitor cluster health, shard sizing, and slow query logs.

## Required Checks

- tenantId (or equivalent) in every search filter
- Painless scripts reviewed — no unbounded script complexity
- Reindex playbook documented (alias cutover, rollback)
- User input sanitized — no leading wildcard queries on analyzed text

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Elasticsearch for search/browse; primary DB remains source of truth.
- Use ingest pipelines for denormalization; keep sync idempotent.
- OpenSearch compatible patterns when on AWS — document divergence if any.
- Consider managed (Elastic Cloud, OpenSearch Serverless) vs self-hosted ops cost.

## Common Rationalizations And Rebuttals

- "Dynamic mapping is fine early." -> Mapping explosions break sorting and aggregations later.
- "Search DB can skip auth." -> Tenant leaks via search are critical; filter in query.
- "Reindex live cluster in place." -> Use new index + alias swap for zero-downtime reindex.

## Evidence Pack

- Mapping JSON and analyzer rationale
- Bulk reindex runbook with alias swap steps
- Search API load test at target QPS
- Sample slow query log remediation

## Exit Criteria

- Indexes are versioned; reindex path is tested
- Search API enforces tenant scope and pagination limits
- Sync from primary store is idempotent and monitored
""",
    ),
    "skill-packs/ai/langchain/langchain-agent-orchestration": (
        "py",
        """# GOOD — bounded tool loop, structured output, timeout on LLM call
@tool
def lookup_order(order_id: str) -> str:
    \"\"\"Fetch order status by id.\"\"\"
    return order_service.get_status(order_id)

agent = create_react_agent(llm, tools=[lookup_order], checkpointer=memory)
result = agent.invoke(
    {"messages": [("user", query)]},
    config={"recursion_limit": 8, "timeout": 30},
)
""",
        """# BAD — unbounded loop, arbitrary code exec, no tool schema
while True:
    response = llm(f"Do anything to answer: {user_input}")
    exec(response)  # never
""",
        "tools.py",
        """from langchain_core.tools import tool

@tool
def search_docs(query: str) -> str:
    \"\"\"Search internal documentation.\"\"\"
    return retriever.invoke(query)
""",
        """---
name: langchain-agent-orchestration
description: Build LangChain/LangGraph agents with tool registries, memory checkpointers, structured outputs, and production guardrails. Use for Python backend AI orchestration beyond generic LLM integration skills.
disable-model-invocation: true
---

# LangChain Agent Orchestration

## Use When

- Implementing multi-step AI agents in Python with LangChain or LangGraph
- Wiring tools, memory, human-in-the-loop, and eval hooks
- Pairing with `skills/ai-llm-integration-in-fullstack-apps` for Python depth

## Workflow

1. Define tools with explicit schemas and docstrings — one capability per tool.
2. Choose graph (LangGraph) for branching; ReAct for simpler loops.
3. Set recursion_limit, timeouts, and max tokens on LLM calls.
4. Persist state with checkpointer (Redis/Postgres) for resumable sessions.
5. Log prompts, tool calls, and latencies with PII redaction.
6. Evaluate with golden datasets before prompt/tool changes ship.

## Required Checks

- No arbitrary code execution tools in production without sandbox
- Tool inputs validated; outputs truncated before re-prompting
- Human approval step for destructive or billing actions
- Fallback response when LLM or tool chain fails

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- LangGraph when flows have branches, retries, or human gates.
- Structured output (Pydantic) for machine-consumed responses.
- RAG retriever behind dedicated search tool — not raw DB in prompt.
- Separate dev/staging LLM keys and rate limits per tenant.

## Common Rationalizations And Rebuttals

- "More tools make agents smarter." -> Tool sprawl confuses routing; curate minimal set.
- "Unlimited recursion fixes hard tasks." -> Causes cost loops; cap steps and budget.
- "Prompt logging is enough observability." -> Trace tool latency and failure rates too.

## Evidence Pack

- Eval run scores on golden questions
- Trace with tool spans and redacted prompts
- Recursion/timeout test proving loop termination
- Human-in-the-loop audit for sensitive actions

## Exit Criteria

- Agent terminates within configured limits
- Tools are schema-safe and authorization-checked
- Observability and eval gates pass before production enablement
""",
    ),
    "skill-packs/ai/vercel-ai-sdk/vercel-ai-sdk-streaming": (
        "ts",
        """// GOOD — streamText with tools, onFinish logging, abort signal
const result = streamText({
  model: openai('gpt-4o'),
  system: systemPrompt,
  messages,
  tools: { lookupOrder: orderTool },
  maxSteps: 5,
  abortSignal: req.signal,
  onFinish: ({ usage, finishReason }) => audit.log({ usage, finishReason }),
});
return result.toDataStreamResponse();
""",
        """// BAD — no streaming backpressure, secrets in client, unlimited steps
const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });
export default async function handler(req, res) {
  const completion = await openai.chat.completions.create({ model: 'gpt-4', messages: req.body.messages });
  res.json(completion); // blocks, exposes key if misconfigured
}
""",
        "route.ts",
        """import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';

export async function POST(req: Request) {
  const { messages } = await req.json();
  const result = streamText({
    model: openai('gpt-4o'),
    messages,
    abortSignal: req.signal,
  });
  return result.toDataStreamResponse();
}
""",
        """---
name: vercel-ai-sdk-streaming
description: Build streaming AI features in Next.js with Vercel AI SDK, tool calling, RSC/UI hooks, and edge-safe API routes. Use for TypeScript fullstack AI UX with React Server Components.
disable-model-invocation: true
---

# Vercel AI SDK Streaming

## Use When

- Implementing streaming chat or copilot UX in Next.js App Router
- Using Vercel AI SDK (ai package) with OpenAI, Anthropic, or custom providers
- Pairing with `skills/nextjs-app-router-and-streaming-ui` and `skills/ai-llm-integration-in-fullstack-apps`

## Workflow

1. Keep provider API keys server-side only — Route Handlers or server actions.
2. Use streamText/generateText with typed tools and maxSteps limits.
3. Wire useChat/useAssistant on client with optimistic UI and error states.
4. Pass abortSignal from request for client disconnect cancellation.
5. Log usage in onFinish; rate limit per user/session at edge or API.
6. Test streaming contracts with integration tests and mock language model.

## Required Checks

- API keys never imported in client components
- maxSteps and token budgets configured per endpoint
- Tool calls authorized per user — not global admin tools
- Stream errors surfaced to UI — not silent hangs

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- streamText for chat UX; generateObject for structured form fill.
- Edge runtime only when latency dominates and deps are compatible.
- Persist messages server-side for compliance — not only browser state.
- AI SDK UI components for rapid UX; headless hooks for custom design systems.

## Common Rationalizations And Rebuttals

- "Client-side OpenAI is simpler." -> Exposes keys and bypasses auth; always server proxy.
- "Unlimited tool steps." -> Runaway cost; cap steps and tool allowlist.
- "Streaming skips validation." -> Validate tool inputs/outputs same as REST APIs.

## Evidence Pack

- Route handler test with mock stream
- Rate limit configuration and burst test
- UX recording of error/retry behavior
- Token usage dashboard sample per feature

## Exit Criteria

- Streaming chat works with abort and error handling
- Keys and auth remain server-side
- Tool calling respects user authorization and step limits
""",
    ),
}


def write_pack(rel: str, ext: str, good: str, bad: str, tmpl_name: str, tmpl_body: str, skill_md: str) -> None:
    skill_dir = ROOT / rel
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(skill_md.strip() + "\n", encoding="utf-8")

    examples = skill_dir / "examples"
    templates = skill_dir / "templates"
    examples.mkdir(exist_ok=True)
    templates.mkdir(exist_ok=True)

    good_name = f"good-example.{ext}"
    bad_name = f"bad-example.{ext}"
    if ext == "json":
        good_name = "good-mapping.json"
        bad_name = "bad-query.json"

    (examples / good_name).write_text(good.strip() + "\n", encoding="utf-8")
    (examples / bad_name).write_text(bad.strip() + "\n", encoding="utf-8")
    (templates / tmpl_name).write_text(tmpl_body.strip() + "\n", encoding="utf-8")


def main() -> None:
    for rel, (ext, good, bad, tmpl_name, tmpl_body, skill_md) in PACKS.items():
        write_pack(rel, ext, good, bad, tmpl_name, tmpl_body, skill_md)
        print(f"created {rel}")
    print(f"OK: scaffolded {len(PACKS)} missing skill packs")


if __name__ == "__main__":
    main()
