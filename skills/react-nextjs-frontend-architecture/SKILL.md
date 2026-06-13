---
name: react-nextjs-frontend-architecture
description: Build React and Next.js applications with scalable architecture, server and client boundaries, state management discipline, and performance guardrails. Use when implementing or refactoring production frontend systems.
disable-model-invocation: true
---

# React Next.js Frontend Architecture

## Use When

- Building feature pages, dashboards, or flows in React and Next.js
- Refactoring frontend folders, state strategy, or rendering modes
- Improving frontend reliability and runtime performance

## Workflow

1. Choose route and rendering model per page (SSR, SSG, ISR, client-side hydration).
2. Define folder and component boundaries (feature modules, shared primitives, hooks).
3. Implement typed service clients for API access and explicit error normalization.
4. Manage state by lifecycle: server state, URL state, local UI state, and form state.
5. Enforce interaction resilience with suspense boundaries, skeletons, and retry UX.
6. Validate accessibility, bundle size, and Core Web Vitals before merge.

## Architecture Rules

- Keep data fetching close to route boundaries
- Avoid global state when URL or server state is sufficient
- Separate display components from data orchestration components
- Use typed DTO mapping to avoid leaking backend internals into UI
- Treat loading and error states as first-class behavior, not afterthoughts

## Required Checks

- Keyboard navigation and focus recovery work across modal and route transitions
- Error boundaries are present for top-level route trees
- Slow network behavior is acceptable for key user journeys
- Client bundle additions are reviewed and justified
- Visual regression coverage exists for high-traffic pages

## Decision Framework

- Prefer server components for static or cacheable content; use client components for interactivity only.
- Prefer URL state for shareable filters and pagination; avoid hidden in-memory state for navigable views.
- Prefer colocated feature modules over centralized "mega" folders when team ownership is clear.
- If route latency exceeds targets, evaluate streaming, prefetch, and cache revalidation before new libraries.

## Common Rationalizations And Rebuttals

- "One global store is easier." -> It often increases coupling; use smallest state scope that solves the problem.
- "Accessibility can come later." -> Retrofits are expensive; include semantics and focus behavior during build.
- "We need this large UI dependency for speed." -> Validate bundle and maintenance cost first.

## Evidence Pack

- Rendering strategy table by route
- Before and after performance snapshot (LCP, INP, CLS or equivalent)
- Accessibility checks for changed surfaces
- Test evidence for loading/error/empty/success states

## Exit Criteria

- Feature integrates with existing design system primitives
- State and API boundaries are explicit and maintainable
- Accessibility and performance regressions are addressed or documented
