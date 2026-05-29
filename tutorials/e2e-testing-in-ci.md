# E2E Testing in CI Tutorial

## Goal

Protect critical user journeys with Playwright or Cypress in your delivery pipeline.

## Steps

1. Load `starter-packs/gitops-cicd-starter.yaml`.
2. Follow `e2e-testing-playwright-cypress` for journey selection and stable selectors.
3. Integrate tests in `cicd-gitops-and-progressive-deployment` quality gates.
4. Use `/validate` before `/ship` with evidence from CI runs.

## Exit

- Critical journeys run on every merge
- Flaky tests quarantined with owners
- Failures include actionable diagnostics
