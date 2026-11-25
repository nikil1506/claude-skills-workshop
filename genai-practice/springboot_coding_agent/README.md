# Todo REST API

A small Spring Boot 3 (Java 21) REST API for managing todos. Data is kept in memory
(`ConcurrentHashMap` + `AtomicLong` id generator), so it is lost when the app stops.

## Requirements

- Java 21
- Maven 3.9+ (`mvn` on your PATH; this project has no Maven wrapper)

## Build and run

```bash
# Build the jar
mvn clean package

# Run with Maven
mvn spring-boot:run

# Or run the built jar
java -jar target/todo-0.0.1-SNAPSHOT.jar
```

The app starts on http://localhost:8080.

## Model

```json
{ "id": 1, "title": "Buy milk", "completed": false }
```

Request body for create/update:

```json
{ "title": "Buy milk", "completed": false }
```

- `title` is required and must not be blank (max 255 characters).
- `completed` is optional and defaults to `false`.

## Endpoints

| Method | Path              | Description        | Success | Errors   |
|--------|-------------------|--------------------|---------|----------|
| GET    | `/api/todos`      | List all todos     | 200     |          |
| GET    | `/api/todos/{id}` | Get one todo       | 200     | 404      |
| POST   | `/api/todos`      | Create a todo      | 201 + `Location` header | 400 |
| PUT    | `/api/todos/{id}` | Update title/completed | 200 | 400, 404 |
| DELETE | `/api/todos/{id}` | Delete a todo      | 204     | 404      |

## curl examples

On Windows PowerShell, use `curl.exe` instead of `curl` (and escape the inner quotes),
or run these from Git Bash.

```bash
# List all
curl http://localhost:8080/api/todos

# Create (201, Location: http://localhost:8080/api/todos/1)
curl -i -X POST http://localhost:8080/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","completed":false}'

# Get one
curl http://localhost:8080/api/todos/1

# Update
curl -X PUT http://localhost:8080/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy oat milk","completed":true}'

# Delete (204)
curl -i -X DELETE http://localhost:8080/api/todos/1

# Blank title (400)
curl -i -X POST http://localhost:8080/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"   "}'

# Missing todo (404)
curl -i http://localhost:8080/api/todos/999
```
