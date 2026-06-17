---
name: vercel-ai-sdk-streaming
description: Build streaming AI features in Next.js with Vercel AI SDK, tool calling, RSC/UI hooks, and edge-safe API routes. Use for TypeScript fullstack AI UX with React Server Components.
disable-model-invocation: true
---

# Vercel AI SDK Streaming

## Use When

- Implementing streaming chat or copilot UX in Next.js App Router
- Using Vercel AI SDK (ai package) with OpenAI, Anthropic, or custom providers
- Pairing with `skills/nextjs-app-router-and-streaming-ui` and `skills/ai-llm-integration-in-fullstack-apps`

## Workflow

1. Keep provider API keys server-side only — Route Handlers or server actions.
2. Use streamText/generateText with typed tools and maxSteps limits.
3. Wire useChat/useAssistant on client with optimistic UI and error states.
4. Pass abortSignal from request for client disconnect cancellation.
5. Log usage in onFinish; rate limit per user/session at edge or API.
6. Test streaming contracts with integration tests and mock language model.

## Required Checks

- API keys never imported in client components
- maxSteps and token budgets configured per endpoint
- Tool calls authorized per user — not global admin tools
- Stream errors surfaced to UI — not silent hangs

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- streamText for chat UX; generateObject for structured form fill.
- Edge runtime only when latency dominates and deps are compatible.
- Persist messages server-side for compliance — not only browser state.
- AI SDK UI components for rapid UX; headless hooks for custom design systems.

## Common Rationalizations And Rebuttals

- "Client-side OpenAI is simpler." -> Exposes keys and bypasses auth; always server proxy.
- "Unlimited tool steps." -> Runaway cost; cap steps and tool allowlist.
- "Streaming skips validation." -> Validate tool inputs/outputs same as REST APIs.

## Evidence Pack

- Route handler test with mock stream
- Rate limit configuration and burst test
- UX recording of error/retry behavior
- Token usage dashboard sample per feature

## Exit Criteria

- Streaming chat works with abort and error handling
- Keys and auth remain server-side
- Tool calling respects user authorization and step limits
