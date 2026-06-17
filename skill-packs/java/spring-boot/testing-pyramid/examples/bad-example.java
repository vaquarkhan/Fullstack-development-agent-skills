// BAD — @SpringBootTest for every controller assertion (slow, brittle)
@SpringBootTest(webEnvironment = RANDOM_PORT)
class OrderControllerTest { /* loads entire context */ }
