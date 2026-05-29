# Example: AWS Edge Fullstack Delivery

## Architecture

- CloudFront CDN for static and cacheable assets
- ALB for API traffic distribution
- API Gateway/WAF for edge policy enforcement
- Observability via metrics, logs, and traces

## Skills Used

- frontend-load-balancing-and-global-delivery
- load-balancer-strategy-and-traffic-distribution
- api-gateway-and-edge-security
- fullstack-observability-and-release-engineering

## Validation Focus

- Regional failover behavior
- Cache invalidation during release
- Unauthorized request blocking at edge
