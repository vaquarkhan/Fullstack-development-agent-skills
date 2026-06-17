// GOOD — axum handler with State, typed Json, error mapping
async fn create_order(
    State(state): State<AppState>,
    Json(payload): Json<CreateOrderRequest>,
) -> Result<(StatusCode, Json<OrderResponse>), AppError> {
    let order = state.orders.create(payload).await?;
    Ok((StatusCode::CREATED, Json(order.into())))
}
