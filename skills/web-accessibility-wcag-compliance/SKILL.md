---
name: web-accessibility-wcag-compliance
description: Deliver accessible UI that meets WCAG-oriented requirements with keyboard, screen reader, and contrast validation.
disable-model-invocation: true
---

# Web Accessibility Wcag Compliance

## Use When

- Regulated or enterprise accessibility requirements
- Public sector or inclusive design commitments

## Workflow

1. Define accessibility acceptance criteria per feature
2. Implement semantic structure and focus management
3. Validate color contrast and responsive behavior
4. Add automated and manual accessibility tests
5. Document known exceptions with remediation plan

## Required Checks

- Keyboard-only navigation works for critical flows
- Focus order is logical and visible
- Form errors are announced and associated
- Contrast meets target levels for text and controls

## Decision Framework

- Treat accessibility as release criteria, not audit-only
- Test with real assistive technology scenarios
- Fix blocking issues before feature flags go wide
- Train teams on accessible component usage

## Common Rationalizations And Rebuttals

- "We will audit after launch." -> Rework and compliance risk increase.
- "ARIA fixes bad HTML." -> Semantic HTML comes first; ARIA supplements.
- "Only homepage needs accessibility." -> Legal and user impact applies to all critical journeys.

## Evidence Pack

- Automated axe or equivalent report
- Manual test notes for keyboard and screen reader
- Contrast validation for updated tokens
- Remediation list with owners and dates

## Exit Criteria

- Critical journeys meet accessibility targets
- Regressions are prevented in CI
