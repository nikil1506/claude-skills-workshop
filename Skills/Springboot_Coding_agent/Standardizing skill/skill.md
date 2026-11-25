---
name: springboot-code-standards
description: Use when creating or modifying Spring Boot 3.x backend code (controllers, services, repositories, entities, DTOs, exception handling). Ensures consistent, standardized structure.
---

# Spring Boot Code Standards

1. Use package-by-feature: controller, service, repository, dto.
2. Use constructor injection only, never field @Autowired.
3. Controllers return DTOs, never entities.
4. Handle errors with one global @RestControllerAdvice.

