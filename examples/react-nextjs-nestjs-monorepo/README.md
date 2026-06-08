# Example: React Next.js + NestJS Monorepo

## Architecture

- `apps/web`: Next.js frontend
- `apps/api`: NestJS backend
- `packages/contracts`: shared API schemas and DTO types

## Skills Used

- react-nextjs-frontend-architecture
- nodejs-nestjs-backend-microservices
- api-contract-first-development
- fullstack-testing-and-quality-gates

## Validation Commands

```bash
# contract checks
npm run test:contracts

# frontend checks
npm run test:web

# backend checks
npm run test:api
```

## Success Criteria

- Shared contract changes fail fast in CI when incompatible
- Critical user journey passes end-to-end tests
