public interface OrderRepository extends JpaRepository<Order, UUID> {
    @EntityGraph(attributePaths = "lines")
    Optional<Order> findWithLinesById(UUID id);
}
