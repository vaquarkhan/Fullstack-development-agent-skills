class CreateOrderRequest extends FormRequest {
    public function rules(): array {
        return ['customer_email' => ['required', 'email']];
    }
}
