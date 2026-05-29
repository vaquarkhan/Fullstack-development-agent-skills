# AWS Serverless Fullstack Delivery

Use preset `presets/aws-serverless-fullstack/SKILL.md` and starter `starter-packs/aws-serverless-fullstack-starter.yaml`.

## Architecture

- CloudFront + S3 for UI
- API Gateway + Lambda for APIs
- Cognito for identity
- EventBridge/SQS for async workflows

## Validation

- Run `references/aws-fullstack-checklist.md`
- Test DLQ replay and auth negative paths
