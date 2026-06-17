// GOOD — explicit route with timeout and strip sensitive headers
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
