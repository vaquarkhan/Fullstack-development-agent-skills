public class OrderConfiguration : IEntityTypeConfiguration<Order>
{
    public void Configure(EntityTypeBuilder<Order> builder)
    {
        builder.HasKey(o => o.Id);
        builder.Property(o => o.Status).HasMaxLength(32).IsRequired();
        builder.HasIndex(o => o.TenantId);
    }
}
