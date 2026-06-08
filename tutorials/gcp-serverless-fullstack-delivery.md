# GCP Serverless Fullstack Delivery

Use preset `presets/gcp-serverless-fullstack/SKILL.md` and starter `starter-packs/gcp-serverless-fullstack-starter.yaml`.

## Architecture

- Cloud CDN + hosting for UI
- Cloud Run for APIs
- Pub/Sub for async workflows
- Cloud Monitoring for SLOs

## Validation

- Run `references/gcp-fullstack-checklist.md`
- Validate Pub/Sub replay and cache purge during release
