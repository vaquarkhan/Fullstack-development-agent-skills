// BAD — tracking leak, sync ToList, loads entire graph
public Order Get(Guid id) =>
    _db.Orders.Include(o => o.Items).Include(o => o.Customer).First(o => o.Id == id);
