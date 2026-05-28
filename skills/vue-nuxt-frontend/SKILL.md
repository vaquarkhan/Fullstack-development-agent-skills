---
name: vue-nuxt-frontend
description: Build and review Vue and Nuxt frontend systems with composable components, SSR or SSG strategy, accessibility, and performance defaults. Use when users request Vue, Nuxt, or component-driven UI delivery.
disable-model-invocation: true
---

# Vue Nuxt Frontend

## Workflow

1. Define rendering strategy per route (SSR, SSG, or client).
2. Use composables for reusable logic.
3. Keep components focused and testable.
4. Implement accessibility and interaction states.
5. Verify performance and hydration behavior.

## Required Checks

- Stable component props and emitted events
- Predictable data fetching boundaries
- Route-level error and loading states
- Tests for critical user flows

## Decision Framework

- Prefer the simplest architecture that preserves maintainability under team growth.
- Make rendering, state, and API boundary decisions explicit before implementation.
- If a feature affects critical user journeys, require performance and accessibility checks.
- If introducing dependencies, justify bundle and long-term maintenance cost.

## Common Rationalizations And Rebuttals

- "We can optimize later." -> Performance debt compounds quickly; set budgets now.
- "Accessibility is polish." -> Accessibility is core behavior and should ship with the feature.
- "One global state store is easiest." -> Over-centralization increases coupling and slows iteration.

## Evidence Pack

- UX state coverage (loading, empty, error, success) for changed flows
- Accessibility checks for keyboard, focus, and semantics
- Performance snapshot for key routes or interactions
- Test evidence for critical user paths

## Exit Criteria

- Workflow decisions are documented and implementation-ready
- Validation evidence exists for quality, reliability, and compatibility
- Operational readiness and rollback expectations are explicit

