// GOOD — async repository, AsNoTracking for reads, explicit includes
public async Task<OrderDto?> GetByIdAsync(Guid id, CancellationToken ct)
{
    return await _db.Orders
        .AsNoTracking()
        .Where(o => o.Id == id)
        .Select(o => new OrderDto(o.Id, o.Status))
        .FirstOrDefaultAsync(ct);
}
