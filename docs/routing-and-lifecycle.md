# Routing And Lifecycle Guide

This guide explains how to route work through the repository for consistent fullstack delivery.

## Lifecycle

1. `/spec`: clarify outcomes, contracts, and risk boundaries
2. `/plan`: convert scope into sequenced implementation slices
3. `/build`: implement with contract and compatibility discipline
4. `/validate`: prove quality and operational safety
5. `/review`: run frontend, reliability, and security reviewer lenses
6. `/ship`: release with staged rollout and explicit rollback triggers

## Routing Matrix

- UI architecture work -> `react-nextjs-frontend-architecture`, `ui-engineering-and-design-systems`
- Backend service work -> `nodejs-nestjs-backend-microservices`, `backend-microservices-architecture`
- API compatibility changes -> `api-contract-first-development`
- Auth and permission changes -> `authentication-and-authorization-fullstack`
- Release and production readiness -> `fullstack-observability-and-release-engineering`

## Starter Pack Selection

- Fast MVP -> `starter-packs/fullstack-mvp-starter.yaml`
- Legacy modernization -> `starter-packs/enterprise-modernization-starter.yaml`
- Reliability hardening -> `starter-packs/platform-reliability-starter.yaml`
