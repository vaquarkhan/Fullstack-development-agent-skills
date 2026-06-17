// BAD — catch-all proxy, no timeout, forwards cookies to upstream
.route(r -> r.path("/**").uri("http://backend:8080"))
