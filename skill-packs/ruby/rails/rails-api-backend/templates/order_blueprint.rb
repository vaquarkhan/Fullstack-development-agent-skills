class OrderBlueprint < Blueprinter::Base
  identifier :id
  fields :customer_email, :status
end
