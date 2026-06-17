@Singleton
public class OrderRepository {
    private final DataSource dataSource;
    public OrderRepository(DataSource dataSource) { this.dataSource = dataSource; }
}
