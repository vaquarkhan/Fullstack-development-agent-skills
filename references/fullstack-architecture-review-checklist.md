# Fullstack Architecture Review Checklist

Use this checklist to validate whether a fullstack design is production-ready before implementation or major refactor.

## Product And Scope

- [ ] User personas and business outcomes are explicit
- [ ] Acceptance criteria include success and failure behavior
- [ ] Out-of-scope items are documented to reduce churn

## UI Architecture

- [ ] Route and component boundaries are clear
- [ ] State ownership is defined (server, URL, local, form)
- [ ] Loading, empty, and error states are covered for every key journey
- [ ] Accessibility requirements are translated into testable checks

## API And Service Design

- [ ] Contracts are documented and versioning policy is defined
- [ ] Error model is consistent and machine-parseable
- [ ] Service boundaries prevent cross-domain coupling
- [ ] Idempotency and retry semantics are explicit

## Data And Persistence

- [ ] Schema changes include migration and rollback strategy
- [ ] Data retention and deletion requirements are documented
- [ ] Indexing and query plans are reviewed for scale assumptions

## Security And Compliance

- [ ] Authentication and authorization model is coherent across UI and API
- [ ] Sensitive data handling is documented end-to-end
- [ ] Audit logging requirements are defined for privileged actions

## Operations And Release

- [ ] SLOs, dashboards, and alerts are planned before launch
- [ ] Rollout strategy (flag, canary, phased) is selected
- [ ] Incident and rollback owner is assigned

## Provenance

- Sources: 12-Factor App, architecture review best practices
- Last reviewed: 2026-06
