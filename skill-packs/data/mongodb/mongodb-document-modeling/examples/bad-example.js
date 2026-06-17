// BAD — unbounded array growth, no index, full document scan
await db.collection('orders').updateOne(
  { _id: id },
  { $push: { events: { type: 'note', text: hugeLog } } } // unbounded array
);
const all = await db.collection('orders').find({}).toArray();
