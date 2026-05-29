# Skill Routing Benchmark

| Scenario | Expected command | Expected skills (any order) | Pass criteria |
|----------|------------------|----------------------------|---------------|
| New SaaS MVP | `/spec` then `/plan` | `fullstack-product-specification`, `react-nextjs-frontend-architecture` | Names correct lifecycle + core skills |
| Add Okta login | `/build` | `oauth2-oidc-and-token-lifecycle`, `okta-identity-integration-patterns` | Identity skills cited |
| Rename API field in production | `/migrate` | `api-contract-first-development`, `database-migrations-zero-downtime` | Migration + contract skills |
| AWS Lambda + CloudFront SPA | `/build` | `aws-serverless-fullstack-architecture` | Serverless AWS skill cited |
| User requests data deletion (EU) | `/harden` | `compliance-gdpr-and-data-privacy-fullstack` | Privacy skill + propagation |
| P1 outage, elevated errors | `/incident` | `incident-triage-and-oncall-runbooks` | Incident skill + runbook focus |
| Kafka consumer lag spike | `/optimize` | `kafka-event-backbone-patterns`, `fullstack-observability-and-release-engineering` | Event + observability skills |
| Add Playwright CI suite | `/validate` | `e2e-testing-playwright-cypress`, `fullstack-testing-and-quality-gates` | E2E + quality gates |
| Multi-tenant isolation audit | `/review` | `multi-tenant-data-isolation-patterns` | Isolation skill + negative tests |
| Cutover monolith to services | `/migrate` | `monolith-to-microservices-migration-strategy` | Migration strategy skill |

Score: **pass** if command and at least one expected skill match; **partial** if only skills match; **fail** otherwise.
