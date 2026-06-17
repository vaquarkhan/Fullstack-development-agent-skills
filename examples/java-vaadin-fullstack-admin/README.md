# Example: Vaadin Java Full-Stack Admin UI

## Architecture

- `admin-ui`: Vaadin Flow views with Spring Boot backend
- `core-services`: Shared `@Service` layer used by Vaadin views and optional REST API
- Lazy grids with `CallbackDataProvider` for large datasets

## Skill Packs Used

- `skill-packs/java/vaadin/vaadin-java-fullstack-ui`
- `skill-packs/java/spring-boot/layered-architecture`
- `skill-packs/java/spring-boot/spring-security-jwt`

## Validation Commands

```bash
./mvnw test
./mvnw -pl admin-ui verify
```

## Success Criteria

- Views delegate to services; no business logic in UI classes
- Grids use lazy loading for lists over 100 rows
- Spring Security protects routes by role
