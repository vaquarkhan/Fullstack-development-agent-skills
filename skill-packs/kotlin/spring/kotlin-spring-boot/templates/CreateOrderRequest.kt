data class CreateOrderRequest(
    @field:Email val customerEmail: String,
    @field:NotBlank val sku: String,
)
