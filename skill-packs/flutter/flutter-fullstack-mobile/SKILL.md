---
name: flutter-fullstack-mobile
description: Build Flutter mobile clients with clean architecture, Riverpod/Bloc state, typed REST/GraphQL clients, offline sync, and secure token storage. Use for fullstack mobile delivery paired with backend APIs.
disable-model-invocation: true
---

# Flutter Fullstack Mobile

## Use When

- Building Flutter apps consuming REST or GraphQL backends
- Implementing auth, offline-first sync, or real-time features on mobile
- Pairing with `skills/react-native-fullstack-integration` patterns for Flutter stacks

## Workflow

1. Layer app: presentation (widgets), domain (entities/use cases), data (repositories).
2. Choose Riverpod or Bloc for state; keep widgets dumb.
3. Implement ApiClient with interceptors for auth refresh and correlation IDs.
4. Use secure_storage for tokens; never SharedPreferences for secrets.
5. Handle offline with local DB (Drift/Isar) and sync queue patterns.
6. Test repositories with mock clients; widget tests for critical flows.

## Required Checks

- No API keys or secrets in source — use flavors and CI injection
- Token refresh handled centrally — not per-screen ad hoc
- List views paginated — no unbounded fetch in build()
- Accessibility semantics on interactive widgets (Semantics)

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer repository abstraction over calling http in widgets.
- GraphQL when schema is stable and mobile needs flexible queries; REST for simpler CRUD.
- go_router for navigation with deep link handling.
- Feature flags via remote config for risky mobile releases.

## Common Rationalizations And Rebuttals

- "setState in screen is fastest." -> Untestable; use state management and repositories.
- "Store JWT in SharedPreferences." -> Insecure on rooted devices; use secure_storage.
- "Load all data on startup." -> Slow cold start; paginate and lazy-load.

## Evidence Pack

- Widget/repository test output
- Offline sync conflict resolution notes
- Auth refresh sequence diagram
- App size and startup time baseline

## Exit Criteria

- UI decoupled from HTTP; errors mapped to user-visible states
- Auth and secrets handled securely
- Critical flows covered by automated tests
