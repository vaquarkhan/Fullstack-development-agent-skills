# GOOD — strong params, policy, serializer/blueprint
class OrdersController < ApplicationController
  def create
    authorize Order
    order = OrderService.new(current_user).create(order_params)
    render json: OrderBlueprint.render(order), status: :created
  end

  private

  def order_params
    params.require(:order).permit(:customer_email)
  end
end
