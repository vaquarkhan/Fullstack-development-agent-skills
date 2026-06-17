// GOOD — lazy associations, version column, business-key equals
@Entity
@Table(name = "orders")
public class Order {
    @Id @GeneratedValue private UUID id;
    @Version private long version;
    @OneToMany(mappedBy = "order", fetch = FetchType.LAZY)
    private List<OrderLine> lines = new ArrayList<>();
}
