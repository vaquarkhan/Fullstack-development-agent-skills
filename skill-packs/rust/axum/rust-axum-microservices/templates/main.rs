#[tokio::main]
async fn main() {
    let state = AppState::new().await.expect("init state");
    let app = Router::new()
        .route("/health", get(health))
        .route("/api/v1/orders", post(create_order))
        .with_state(state);
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
