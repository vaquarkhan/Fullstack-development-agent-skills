# Microservices Architecture Patterns Checklist

Use this checklist when designing or reviewing large microservice estates.

## Boundary And Organization

- [ ] Bounded contexts and service ownership are explicitly documented
- [ ] Team structure supports independent release and operation
- [ ] Cognitive load limits are considered in service decomposition

## Anti-Patterns And Coupling

- [ ] Distributed monolith indicators are monitored (lockstep deploys, deep sync chains)
- [ ] Shared database write ownership is eliminated or migration-planned
- [ ] Cross-service contract changes follow compatibility policy

## Data And Transactions

- [ ] Distributed transaction strategy is defined (saga/compensation)
- [ ] Event publishing uses outbox or equivalent reliability pattern
- [ ] Replay and reconciliation procedures exist for event workflows

## Communication And Observability

- [ ] Protocol decisions (REST/gRPC/GraphQL) are intentional and documented
- [ ] Trace context propagates across all boundaries
- [ ] SLOs, dashboards, and incident runbooks are tied to user impact

## Migration And Evolution

- [ ] Monolith modernization uses strangler-style incremental cutover
- [ ] Rollback paths exist for each migration slice
- [ ] Architectural fitness metrics are reviewed continuously
