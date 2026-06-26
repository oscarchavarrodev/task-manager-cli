# 🗂 Task Manager CLI

A professional task management system built with **Python**, designed using **Clean Architecture** and **Domain-Driven Design (DDD)** principles.

This project is being developed incrementally through sprints to simulate a real-world backend development workflow.

---

# 🎯 Goals

* Learn Clean Architecture
* Understand Domain-Driven Design (DDD)
* Build maintainable backend systems in Python
* Apply Test-Driven Development (TDD)
* Implement the Repository Pattern
* Learn dependency inversion
* Transition from in-memory storage to SQLite persistence
* Build a production-ready CLI application

---

# 🧱 Architecture

```text
task_manager/
├── domain/
│   ├── task.py
│   └── enums.py
│
├── application/
│   ├── create_task.py
│   ├── complete_task.py
│   ├── get_task.py
│   └── delete_task.py
│
├── application/ports/
│   └── task_repository.py
│
├── infrastructure/
│   └── persistence/
│       ├── in_memory_task_repository.py
│       └── sqlite_task_repository.py
│
└── tests/
    ├── application/
    ├── integration/
    └── domain/
```

---

# ⚙️ Features

## 🟢 Task Management (CRUD)

* Create tasks
* Retrieve tasks by ID
* List all tasks
* Complete tasks
* Delete tasks

---

## 💾 Persistence

The application currently supports two repository implementations:

* **InMemoryTaskRepository** (used for fast unit testing)
* **SqliteTaskRepository** (persistent storage using SQLite)

Both implementations follow the same `TaskRepository` interface through the **Repository Pattern**, allowing the application layer to remain independent of the persistence technology.

---

## 🧠 Business Rules

* A task starts in the `PENDING` state.
* A task can only be completed once.
* A completed task cannot be completed again.
* A completed task cannot be deleted.
* A task must exist before it can be retrieved, completed, or deleted.

---

# 🧪 Testing Strategy

The project uses **pytest** with fixtures to keep tests clean, reusable, and maintainable.

## ✔ Unit Tests

* Domain validation
* Task creation
* Task completion
* Task retrieval
* Task deletion
* Business rule validation

## ✔ Integration Tests

* SQLite persistence
* Create using SQLite
* Get by ID
* Get all tasks
* Complete task
* Delete task
* Delete validation

Current status:

* ✅ 20 automated tests passing

---

# ▶ Run Tests

```bash
pytest -q
```

---

# 🛠 Code Quality

Format code:

```bash
black .
```

Run static analysis:

```bash
ruff check .
```

---

# 📌 Project Status

* ✅ Sprint 1 — Domain Layer
* ✅ Sprint 2 — Application Layer
* ✅ Sprint 3 — Persistence Layer (SQLite)
* 🚧 Sprint 4 — Command Line Interface (Typer)

---

# 🚀 Upcoming Features

* CLI built with Typer
* Package distribution
* Configuration management
* Logging
* Better error handling
* Docker support
* CI/CD pipeline

---

# 👨‍💻 Author

**Oscar Chavarro**
