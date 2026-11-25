# task.md — Multi-Agent Spring Boot Code Generator

## Goal
Build a custom multi-agent system. The user gives only a plain-English requirement;
the agents write, check, and quality-review a Spring Boot (Java) backend.
Every agent reads and updates this `task.md` — it is the shared memory between agents.

Status: TODO
Iteration: 0
Quality Score: -

<!-- Status flow: TODO → BUILT → REVIEW_FAILED | REVIEW_PASSED → QUALITY_FAILED | DONE -->

## Requirement
<!-- User's plain-English requirement goes here -->

## Output Tech Stack (code the agents generate)
- Java 17, Spring Boot 3.x, Maven (`./mvnw`)
- Spring Web, Spring Data JPA, Validation, H2
- JUnit 5 + Mockito
- Output folder: `./backend`

---

## Task 0 — Orchestrator Agent
- **Role:** Controls the pipeline; does not write Java code
- **Input:** User requirement
- **Steps:**
  - [ ] Write the requirement into `## Requirement`
  - [ ] Break it into the Build Checklist (Task 1)
  - [ ] Run Builder → Reviewer → Quality in order
  - [ ] If Status is `REVIEW_FAILED` or `QUALITY_FAILED`, send back to Builder (max 3 iterations)
  - [ ] Stop on `DONE` and print a summary
- **Output:** Final status report to the user

---

## Task 1 — Builder Agent (code building)
- **Role:** Writes Spring Boot backend code + tests
- **Input:** Requirement, Build Checklist, open Review/Quality findings
- **Tools needed:** read file, write file, run shell (`./mvnw clean verify`)
- **Build Checklist:**
  - [ ] Scaffold project (Spring Initializr)
  - [ ] Entities
  - [ ] Repositories
  - [ ] DTOs + mappers
  - [ ] Services (interface + impl)
  - [ ] Controllers (REST endpoints)
  - [ ] Validation + global exception handler (`@RestControllerAdvice`)
  - [ ] Service unit tests + controller tests
  - [ ] `./mvnw clean verify` passes
- **Output:** Code in `./backend`, ticked checklist, Status → `BUILT`, log entry

---

## Task 2 — Reviewer Agent (code check)
- **Role:** Checks correctness — does not edit source code
- **Input:** Requirement + code in `./backend`
- **Tools needed:** read file, run shell, edit `task.md` only
- **Checks:**
  - [ ] Build and tests pass
  - [ ] Every requirement implemented (endpoints, methods, paths, status codes)
  - [ ] Validation and error handling (400 / 404 / 409)
  - [ ] Logic bugs, null handling, `@Transactional` boundaries
  - [ ] Tests actually verify behaviour
  - [ ] Run app and `curl` main endpoints
- **Output:** Findings below, Status → `REVIEW_PASSED` or `REVIEW_FAILED`, log entry

### Review Findings
<!-- - [ ] [HIGH|MEDIUM|LOW] path/File.java:line — problem — expected fix -->

---

## Task 3 — Quality Agent (code quality)
- **Role:** Checks maintainability and best practices — does not edit source code
- **Input:** Code in `./backend`
- **Tools needed:** read file, run shell, edit `task.md` only
- **Checks:**
  - [ ] Layering: no logic in controllers, DTOs at API boundary, entities not exposed
  - [ ] Clean code: naming, short methods, no duplication / dead code / magic numbers
  - [ ] SOLID, constructor injection (no field `@Autowired`)
  - [ ] Security: no hard-coded secrets, validated input, no sensitive fields returned
  - [ ] Logging via SLF4J, no `System.out.println`
  - [ ] Test quality and coverage
  - [ ] RESTful API design, pagination on list endpoints
- **Output:** Findings below, Quality Score /10, Status → `DONE` (score ≥ 8, no HIGH/MEDIUM open) or `QUALITY_FAILED`, log entry

### Quality Findings
<!-- - [ ] [HIGH|MEDIUM|LOW] path/File.java:line — issue — suggested fix -->

---

## Log
<!-- Each agent appends: - [agent] <date> <summary> -->
