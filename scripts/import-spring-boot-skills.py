#!/usr/bin/env python3
"""Import and adapt spring-boot-skills into skill-packs/java/spring-boot/."""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/spring-boot-skills-ref")
TARGET_ROOT = ROOT / "skill-packs" / "java" / "spring-boot"

USE_WHEN = {
    "spring-ai-integration": [
        "Integrating LLMs, chat clients, embeddings, or RAG into Spring Boot",
        "User mentions Spring AI, ChatClient, vector stores, or structured LLM output",
    ],
    "mcp-server": [
        "Building MCP servers in Java/Spring Boot for AI agent tool access",
        "User mentions MCP, Model Context Protocol, or Java agent tool registration",
    ],
    "ai-observability": [
        "Monitoring token usage, latency, and prompt/response quality for Spring AI apps",
    ],
    "layered-architecture": [
        "Generating or modifying Spring Boot controllers, services, repositories, or DTOs",
    ],
    "hexagonal-architecture": [
        "Applying ports-and-adapters architecture in Spring Boot services",
    ],
    "domain-driven-design": [
        "Modeling aggregates, value objects, and domain events in Spring Boot",
    ],
    "multi-module-maven": [
        "Structuring multi-module Maven Spring Boot monorepos",
    ],
    "rest-api-conventions": [
        "Creating REST controllers, response envelopes, pagination, or error handlers",
    ],
    "openapi-first": [
        "Generating controllers and DTOs from OpenAPI specifications",
    ],
    "problem-details-rfc9457": [
        "Implementing RFC 9457 ProblemDetail error responses in Spring Boot",
    ],
    "hateoas": [
        "Adding hypermedia links with Spring HATEOAS",
    ],
    "spring-data-jpa": [
        "Working with JPA entities, repositories, projections, or N+1 prevention",
    ],
    "flyway-migrations": [
        "Writing Flyway migrations with safe multi-step schema changes",
    ],
    "spring-data-redis": [
        "Implementing Redis caching, TTL strategy, or cache-aside patterns",
    ],
    "transactional-patterns": [
        "Configuring @Transactional propagation, sagas, or after-commit side effects",
    ],
    "spring-security-jwt": [
        "Implementing JWT authentication and RBAC with Spring Security",
    ],
    "oauth2-resource-server": [
        "Configuring OAuth2 resource server JWT validation and scope checks",
    ],
    "testing-pyramid": [
        "Writing Spring Boot unit, slice, integration, or Testcontainers tests",
    ],
}

WORKFLOW = [
    "1. Confirm the change matches this skill's domain triggers before coding.",
    "2. Follow the domain guide conventions and gotchas below — not generic Spring Boot defaults.",
    "3. Apply project-specific response envelopes, DTO boundaries, and dependency injection rules.",
    "4. Validate with targeted tests (slice, integration, or contract as appropriate).",
    "5. Capture evidence before merge: tests, migration notes, or observability proof.",
]

REQUIRED_CHECKS = [
    "Constructor injection used; no @Autowired field injection on new code",
    "Controllers return DTOs/envelopes — never raw JPA entities",
    "Business logic stays in @Service layer, not controllers or repositories",
    "Error handling uses project-standard envelope or RFC 9457 ProblemDetail",
]

DECISION_FRAMEWORK = [
    "Prefer Spring Boot 3.x and Spring AI 1.0 GA artifact coordinates — reject pre-GA dead names.",
    "Use constructor injection and immutable dependencies by default.",
    "Keep domain content in services; controllers are HTTP adapters only.",
    "Externalize prompts, API keys, and migration scripts — never hardcode secrets.",
]

RATIONALIZATIONS = [
    '"@Autowired fields are fine for prototypes." -> Field injection hides dependencies and breaks testability; use constructor injection.',
    '"The agent knows Spring Boot." -> Agents default to outdated patterns; follow this skill\'s gotchas and GA coordinates.',
    '"We can skip Flyway for this column." -> Manual DDL drifts from environments; use versioned migrations.',
]

EVIDENCE = [
    "Test output for changed endpoints, services, or migrations",
    "Diff showing DTO boundaries and no entity leakage in API layer",
    "Dependency or coordinate list confirming GA artifact names",
    "Observability or security checklist for auth/AI changes",
]

EXIT = [
    "Generated code matches project layering and naming conventions",
    "No pre-GA Spring AI or MCP artifact names in pom/build files",
    "Tests pass for happy path and at least one failure/edge case",
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    block = match.group(1)
    body = text[match.end() :]
    fields: dict[str, str] = {}
    name = re.search(r"^name:\s*(.+)$", block, re.MULTILINE)
    desc = re.search(r"^description:\s*(>?\s*\n(?:\s+.+\n?)*)", block, re.MULTILINE)
    if name:
        fields["name"] = name.group(1).strip()
    if desc:
        raw = desc.group(1)
        fields["description"] = re.sub(r"\s+", " ", raw.replace(">", "").strip())
    return fields, body


def build_skill(name: str, description: str, domain_body: str) -> str:
    use_when = USE_WHEN.get(name, [f"Working on {name.replace('-', ' ')} in a Spring Boot codebase"])
    if len(use_when) < 2:
        use_when.append("Spring Boot code generation or refactor where agent defaults would be wrong")
    use_lines = "\n".join(f"- {line}" for line in use_when)
    workflow_lines = "\n".join(WORKFLOW)
    checks = "\n".join(f"- {line}" for line in REQUIRED_CHECKS)
    decision = "\n".join(f"- {line}" for line in DECISION_FRAMEWORK)
    rational = "\n".join(f"- {line}" for line in RATIONALIZATIONS)
    evidence = "\n".join(f"- {line}" for line in EVIDENCE)
    exit_lines = "\n".join(f"- {line}" for line in EXIT)

    title = name.replace("-", " ").title()
    desc_one_line = description[:900] if len(description) > 900 else description

    return f"""---
name: {name}
description: {desc_one_line}
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# {title}

## Use When

{use_lines}

## Workflow

{workflow_lines}

## Required Checks

{checks}

## Domain Guide

{domain_body.strip()}

## Decision Framework

{decision}

## Common Rationalizations And Rebuttals

{rational}

## Evidence Pack

{evidence}

## Exit Criteria

{exit_lines}
"""


def main() -> int:
    source_skills = SOURCE / "skills"
    if not source_skills.exists():
        print(f"Source not found: {source_skills}", file=sys.stderr)
        return 1

    TARGET_ROOT.mkdir(parents=True, exist_ok=True)
    count = 0

    for skill_dir in sorted(source_skills.iterdir()):
        if not skill_dir.is_dir():
            continue
        src_skill = skill_dir / "SKILL.md"
        if not src_skill.exists():
            continue

        text = src_skill.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        name = meta.get("name", skill_dir.name)
        description = meta.get("description", f"Spring Boot skill for {name}.")

        # Strip duplicate H1 from body if present
        body = re.sub(r"^# .+\n+", "", body, count=1)

        dest_dir = TARGET_ROOT / name
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / "SKILL.md").write_text(build_skill(name, description, body), encoding="utf-8")

        # Copy examples/ and templates/ if present
        for sub in ("examples", "templates"):
            src_sub = skill_dir / sub
            if src_sub.exists():
                dest_sub = dest_dir / sub
                if dest_sub.exists():
                    shutil.rmtree(dest_sub)
                shutil.copytree(src_sub, dest_sub)

        count += 1
        print(f"imported {name}")

    readme = TARGET_ROOT / "README.md"
    readme.write_text(
        "# Java Spring Boot Skill Pack\n\n"
        f"{count} production-grade Spring Boot skills adapted from "
        "[spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) (MIT).\n\n"
        "Includes Spring AI integration, MCP server building, JPA, Flyway, security, and testing.\n",
        encoding="utf-8",
    )
    print(f"OK: imported {count} skills to {TARGET_ROOT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
