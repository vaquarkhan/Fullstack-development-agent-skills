---
name: aws-serverless-fullstack
description: AWS serverless defaults for API Gateway, Lambda, Cognito, DynamoDB or RDS, S3, CloudFront, EventBridge, and CloudWatch observability.
disable-model-invocation: true
---

# AWS Serverless Fullstack Preset

## Defaults

- API Gateway + Lambda for synchronous APIs
- Cognito for user authentication
- S3 + CloudFront for frontend assets
- EventBridge or SQS for async workflows
- X-Ray and CloudWatch alarms for critical paths

## Recommended Pairings

- aws-serverless-fullstack-architecture
- aws-cognito-authentication-patterns
- serverless-event-driven-and-workflow-orchestration
