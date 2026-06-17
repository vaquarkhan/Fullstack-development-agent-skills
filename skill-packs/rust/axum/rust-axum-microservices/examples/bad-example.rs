// BAD — unwrap panics, no error type, blocking call
async fn create_order(Json(p): Json<serde_json::Value>) -> String {
    let conn = db::connect().unwrap();
    conn.execute("INSERT ...").unwrap();
    "ok".into()
}
