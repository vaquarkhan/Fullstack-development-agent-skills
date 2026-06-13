#!/usr/bin/env python3
"""One-time helper to append provenance footers to reference checklists."""
from pathlib import Path

SOURCES = {
    "fullstack-auth-security": "OWASP ASVS, OAuth 2.0 RFC 6749, NIST SP 800-63",
    "aws-fullstack": "AWS Well-Architected Framework, AWS Security Best Practices",
    "azure-fullstack": "Azure Well-Architected Framework, Microsoft Cloud Adoption Framework",
    "gcp-fullstack": "Google Cloud Architecture Framework, GCP security foundations",
    "frontend-review": "WCAG 2.2, web.dev performance guidance, React documentation",
    "frontend-scaling-and-edge-security": "OWASP Top 10, CDN and edge security guidance",
    "ui-production-readiness": "WCAG 2.2, Core Web Vitals, design system governance practices",
    "microservice-patterns": "Microservices.io patterns, enterprise integration patterns",
    "microservices-architecture-patterns": "Domain-Driven Design, microservices architecture guides",
    "microservice-reliability": "Google SRE workbook, release engineering resilience practices",
    "fullstack-architecture-review": "12-Factor App, architecture review best practices",
    "cloud-fullstack-readiness": "12-Factor App, cloud-native foundations",
    "cloud-serverless-patterns": "AWS/Azure/GCP serverless reference architectures",
    "identity-edge-and-delivery": "OAuth 2.0/OIDC specs, OWASP API Security Top 10, CDN best practices",
}

for path in sorted(Path("references").glob("*-checklist.md")):
    text = path.read_text(encoding="utf-8")
    if "## Provenance" in text:
        continue
    key = next((item for item in SOURCES if item in path.stem), "fullstack-architecture-review")
    footer = (
        "\n\n## Provenance\n\n"
        f"- Sources: {SOURCES[key]}\n"
        "- Last reviewed: 2026-06\n"
    )
    path.write_text(text.rstrip() + footer, encoding="utf-8")
    print(f"updated {path.name}")
