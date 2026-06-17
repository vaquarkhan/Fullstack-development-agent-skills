// BAD — EAGER collection, Lombok @Data on entity, no version
@Entity @Data
public class Order {
    @OneToMany(fetch = FetchType.EAGER)
    private List<OrderLine> lines;
}
