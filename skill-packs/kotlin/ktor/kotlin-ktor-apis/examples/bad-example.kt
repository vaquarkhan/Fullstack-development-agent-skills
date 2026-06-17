// BAD — raw map, no validation, runBlocking JDBC
post("/orders") {
    val body = call.receive<Map<String, Any>>()
    runBlocking { jdbc.update("INSERT ...") }
    call.respond(mapOf("ok" to true))
}
