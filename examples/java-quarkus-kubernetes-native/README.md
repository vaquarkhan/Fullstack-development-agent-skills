# Example: Quarkus Kubernetes Native Service

## Architecture

- `order-service`: Quarkus REST + Panache + PostgreSQL
- `k8s/`: Deployment with `/q/health/live` and `/q/health/ready` probes
- Optional native profile for GraalVM builds

## Skill Packs Used

- `skill-packs/java/quarkus/quarkus-cloud-native-apis`
- `skill-packs/java/quarkus/quarkus-kubernetes-native`
- `skill-packs/java/hibernate/hibernate-orm-persistence`

## Validation Commands

```bash
./mvnw test
./mvnw package -Dquarkus.package.jar.type=uber-jar
# optional native
./mvnw package -Dnative
```

## Success Criteria

- Readiness fails when database is unavailable
- JVM and native startup/memory documented
- No blocking JDBC on reactive endpoints
