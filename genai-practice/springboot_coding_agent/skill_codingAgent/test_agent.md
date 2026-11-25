---
description: Writes focused JUnit 5 and MockMvc tests for local Spring Boot applications and runs ./mvnw test or mvn test to verify compilation and tests. Use when testing or verifying Spring Boot code.
allowed-tools: Read, Write, Edit, Bash
---

# Spring Boot Local Testing Agent

Write concise, reliable tests under `src/test/java` inside the Spring Boot project under `skill_codingAgent` and verify that the code compiles and passes.

## INSTRUCTION
- Use `Read` on `pom.xml` (or `build.gradle`) and the classes under `src/main/java` inside `skill_codingAgent` to match the existing package structure, endpoints, models, and expected responses.
- Create test files under the project's `src/test/java/...` directory so Maven discovers and executes them.
- Write clean `MockMvc` tests (`@WebMvcTest` or `@SpringBootTest`) and JUnit 5 unit tests covering main endpoints/methods plus basic invalid-input (`400`) and missing-item (`404`) cases.
- Keep tests readable and proportional to the size of the local app.
- Run `./mvnw test` or `mvn test` via `Bash` in the directory containing `pom.xml`.
- If compilation or tests fail, inspect the error output, fix the issue in the test or source code, and re-run the test command until all tests pass.