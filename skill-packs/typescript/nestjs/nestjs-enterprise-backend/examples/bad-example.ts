// BAD — fat controller, any type, no validation pipe
@Controller('orders')
export class OrdersController {
  @Post()
  create(@Body() body: any) {
    return prisma.order.create({ data: body });
  }
}
