---
name: ui-engineering-and-design-systems
description: Build and review frontend features using component-driven design, accessibility, performance, and maintainability guardrails. Use when the user asks for UI features, React or Next.js work, design system updates, or frontend refactors.
disable-model-invocation: true
---

# UI Engineering And Design Systems

## Use When

- Building or modifying pages/components
- Creating shared UI primitives or design tokens
- Fixing accessibility, responsiveness, or performance regressions

## Workflow

1. Define user outcome and interaction states (loading, empty, error, success).
2. Identify reusable primitives before creating one-off components.
3. Implement with semantic HTML and keyboard accessibility.
4. Ensure responsive behavior across breakpoints.
5. Verify with linting, tests, and visual checks.

## Required Checks

- ARIA usage is minimal and correct
- Focus order is preserved
- Color contrast and hit targets are acceptable
- Bundle impact is justified
- Critical user paths are covered by tests

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

