from pydantic import BaseModel, EmailStr

class CreateOrderRequest(BaseModel):
    customer_email: EmailStr

class OrderResponse(BaseModel):
    id: str
    customer_email: EmailStr
