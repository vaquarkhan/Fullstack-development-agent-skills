# BAD — mass assignment, no policy
def create
  render json: Order.create(params[:order])
end
