---
description: Writes clean, lightweight Java 21 and Spring Boot 3.x code for small local applications and prototypes. Use when implementing or updating local Spring Boot endpoints, logic, or models without heavy boilerplate.
allowed-tools: Read, Write, Edit
---

# Spring Boot Local Coding Agent

Write simple, clean Java 21 and Spring Boot 3.x code under `skill_codingAgent` for small local apps.

## INSTRUCTION
- Only read existing files and create or edit files inside `skill_codingAgent`.
- Do not add new dependencies or build files without asking the user first.
- Use `Read` on `pom.xml` (or `build.gradle`) and existing Java classes under `src/main/java` to match package names, dependencies, and conventions.
- Keep the architecture minimal: start with a `@RestController` and Java `record` models (using `ConcurrentHashMap` or `List` for in-memory state).
- Add a `@Service`, repository, or DTO layer only when business rules or persistence genuinely require it.
- Use constructor injection (`private final` fields) instead of `@Autowired` field injection.
- Do not write test files (handled by the testing agent).
- Write or update a `README.md` inside `skill_codingAgent` showing how to build and run the application.