fun Application.module() {
    install(ContentNegotiation) { json() }
    install(Authentication) { jwt { /* configure */ } }
    install(StatusPages) { exception<ValidationException> { call, cause -> /* 400 */ } }
    routing {
        route("/api/v1") { orderRoutes() }
    }
}
