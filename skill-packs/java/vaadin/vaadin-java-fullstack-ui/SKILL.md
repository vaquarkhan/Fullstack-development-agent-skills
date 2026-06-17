---
name: vaadin-java-fullstack-ui
description: Build reactive full-stack web UIs entirely in Java with Vaadin Flow — components, data binding, and server-side rendering without client-side JavaScript frameworks. Use for Java-only teams building internal enterprise UIs.
disable-model-invocation: true
---

# Vaadin Java Fullstack UI

## Use When

- Building enterprise web UIs with Java only (no React/Angular/Vue in the stack)
- Internal admin tools, dashboards, or B2B portals need rapid Java-centric delivery
- Server-driven UI with automatic client sync via Vaadin Flow is acceptable

## Workflow

1. Create `@Route` views extending `VerticalLayout` or similar layouts.
2. Bind UI components to domain data with `Binder<T>` and validators.
3. Inject Spring services with `@Autowired` constructor in `@Route` views (Spring Boot + Vaadin).
4. Use lazy loading grids (`CallbackDataProvider`) for large datasets.
5. Apply theme and accessibility; test with Vaadin TestBench or component unit tests.

## Required Checks

- No business logic duplicated in UI — delegate to service layer
- Grids and lists use lazy data providers for tables over ~100 rows
- Session timeout and CSRF handled per Vaadin + Spring Security integration guide
- Push enabled only when needed (WebSocket/Long polling) — understand server load

## Decision Framework

- Prefer Vaadin when team skill is Java-heavy and UI complexity is forms/grids/wizards.
- Use Hilla (Vaadin) if lightweight React frontend with Java endpoints is acceptable hybrid.
- Prefer separate React/Next frontend when SEO, mobile-first consumer UX, or large SPA team exists.
- Keep view classes thin; reuse components via `@Component` or composite custom components.

## Common Rationalizations And Rebuttals

- "Vaadin removes need for API layer." -> Still define service boundaries; may expose REST for integrations later.
- "Load all data in memory for grids." -> Use CallbackDataProvider; server OOM on large tables otherwise.
- "Skip Spring Security integration." -> Vaadin routes need explicit security config like any web app.

## Evidence Pack

- Route map with roles/permissions per view
- Binder validation test for critical forms
- Grid performance note (page size, filter debounce)
- Screenshot or TestBench run for primary user journeys

## Exit Criteria

- Primary views are composable, service-backed, and role-aware
- Large lists perform acceptably with lazy loading
- Security and session policies documented
