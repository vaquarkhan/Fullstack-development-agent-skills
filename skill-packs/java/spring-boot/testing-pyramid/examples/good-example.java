// GOOD — @WebMvcTest slice for controller only
@WebMvcTest(OrderController.class)
class OrderControllerTest {
    @Autowired MockMvc mockMvc;
    @MockitoBean OrderService orderService;

    @Test
    void create_returns201() throws Exception {
        when(orderService.create(any())).thenReturn(new Order(UUID.randomUUID()));
        mockMvc.perform(post("/api/v1/orders").contentType(APPLICATION_JSON)
                .content("{"customerEmail":"a@b.com"}"))
            .andExpect(status().isCreated());
    }
}
