---
name: multi-module-maven
description: Use when working in a multi-module Maven project. Covers parent POM conventions, shared dependency management, inter-module rules, and build ordering.
disable-model-invocation: true
source: Adapted from spring-boot-skills (MIT) by rrezartprebreza
---

# Multi Module Maven

## Use When

- Structuring multi-module Maven Spring Boot monorepos
- Spring Boot code generation or refactor where agent defaults would be wrong

## Workflow

1. Confirm the change matches this skill's domain triggers before coding.
2. Follow the domain guide conventions and gotchas below — not generic Spring Boot defaults.
3. Apply project-specific response envelopes, DTO boundaries, and dependency injection rules.
4. Validate with targeted tests (slice, integration, or contract as appropriate).
5. Capture evidence before merge: tests, migration notes, or observability proof.

## Required Checks

- Constructor injection used; no @Autowired field injection on new code
- Controllers return DTOs/envelopes — never raw JPA entities
- Business logic stays in @Service layer, not controllers or repositories
- Error handling uses project-standard envelope or RFC 9457 ProblemDetail

## Domain Guide

## Typical Structure

```
my-app/
├── pom.xml                  ← Parent POM (packaging = pom)
├── my-app-domain/           ← Pure Java domain — no Spring
│   └── pom.xml
├── my-app-application/      ← Use cases — depends on domain
│   └── pom.xml
├── my-app-infrastructure/   ← JPA, Redis, HTTP clients
│   └── pom.xml
└── my-app-web/              ← Spring Boot app, REST — depends on all above
    └── pom.xml
```

## Parent POM

```xml
<!-- pom.xml (parent) -->
<project>
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>my-app-domain</module>
        <module>my-app-application</module>
        <module>my-app-infrastructure</module>
        <module>my-app-web</module>
    </modules>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.0</version>
    </parent>

    <!-- Shared versions — all modules inherit -->
    <properties>
        <java.version>21</java.version>
        <mapstruct.version>1.6.0</mapstruct.version>
        <testcontainers.version>1.19.8</testcontainers.version>
    </properties>

    <!-- Dependency management — centralizes versions, NOT adding to classpath -->
    <dependencyManagement>
        <dependencies>
            <!-- Inter-module dependencies -->
            <dependency>
                <groupId>com.example</groupId>
                <artifactId>my-app-domain</artifactId>
                <version>${project.version}</version>
            </dependency>
            <dependency>
                <groupId>com.example</groupId>
                <artifactId>my-app-application</artifactId>
                <version>${project.version}</version>
            </dependency>
            <!-- Third-party versions -->
            <dependency>
                <groupId>org.mapstruct</groupId>
                <artifactId>mapstruct</artifactId>
                <version>${mapstruct.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Shared plugins -->
    <build>
        <pluginManagement>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <configuration>
                        <source>${java.version}</source>
                        <target>${java.version}</target>
                        <annotationProcessorPaths>
                            <path>
                                <groupId>org.projectlombok</groupId>
                                <artifactId>lombok</artifactId>
                            </path>
                            <path>
                                <groupId>org.mapstruct</groupId>
                                <artifactId>mapstruct-processor</artifactId>
                                <version>${mapstruct.version}</version>
                            </path>
                        </annotationProcessorPaths>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

## Child Module POM (domain — no Spring)

```xml
<project>
    <parent>
        <groupId>com.example</groupId>
        <artifactId>my-app</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>

    <artifactId>my-app-domain</artifactId>

    <dependencies>
        <!-- No Spring. No JPA. Pure Java only. -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
    </dependencies>
</project>
```

## Child Module POM (web — the runnable app)

```xml
<project>
    <parent>...</parent>
    <artifactId>my-app-web</artifactId>

    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>my-app-application</artifactId>
        </dependency>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>my-app-infrastructure</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Only in the runnable module, not parent -->
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

## Dependency Rules

| Module | Can depend on | Cannot depend on |
|--------|---------------|------------------|
| `domain` | Nothing | Everything |
| `application` | `domain` | `infrastructure`, `web` |
| `infrastructure` | `domain`, `application` | `web` |
| `web` | All modules | — |

## Gotchas
- Agent puts `spring-boot-maven-plugin` in parent POM — only in the runnable module
- Agent adds `<dependencies>` in parent instead of `<dependencyManagement>` — adds to all modules' classpath
- Agent creates circular dependencies between modules — enforce the dependency direction above
- Agent imports Spring in `domain` module — domain must be framework-free
- Agent uses `${project.version}` for inter-module versions — correct, but update parent version to update all

## Decision Framework

- Prefer Spring Boot 3.x and Spring AI 1.0 GA artifact coordinates — reject pre-GA dead names.
- Use constructor injection and immutable dependencies by default.
- Keep domain content in services; controllers are HTTP adapters only.
- Externalize prompts, API keys, and migration scripts — never hardcode secrets.

## Common Rationalizations And Rebuttals

- "@Autowired fields are fine for prototypes." -> Field injection hides dependencies and breaks testability; use constructor injection.
- "The agent knows Spring Boot." -> Agents default to outdated patterns; follow this skill's gotchas and GA coordinates.
- "We can skip Flyway for this column." -> Manual DDL drifts from environments; use versioned migrations.

## Evidence Pack

- Test output for changed endpoints, services, or migrations
- Diff showing DTO boundaries and no entity leakage in API layer
- Dependency or coordinate list confirming GA artifact names
- Observability or security checklist for auth/AI changes

## Exit Criteria

- Generated code matches project layering and naming conventions
- No pre-GA Spring AI or MCP artifact names in pom/build files
- Tests pass for happy path and at least one failure/edge case
