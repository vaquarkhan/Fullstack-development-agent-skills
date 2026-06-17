---
name: jakarta-ee-enterprise-platform
description: Build standards-based enterprise Java with Jakarta EE (JAX-RS, CDI, JPA, Bean Validation, Security) for regulated industries and portable application servers. Use when Jakarta EE compliance matters more than Spring-specific conventions.
disable-model-invocation: true
---

# Jakarta EE Enterprise Platform

## Use When

- Delivering Java EE/Jakarta EE compliant applications on Payara, WildFly, OpenLiberty, or similar
- Regulated industries require standards-based, vendor-portable APIs
- Team standardizes on `jakarta.*` namespaces (EE 9+) instead of `javax.*`

## Workflow

1. Structure as enterprise archive: web (JAX-RS/Servlet), EJB/CDI services, JPA persistence unit.
2. Use CDI `@Inject` for wiring; `@ApplicationScoped` for services; `@Transactional` on boundaries.
3. Expose REST with JAX-RS `@Path` resources; validate with Bean Validation (`@NotNull`, `@Valid`).
4. Configure `persistence.xml` and datasource via server admin or MicroProfile Config.
5. Deploy with server-managed security (Jakarta Security) or OIDC via MicroProfile JWT.

## Required Checks

- Packages use `jakarta.*` imports — no legacy `javax.*` on EE 10+ projects
- JPA entities managed in persistence unit; no entity leakage in JAX-RS responses (use DTOs)
- Transactions demarcated at service layer with clear rollback rules
- Server-specific deployment descriptors documented (datasources, JNDI, security realms)

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer Jakarta EE when portability across app servers and standards audit trail matter.
- Use MicroProfile (Config, Health, JWT, OpenAPI) for cloud-native extensions on EE runtimes.
- Prefer Spring Boot when ecosystem velocity and Spring AI integration outweigh portability.
- Map security requirements to Jakarta Security annotations before custom filters.

## Common Rationalizations And Rebuttals

- "Jakarta EE is legacy." -> EE 10+ is actively evolved; major vendors ship modern runtimes.
- "EJB is always required." -> CDI + JAX-RS + JPA covers many apps; use EJB when spec needs container transactions/messaging.
- "javax and jakarta are interchangeable." -> Migration breaks compilation; enforce jakarta imports.

## Evidence Pack

- Deployment descriptor or server config for datasource and security
- JAX-RS resource tests with Arquillian or embedded container
- Persistence unit diagram and transaction boundary notes
- Standards compliance checklist (JAX-RS, CDI, JPA, Validation)

## Exit Criteria

- Application deploys cleanly on target Jakarta EE runtime
- REST and persistence layers use DTOs and validated boundaries
- Security and transaction behavior documented for auditors
