# BAD — sync blocking DB in async def, no validation model
@router.post("/orders")
async def create_order(data: dict):
    return db.execute("INSERT INTO orders ...")  # blocks event loop
