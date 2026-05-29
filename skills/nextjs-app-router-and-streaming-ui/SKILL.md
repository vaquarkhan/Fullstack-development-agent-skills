---
name: nextjs-app-router-and-streaming-ui
description: Build production Next.js App Router experiences with streaming, suspense, caching, and performance-aware data boundaries.
disable-model-invocation: true
---

# Nextjs App Router And Streaming Ui

## Use When

- App Router migration or greenfield Next.js UI
- Need better perceived performance and SEO

## Workflow

1. Choose rendering mode per route segment
2. Define server/client component boundaries
3. Implement streaming and skeleton states
4. Configure cache and revalidation policy
5. Validate accessibility and Core Web Vitals

## Required Checks

- Loading and error UI exist for each critical route
- Cache invalidation strategy supports releases
- Auth-sensitive data never leaks via client caches
- Bundle impact reviewed for new dependencies

## Decision Framework

- Prefer server components unless interactivity requires client
- Use streaming for slow dependencies on key pages
- Keep fetch logic near route boundaries
- Measure INP/LCP before and after changes

## Common Rationalizations And Rebuttals

- "Client-side fetch everywhere is simpler." -> SEO, latency, and consistency suffer.
- "We can skip error.tsx." -> Failures become blank screens in production.
- "Cache forever for speed." -> Stale or unauthorized data risks increase.

## Evidence Pack

- Route rendering decision table
- Performance snapshot for changed routes
- Accessibility validation for interactive surfaces
- E2E evidence for critical journeys

## Exit Criteria

- App Router UX is resilient and performant
- Release-safe caching behavior is documented
