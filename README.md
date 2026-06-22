# 🗂 Task Manager CLI

A professional task management system built with Python, designed using **Clean Architecture** and **Domain-Driven Design (DDD) principles**.

This project is structured in incremental sprints to simulate real-world backend development practices.

---

# 🎯 Goals

- Learn software architecture (Clean Architecture)
- Understand Domain-Driven Design (DDD)
- Build maintainable backend systems in Python
- Implement test-driven development (TDD)
- Learn repository pattern and dependency inversion
- Transition from in-memory to real persistence (SQLite)
- Build a CLI-ready backend system

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
│       └── in_memory_task_repository.py
│
└── tests/
    └── application/
    └── domain/
```
---

# ⚙️ Features

## 🟢 Task Management (CRUD)

- Create task
- Complete task
- Get task by ID
- Delete task

---

## 🧠 Business Rules

- A task starts in `PENDING` state
- A task can only be completed once
- A completed task cannot be completed again
- A completed task cannot be deleted
- Tasks must exist before operations

---

# 🧪 Testing Strategy

This project uses `pytest` with fixtures for clean and reusable test setup.

## ✔ Covered scenarios

- Task creation
- Task completion
- Task deletion
- Task retrieval
- Error handling (invalid states, missing tasks)

---

## ▶ Run tests

```bash
pytest -q

---

# 📌 Project Status

✔ Sprint 1: Domain Layer  
✔ Sprint 2: Application Layer (COMPLETED)  
🚧 Sprint 3: Persistence Layer (upcoming)

---

# 👨‍💻 Author
Oscar Chavarro