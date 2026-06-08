---
name: azure-serverless-fullstack-architecture
description: Build Azure serverless fullstack solutions with API Management, Azure Functions, Entra ID, Cosmos DB or SQL, Static Web Apps, Service Bus, and Application Insights.
disable-model-invocation: true
---

# Azure Serverless Fullstack Architecture

## Use When

- Azure-native fullstack delivery
- Enterprise identity with Microsoft Entra ID

## Workflow

1. Define Static Web Apps or frontend hosting strategy
2. Model API Management policies for auth, throttling, and validation
3. Implement Azure Functions with durable workflows where needed
4. Integrate Entra ID app registrations and token validation
5. Configure Service Bus or Event Grid for async integration
6. Enable Application Insights and alert rules

## Required Checks

- Managed identities used instead of long-lived secrets where possible
- APIM policies enforce auth before backend invocation
- Function retry and DLQ behavior is explicit
- Bicep or Terraform plan reviewed for environment drift

## Decision Framework

- Use APIM when multiple clients need centralized policy
- Use Durable Functions for long-running orchestration
- Prefer private endpoints for data services in regulated workloads
- Define per-environment configuration and secret rotation

## Common Rationalizations And Rebuttals

- "Functions alone are enough without APIM." -> Policy sprawl and inconsistent security follow.
- "Shared function app for all domains is fine." -> Blast radius and scaling conflicts increase.
- "We can configure auth only in frontend." -> Server-side enforcement is mandatory.

## Evidence Pack

- APIM policy test evidence
- Entra ID token validation negative tests
- Async replay and DLQ drill results
- IaC deployment plan with rollback notes

## Exit Criteria

- Azure serverless paths meet security and reliability targets
- Observability covers UI, API, and async workflows
