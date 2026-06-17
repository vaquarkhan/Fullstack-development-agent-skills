# Changelog

## 0.4.0

### Added

- `skill-packs/` segregated catalog: Java Spring Boot (22), Quarkus (2), Micronaut (2), Jakarta EE, Hibernate, Vaadin, Python, Go, PHP, Ruby
- Spring Boot pack adapted from [spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) (MIT): Spring AI, MCP server, JPA, Flyway, security, testing
- `java-agent-core` skill for JVM agent orchestration and tool registries
- `scripts/import-spring-boot-skills.py` and `scripts/skill_discovery.py` for multi-root skill validation

### Changed

- Registry v0.4.0: 106 total skills (72 core + 34 packs)
- Validators and sync scripts scan both `skills/` and `skill-packs/`

## 0.3.0

### Added

- 72 workflow skills including Postgres, Redis, Kafka, GDPR, GitOps, chaos, load testing, AI/LLM, multi-tenant, DR, cost, mobile, and E2E testing
- Six starter packs: data/events, compliance, AI features, mobile, chaos/SRE, GitOps CI/CD
- Review agents: platform engineering, privacy/compliance, SRE reliability
- Evals benchmark, Claude plugin manifest, JetBrains scaffold, expanded MCP templates
- Docs for Copilot, Kiro, Windsurf, and JetBrains; tutorials for data platform and E2E CI
- `scripts/sync-registry.py` and `scripts/sync-skills-index.py`

### Changed

- Registry bumped to 0.3.0 with full filesystem sync
- README and skills-index reflect complete catalog

## Unreleased

### Added

- (none)
- Multi-cloud presets and serverless starter packs for AWS, Azure, and GCP
- Tutorials, examples, case studies, hooks, and MCP templates
- Validation and bootstrap install scripts
- VS Code extension scaffold and multi-agent adapter surfaces
- Lifecycle commands including migrate, harden, incident, and optimize

### Changed

- Deepened all skills with decision frameworks and evidence packs
- Expanded registry and documentation for machine-readable discovery

## 0.1.0

- Initial fullstack skill pack and core lifecycle commands
