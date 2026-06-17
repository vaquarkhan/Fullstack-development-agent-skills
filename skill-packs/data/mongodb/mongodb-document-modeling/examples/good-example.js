// GOOD — bounded document, indexed query, projection
db.orders.createIndex({ tenantId: 1, createdAt: -1 });
const orders = await db.collection('orders')
  .find({ tenantId, status: 'open' })
  .project({ _id: 1, status: 1, totalCents: 1 })
  .sort({ createdAt: -1 })
  .limit(50)
  .toArray();
