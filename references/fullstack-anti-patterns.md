# Fullstack Anti-Patterns

| Anti-pattern | Why it fails | Better pattern |
| --- | --- | --- |
| UI-driven API design | Contract drift and backend rework | Spec and contract-first delivery |
| Shared database writes across services | Coupling and outage blast radius | Domain-owned data and explicit integration |
| Unbounded retries | Cascading failures under outage | Retry budgets and circuit breakers |
| Client-only authorization | Bypassable security | Server-side authz at every boundary |
| Missing loading/error states | Production UX failures | State matrix for all critical journeys |
| Big-bang releases | High rollback risk | Progressive delivery with flags/canary |
| No observability on new paths | Slow incident response | Metrics, logs, traces, and alerts per journey |
| Secrets in frontend bundles | Credential exposure | Managed secrets and short-lived tokens |
| Cache without invalidation plan | Stale or unauthorized data | Explicit TTL, purge, and release strategy |
| Skipping migration rollback design | Irreversible production changes | Expand-migrate-contract and dual-write windows |
