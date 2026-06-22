from uuid import UUID

from task_manager.domain.task import Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[UUID, Task] = {}

    def save(self, task: Task) -> None:
        self._tasks[task.id] = task

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get_by_id(self, task_id: UUID) -> Task | None:
        return self._tasks.get(task_id)

    def delete(self, task_id: UUID) -> None:
        if task_id in self._tasks:
            del self._tasks[task_id]
