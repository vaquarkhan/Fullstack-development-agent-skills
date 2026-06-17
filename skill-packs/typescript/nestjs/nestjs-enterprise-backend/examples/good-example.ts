// GOOD — module boundaries, DTO validation, service injection
@Controller('orders')
export class OrdersController {
  constructor(private readonly orders: OrdersService) {}

  @Post()
  @HttpCode(201)
  create(@Body() dto: CreateOrderDto): Promise<OrderResponseDto> {
    return this.orders.create(dto);
  }
}
