import { IsEmail, IsNotEmpty } from 'class-validator';

export class CreateOrderDto {
  @IsEmail()
  customerEmail!: string;

  @IsNotEmpty()
  sku!: string;
}
